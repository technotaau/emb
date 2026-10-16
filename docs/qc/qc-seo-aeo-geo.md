# QC report: SEO, AEO and GEO (EmbryoGenesis site build)

**Prepared by:** TechnoTaau Team (SEO/AEO/GEO Quality Control)
**Date:** 16 October 2026
**Scope:** `site/` (19 pages). Files changed are limited to `site/src/pages/*.json`, `site/src/llms.txt`, `site/src/_redirects`, `site/src/.htaccess` and the ORG/PERSON/WEBSITE constants and head SEO tags in `site/build.py`.
**Result:** `python3 site/build.py` builds 19 pages. `python3 site/qc.py` reports 0 errors and 0 warnings. A schema.org vocabulary validator, run against the full current schema.org release, reports 0 problems. Before the fixes it reported 59.

---

## 1. Scorecard

| Area | Before | After | Notes |
|---|---|---|---|
| Titles and meta descriptions | 8/10 | 9/10 | All are unique, branded and within 51–59 / 147–160 characters. Keyword focus is sharper on 4 pages. |
| Structured data (JSON-LD) | 6/10 | 9.5/10 | 59 issues before, 0 now. The remaining gap is the logo size (asset needed, see 6.3). |
| AEO (question headings and answers) | 7/10 | 7/10 | Good on the service, course and EIP pages. The blog posts and About/Contact need HTML changes (section 4). |
| GEO / entity consistency | 6/10 | 8.5/10 | Schema, llms.txt and NAP are now complete. The visible NAP and the brand spelling still vary (section 4). |
| Internal linking | 7/10 | 7/10 | No orphans and no broken links. Five pages are weak; the anchors to add are in section 5. |
| Redirects / migration | 5/10 | 10/10 | All 28 audited old URLs, plus the extra ones, return 200 or redirect in one hop. |

---

## 2. What I fixed

### 2.1 Organization / Person / WebSite constants (`site/build.py`)
- **Type** changed from `["MedicalOrganization","DiagnosticLab"]` to `["DiagnosticLab","MedicalBusiness"]`. `geo` is only valid on a Place, so it was invalid on all 19 pages. `MedicalBusiness` is a LocalBusiness and a Place, which makes `geo` and `hasMap` valid and makes the lab eligible for local-business features.
- **Address** completed from the 2024 brochures: added `VPO Sahauran, Tehsil Kharar` and `postalCode 140302`.
- **geo** corrected to the pin of the client's own Google Maps place. The link `maps.app.goo.gl/C5ciaW6wBCrUkU9Q6` comes from the old Contact page and resolves to 30.7809862, 76.6193467. The old value was about 160 m off and had no source.
- **hasMap** added. It uses the same link, which is in the sources.
- **openingHours** was not added because no hours appear in any source.
- **medicalSpecialty**: `"Laboratory"` is not a schema.org MedicalSpecialty value, so it was changed to `"LaboratoryScience"`.
- **sameAs**: removed `linkedin.com/company/embryogenesis`. It is not in any source, and the brief says there is no LinkedIn page yet.
- **founder** is now an inline Person (with `@id`, `name` and `url`). Before, it was a bare `@id` that was undefined on 16 of 19 pages (dangling reference).
- **image**: this was the Unsplash stock lab photo (`lab.jpg`), which wrongly implied it showed the client's lab. It now points to the logo ImageObject (`#logo`, with width and height).
- **Added from sources:**
  - `contactPoint`: customer service +91 8146217196 / info.embryogenesis@gmail.com; admissions +91 9691736435 and +91 9815692195.
  - `slogan`: "Redefining Fertility Evaluation".
  - `award`: Best Innovator Award for Human Infertility Treatment, Research & Innovation Park, New Delhi, 27 Nov 2024.
  - The `EMBRYOGENESIS` spelling added to `alternateName`.
- **WebSite**: added `alternateName`. `inLanguage` is now `["en-IN","hi-IN"]` because of the Hindi post.

### 2.2 Head template SEO tags (`site/build.py`, `page_html`)
- Added `og:image:width`, `og:image:height` (read from the file) and `og:image:alt`.
- Added `article:published_time`, `article:modified_time` and `article:publisher` on blog posts. The dates come from the post's BlogPosting node.
- `twitter:card` now falls back to `summary` when the OG image is narrower than 600 px. Only the founder page (350×373) is affected, and this stops a blurry large card.

### 2.3 Page JSON (`site/src/pages/*.json`)
- **Dangling `@id` fixed:** on the 5 blog posts, `isPartOf → /blog/#blog` is now an inline `Blog` node with name and url.
- **`breadcrumb` reference** added to the WebPage node on every page that has a BreadcrumbList (about, contact-us, media-event and the others that lacked it).
- **`articleSection`** changed from "Uncategorized" to the category shown on the blog index: LIT post = Reproductive Immunology; Hindi post and Unexplained Infertility = Fertility Testing & Diagnostics. `keywords` added to the LIT and Unexplained posts.
- **`date_modified: "2026-10-16"`** set on all indexable pages. Without it, the builder writes today's date into the sitemap `lastmod` on every build. Google ignores a `lastmod` that always changes. Update this field only when the page content changes.
- **Titles and descriptions** (all keep "EmbryoGenesis"):

| Page | Old | New |
|---|---|---|
| `/diagnostic/` title | Diagnostic Tests: ERFA, Endo-Immune & EIT \| EmbryoGenesis | **Endometrial Receptivity Test (ERFA), Mohali \| EmbryoGenesis** (59) |
| `/diagnostic/` description | ERFA – The Soil Test, Endo-Immune Test and … sample timing and 7–10 day results. | ERFA – The Soil Test for endometrial receptivity, Endo-Immune Test and Endometrial Infection Test at EmbryoGenesis, Mohali: who each is for, 7–10 day results. (158) |
| ERFA post title | ERFA The Soil Test: Endometrial Receptivity \| EmbryoGenesis | **ERFA – The Soil Test & Embryo Implantation \| EmbryoGenesis** (58). This stops the post competing with `/diagnostic/` for "endometrial receptivity test" and gives it the informational angle of its H1. |
| ERFA post description | … Who it can help. | ERFA – The Soil Test (Endometrial Receptivity & Function Assay) evaluates endometrial biomarkers in the window of implantation: what it checks, who it can help. (160) |
| `/courses/` title | Clinical Embryology Courses, B.Sc. to Ph.D. \| EmbryoGenesis | **Clinical Embryology Courses in Punjab & HP \| EmbryoGenesis** (58), targeting "clinical embryology course Punjab" |
| `/courses/` description | Admission open 2025-26: … | Clinical embryology courses with EmbryoGenesis and ITHS: B.Sc., M.Sc., Ph.D. and PG Diploma at Rayat Bahra University, Mohali, and Bahra University, Himachal. (158). The out-of-date "2025-26" session was removed (today is Oct 2026). |
| `/` description | EmbryoGenesis is an infertility diagnostic … tests and courses. | EmbryoGenesis, infertility diagnostic & research centre in Mohali, Punjab: ERFA endometrial receptivity test, Endo-Immune and EIT tests, and embryology courses. (160) |
| `/contact-us/` description | … visit a collection centre in Mumbai, Udaipur, Jalandhar. | Contact EmbryoGenesis, Rayat Bahra campus, Kharar, Mohali: call or WhatsApp +91 8146217196, email info.embryogenesis@gmail.com, or find a collection centre. (156) |
| `/pulakes-purkait-profile/` description | … patent list, awards and memberships. | Prof. (Dr.) Pulakes Purkait, Founder & Director of EmbryoGenesis, Mohali, reproductive geneticist: biography, education, patent applications and awards. (152). It now says "patent applications" instead of "patent list", in line with guardrail 2. |
| Hindi post description | …EMBRYOGENESIS में… | …EmbryoGenesis में… (brand spelling; the BlogPosting description is synced) |

The other titles were already in range and on-keyword: LIT post "LIT Therapy for Recurrent Pregnancy Loss", EIP post (its description includes "repeated IVF failures"), Unexplained Infertility, both course pages, About, Training and Media. I did not push the therapies page harder for "LIT therapy" because therapy promotion is on legal hold.

### 2.4 llms.txt (rewritten)
It now lists every indexable page, grouped as Main pages / Courses and training / Blog (all 5 posts with dates; the Hindi post is marked) / Optional. It also has a fuller key-facts block, all taken from the sources:
- full address with PIN;
- founder with ORCID, and the pathologist;
- tests, with the ERFA patent application number and sample timing;
- the 7–10 day turnaround;
- named collection centres;
- the programmes with their universities;
- the award;
- phones by role, email, the map link and social handles;
- the medical-information disclaimer;
- the disambiguation from the biological term.

### 2.5 Redirects (`_redirects` and `.htaccess`, rewritten)
- Every old URL from the audit inventory now returns 200 or redirects in one hop. A script checked all 28 URLs against both files.
- **Changed `/research-and-training/`** from `/skill-development-training/` to **`/pulakes-purkait-profile/`**. The old page was only a patent list, and that list now lives on the profile (`#patents`). The training page was a topical mismatch.
- **Added:**
  - the 4 category archives (`/category/erfa-the-soil-test/` → ERFA post; `/category/fertility-testing-diagnostics/` → `/diagnostic/`; `/category/reproductive-immunology/` → EIP post; any other category → `/blog/`);
  - `/author/*` → `/blog/`;
  - `/endometrial-receptivity-analysis`, the old broken canonical → ERFA post;
  - the dead brochure PDF → the Bahra course page;
  - the Rank Math sitemaps (`sitemap_index.xml`, `post-sitemap.xml` and others) → `/sitemap.xml`;
  - `/feed/` → `/blog/`;
  - `/blog/page/*` → `/blog/`.
- **`/cache/`**: Cloudflare Pages `_redirects` does not support status 410, so the old `/cache/ / 410` line would have been rejected. `_redirects` now sends `/cache/` 301 to the EIP post it embedded, which is the audit's stated alternative. `.htaccess` returns 410 Gone.
- `.htaccess` now uses anchored `RedirectMatch` with an optional trailing slash. Before, it used prefix `Redirect`, which missed `/apply-now` without a slash and lacked `/home/`. It is wrapped in `<IfModule mod_alias.c>`, and `ErrorDocument 410` was added.

---

## 3. Checks that passed (no change needed)
- **Canonical** on every page is the absolute https URL with a trailing slash, and it equals `og:url`. The 404 page is noindex.
- **Hindi post:**
  - `<html lang="hi">`, `og:locale hi_IN`, `hreflang="hi-IN"` (self-reference; there is no English equivalent, so no alternates are needed);
  - BlogPosting `inLanguage hi-IN`.
- **Sitemap** has all 17 indexable URLs. It leaves out 404 and privacy-policy (noindex placeholder).
- **OG images:** all 19 exist. The 18 photographic ones are at least 1000 px wide. The founder photo is 350 px (see 6.3).
- **FAQPage** appears only on the 3 pages with a visible FAQ (home, diagnostic, therapies). Every question and answer in the JSON matches the visible text. The diagnostic and therapies FAQs match the old site word for word.
- **Course nodes** (6 university programmes and 8 training courses) all have name, description and provider (`#org`, defined in the same graph). BlogPosting nodes all have headline, image, datePublished and author.
- **Brand spelling** in all titles and descriptions is "EmbryoGenesis". No "best", "No. 1" or "patented" appears in any title, description or schema text; "Best Innovator Award" is the award's proper name.

---

## 4. HTML changes I recommend (for the page owners)
I made no edits to `.html`. Each item gives the file, the current text and the new text.

### 4.1 AEO: question headings and 40–60-word answers

**`site/src/pages/home.html`**
1. Line 7, H1. Current: `<h1>Advanced Fertility Solutions</h1>`. New: `<h1>Advanced Fertility Solutions at EmbryoGenesis, Mohali</h1>`. The H1 carries no entity or location now.
2. FAQ block (`<h2 class="center">FAQs</h2>` + `<!--FAQ-->`). Its 3 Q&As are copied word for word from `/diagnostic/`, and the old home page had no FAQ. That puts duplicate FAQPage markup on two URLs, and Google asks for one instance only.
   - Recommended: replace the block with `<p><a href="/diagnostic/#faqs">Read our diagnostic test FAQs</a></p>`.
   - Then set `"faq": []` in `home.json` (I will do this, or the page owner can).
3. Lines 152–154 ("Real Stories, Real Smiles: Our Patients Speak" + "Testimonials" + the placeholder text "Google Reviews widget (to be reconnected…)").
   - Recommended: remove the whole section until legal review. It is a visible placeholder (thin content) under a heading that promises patient testimonials (guardrail 6).

**`site/src/pages/about.html`**
4. Line 16, under `<h2>What is EmbryoGenesis?</h2>`. The paragraph never defines the entity (it starts "We at EMBRYOGENESIS are committed…").
   - Insert before it: `<p class="answer">EmbryoGenesis – Infertility Diagnostic &amp; Research is an infertility diagnostic and research centre in Mohali, Punjab, established in November 2023 on the top floor of Rayat Bahra Dental College &amp; Hospital, Rayat Bahra University Campus. It offers endometrial diagnostic tests, fertility therapies, and clinical embryology courses with ITHS and partner universities.</p>` (51 words, all from the key facts).
5. Lines 8 and 36 say "Best Innovation Award" and "Best Innovation Awardee". Lines 31 and 47 and the Media page say "Best Innovator Award". Use one form ("Best Innovator Award for Human Infertility Treatment") so AI systems see one fact. The client should confirm the exact award name.

**`site/src/pages/diagnostic.html`**
6. Line 29. Current `<h3 class="sm">What is ERFA?</h3>` → `<h3 class="sm">What is ERFA – The Soil Test?</h3>`. This matches "ERFA test" queries.
7. Line 41. Current `<h3>ERFA – The Soil Test: sample requirements and key facts</h3>` → `<h3>When is the ERFA sample taken, and how soon are results ready?</h3>`. Then add before the `<dl>`:
   - `<p class="answer">ERFA – The Soil Test needs an endometrial biopsy (D&amp;C or needle biopsy) taken on cycle day 21–23, preferably day 21; on LH+7 to LH+9 in a natural cycle; or on P+6 to P+8 in an HRT cycle. Results are typically available within 7–10 days, depending on the complexity of the test.</p>` (50 words, from the key facts list).
8. Line 79. Current `<h3 class="sm">Who should consider this test?</h3>` → `<h3 class="sm">Who should consider the Endometrial Infection Test?</h3>`. As it stands, the heading cannot be quoted out of context.
9. Line 35, typo: `ERFA – The SoiL Test` → `ERFA – The Soil Test`.
10. Line 92, "Experienced Specialists" card. Link "Our team of dedicated experts" to `/about/` and add `Led by <a href="/pulakes-purkait-profile/">Prof. (Dr.) Pulakes Purkait</a>.` This is E-E-A-T and also an internal link to the founder page.

**`site/src/pages/courses.html`**
11. Line 57. Current `<h2 id="compare-h">Eligibility, duration and fee for each programme</h2>` → `<h2 id="compare-h">What are the eligibility, duration and fees for each programme?</h2>`.
12. Lines 5 and 11 ("Admission Open For Session 2025-26"), and the same on both course pages and the training page. The 2025-26 session has ended (today is 16 Oct 2026). Ask the client for the current session (2026-27?) and update every instance.
13. Line 131. The CTA band repeats `<h2>ADMISSION OPEN NOW!</h2>` (the second H2 with this text on the page). Change it to `<p class="h2like">ADMISSION OPEN NOW!</p>` or similar.

**`site/src/pages/art-and-clinical-embryology-in-rayat-bahra-university.html`** and **`bsc-in-clinical-embryology-in-bahra-university.html`**
14. The per-programme answers are 3–8-word fragments ("Duration: 4 Years"). Under the programmes H2, add one summary answer box.
    - Rayat Bahra page: `<h3>Which ART &amp; Clinical Embryology programmes are offered at Rayat Bahra University?</h3><p class="answer">EmbryoGenesis and ITHS offer four programmes at Rayat Bahra University, Mohali: a 4-year B.Sc. (12th with Physics, Chemistry and Biology/Math), a 2-year M.Sc. (B.Sc./B.Tech in Life Sciences, MBBS, BDS), a 3–4-year Ph.D. (post-graduation in a relevant field) and a 1-year PG Diploma (B.Sc./M.Sc. in Life Sciences, MBBS).</p>` (about 55 words).
    - Bahra page, the same pattern: `The BSc in Clinical Embryology at Bahra University, Shimla Hills, runs 4 years for students with 12th in Physics, Chemistry and Biology, at ₹39,875 per semester; the MSc runs 2 years (4 semesters) at INR 1,00,000 per semester.`
15. Bahra page. The MSc block asks "How long…?" before "Who can apply…?", which is the reverse of the BSc order. Swap them so both blocks read the same way.

**`site/src/pages/skill-development-training.html`**
16. Line 47. Current `<h2 id="progs">Training programmes, duration and fee</h2>` → `<h2 id="progs">How long is each training programme, and what is the fee?</h2>`, followed by `<p class="answer">Each hands-on course at EmbryoGenesis, Mohali, runs for 1 to 5 days with 10 seats per batch. Fees range from ₹1,000 for Biochemistry (Semi Auto Analyser, 1 day) to ₹35,000 for Stem Cell Processing &amp; Cryopreservation (1 day).</p>`.

**`site/src/pages/contact-us.html`**
17. Line 11. Current `<h2 class="core-h3">Visit</h2><address>Top Floor, Rayat Bahra Dental College &amp; Hospital, Rayat Bahra University Campus, Kharar, Mohali, Punjab</address>` → `<h2 class="core-h3">Where is EmbryoGenesis located?</h2><address>Top Floor, Rayat Bahra Dental College &amp; Hospital, Rayat Bahra University Campus, VPO Sahauran, Tehsil Kharar, Dist. Mohali, Punjab 140302</address>`. The new address is the brochure version and matches the schema.
18. `<h2 id="centres-h" class="center">Our Collection Centre</h2>` → add below it: `<p class="answer">Besides its central laboratory in Mohali, EmbryoGenesis has sample collection centres in Navi Mumbai, Udaipur and Jalandhar.</p>`. Use the same on `about.html` line 63.

**Blog posts.** The headings end in colons and are not questions:
19. `erfa-the-soil-test-…html`:
    - `Understanding Endometrial Receptivity:` → `What is endometrial receptivity?`
    - `Introducing the “ERFA-The Soil Test: Redefining Fertility Evaluation:` → `What is ERFA – The Soil Test?` (this also fixes the unbalanced quote)
    - `The ERFA-The Soil Test looks at several factors in the endometrium:` → `What does ERFA – The Soil Test assess?`
    - `Indications for the ERFA-The Soil Test` → `Who should consider ERFA – The Soil Test?`
    - In each remaining heading, drop the trailing colon (`Introduction:` → `Introduction`).
20. `exploring-lit-therapy-…html`:
    - `Understanding LIT Therapy:` → `What is LIT therapy?`
    - `How LIT Therapy Supports Fertility:` → `How does LIT therapy work?`
    - `Considerations and Side Effects:` → `What are the side effects of LIT therapy?`
21. `unexplained-infertility.html`:
    - `Symptoms and Causes:` → `What are the symptoms and causes of unexplained infertility?`
    - `Treatment for unexplained infertility:` → `How is unexplained infertility treated?`
    - H4 typo `Uterine Abnormalities Uterine:` → `Uterine Abnormalities`
    - H3 `Diagnosis: – ERFA- Soil Testing:` → `ERFA – The Soil Test`
22. `endometrial-immune-profiling-…html`. The H3 `Women with:` is a fragment used as a heading. Change it to `<p><strong>Women with:</strong></p>`, then add a one-sentence answer under "Who Should Consider Endometrial Immune Profiling?": `EIP is mainly considered for women with repeated IVF failures, recurrent implantation failure or recurrent pregnancy loss.` Use the post's own wording.
23. All posts and the medical pages. Add the review line from guardrail 7 near the byline once the actual sign-off has happened: `Scientifically reviewed by <a href="/pulakes-purkait-profile/">Prof. (Dr.) Pulakes Purkait</a> · <time datetime="YYYY-MM-DD">…</time>`. After that, I will add `reviewedBy` and `lastReviewed` to the MedicalWebPage/BlogPosting schema. I did not add them now because the review is not visible on the page.

### 4.2 Shared partials (owner: core)
24. `site/src/partials/footer.html`:
    - Remove the LinkedIn icon (`https://www.linkedin.com/company/embryogenesis`). The page does not exist (brief section 2), so the icon is a broken entity link on every page. I removed it from the schema.
    - Address line: `Top Floor, Rayat Bahra Dental College &amp; Hospital, Mohali, Punjab` → `Top Floor, Rayat Bahra Dental College &amp; Hospital, Rayat Bahra University Campus, VPO Sahauran, Tehsil Kharar, Mohali, Punjab 140302`. One NAP sitewide.
    - "As the best fertility centre, we believe…": this sitewide superlative appears on all 19 pages (guardrail 1). It is the client's wording; flag it to Jakhar Singh.
25. Header and footer: add `/pulakes-purkait-profile/` ("Our Founder") to the footer Quick Links. This lifts the founder page, the main E-E-A-T asset, from 3 inbound links to 19.

### 4.3 Wording flags for the client (not changed; client's call per the agent brief)
- **Unverifiable superlative or leadership claims:**
  - `home.html` line 38: "India’s trusted infertility diagnostic and research center";
  - lines 37, 60, 91 and 93: "Leaders… / leads… / a leader…";
  - `about.html` line 36: "best fertility diagnostic centre in India";
  - `advanced-fertility-therapies.html` line 72: "Our center leads…";
  - `bsc-…html` line 84: "a leader in…".
- **"Patented":**
  - `erfa-the-soil-test-…html` line 17: "a patented groundbreaking…";
  - `home.html` line 61: "Patented diagnostic test";
  - `about.html` line 44: "LIT -H2 Antioxidant Therapy (Patented)";
  - `art-…html` line 87: "patented technologies".

  Guardrail 2 asks for "patent application published (No. …)".
- **Uncited statistics:** LIT post "8-10% increase in live birth rates"; Unexplained Infertility post "NIH… 92%". Add citations or remove.

---

## 5. Internal linking map and additions
I counted inbound contextual links from page bodies, excluding header and footer:

| Page | Inbound | Status |
|---|---|---|
| `/`, `/contact-us/`, `/diagnostic/`, `/about/`, `/advanced-fertility-therapies/` | 11–18 | Strong |
| `/courses/`, `/bsc-…/`, `/skill-development-training/`, `/blog/` | 7–9 | OK |
| `/art-and-clinical-embryology-…/`, `/erfa-the-soil-test-…/` | 5 | OK |
| `/endometrial-immune-profiling-…/`, `/exploring-lit-therapy-…/`, `/unexplained-infertility/`, `/pulakes-purkait-profile/` | 3 | **Weak** |
| `/tips-and-treatments-for-pregnancy-after-ivf-failure/` (Hindi), `/media-event/` | 2 | **Weak** (`/media-event/` is in the header nav) |

There are no orphans and no broken internal links. Anchors to add:
1. `diagnostic.html` line 32, ERFA "Who is ERFA for?": make "Individuals with unexplained infertility" link to `/unexplained-infertility/` with the anchor "unexplained infertility".
2. `diagnostic.html` line 32: after "Women facing repeated IVF failures…", add the link `<a href="/tips-and-treatments-for-pregnancy-after-ivf-failure/" hreflang="hi" lang="hi">IVF फेलियर के बाद अगले कदम</a> (Hindi)`.
3. `advanced-fertility-therapies.html`, LIT and PBMC "What is…" paragraphs: link "immune-related fertility challenges" to `/endometrial-immune-profiling-what-it-is-why-it-matters-and-who-should-consider-it/` with the anchor "endometrial immune profiling".
4. The "Related at EmbryoGenesis" section of each post:
   - EIP post: add "LIT therapy for recurrent pregnancy loss" → LIT post, and "IVF फेलियर के बाद अगले कदम (Hindi)" → Hindi post.
   - ERFA post: add "unexplained infertility" → Unexplained post.
   - Unexplained post: add "endometrial immune profiling" → EIP post.
5. `home.html` "Our Patents & Recognition" section: add `<a href="/media-event/">See awards and media coverage</a>` and `<a href="/pulakes-purkait-profile/#patents">View the patent applications</a>`.
6. `media-event.html` line 14, the Best Innovator Award card: link it to `/pulakes-purkait-profile/` with the anchor "Prof. (Dr.) Pulakes Purkait".
7. Course pages, the "Expert Faculty" / "Expert Guidance" cards: link "faculty" to `/pulakes-purkait-profile/`.
8. Footer Quick Links: add "Our Founder" (see 4.2, item 25).

---

## 6. Outside my file scope: needs the build.py owner or the client

### 6.1 robots.txt (generated in `build.py` `main()`, not in my editable range)
The current file allows GPTBot, ClaudeBot, PerplexityBot and Google-Extended. It is missing OpenAI's search crawler and the user-triggered fetchers. A named group also overrides `*`, so those bots can currently crawl `/wp-admin/`. Replace the `robots = …` string with:
```
User-agent: *
Allow: /
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /?s=

# AI search and answer engines are welcome (GEO)
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Google-Extended
User-agent: Applebot-Extended
Allow: /
Disallow: /wp-admin/

Sitemap: https://embryogenesis.in/sitemap.xml
```
If the client wants to opt out of AI training, change only the GPTBot, Google-Extended and Applebot-Extended lines to `Disallow: /` (SEO strategy 5.6).

### 6.2 Builder (optional)
The single self-referencing `hreflang` on English pages is harmless but adds nothing. It could be emitted only when a page declares `alternates`. No action is needed now.

### 6.3 Assets for the client
- **Logo for Google:** `logo.png` is 403×102. Google's Organization logo needs at least 112 px on each side, so supply a square emblem logo (512×512 PNG). I will then point `ORG.logo` to it.
- **OG images:** the founder page uses a 350×373 headshot. Supply a 1200×630 version, and ideally a branded 1200×630 default OG card for pages without a hero.
- **To confirm:**
  - the founder's ResearchGate URL (`researchgate.net/profile/Pulakes-Purkait` is used on the profile page and in `PERSON.sameAs`; it returns 403 to bots, so I could not verify it; the old site linked a generic directory page);
  - opening hours (needed for `openingHoursSpecification` and the Google Business Profile);
  - which collection centres are active (website vs brochure conflict).

---

## 7. How to re-check
```
python3 site/build.py && python3 site/qc.py
```
The validator script is at `/tmp/claude-0/-home-user-emb/b14c7f6e-a696-51d0-a38b-d172266186db/scratchpad/seo/validate_ld.py`. Run it with `python3 -I`; it needs `schemaorg.jsonld` in the same folder. It checks:
- types and properties against the schema.org vocabulary, including domain, range and enumeration values;
- dangling `@id` references;
- the required Course and BlogPosting fields;
- that FAQ entries are visible on the page.
