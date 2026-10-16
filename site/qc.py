#!/usr/bin/env python3
"""EmbryoGenesis automated QC (TechnoTaau Team). Run after build.py.
Checks every page in dist/ for SEO, AEO/GEO structure, accessibility basics and broken links.
Exit code 1 if any ERROR. Usage: python3 site/qc.py [--json]"""
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent; DIST = ROOT / 'dist'

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.h = []; s.imgs = []; s.links = []; s.title = ''; s._t = False; s.meta = {}; s.canon = None
        s.ld = []; s._ld = False; s.inputs = []; s.labels_for = set(); s._label_depth = 0; s.lang = None; s.ids = set()
        s._h = None; s.text_in_h = {}
    def handle_starttag(s, tag, a):
        a = dict(a)
        if 'id' in a: s.ids.add(a['id'])
        if tag == 'html': s.lang = a.get('lang')
        if tag == 'title': s._t = True
        if tag == 'meta' and a.get('name'): s.meta[a['name']] = a.get('content', '')
        if tag == 'meta' and a.get('property'): s.meta[a['property']] = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical': s.canon = a.get('href')
        if tag == 'script' and a.get('type') == 'application/ld+json': s._ld = True; s.ld.append('')
        if re.fullmatch(r'h[1-6]', tag): s.h.append(int(tag[1])); s._h = len(s.h) - 1; s.text_in_h[s._h] = ''
        if tag == 'img': s.imgs.append(a)
        if tag == 'a' and a.get('href'): s.links.append(a['href'])
        if tag == 'label': s._label_depth += 1; s.labels_for.add(a.get('for'))
        if tag in ('input', 'select', 'textarea') and a.get('type') not in ('hidden', 'submit', 'button'):
            s.inputs.append((a, s._label_depth > 0))
    def handle_endtag(s, tag):
        if tag == 'title': s._t = False
        if tag == 'script': s._ld = False
        if tag == 'label': s._label_depth -= 1
        if re.fullmatch(r'h[1-6]', tag): s._h = None
    def handle_data(s, d):
        if s._t: s.title += d
        if s._ld: s.ld[-1] += d
        if s._h is not None: s.text_in_h[s._h] += d

def check(path):
    rel = '/' + str(path.relative_to(DIST)).replace('index.html', '')
    html = path.read_text(encoding='utf-8'); p = P(); p.feed(html)
    out = []
    E = lambda m: out.append(('ERROR', m)); W = lambda m: out.append(('WARN', m))
    noindex = 'noindex' in p.meta.get('robots', '')
    if p.h.count(1) != 1: E(f'{p.h.count(1)} <h1> elements (need exactly 1)')
    prev = 0
    for lv in p.h:
        if prev and lv > prev + 1: W(f'heading level jumps h{prev}→h{lv}'); break
        prev = lv
    t = p.title.strip(); d = p.meta.get('description', '')
    if not (30 <= len(t) <= 65): (W if t else E)(f'title length {len(t)}: "{t}"')
    if not (110 <= len(d) <= 165): (W if d else E)(f'description length {len(d)}')
    if 'TODO' in d or 'TODO' in t: E('TODO in title/description')
    if not p.canon: E('no canonical')
    if not p.lang: E('no html lang')
    for k in ('og:title', 'og:description', 'og:image'):
        if k not in p.meta: W(f'missing {k}')
    types = []
    for blob in p.ld:
        try:
            data = json.loads(blob)
            for n in data.get('@graph', [data]):
                t_ = n.get('@type'); types += t_ if isinstance(t_, list) else [t_]
        except Exception as e: E(f'JSON-LD parse error: {e}')
    if not noindex and rel != '/' and 'BreadcrumbList' not in types: W('no BreadcrumbList')
    pagetypes = {'WebPage', 'MedicalWebPage', 'AboutPage', 'ContactPage', 'CollectionPage', 'ProfilePage', 'BlogPosting', 'Course', 'ItemList'}
    if not noindex and not (set(types) & pagetypes): W(f'no page-level schema (types: {sorted(set(map(str, types)))})')
    for im in p.imgs:
        if 'alt' not in im: E(f'img without alt: {im.get("src")}')
        src = im.get('src', '')
        if src.startswith('/') and not (DIST / src.lstrip('/')).exists(): E(f'missing image file {src}')
        if 'width' not in im: W(f'img without width/height: {src}')
    for href in p.links:
        if href.startswith('/') and not href.startswith('//'):
            target = href.split('#')[0]
            f = DIST / target.lstrip('/')
            if not (f.exists() and f.is_file()) and not (f / 'index.html').exists(): E(f'broken internal link {href}')
        if href.startswith('#') and href[1:] and href[1:] not in p.ids and not href.startswith('#i-'): W(f'anchor without target {href}')
    for a, wrapped in p.inputs:
        if not (wrapped or a.get('aria-label') or a.get('id') in p.labels_for or a.get('aria-labelledby')):
            E(f'unlabelled form control name={a.get("name")} id={a.get("id")}')
        if not a.get('name'): E(f'form control without name attribute id={a.get("id")}')
    if '{{' in html: E('template placeholder {{ }} left in page')
    for word in ('lorem', 'TODO', 'FIXME'):
        if word in re.sub(r'<script.*?</script>', '', html, flags=re.S): W(f'"{word}" found in page')
    internal = [h for h in p.links if h.startswith('/') and not h.startswith('/assets')]
    if len(set(internal)) < 8: W(f'only {len(set(internal))} unique internal links')
    return rel, t, d, out

def main():
    pages = sorted(DIST.rglob('*.html'))
    titles, descs, report, errors = {}, {}, [], 0
    for f in pages:
        rel, t, d, issues = check(f)
        titles.setdefault(t, []).append(rel); descs.setdefault(d, []).append(rel)
        report.append((rel, issues)); errors += sum(1 for s, _ in issues if s == 'ERROR')
    for t, rs in titles.items():
        if len(rs) > 1: report.append(('(site)', [('ERROR', f'duplicate title "{t}" on {rs}')])); errors += 1
    for d, rs in descs.items():
        if len(rs) > 1 and d: report.append(('(site)', [('WARN', f'duplicate description on {rs}')]))
    sm = (DIST / 'sitemap.xml').read_text()
    for f in pages:
        rel = '/' + str(f.relative_to(DIST)).replace('index.html', '')
        html = f.read_text()
        if 'noindex' not in html and f.name == 'index.html' and f'https://embryogenesis.in{rel}<' not in sm:
            report.append((rel, [('WARN', 'indexable page missing from sitemap')]))
    if '--json' in sys.argv: print(json.dumps(report, indent=1)); return
    for rel, issues in report:
        if issues:
            print(rel); [print(f'  {s}: {m}') for s, m in issues]
    print(f'\n{len(pages)} pages checked, {errors} errors, {sum(1 for _, i in report for s, _ in i if s == "WARN")} warnings')
    sys.exit(1 if errors else 0)

if __name__ == '__main__':
    main()
