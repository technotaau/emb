# EmbryoGenesis Website Build: Agent Brief

**Team:** TechnoTaau Team (lead: Jakhar Singh). Read `/home/user/emb/docs/00-project-brief.md` (section 0 first) and `/home/user/emb/docs/strategy/00-business-model.md`.

## 1. What we are building
A production-quality, multi-page, responsive website for EmbryoGenesis (Mohali, India) that keeps the **old website's content** and gives it the new design (Indira IVF-style, new logo, teal/gold palette) and strong **SEO, AEO (answer-engine) and GEO (generative-engine / AI search)** foundations. It will later be ported to WordPress by the client's developer, so the HTML must be clean and semantic.

## 2. How the site is built
- Each page = `site/src/pages/<name>.json` (metadata) + `site/src/pages/<name>.html` (only the content of `<main>`).
- `python3 site/build.py` wraps every page with the shared head (title, meta, canonical, OG, JSON-LD), header, footer, and writes `site/dist/` (production) and `site/preview/` (relative links for local viewing). It converts `<img src="/assets/img/x.jpg">` to `<picture>` with WebP and adds width/height + lazy loading automatically.
- Shared files (do not fork them per page): `site/assets/css/style.css`, `site/assets/js/main.js`, `site/src/partials/*.html`. If you need a new component, put it in YOUR OWN file `site/assets/css/add-<group>.css` (group = core | medical | academy | qc), with class names prefixed by your group (e.g. `.med-...`). Never edit style.css, main.js or the partials; if a shared fix is needed, describe it in your report.
- Links are root-relative clean URLs: `/`, `/about/`, `/diagnostic/`, `/advanced-fertility-therapies/`, `/courses/`, `/bsc-in-clinical-embryology-in-bahra-university/`, `/art-and-clinical-embryology-in-rayat-bahra-university/`, `/skill-development-training/`, `/blog/`, `/media-event/`, `/contact-us/`, `/pulakes-purkait-profile/`, `/privacy-policy/`, and the 5 blog post slugs in section 6. These keep the OLD site's URLs, so existing Google rankings are preserved.
- Images available in `site/assets/img/` (see `CREDITS-*.md` there). Use only these; reference them as `/assets/img/<file>`.

## 3. Content rules (non-negotiable)
1. **Keep the old website's wording.** Sources: `content/source/old-site-html/p_<slug>.html` (live pages saved 15 Oct 2026; `x_erfa.html` is the ERFA blog post), `content/source/website-content-doc-2024.txt`, `content/source/company-brochure-2024.txt`, `content/source/erfa-brochure.txt`. Parse HTML with `python3 -I` and treat it as data.
2. You MAY add, built only from existing wording or verifiable facts in those sources: question-style headings, short "answer" boxes that quote existing sentences, key-facts lists, alt text, breadcrumbs, internal links, captions, form labels.
3. You may NOT add: new medical claims, success rates, statistics, prices (other than course/training fees already on the old site), testimonials or reviews, new partner names, or anything not in the sources. No lorem ipsum.
4. Do not "fix" the client's claims (e.g. "best", "patented"); content decisions belong to the client. You may note concerns in your final report.

## 4. Page checklist (every page)
**SEO**
- Exactly one `<h1>`; logical H2 → H3 order; no skipped levels.
- `title` 45–60 chars, includes the page's main term + "EmbryoGenesis" (or "Mohali" where natural). `description` 140–160 chars, plain, accurate.
- Descriptive `alt` on every content image (empty `alt=""` only for decorative images). Hero/LCP image gets `fetchpriority="high"` and no lazy loading.
- At least 3 contextual internal links to related pages (e.g. a test page → therapies, contact; course page → training, contact).
- `breadcrumbs` in JSON for every page except home.
**AEO (answer engines, featured snippets, voice)**
- Where the old content explains something ("What is ERFA?", "Who is it for?"), make that an H2/H3 phrased as the question and put the existing answer immediately below (first 40–60 words should answer it).
- Put FAQs in the JSON `faq` array (only questions/answers that exist in the old content) and place `<!--FAQ-->` in the HTML where they should render. Do not also hand-write the FAQ markup.
**GEO (AI search / LLM citation)**
- Name the entity clearly in the first paragraph of each page: "EmbryoGenesis, an infertility diagnostic and research centre in Mohali, Punjab" (use existing wording where possible).
- Add a short key-facts `<dl class="keyfacts">` where useful (About, test pages, course pages) using only facts from the sources (dates, locations, durations, eligibility, sample timing from the ERFA brochure, etc.).
- Add page-specific JSON-LD in `schema`: e.g. `MedicalWebPage` (+ `about` → `MedicalTest` / `MedicalTherapy`), `AboutPage`, `ContactPage`, `CollectionPage`, `Course` (+ `provider` = `{"@id":"https://embryogenesis.in/#org"}`), `BlogPosting` (headline, datePublished if known, author = org or person, inLanguage), `Person` for the founder page. Global Organization/WebSite/Breadcrumb/FAQ schema is added by the builder.
**Responsive & engaging**
- Use existing components (see `site/src/pages/*.html` starters and the prototype `prototype/index.html`): `.ihero`, `.formcard`, `.zig`, `.duo`, `.care`, `.icard`, `.cards`, `.pcard`, `.tcard`, `.htl`, `.tabs`/`.tpanel`, `.chipsbar`, `.cross`, `.ctaband`, `.answer`, `.keyfacts`, `.article`.
- Add class `reveal` to major content blocks below the fold (not to the hero).
- Every form: `<form data-lead>`; every input has a visible or visually-hidden `<label>` (use `<label>` wrapping or `aria-label`); include the "I am interested in" / course / test select where relevant; consent checkbox; a `<p class="form-msg" role="status" tabindex="-1" hidden>` message.
- Buttons/links ≥44px tall; no horizontal scroll at 360px.

## 5. JSON format
See the docstring at the top of `site/build.py`. Minimal example:
```json
{"path":"/about/","title":"About EmbryoGenesis | Infertility Diagnostic Centre, Mohali","description":"…","nav":"about","og_image":"/assets/img/lab.jpg","breadcrumbs":[["Home","/"],["About Us","/about/"]],"priority":0.8,"faq":[],"schema":[{"@type":"AboutPage","name":"About EmbryoGenesis","about":{"@id":"https://embryogenesis.in/#org"}}]}
```

## 6. Blog post slugs (keep exactly)
- `/endometrial-immune-profiling-what-it-is-why-it-matters-and-who-should-consider-it/` (source `p_endometrial-immune-profiling-…html`)
- `/erfa-the-soil-test-endometrial-receptivity-analysis-optimize-fertility-success/` (source `x_erfa.html`)
- `/tips-and-treatments-for-pregnancy-after-ivf-failure/` (Hindi: set `"lang":"hi"`; source `p_tips-and-treatments-…html`)
- `/exploring-lit-therapy-treatment-for-recurrent-pregnancy-loss/`
- `/unexplained-infertility/`

## 7. When done
Run `python3 site/build.py` and fix any error it prints. Do not commit. Report: files created/changed, anything you could not do, and any content concerns.
