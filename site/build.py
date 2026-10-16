#!/usr/bin/env python3
"""EmbryoGenesis static site builder (TechnoTaau Team).

Each page = src/pages/<name>.json (metadata) + src/pages/<name>.html (the <main> content).
Outputs:
  dist/     production build, root-relative clean URLs (deploy as-is, or port to WordPress)
  preview/  same pages with relative links + index.html, for local / artifact preview
Also writes sitemap.xml, robots.txt, llms.txt, 404.html and WebP copies of images.

Page JSON fields:
  path         "/about/"  (URL path; "/" for home)
  title        <title> (50-60 chars ideal)
  description  meta description (140-160 chars ideal)
  nav          header item to mark current: home|about|diagnostic|therapeutic|courses|training|blog|media|contact
  lang         "en" (default) or "hi"
  og_image     "/assets/img/xxx.jpg"
  breadcrumbs  [["Home","/"],["About Us","/about/"]]   (BreadcrumbList is generated)
  faq          [{"q":"...","a":"..."}]  rendered where the HTML contains <!--FAQ--> and emitted as FAQPage JSON-LD
  schema       [ {...}, ... ]  extra JSON-LD nodes for this page (WebPage subtype, Course, MedicalTest, BlogPosting, Person...)
  noindex      true to exclude from index and sitemap
  priority     sitemap priority (0.1-1.0)
  date_modified ISO date (default: today)
"""
import json, os, re, shutil, sys, html, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC, ASSETS = ROOT / 'src', ROOT / 'assets'
SITE = 'https://embryogenesis.in'
TODAY = datetime.date.today().isoformat()

ORG = {
  "@type": ["MedicalOrganization", "DiagnosticLab"],
  "@id": SITE + "/#org",
  "name": "EmbryoGenesis",
  "alternateName": ["EmbryoGenesis – Infertility Diagnostic & Research", "Embryogenesis Mohali"],
  "description": "EmbryoGenesis is an infertility diagnostic and research centre in Mohali, Punjab, India, offering endometrial diagnostic tests (ERFA – The Soil Test, Endo-Immune Test, Endometrial Infection Test), fertility therapies, and B.Sc./M.Sc. Clinical Embryology programmes with ITHS, Bahra University and Rayat Bahra University.",
  "disambiguatingDescription": "EmbryoGenesis (Mohali, India) is an infertility diagnostic and research centre. It is not the biological process of embryogenesis.",
  "url": SITE + "/",
  "logo": SITE + "/assets/img/logo.png",
  "image": SITE + "/assets/img/lab.jpg",
  "foundingDate": "2023-11",
  "telephone": "+91-8146217196",
  "email": "info.embryogenesis@gmail.com",
  "address": {"@type": "PostalAddress", "streetAddress": "Top Floor, Rayat Bahra Dental College & Hospital, Rayat Bahra University Campus, Kharar", "addressLocality": "Mohali", "addressRegion": "Punjab", "addressCountry": "IN"},
  "geo": {"@type": "GeoCoordinates", "latitude": 30.7811558, "longitude": 76.6176566},
  "areaServed": {"@type": "Country", "name": "India"},
  "medicalSpecialty": ["Gynecologic", "Pathology", "Laboratory"],
  "founder": {"@id": SITE + "/pulakes-purkait-profile/#person"},
  "sameAs": ["https://www.facebook.com/EmbryoGenesis", "https://www.instagram.com/embryo_genesis", "https://twitter.com/EmbryoGenesiss", "https://www.youtube.com/@Embryo-Genesis", "https://www.linkedin.com/company/embryogenesis"],
  "knowsAbout": ["Endometrial receptivity", "Recurrent implantation failure", "Recurrent pregnancy loss", "Chronic endometritis", "Reproductive immunology", "Clinical embryology"]
}
PERSON = {
  "@type": "Person", "@id": SITE + "/pulakes-purkait-profile/#person",
  "name": "Prof. (Dr.) Pulakes Purkait", "jobTitle": "Founder & Director", "worksFor": {"@id": SITE + "/#org"},
  "url": SITE + "/pulakes-purkait-profile/", "image": SITE + "/assets/img/founder.jpg",
  "sameAs": ["https://orcid.org/0000-0002-8814-9939", "https://in.linkedin.com/in/pulakes-purkait-aa634094", "https://www.researchgate.net/profile/Pulakes-Purkait"]
}
WEBSITE = {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "EmbryoGenesis", "publisher": {"@id": SITE + "/#org"}, "inLanguage": "en-IN"}

def read(p): return Path(p).read_text(encoding='utf-8')

def img_dims(path):
    try:
        from PIL import Image
        with Image.open(path) as im: return im.size
    except Exception: return None

def make_webp():
    try:
        from PIL import Image
    except ImportError:
        print('Pillow missing: skipping WebP'); return
    for f in (ASSETS / 'img').glob('*'):
        if f.suffix.lower() in ('.jpg', '.jpeg', '.png') and f.stem != 'logo':
            out = f.with_suffix('.webp')
            if not out.exists() or out.stat().st_mtime < f.stat().st_mtime:
                with Image.open(f) as im:
                    im = im.convert('RGBA' if f.suffix.lower() == '.png' else 'RGB')
                    im.save(out, 'WEBP', quality=72, method=6)

IMG_RE = re.compile(r'<img\b([^>]*?)\bsrc="(/assets/img/[^"]+?\.(?:jpe?g|png))"([^>]*)>', re.I)
def enhance_imgs(markup):
    def rep(m):
        before, src, after = m.group(1), m.group(2), m.group(3)
        attrs = before + after
        local = ASSETS / src[len('/assets/'):]
        extra = ''
        if 'width=' not in attrs:
            dims = img_dims(local)
            if dims: extra += f' width="{dims[0]}" height="{dims[1]}"'
        if 'loading=' not in attrs and 'fetchpriority' not in attrs: extra += ' loading="lazy"'
        if 'decoding=' not in attrs: extra += ' decoding="async"'
        tag = f'<img{before}src="{src}"{after}{extra}>'
        webp = local.with_suffix('.webp')
        if webp.exists() and not src.endswith('logo.png'):
            return f'<picture><source type="image/webp" srcset="{src.rsplit(".",1)[0]}.webp">{tag}</picture>'
        return tag
    return IMG_RE.sub(rep, markup)

def faq_html(faq):
    items = ''.join(f'<details{" open" if i == 0 else ""}><summary>{html.escape(x["q"])}</summary><p>{x["a"]}</p></details>' for i, x in enumerate(faq))
    return f'<div class="faq">{items}</div>'

def strip_tags(s): return re.sub(r'<[^>]+>', '', s)

def jsonld(meta, url):
    graph = [ORG, WEBSITE]
    if meta.get('path') in ('/', '/about/', '/pulakes-purkait-profile/'): graph.append(PERSON)
    bc = meta.get('breadcrumbs') or []
    if len(bc) > 1:
        graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(bc)]})
    if meta.get('faq'):
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
            {"@type": "Question", "name": x['q'], "acceptedAnswer": {"@type": "Answer", "text": strip_tags(x['a'])}} for x in meta['faq']]})
    for node in meta.get('schema', []):
        node = dict(node)
        if node.get('@type') in ('WebPage', 'MedicalWebPage', 'AboutPage', 'ContactPage', 'CollectionPage', 'ItemPage'):
            node.setdefault('url', url)
        graph.append(node)
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)

def page_html(meta, main):
    url = SITE + meta['path']
    lang = meta.get('lang', 'en')
    title = html.escape(meta['title']); desc = html.escape(meta['description'])
    og = SITE + meta.get('og_image', '/assets/img/hero-couple.jpg')
    robots = 'noindex, follow' if meta.get('noindex') else 'index, follow, max-image-preview:large, max-snippet:-1'
    header = read(SRC / 'partials/header.html'); footer = read(SRC / 'partials/footer.html'); sprite = read(SRC / 'partials/sprite.html')
    nav = meta.get('nav')
    if nav:
        header = header.replace(f'data-nav="{nav}"', f'data-nav="{nav}" aria-current="page"')
        if nav in ('diagnostic', 'therapeutic'): header = header.replace('<div class="dd" data-nav-group="services">', '<div class="dd current" data-nav-group="services">')
    if '<!--FAQ-->' in main:
        main = main.replace('<!--FAQ-->', faq_html(meta.get('faq', [])))
    main = enhance_imgs(main); header = enhance_imgs(header)
    hreflang = f'<link rel="alternate" hreflang="{"hi-IN" if lang == "hi" else "en-IN"}" href="{url}">'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
{hreflang}
<meta name="theme-color" content="#0E6970">
<meta property="og:type" content="{'article' if meta.get('article') else 'website'}">
<meta property="og:site_name" content="EmbryoGenesis">
<meta property="og:locale" content="{'hi_IN' if lang == 'hi' else 'en_IN'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@EmbryoGenesiss">
<link rel="icon" href="/assets/img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@500;600;700&family=Lato:wght@400;700&display=swap">
<link rel="stylesheet" href="/assets/css/style.css">
<script type="application/ld+json">
{jsonld(meta, url)}
</script>
</head>
<body>
{sprite}{header}
<main id="main">
{main.strip()}
</main>
{footer}
<script src="/assets/js/main.js" defer></script>
</body>
</html>
'''

def out_path(base, path, file=None):
    if file: return base / file
    return base / (path.strip('/') + '/index.html' if path != '/' else 'index.html')

def relativize(markup, path, file=None):
    depth = len(file.split('/')) - 1 if file else (0 if path == '/' else len(path.strip('/').split('/')))
    pre = '../' * depth or './'
    def fix(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith('//'): return m.group(0)
        tail = ''
        if '#' in val: val, frag = val.split('#', 1); tail = '#' + frag
        if val.endswith('/'): val += 'index.html'
        return f'{attr}="{pre}{val.lstrip("/")}{tail}"'
    return re.sub(r'\b(href|src|srcset)="(/[^"]*)"', fix, markup)

def main():
    make_webp()
    pages = []
    for j in sorted((SRC / 'pages').glob('*.json')):
        meta = json.loads(read(j))
        body = SRC / 'pages' / (j.stem + '.html')
        if not body.exists(): print('missing body for', j.name); continue
        pages.append((meta, read(body)))
    css = read(ASSETS / 'css/style.css') + ''.join('\n/* ---- ' + f.name + ' ---- */\n' + read(f) for f in sorted((ASSETS / 'css').glob('add-*.css')))
    for d in ('dist', 'preview'):
        shutil.rmtree(ROOT / d, ignore_errors=True)
        shutil.copytree(ASSETS, ROOT / d / 'assets', ignore=shutil.ignore_patterns('add-*.css', 'CREDITS-*'))
        (ROOT / d / 'assets/css/style.css').write_text(css, encoding='utf-8')
    for meta, body in pages:
        doc = page_html(meta, body)
        for d in ('dist', 'preview'):
            p = out_path(ROOT / d, meta['path'], meta.get('file')); p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(relativize(doc, meta['path'], meta.get('file')) if d == 'preview' else doc, encoding='utf-8')
    # sitemap
    urls = ''.join(f'<url><loc>{SITE}{m["path"]}</loc><lastmod>{m.get("date_modified", TODAY)}</lastmod><priority>{m.get("priority", 0.6)}</priority></url>\n' for m, _ in pages if not m.get('noindex') and not m.get('file'))
    sm = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'
    robots = f'User-agent: *\nAllow: /\nDisallow: /wp-admin/\n\n# AI crawlers welcome (GEO)\nUser-agent: GPTBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n'
    for d in ('dist', 'preview'):
        (ROOT / d / 'sitemap.xml').write_text(sm); (ROOT / d / 'robots.txt').write_text(robots)
        if (SRC / 'llms.txt').exists(): shutil.copy(SRC / 'llms.txt', ROOT / d / 'llms.txt')
        for extra in ('_redirects', '.htaccess'):
            if (SRC / extra).exists(): shutil.copy(SRC / extra, ROOT / d / extra)
    print(f'built {len(pages)} pages -> dist/ and preview/')

if __name__ == '__main__':
    main()
