# EmbryoGenesis: SEO Strategy and Technical Specification

**Prepared by:** TechnoTaau Team (SEO Strategist; project lead: Jakhar Singh)
**For:** EmbryoGenesis, Mohali ("Redefining Fertility Evaluation"), https://embryogenesis.in
**Date:** 15 October 2026 | **Version:** 1.0
**Who uses this:** the client's WordPress developer (sections 1, 2, 5, 6), our writers (sections 3, 4, 8, 9), and the project lead and client (sections 7, 10).

**Sources and rules this document follows**
- `docs/00-project-brief.md` sets the binding rules: B2B first, English only, pan-India, WordPress + Rank Math, no test prices, therapies held, no superlatives, "patent application published", and no testimonials.
- `docs/strategy/01-project-blueprint.md` is the master plan. Navigation, timeline and KPIs here match it.
- Evidence comes from `docs/research/01-industry-research.md`, `02-competitor-keyword-social.md` and `03-current-site-audit.md`.
- Search volumes and difficulty are **qualitative**. No keyword-volume tool was available. Re-check them once Search Console has 30 days of data.

**Placeholders.** Anything we do not know yet is written as `{{LIKE_THIS}}`. The full list is in section 11. Nothing in a placeholder may be guessed by the developer or writers.

---

## Contents

1. Information architecture and sitemap
2. 301 redirect map
3. Keyword-to-page map (plus the parked Hindi/Hinglish list)
4. On-page templates
5. Technical SEO specification for the developer
6. Schema plan with JSON-LD templates
7. Entity and brand disambiguation plan
8. GEO / AI-search visibility plan
9. 90-day editorial calendar (24 articles)
10. Off-page and link plan, and KPIs
11. Placeholders and items needing client input

---

## 1. Information architecture and sitemap

### 1.1 Principles

1. **One page, one job, one primary keyword.** Every indexable URL owns a distinct query set, so pages do not compete with each other.
2. **Two layers for the same tests:**
   - `/diagnostics/` explains *what each test is*. Clinicians and patients both use it.
   - `/for-clinicians/` explains *how to work with us*: ordering, protocols, reports and CME.
   - Patient pages always point to "your doctor orders this test", never to self-ordering.
3. **Local pages only where a real collection point exists:** Mohali (main lab), Navi Mumbai, Udaipur and Jalandhar. We add a new city page only when a partner agreement is signed *and* the page has at least 400 words of content unique to that city. Anything less is a doorway page.
4. **Held content stays out of the index and out of navigation.** This covers the therapy pages.
5. **URLs** are short, lowercase and hyphenated, with a trailing slash. There are no dates, no stop-words where avoidable and no file extensions. Blog posts sit under `/blog/`.
6. **Navigation follows the blueprint:**
   - Primary navigation: For Clinicians · Diagnostics · Collection Network · Academy · Research · About · Contact.
   - Header CTA: **Become a Collection Partner**.
   - Utility bar (top right, small): For Patients · For Students · WhatsApp.

### 1.2 What we changed from the draft, and why

| Change | Reason |
|---|---|
| Added `/for-clinicians/order-a-test/` | The draft had no page for the main B2B conversion: kit request, requisition form and pick-up booking. It is the target for "requisition form", "how to send samples" and similar queries, and for the `generate_lead` (form_type = clinician_order) event. |
| Added `/academy/admissions/` | Combines three thin or empty URLs (`/apply-now/`, `/clinical-embryology-scholarship/` and the header "Apply Now" target) into one application page with eligibility, the degree-validity statement, scholarship rules and a DPDP-compliant form that handles applicants under 18. |
| Added `/about/editorial-policy/` | YMYL trust signal: who writes, who reviews, how references are chosen, the update cycle and the corrections policy. Every medical page links to it from the reviewer line. |
| Named the two university program pages `/academy/clinical-embryology-bahra-university/` and `/academy/art-clinical-embryology-rayat-bahra-university/` | Each page puts the program keyword and the **degree-awarding university** in the URL, which ASCI's education guidelines require to be prominent. The current B.Sc. page has a URL/title mismatch (Bahra vs Rayat Bahra); this fixes it. |
| Event pages under `/for-clinicians/cme-webinars/{slug}/` | Each webinar needs its own URL for Event schema, registration and a later recording/recap. |
| `/research/` launches as **one page** with anchored sections (publications, patent applications, awards, collaborations, MoUs) | There is not yet enough content for four sub-pages. We split it out (e.g. `/research/publications/`) once a section passes about 600 words. |
| `/research-programs/` and children stay **WordPress Draft/Private** | This is stronger than noindex. See section 5.5. |
| Blog categories at `/blog/topic/{slug}/`, noindexed until each holds at least 5 posts with intro copy | Prevents the thin-archive problem the audit found. |
| Utility page `/thank-you/` (noindex) | A fallback conversion URL in case JavaScript events fail. It is excluded from the sitemap. |
| **Not added:** "ERA test cost" pages, therapy pages, IVF-centre city pages, `/hi/` Hindi section | Respectively: no prices, legal hold, wrong intent (we are a lab, not an IVF centre), and English only for now (Hindi is parked, see 3.4). |

### 1.3 Sitemap tree

```
embryogenesis.in/
├── /                                                   Home
├── /for-clinicians/                                    For Clinicians hub
│   ├── /for-clinicians/order-a-test/                   (new) kit request, requisition form, pick-up
│   ├── /for-clinicians/sample-collection-protocol/     biopsy timing, handling, transport
│   ├── /for-clinicians/report-interpretation/          sample reports, result categories, limits
│   └── /for-clinicians/cme-webinars/                   CME listing
│       └── /for-clinicians/cme-webinars/{webinar-slug}/   one page per event
├── /partner-with-us/                                   Become a collection centre
├── /collection-centres/                                Collection Network (map + list)
│   ├── /collection-centres/mohali/                     Main lab (Rayat Bahra Dental College & Hospital)
│   ├── /collection-centres/navi-mumbai/                Nirmal Multi Speciality Hospital, Kopar Khairane
│   ├── /collection-centres/udaipur/                    Shree B.L. Jain Memorial Hospital, Savina
│   └── /collection-centres/jalandhar/                  Advance Fertility Services & IVF Centre, Shakuntala Devi VIG Hospital
├── /diagnostics/                                       Test menu hub
│   ├── /diagnostics/endometrial-infection-test/        EIT (chronic endometritis): lead test
│   ├── /diagnostics/erfa-endometrial-receptivity-test/ ERFA "The Soil Test"
│   ├── /diagnostics/endo-immune-test/                  uNK / cytokine profile
│   └── /diagnostics/receptivity-px/                    Receptivity PX
├── /patients/                                          Patients hub
│   ├── /patients/repeated-ivf-failure/
│   ├── /patients/recurrent-miscarriage/
│   └── /patients/how-to-get-tested/
├── /research/                                          Publications, patent applications, awards, collaborations
├── /research-programs/                                 HELD: Draft/Private, noindex, not in sitemap or nav
│   └── /research-programs/{program}/                   HELD (LIT, PBMC, PRP, molecular hydrogen; see 5.5 on stem cells)
├── /academy/                                           Academy hub
│   ├── /academy/clinical-embryology-bahra-university/
│   ├── /academy/art-clinical-embryology-rayat-bahra-university/
│   ├── /academy/lab-training/
│   └── /academy/admissions/                            (new) apply, eligibility, scholarships, degree validity
├── /about/
│   ├── /about/pulakes-purkait/
│   ├── /about/team/
│   └── /about/editorial-policy/                        (new) review and corrections policy
├── /news-events/
│   └── /news-events/{slug}/                            MoUs, awards, conference talks
├── /blog/
│   ├── /blog/{post-slug}/
│   └── /blog/topic/{for-clinicians | patient-education | embryology-careers}/   noindex until ≥5 posts
├── /contact/
├── /privacy-policy/
├── /terms/
├── /medical-disclaimer/
└── /thank-you/                                         utility, noindex
```

### 1.4 Page table

Intent codes: I = informational, C = commercial investigation, T = transactional, N = navigational, L = local.

| URL | Page purpose | Primary audience | Primary keyword | Secondary keywords | Intent | Primary CTA |
|---|---|---|---|---|---|---|
| `/` | Says what EmbryoGenesis is in one screen; four "doors" (clinicians, partners, couples, students) | Clinicians, partners | endometrial diagnostics lab india | embryogenesis mohali; fertility diagnostic lab; endometrial testing for ivf clinics | N / C | Become a Collection Partner |
| `/for-clinicians/` | Hub for referring doctors: test menu by indication, logistics, turnaround, evidence summaries | IVF clinicians, embryologists | endometrial testing for ivf clinics | send-out endometrial tests; referral lab for ivf clinics; RIF diagnostic lab india | C | Order a test / request a kit |
| `/for-clinicians/order-a-test/` | Kit request, requisition form (PDF), pick-up booking, partner rate card on request | Clinicians, clinic coordinators | endometrial test requisition form | how to send endometrial biopsy to lab; request sample kit | T | Request kit (form) |
| `/for-clinicians/sample-collection-protocol/` | Biopsy timing (natural cycle, HRT), sample handling, transport media, temperature, packing, rejection criteria | Clinicians, embryologists, nurses | endometrial biopsy timing for receptivity test | LH+7 biopsy; P+5 biopsy; endometrial biopsy transport medium; sample rejection criteria | I (pro) | Download protocol PDF |
| `/for-clinicians/report-interpretation/` | Sample reports with result categories, what each result can and cannot tell, next-step considerations | Clinicians | endometrial receptivity report interpretation | receptive vs pre-receptive; CD138 report interpretation; uNK report | I (pro) | Book a report discussion call |
| `/for-clinicians/cme-webinars/` | Upcoming and past CME sessions, recordings, slides | Clinicians, embryologists | ivf cme webinar india | reproductive medicine cme online; embryology webinar india | C | Register for next webinar |
| `/for-clinicians/cme-webinars/{slug}/` | One event: speakers, agenda, registration, then recording and recap | Clinicians | {topic} cme webinar | topic terms | T | Register |
| `/partner-with-us/` | Explains the collection-centre model: what partners get (kits, training, logistics, reports), steps, requirements, FAQ | Hospital and IVF-clinic owners, administrators | diagnostic collection centre partnership | fertility lab partnership; become a sample collection centre; collection centre franchise (answered in FAQ: "this is a partnership, not a franchise"); lab partnership for ivf clinics | C / T | Partner enquiry form |
| `/collection-centres/` | Map and list of collection points; how sample collection works | Clinicians, patients | endometrial biopsy test collection centre | embryogenesis centres; endometrial biopsy test near me | L / N | Find your nearest centre / WhatsApp |
| `/collection-centres/mohali/` | Main lab: address, directions, hours, what happens on-site, lab team, GBP landing page | Clinicians (Punjab/Chandigarh tricity), patients | fertility diagnostic lab mohali | endometrial biopsy test mohali; endometrial receptivity test chandigarh; chronic endometritis test punjab | L | Call / WhatsApp / directions |
| `/collection-centres/navi-mumbai/` | Partner collection point at Nirmal Multi Speciality Hospital, Kopar Khairane | Clinicians and patients in Navi Mumbai and Mumbai | endometrial receptivity test navi mumbai | chronic endometritis test mumbai; endometrial biopsy test kopar khairane | L | Contact collection point |
| `/collection-centres/udaipur/` | Partner collection point at Shree B.L. Jain Memorial Hospital, Savina | Clinicians and patients in south Rajasthan | endometrial receptivity test udaipur | chronic endometritis test udaipur; endometrial biopsy test rajasthan | L | Contact collection point |
| `/collection-centres/jalandhar/` | Partner collection point at Advance Fertility Services & IVF Centre, Shakuntala Devi VIG Hospital | Clinicians and patients in Doaba / Punjab | endometrial receptivity test jalandhar | chronic endometritis test jalandhar; endometrial biopsy test jalandhar | L | Contact collection point |
| `/diagnostics/` | Test menu with an indication table (test, what it looks at, sample, timing, turnaround, evidence status) | Clinicians, patients | endometrial tests for ivf failure | endometrial biopsy tests; endometrial receptivity and immune tests; fertility diagnostic tests india | C | Order a test (clinicians) / How to get tested (patients) |
| `/diagnostics/endometrial-infection-test/` | EIT: chronic endometritis testing. **Lead test** (ESHRE RIF 2023: assessment "can be considered") | Clinicians first, patients second | chronic endometritis test | chronic endometritis test lab india; CD138 testing; CD138 immunohistochemistry endometrium; endometrial infection test | C | Order this test |
| `/diagnostics/erfa-endometrial-receptivity-test/` | ERFA "The Soil Test": what it measures, who it is for, limits, evidence box (ESHRE: insufficient data for routine use), patent application published (No. 202431001616 A) | Clinicians | endometrial receptivity test | endometrial receptivity test lab; ERA test alternative india; ERFA test; window of implantation test; soil test ivf | C | Order this test |
| `/diagnostics/endo-immune-test/` | Endo-Immune Test (uNK / cytokine profile): specialised, clinician-directed; evidence box (ESHRE: not recommended routinely) | Clinicians | endometrial immune profiling | uterine NK cell test; uNK cell testing; endometrial cytokine profile; reproductive immunology test india | C | Discuss with our team |
| `/diagnostics/receptivity-px/` | Receptivity PX: what it measures and how it differs from ERFA; patent application published (No. 202411059621 A); evidence box | Clinicians | receptivity px | endometrial receptivity biomarker test; endometrial receptivity and immune competency | C / N | Order this test |
| `/patients/` | Plain-English hub: "your doctor can order these tests"; how testing fits into treatment | Couples | tests after failed ivf | fertility tests for women after ivf failure; endometrial tests explained | I | How to get tested |
| `/patients/repeated-ivf-failure/` | What repeated IVF failure / RIF means, common causes, which tests to discuss with your doctor, what the evidence says | Couples | repeated ivf failure | ivf failure what next; multiple ivf failure; repeated implantation failure; implantation failure reasons | I | Download "questions to ask your doctor" checklist |
| `/patients/recurrent-miscarriage/` | Recurrent pregnancy loss: guideline-backed tests (ESHRE 2022), where endometrial testing fits and where it does not | Couples | recurrent miscarriage tests | recurrent miscarriage causes; recurrent pregnancy loss testing; tests after 2 miscarriages | I | Questions-to-ask checklist |
| `/patients/how-to-get-tested/` | Step by step: doctor referral, biopsy day, what it feels like, sample travel, report to your doctor; collection points | Couples | endometrial biopsy test procedure | how is endometrial biopsy done; endometrial biopsy pain; endometrial biopsy test near me | I / T | Find a collection centre / WhatsApp |
| `/research/` | Publications, patent applications (exact wording), awards, collaborations, MoUs | Clinicians, journalists, students | embryogenesis research | pulakes purkait publications; ERFA patent application; endometrial receptivity research india | N / I | Collaborate with us |
| `/research-programs/` (+ children) | HELD therapy and research-program drafts | n/a | none (not indexed) | none | n/a | none |
| `/academy/` | Academy hub: university programs, lab training, careers, admissions | Students, parents, working professionals | clinical embryology course in punjab | embryology course chandigarh; embryology course mohali; clinical embryology courses india; b.sc clinical embryology; m.sc clinical embryology | C | Apply / download brochure |
| `/academy/clinical-embryology-bahra-university/` | B.Sc./M.Sc. Clinical Embryology with ITHS + Bahra University (Shimla Hills, HP): awarding university, campus, eligibility, duration, syllabus, fees (if approved), FAQ | Students, parents | clinical embryology course bahra university | b.sc clinical embryology himachal pradesh; m.sc clinical embryology shimla | C / T | Apply |
| `/academy/art-clinical-embryology-rayat-bahra-university/` | B.Sc./M.Sc. ART & Clinical Embryology with ITHS + Rayat Bahra University (Mohali); PG Diploma / Ph.D. only if still current | Students, parents | art and clinical embryology course mohali | m.sc clinical embryology punjab; b.sc art and clinical embryology; rayat bahra university clinical embryology | C / T | Apply |
| `/academy/lab-training/` | Short hands-on courses: modules, duration, eligibility, batch size, certificate. **Diagnostic-lab modules only at launch** (see 5.5) | Graduates, lab staff, clinic staff | embryology hands-on training | immunohistochemistry training course; tissue processing and microtomy training; molecular genetics hands-on training chandigarh | C / T | Enquire / apply |
| `/academy/admissions/` | Application form, eligibility, degree-validity statement, scholarship rules, dates | Students, parents | clinical embryology admission 2027 | clinical embryology scholarship; apply clinical embryology course | T | Submit application |
| `/about/` | Who we are, the disambiguation line, mission, facilities, accreditations, timeline | All | embryogenesis mohali | embryogenesis lab; about embryogenesis | N | Contact |
| `/about/pulakes-purkait/` | Founder profile: qualifications, ORCID, publications, awards, patent applications | All, journalists | pulakes purkait | prof pulakes purkait; pulakes purkait embryogenesis | N | View publications |
| `/about/team/` | Team with roles, qualifications, registration numbers where applicable | All | embryogenesis team | Dr. Vidhu Wadhwa pathologist; Dr. Meenu Bhanot embryologist | N | Contact |
| `/about/editorial-policy/` | How content is written, reviewed, referenced and corrected | All, raters | (none) | medical review policy | N | n/a |
| `/news-events/` + `/news-events/{slug}/` | MoUs (e.g. Guru Ghasidas Vishwavidyalaya, Nov 2024), awards, conference talks, new partner centres | All, press | embryogenesis news | embryogenesis mou; embryogenesis award | N | Press contact |
| `/blog/` + posts | Evidence-honest articles (see section 9) | Split by topic | per article | per article | I | Contextual per article |
| `/contact/` | One primary phone, WhatsApp, email, address with PIN, map, forms by audience | All | contact embryogenesis | embryogenesis phone number; embryogenesis address | N | Contact form / WhatsApp |
| `/privacy-policy/`, `/terms/`, `/medical-disclaimer/` | Legal pages (DPDP notice, grievance officer, disclaimer) | All | none | none | N | n/a |
| `/thank-you/` | Form confirmation (noindex) | All | none | none | n/a | Next step links |

### 1.5 Internal linking rules (for writers and the developer)

- **Hub and spoke.** Every child page links up to its hub (breadcrumb plus one in-copy link). Every hub links to all its children.
- **Test pages** link to:
  - `/for-clinicians/sample-collection-protocol/`
  - `/for-clinicians/report-interpretation/`
  - `/for-clinicians/order-a-test/`
  - the matching patient page
  - `/collection-centres/`
- **Patient pages** link to the relevant test page (in a "What your doctor may discuss" box) and to `/patients/how-to-get-tested/`. They never link to ordering forms or to `/research-programs/`.
- **City pages** link to all four test pages, `/patients/how-to-get-tested/` and `/partner-with-us/` ("Want to become a collection point in your city?").
- **Academy** is its own silo. Academy pages link to each other, to `/research/` and to `/about/pulakes-purkait/`, and lightly to `/diagnostics/` (lab context). Do not link from academy pages into patient pages.
- **Blog posts:**
  - 1 link to the target page in section 9, placed in the first 150 words;
  - 2–4 contextual links to related posts or pages;
  - descriptive anchor text, never "click here".
- **Nothing links to held pages,** in navigation, footer, content or the sitemap.
- **Footer** carries:
  - NAP (one phone, WhatsApp, email, address with PIN);
  - the main hubs;
  - the three legal pages;
  - social links;
  - a dynamic © year.

---

## 2. 301 redirect map

**How to implement**
- Use Rank Math > Redirections (module on; type 301, or 410 where stated; match "Exact"). The `.htaccess` alternative is in 2.3.
- Every redirect must reach a **200 page in one hop**. Update internal links to the new URLs so the site itself never relies on a redirect.
- Before launch, crawl the old URL list with Screaming Frog in list mode and confirm "single 301 → 200" for every row.

### 2.1 Every URL in the audit inventory

| # | Old URL | New URL | Code | Note |
|---|---|---|---|---|
| 1 | `/` | `/` | — | Rebuilt in place. Fix H1, title, meta and images. |
| 2 | `/bsc-in-clinical-embryology-in-bahra-university/` | `/academy/clinical-embryology-bahra-university/` | 301 | Fixes the Bahra vs Rayat Bahra title mismatch |
| 3 | `/art-and-clinical-embryology-in-rayat-bahra-university/` | `/academy/art-clinical-embryology-rayat-bahra-university/` | 301 | |
| 4 | `/pulakes-purkait-profile/` | `/about/pulakes-purkait/` | 301 | Fix the malformed tel link, the LinkedIn `%20` and the ResearchGate link |
| 5 | `/contact-us/` | `/contact/` | 301 | Remove the "Best" title |
| 6 | `/media-event/` | `/news-events/` | 301 | |
| 7 | `/courses/` | `/academy/` | 301 | Header "Apply Now" now points to `/academy/admissions/` |
| 8 | `/diagnostic/` | `/diagnostics/` | 301 | Remove "best" / "most accurate" |
| 9 | `/about/` | `/about/` | — | Rebuilt in place |
| 10 | `/skill-development-training/` | `/academy/lab-training/` | 301 | Therapy-related modules held (see 5.5) |
| 11 | `/advanced-fertility-therapies/` | `/research/` | 301 | **Never** redirect to `/research-programs/` (held). `/research/` has a neutral "research programs under review" line with no therapy claims. |
| 12 | `/research-and-training/` | `/research/` | 301 | Patent list moves here with corrected wording |
| 13 | `/blog/` | `/blog/` | — | Rebuilt in place |
| 14 | `/diagnostic-services/` | `/diagnostics/` | 301 | Duplicate template page |
| 15 | `/clinical-embryology-scholarship/` | `/academy/admissions/` | 301 | Scholarship section lives here (anchor `#scholarships` in copy, not in the redirect) |
| 16 | `/privacy-policy/` | `/privacy-policy/` | — | Rewrite with a full DPDP notice |
| 17 | `/apply-now/` | `/academy/admissions/` | 301 | |
| 18 | `/endometrial-immune-profiling-what-it-is-why-it-matters-and-who-should-consider-it/` | `/diagnostics/endo-immune-test/` | 301 | Merge its useful "Limitations" section into the test page; add citations |
| 19 | `/cache/` | none | **410** | Junk oEmbed post. Delete the post, then return 410 Gone. |
| 20 | `/exploring-lit-therapy-treatment-for-recurrent-pregnancy-loss/` | `/patients/recurrent-miscarriage/` | 301 | Unpublish the post (therapy promotion, uncited "8–10%" claim). The target page explains the ESHRE 2022 position on LIT neutrally. |
| 21 | `/tips-and-treatments-for-pregnancy-after-ivf-failure/` | `/patients/repeated-ivf-failure/` | 301 | Hindi post; English-only site for now. **Export the Hindi text** to `content/parked/hindi/` as seed copy for the Hindi phase. |
| 22 | `/unexplained-infertility/` | `/blog/unexplained-infertility/` | 301 | Rewritten (calendar item 23). Remove the uncited "NIH 92%" claim; close comments. |
| 23 | `/erfa-the-soil-test-endometrial-receptivity-analysis-optimize-fertility-success/` | `/diagnostics/erfa-endometrial-receptivity-test/` | 301 | Flagship ERFA content merges into the test page. Replace "patented" with "patent application published". |
| 24 | `/category/uncategorized/` | `/blog/` | 301 | |
| 25 | `/category/erfa-the-soil-test/` | `/diagnostics/erfa-endometrial-receptivity-test/` | 301 | |
| 26 | `/category/fertility-testing-diagnostics/` | `/diagnostics/` | 301 | |
| 27 | `/category/reproductive-immunology/` | `/diagnostics/endo-immune-test/` | 301 | |
| 28 | `/author/embryosys/` | `/blog/` | 301 | Also rename the admin display name and disable author archives (5.1) |

### 2.2 Extra URLs found in the audit (not in the inventory table but live or referenced)

| Old URL | New URL | Code | Note |
|---|---|---|---|
| `/endometrial-receptivity-analysis` (and `/endometrial-receptivity-analysis/`) | `/diagnostics/erfa-endometrial-receptivity-test/` | 301 | The broken canonical of the ERFA post pointed here. Redirecting it recovers any signals Google stored. |
| `/Clinical_Embryology-Brochure-2025-2026-Bahra_University.pdf` | `/academy/clinical-embryology-bahra-university/` | 301 | The old brochure is a 404. Upload the new brochure to `/wp-content/uploads/academy/clinical-embryology-bahra-university-brochure.pdf` and link it from the page. |
| `/courses` (no slash) and every non-slash variant | slash version | 301 | Already handled by WordPress; keep. |
| `//{any-path}` (double slash) | single-slash path | 301 | Server already does this. **Also** run a search-replace of `embryogenesis.in//` → `embryogenesis.in/` in the database so no content or OG tag uses it. |
| `/sitemap.xml`, `/wp-sitemap.xml` | `/sitemap_index.xml` | 301 | Keep the existing Rank Math behaviour. |
| `/?s={query}` | — | noindex | Not a redirect. Noindex via Rank Math (5.1). |
| Attachment pages (`/?attachment_id=…`, `/{post}/{image-name}/`) | parent post / file | 301 | Rank Math "Redirect attachments" setting. |
| `/feed/`, `/comments/feed/` | — | — | Leave. Disable comment feeds if comments are off site-wide. |

**Do not redirect** broken image URLs to pages. Restore them or drop them (section 5.10).

### 2.3 `.htaccess` alternative (LiteSpeed, mod_alias)

Place this **above** the `# BEGIN WordPress` block. Anchored patterns avoid prefix-matching surprises.

```apache
# EmbryoGenesis rebuild redirects (TechnoTaau Team, Oct 2026)
RedirectMatch 301 ^/bsc-in-clinical-embryology-in-bahra-university/?$ /academy/clinical-embryology-bahra-university/
RedirectMatch 301 ^/art-and-clinical-embryology-in-rayat-bahra-university/?$ /academy/art-clinical-embryology-rayat-bahra-university/
RedirectMatch 301 ^/pulakes-purkait-profile/?$ /about/pulakes-purkait/
RedirectMatch 301 ^/contact-us/?$ /contact/
RedirectMatch 301 ^/media-event/?$ /news-events/
RedirectMatch 301 ^/courses/?$ /academy/
RedirectMatch 301 ^/diagnostic/?$ /diagnostics/
RedirectMatch 301 ^/diagnostic-services/?$ /diagnostics/
RedirectMatch 301 ^/skill-development-training/?$ /academy/lab-training/
RedirectMatch 301 ^/advanced-fertility-therapies/?$ /research/
RedirectMatch 301 ^/research-and-training/?$ /research/
RedirectMatch 301 ^/clinical-embryology-scholarship/?$ /academy/admissions/
RedirectMatch 301 ^/apply-now/?$ /academy/admissions/
RedirectMatch 301 ^/endometrial-immune-profiling-what-it-is-why-it-matters-and-who-should-consider-it/?$ /diagnostics/endo-immune-test/
RedirectMatch 301 ^/exploring-lit-therapy-treatment-for-recurrent-pregnancy-loss/?$ /patients/recurrent-miscarriage/
RedirectMatch 301 ^/tips-and-treatments-for-pregnancy-after-ivf-failure/?$ /patients/repeated-ivf-failure/
RedirectMatch 301 ^/unexplained-infertility/?$ /blog/unexplained-infertility/
RedirectMatch 301 ^/erfa-the-soil-test-endometrial-receptivity-analysis-optimize-fertility-success/?$ /diagnostics/erfa-endometrial-receptivity-test/
RedirectMatch 301 ^/endometrial-receptivity-analysis/?$ /diagnostics/erfa-endometrial-receptivity-test/
RedirectMatch 301 ^/category/uncategorized/?$ /blog/
RedirectMatch 301 ^/category/erfa-the-soil-test/?$ /diagnostics/erfa-endometrial-receptivity-test/
RedirectMatch 301 ^/category/fertility-testing-diagnostics/?$ /diagnostics/
RedirectMatch 301 ^/category/reproductive-immunology/?$ /diagnostics/endo-immune-test/
RedirectMatch 301 ^/author/embryosys/?$ /blog/
RedirectMatch 301 ^/Clinical_Embryology-Brochure-2025-2026-Bahra_University\.pdf$ /academy/clinical-embryology-bahra-university/
RedirectMatch 410 ^/cache/?$
```

Use **either** Rank Math or `.htaccess` for each rule, never both. Rank Math is easier for the client to maintain; `.htaccess` is faster. Our recommendation is `.htaccess` for this launch set and Rank Math for anything added later.

---

## 3. Keyword-to-page map

### 3.1 How to read this

- **Tier 1:** conversion-critical or brand terms we can win. Their pages ship at launch.
- **Tier 2:** support and traffic terms. Months 1–3.
- **Tier 3:** harder head terms. Months 4–6, after authority builds.
- **Vol and KD** are qualitative and relative within this niche (Very low / Low / Med / High). They come from autocomplete checks and SERP review in research doc 02.
- **B2B terms have very low search volume.** We target them because one partner clinic is worth more than thousands of visits, and because AI assistants answer these questions from pages like ours. Judge them on enquiries, not sessions.
- One primary keyword per page. Secondary terms go in H2s, FAQs and body copy, never as the H1 of another page.

### 3.2 English keyword map

**A. Clinician and B2B (primary business goal)**

| Keyword | Intent | Vol | KD | Audience | Target URL | Tier |
|---|---|---|---|---|---|---|
| chronic endometritis test lab india | C | Very low | Low | Clinician | `/diagnostics/endometrial-infection-test/` | 1 |
| chronic endometritis test | I / C | Med | Med | Clinician, patient | `/diagnostics/endometrial-infection-test/` | 1 |
| CD138 testing / CD138 immunohistochemistry endometrium | I (pro) | Low | Low | Clinician, pathologist | `/diagnostics/endometrial-infection-test/` + blog C4 | 1 |
| cd138 plasma cells endometrium cut-off | I (pro) | Low | Low | Clinician | blog C4 | 2 |
| chronic endometritis diagnosis (biopsy vs hysteroscopy) | I (pro) | Low | Low–Med | Clinician | blog C1 | 2 |
| endometrial receptivity test | I / C | Med | Med | Clinician, patient | `/diagnostics/erfa-endometrial-receptivity-test/` | 1 |
| endometrial receptivity test lab (india) | C | Low | Low–Med | Clinician | `/diagnostics/erfa-endometrial-receptivity-test/` | 1 |
| ERA test alternative india | C | Low | Low | Clinician | `/diagnostics/erfa-endometrial-receptivity-test/` + blog C5 | 1 |
| window of implantation test | I | Med | Med | Both | `/diagnostics/erfa-endometrial-receptivity-test/` | 2 |
| is endometrial receptivity testing worth it / evidence | I | Med | Med | Both | blog C6 | 2 |
| endometrial biopsy timing for receptivity test; LH+7 biopsy; P+5 biopsy | I (pro) | Low | Low | Clinician | `/for-clinicians/sample-collection-protocol/` | 1 |
| endometrial biopsy transport medium / sample shipping | I (pro) | Very low | Low | Clinician, nurse | `/for-clinicians/sample-collection-protocol/` + blog C12 | 2 |
| endometrial receptivity report interpretation; receptive vs pre-receptive | I | Low–Med | Low–Med | Clinician, patient | `/for-clinicians/report-interpretation/` + blog C7 | 1 |
| endometrial immune profiling | I | Low | Low | Clinician | `/diagnostics/endo-immune-test/` | 1 |
| uterine NK cell test; uNK cell testing | I | Low–Med | Low–Med | Clinician | `/diagnostics/endo-immune-test/` + blog C8 | 1 |
| reproductive immunology lab india | C | Low | Med | Clinician | `/diagnostics/endo-immune-test/` | 2 |
| endometrial cytokine profile | I (pro) | Very low | Low | Clinician | `/diagnostics/endo-immune-test/` | 3 |
| receptivity px; erfa test; soil test ivf | N | Very low | None | Both | respective test pages | 1 (brand) |
| endometrial testing for ivf clinics; send-out endometrial tests; referral lab for ivf clinics | C | Very low | Low | Clinician | `/for-clinicians/` | 1 |
| endometrial test requisition form; request sample kit | T | Very low | None | Clinic staff | `/for-clinicians/order-a-test/` | 1 |
| repeated implantation failure workup / investigations | I (pro) | Low–Med | Med | Clinician | blog C11 → `/for-clinicians/` | 2 |
| fertility lab partnership | C | Very low | Low | Partner | `/partner-with-us/` | 1 |
| diagnostic collection centre partnership; become a sample collection centre | C / T | Low | Low–Med | Partner | `/partner-with-us/` | 1 |
| collection centre franchise for diagnostics; pathology lab franchise | C / T | Med | High (franchise ads dominate) | Partner | `/partner-with-us/` (FAQ answers "Is this a franchise?") | 2 |
| send-out testing for small ivf clinics | I | Very low | Low | Clinician, owner | blog C9 | 2 |
| ivf cme webinar india; reproductive medicine cme online | C | Low | Low | Clinician | `/for-clinicians/cme-webinars/` | 2 |

**B. Brand and entity**

| Keyword | Intent | Vol | KD | Target URL | Tier |
|---|---|---|---|---|---|
| embryogenesis mohali; embryogenesis lab; embryogenesis diagnostics | N | Low | Med (results crowded by the biology term) | `/` | 1 |
| pulakes purkait; prof pulakes purkait | N | Low | Low | `/about/pulakes-purkait/` | 1 |
| ERFA patent application; embryogenesis research | N | Very low | None | `/research/` | 2 |

**C. Local (only where a real collection point exists)**

| Keyword | Intent | Vol | KD | Target URL | Tier |
|---|---|---|---|---|---|
| fertility diagnostic lab mohali | L | Low | Low | `/collection-centres/mohali/` | 1 |
| endometrial biopsy test mohali / chandigarh; endometrial receptivity test chandigarh | L | Low | Low | `/collection-centres/mohali/` | 2 |
| chronic endometritis test punjab | L | Very low | Low | `/collection-centres/mohali/` | 2 |
| endometrial receptivity test jalandhar; chronic endometritis test jalandhar | L | Very low | Low | `/collection-centres/jalandhar/` | 2 |
| endometrial receptivity test navi mumbai; chronic endometritis test mumbai | L | Low | Low–Med | `/collection-centres/navi-mumbai/` | 2 |
| endometrial receptivity test udaipur | L | Very low | Low | `/collection-centres/udaipur/` | 2 |
| endometrial biopsy test near me | L | Low–Med | Low–Med | `/collection-centres/` | 2 |

**D. Patient education (English)**

| Keyword | Intent | Vol | KD | Target URL | Tier |
|---|---|---|---|---|---|
| repeated ivf failure; multiple ivf failure | I | Med | Med | `/patients/repeated-ivf-failure/` | 2 |
| ivf failure what next; tests after failed ivf | I | High | Med–High | `/patients/repeated-ivf-failure/` + blog P1 | 2 |
| ivf failure reasons | I | High | High | `/patients/repeated-ivf-failure/` | 3 |
| repeated implantation failure (patient angle) | I | Med | Med–High | `/patients/repeated-ivf-failure/` | 3 |
| recurrent miscarriage tests; recurrent miscarriage causes | I | Med | Med–High | `/patients/recurrent-miscarriage/` + blog P3 | 2 |
| chronic endometritis symptoms | I | Med | Med | blog P2 | 2 |
| endometrial biopsy procedure; endometrial biopsy pain | I | Med | Med | `/patients/how-to-get-tested/` + blog P4 | 2 |
| thin endometrium causes | I | Med–High | Med | blog P5 | 3 |
| unexplained infertility tests | I | Med | Med | blog P6 (`/blog/unexplained-infertility/`) | 3 |

**E. Academy**

| Keyword | Intent | Vol | KD | Target URL | Tier |
|---|---|---|---|---|---|
| clinical embryology course in punjab; embryology course in punjab | C / L | Low–Med | Low | `/academy/` | 1 |
| embryology course chandigarh / mohali | C / L | Low | Low | `/academy/` | 1 |
| m.sc clinical embryology punjab; art and clinical embryology course mohali | C / L | Low | Low–Med | `/academy/art-clinical-embryology-rayat-bahra-university/` | 1 |
| rayat bahra university clinical embryology; b.sc art and clinical embryology | N / C | Low | Low | `/academy/art-clinical-embryology-rayat-bahra-university/` | 1 |
| bahra university clinical embryology; clinical embryology course himachal pradesh | N / L | Very low | Low | `/academy/clinical-embryology-bahra-university/` | 1 |
| embryology hands-on training; ivf lab training course | C | Low–Med | Low–Med | `/academy/lab-training/` | 1 |
| immunohistochemistry training course; tissue processing and microtomy training | C | Low | Low | `/academy/lab-training/` | 2 |
| b.sc clinical embryology; m.sc clinical embryology (generic) | C | Med | Med–High | `/academy/` + blog A1 | 2 |
| how to become an embryologist after 12th; embryologist course | I | Med | Med | blog A3 | 2 |
| clinical embryology salary in india; embryologist salary per month | I | High | Med | blog A4 | 2 |
| is clinical embryology degree valid / ugc approved | I | Low | Low | blog A5 → `/academy/admissions/` | 2 |
| clinical embryology admission 2027; clinical embryology scholarship | T | Low | Low | `/academy/admissions/` | 2 |
| clinical embryology courses in india | C | Med–High | High (Careers360, Shiksha) | `/academy/` | 3 |

### 3.3 Excluded or deferred keywords (do not target)

| Keyword group | Why |
|---|---|
| ivf centre / hospital / clinic in mohali, chandigarh or jalandhar; best ivf centre … | Wrong intent: EmbryoGenesis is a lab, not an IVF centre. The chains dominate these. |
| era test cost / price; endometrial biopsy test price; nk cell test price | No prices are published (client decision). These pages would not satisfy intent. Revisit only if pricing policy changes. |
| lit therapy …; prp for thin endometrium / ovarian rejuvenation; pbmc therapy; stem cell therapy for infertility; molecular hydrogen therapy | Therapies held pending legal review. Stem cell promotion is barred (NMC advisory, 5 Sep 2026; ICMR). |
| "ERA test" as a page title or H1 | ERA is a third-party trademark (Igenomix). Use it only descriptively ("an alternative to imported receptivity panels such as ERA"). |
| Anything with "best", "No. 1", "most accurate", "guaranteed", "success rate" | Compliance guardrail 1. |
| Any sex-selection or gender-of-baby term | PCPNDT Act and ART Act s.32. Never. |
| icsi training course; vitrification course | No such module exists yet. Parked until the academy adds one. |

### 3.4 Parked: Hindi and Hinglish opportunities (later phase)

These are among the clearest gaps in the market (research doc 02, finding 3), but the site is English only for now. Keep this list for Phase 2.

| Keyword (as typed) | Script | Vol | KD | Future page |
|---|---|---|---|---|
| ivf fail hone ke baad kya kare | Hinglish | High | Low–Med | `/hi/ivf-fail-hone-ke-baad-kya-kare/` |
| ivf fail hone ke karan; ivf fail kyu hota hai | Hinglish | High | Low–Med | same page |
| आईवीएफ फेल होने के बाद क्या करें; आईवीएफ फेल होने के कारण | Devanagari | Med | Low | same page (Hindi) |
| garbh nahi thaharta hai to kya kare; garbh kyu nahi thaharta | Hinglish | Med | Low | `/hi/garbh-nahi-thaharta/` |
| bar bar miscarriage kyu hota hai; bar bar miscarriage ho to kya kare | Hinglish | High | Low | `/hi/bar-bar-miscarriage/` |
| recurrent miscarriage meaning in hindi | Mixed | Med | Low | glossary |
| endometrium patla hone ke karan; bachedani ki parat patli | Hinglish | Med | Low | `/hi/endometrium-patla/` (evidence-honest; no PRP promotion) |
| chronic endometritis in hindi | Mixed | Low–Med | Low | Hindi EIT explainer |
| endometrial biopsy kaise hota hai | Hinglish | Low–Med | Low | Hindi "how to get tested" |
| implantation failure symptoms in hindi | Mixed | Med | Low | Hindi RIF explainer |
| era test kya hota hai | Hinglish | Med | Low | Hindi receptivity explainer (descriptive use of "ERA" only) |
| embryologist kaise bane; clinical embryology kya hai | Hinglish | Med (YouTube-heavy) | Low | Hindi academy page + YouTube |

**Phase 2 set-up notes:**
- Use a `/hi/` subfolder with reciprocal `hreflang` (`en-IN`, `hi-IN`, `x-default`). Use Polylang or TranslatePress, not machine translation without review.
- Appoint a Hindi-fluent medical reviewer.
- Seed copy is the exported old Hindi post (redirect #21).
- Punjabi (Gurmukhi) is for social and local trust, not SEO.

---

## 4. On-page templates

**Rules for every template**
- One H1. The title tag ≤ 60 characters and the meta description 140–155 characters.
- Brand suffix ` | EmbryoGenesis` (separator `|`).
- Images are descriptively named WebP with real alt text.
- Every medical page carries, above the footer:
  - the reviewer line: "Scientifically reviewed by Prof. (Dr.) Pulakes Purkait, Founder & Director, on {{DD Mon YYYY}}", plus "Clinically reviewed by {{RMP_NAME}}, {{QUALIFICATION}}, {{NMC/SMC_REG_NO}}" once available;
  - a references list;
  - the disclaimer: "Information only. Testing is ordered and interpreted by your treating doctor."
- No prices, no superlatives, no "patented", no testimonials, no outcome promises. Patent wording is always "Indian patent application published (No. …)".

### 4.1 Test page (e.g. `/diagnostics/endometrial-infection-test/`)

| Element | Formula / rule | Example |
|---|---|---|
| Title | `{Test name} ({what it checks}) \| EmbryoGenesis` | Endometrial Infection Test (Chronic Endometritis) \| EmbryoGenesis |
| Meta | `{What it checks} for {who}. Sample: {sample}. Results in 7–10 days. Ordered through your doctor or partner clinic.` | Chronic endometritis testing (CD138 plasma-cell assessment) for women with repeated implantation failure. Results in 7–10 days via your IVF clinic. |
| URL | `/diagnostics/{test-name-keyword}/` | `/diagnostics/endometrial-infection-test/` |
| H1 | `{Test name}: {plain-English purpose}` | Endometrial Infection Test: checking for chronic endometritis |

**H2 skeleton (in this order)**
1. *Answer-first block* (no heading, directly under the H1). 40–60 words: what the test is, who it is for, the sample, turnaround, and that a doctor orders it. Example: "The Endometrial Infection Test (EIT) looks for signs of chronic endometritis, a low-grade inflammation of the womb lining, in an endometrial biopsy. Clinicians usually consider it after repeated implantation failure or recurrent miscarriage. Results reach the ordering doctor in 7–10 days."
2. **Key facts** table: what it looks at · method (`{{METHOD}}`) · sample type · biopsy timing · transport · turnaround · who orders · report format. No price; add "Partner rate card on request".
3. **Who might consider this test** (indications) and **who it is not for**.
4. **What the result can and cannot tell you.**
5. **What the evidence says** (evidence box; see below).
6. **How to order** (clinicians): 3 steps that link to `/for-clinicians/order-a-test/` and `/for-clinicians/sample-collection-protocol/`.
7. **For patients**: "Ask your doctor whether this test is right for you", linking to `/patients/how-to-get-tested/`.
8. **Where samples can be collected**: links to `/collection-centres/`.
9. **FAQs**: 4–6 real questions, each answered in 2–4 sentences.
10. **References**, then the reviewer line, then the disclaimer.

**Evidence box** (a styled component, green `#218A6A` left border):
- Heading: "What the evidence says ({{Month YYYY}})".
- 2–4 bullets quoting guideline wording exactly, with the source named and linked. For example: "ESHRE good practice recommendations on RIF (2023): assessment for chronic endometritis 'can be considered'."
- One line on limitations or open questions.
- A link to the evidence status in `/for-clinicians/report-interpretation/`.

**Internal links:** protocol, report interpretation, order a test, matching patient page, collection centres, one related blog post.

**Primary CTA:** "Order this test" (clinicians) → `/for-clinicians/order-a-test/`. Secondary: WhatsApp (clinician context).

**Schema:** MedicalWebPage + MedicalTest + FAQPage + BreadcrumbList (6.4, 6.6, 6.9).

### 4.2 Clinician resource (e.g. `/for-clinicians/sample-collection-protocol/`)

| Element | Formula | Example |
|---|---|---|
| Title | `{Resource} for {test/area}: {benefit} \| EmbryoGenesis` (≤ 60) | Endometrial Biopsy Timing & Sample Protocol \| EmbryoGenesis |
| Meta | `{What the clinician gets}: {3 specifics}. Downloadable PDF. For IVF clinics and collection partners.` | Biopsy timing (natural and HRT cycles), sample handling and transport for EmbryoGenesis endometrial tests. Downloadable PDF for clinics. |
| H1 | `{Resource name}` | Endometrial biopsy timing and sample collection protocol |

**H2 skeleton**
1. Answer-first block (40–60 words): the one-paragraph summary a busy clinician needs.
2. **At a glance** table (e.g. cycle type, biopsy day, sample, medium, temperature, maximum transit time).
3. Step-by-step protocol (numbered list, one action per step).
4. Common reasons samples are rejected.
5. Packing and pick-up (links to `/for-clinicians/order-a-test/`).
6. Download (PDF; fires the `brochure_download` event with `file_type = protocol`).
7. FAQs (4–6).
8. References, reviewer line (pathologist co-review: Dr. Vidhu Wadhwa, `{{REG_NO}}`), and "Version {{x.y}}, effective {{date}}".

**Evidence box:** guideline basis for timing where it exists; otherwise "This is EmbryoGenesis laboratory procedure, version {{x.y}}".

**Internal links:** all test pages, report interpretation, order a test, partner page.

**CTA:** "Request a sample kit". Secondary: "Talk to the lab" (WhatsApp, clinician context).

**Schema:** MedicalWebPage (`medicalAudience` = Clinician) + BreadcrumbList; HowTo is not needed.

### 4.3 City collection-centre page (e.g. `/collection-centres/jalandhar/`)

| Element | Formula | Example |
|---|---|---|
| Title | `Endometrial Test Collection in {City} \| EmbryoGenesis` | Endometrial Test Collection in Jalandhar \| EmbryoGenesis |
| Meta | `Sample collection for EmbryoGenesis endometrial tests at {Partner}, {Locality}, {City}. How it works, timings and contact. Ordered by your doctor.` | (fill per city; ≤ 155) |
| H1 | `Endometrial test sample collection in {City}` | Endometrial test sample collection in Jalandhar |

**H2 skeleton**
1. Answer-first block (40–60 words): partner name, locality, which tests can be collected, that samples travel to the Mohali lab, and turnaround.
2. **Collection point details:**
   - partner name exactly as on their signage;
   - full address with PIN;
   - collection days and hours;
   - partner phone;
   - map (static image linking to Google Maps; no iframe above the fold).
3. **Tests available here:** list with links to the 4 test pages.
4. **How it works:** doctor orders, biopsy at partner, cold-chain transport, report to doctor.
5. **For local clinicians:** how to refer from another clinic in {City}.
6. **Getting there:** landmarks, parking, nearest station. This is city-unique content.
7. **FAQs** (4), specific to the city where possible.
8. **"Want to become a collection point?"** banner → `/partner-with-us/`.

**Uniqueness rule:** at least 400 words unique to the city: partner details, local logistics, local clinician notes and landmarks. If we cannot reach that, the page is noindexed until we can.

**Consent:** the partner gives written permission to be named and linked (`{{PARTNER_CONSENT}}`).

**Do not** call the partner "EmbryoGenesis {City}". It is "{Partner name}, an EmbryoGenesis collection point".

**CTA:** "Contact the collection point" (tel to partner). Secondary: WhatsApp to our central desk.

**Schema:** MedicalWebPage + Service + partner Hospital/MedicalClinic + BreadcrumbList (6.3). The Mohali page uses the main Organization/DiagnosticLab node (6.1) instead.

### 4.4 Academy program page (e.g. `/academy/art-clinical-embryology-rayat-bahra-university/`)

| Element | Formula | Example |
|---|---|---|
| Title | `{Degree} {Subject}: {University}, {City} \| EmbryoGenesis` (≤ 60; drop the brand suffix if needed) | B.Sc. & M.Sc. ART & Clinical Embryology, Rayat Bahra |
| Meta | `{Degree} at {University}, {City}: eligibility, duration, syllabus{, fees}. Degree awarded by {University}. Admissions {Session}.` | (≤ 155) |
| H1 | `{Degree} in {Subject} at {University}` | B.Sc. and M.Sc. in ART & Clinical Embryology at Rayat Bahra University |

**H2 skeleton**
1. Answer-first block (40–60 words): program, **degree-awarding university**, campus city, duration, eligibility in one line, and the session.
2. **Who awards the degree** (required box, ASCI): "Degree awarded by {University}. Classes held at {campus address}. ITHS/EmbryoGenesis role: {{ROLE}}." Add a UGC/recognition reference link (`{{UGC_REFERENCE}}`).
3. **Program at a glance** table: duration, semesters, eligibility, intake, fees per semester and total (only if the client approves publishing tuition fees: `{{FEE_POLICY}}`), mode (on-campus).
4. **Syllabus by semester** (accordion). Use the real syllabus only (`{{SYLLABUS_PDF}}`).
5. **Hands-on training:** what lab time students actually get, with real lab photos.
6. **Faculty:** named, with qualifications.
7. **Careers after this course:** roles, with sourced salary ranges linking to blog A4. No placement guarantees, no "100% placement".
8. **How to apply:** steps and dates, linking to `/academy/admissions/`.
9. **FAQs** (6), including "Is this degree valid?" and "Can I apply without NEET?".
10. **Brochure download** (fires `brochure_download`).

**Evidence box equivalent:** a "Facts we can verify" box with university recognition, the MoU date and an accreditation link.

**Internal links:** academy hub, the other program, lab training, admissions, founder profile, blog A1/A3/A4.

**CTA:** "Apply now" → `/academy/admissions/`. Secondary: WhatsApp (academy context); brochure.

**Minors:** the form asks for date of birth; under 18 triggers the parental-consent step. No ad pixels on these pages (5.7).

**Schema:** WebPage + EducationalOccupationalProgram + FAQPage + BreadcrumbList (6.7).

### 4.5 Blog article

| Element | Formula | Example |
|---|---|---|
| Title tag | `{Question or claim-free topic}: {specific angle} \| EmbryoGenesis` (≤ 60; the brand can drop) | Chronic Endometritis Testing in RIF: What ESHRE Says |
| Meta | Answer in one sentence, then the value: `{Direct answer}. {What the reader will learn}.` | (≤ 155) |
| URL | `/blog/{3–6 word keyword slug}/` | `/blog/chronic-endometritis-testing-rif/` |
| H1 | The article title (may be longer than the title tag) | Chronic endometritis testing in repeated implantation failure: what the 2023 ESHRE recommendations say |

**Structure**
1. **Byline block:**
   - "By {Author name, role}" (a real EmbryoGenesis expert who contributed);
   - "Scientifically reviewed by Prof. (Dr.) Pulakes Purkait";
   - "Published {date} · Updated {date}";
   - audience label (For clinicians / For patients / For students).
2. **Answer-first block** (40–60 words) under the H1.
3. **Key takeaways:** 3–5 bullets.
4. **Body:** H2s phrased as the questions people ask. Each H2 opens with a one-sentence answer, then detail. Use tables for comparisons.
5. **Evidence box:** required on clinician and patient posts; optional on academy posts (use a "Sources" box instead).
6. **"What this means for you"** (patients) or **"Practical points for your clinic"** (clinicians), or **"Next steps"** (students).
7. **FAQs:** 3–5.
8. **References:** numbered, linked, primary sources first (ESHRE, Cochrane, HFEA, NICE, PubMed).
9. **Disclaimer** (medical posts) and the editorial-policy link.
10. **CTA block** that matches the audience:
    - clinician: "Order a test" or "Join the next CME";
    - patient: "How to get tested through your doctor";
    - student: "Apply" or "Download brochure".

**Length:** clinician posts 1,200–1,800 words; patient posts 1,000–1,500; academy posts 1,200–2,000. Depth beats length.

**Internal links:** the target page from section 9 within the first 150 words, plus 2–4 related links.

**Schema:** MedicalWebPage (medical posts) or WebPage (academy posts) + Article + FAQPage + BreadcrumbList (6.8).

---

## 5. Technical SEO specification (for the WordPress developer)

The blueprint recommends a lightweight block theme (or Astra with native blocks) in place of the Elementor + Prime Slider + Sina + ElementsKit stack. Keep Rank Math, LiteSpeed Cache and Forminator. Everything below assumes that build. Where Elementor stays, the same budgets apply.

### 5.1 WordPress and Rank Math settings

**WordPress core**

| Setting | Value |
|---|---|
| Settings > General > Site language | English (India), so `<html lang="en-IN">` and `og:locale` is `en_IN` |
| Settings > Permalinks | Custom structure `/blog/%postname%/`; category base `topic` (gives `/blog/topic/{slug}/`); tag base unused |
| Pages | Set parent pages so URLs and breadcrumbs follow the tree in 1.3 |
| Comments | Off site-wide (Settings > Discussion), and closed on all existing posts |
| Users | Rename the admin display name (not "embryosys"); create real author users (e.g. Prof. Pulakes Purkait, Dr. Meenu Bhanot, Dr. Vidhu Wadhwa); block `/wp-json/wp/v2/users` for unauthenticated requests |
| Reading > Search engine visibility | **Unchecked on production.** Staging uses HTTP basic auth *and* "discourage". Check at go-live. |
| Footer © | Dynamic year |

**Rank Math**

| Area | Setting |
|---|---|
| Dashboard > Modules | On: SEO Analysis, Sitemap, Schema, Redirections, 404 Monitor, Instant Indexing (IndexNow), Image SEO, Local SEO (Knowledge Graph). Off: Rank Math Analytics/GA install (we use GTM; avoid double tagging), Role Manager only if needed. |
| General > Links | Strip category base: **off** (we want `/blog/topic/`). Redirect attachments: **on**. Nofollow external: off. Open external links in new tab: on (Rank Math adds `noopener`). |
| General > Breadcrumbs | On. Separator `›`. Home label "Home". Show post category: on (primary category). Hide current page title: off. |
| General > Image SEO | Do **not** auto-add alt or title from filenames. Writers supply real alt text. |
| General > Others | RSS: no "Powered by"; no extra links. |
| Titles & Meta > Global | Separator `\|` (fixes the empty `%sep%` bug). Robots default `index, follow`, `max-image-preview:large`, `max-snippet:-1`, `max-video-preview:-1`. OG image fallback: 1200×630 brand image. Twitter card: `summary_large_image`. |
| Titles & Meta > Local SEO | Organization; name "EmbryoGenesis"; logo 600×600; URL; contact. Our filter (6.11) overrides the type to DiagnosticLab/MedicalBusiness. |
| Titles & Meta > Social | Facebook page, Twitter/X handle: use the unified handles (7.3) only after they are confirmed. |
| Titles & Meta > Homepage | Title "EmbryoGenesis \| Endometrial Diagnostics Lab, Mohali" (≤ 60); description per copy deck; OG image set |
| Titles & Meta > Authors | **Disable author archives.** Author URLs in schema point to `/about/pulakes-purkait/` and `/about/team/#{name}` instead. |
| Titles & Meta > Misc | Date archives: disabled. Search results: **noindex**. 404 title: "Page not found \| EmbryoGenesis". Noindex password-protected pages: on. Noindex empty category/tag archives: on. Noindex paginated pages: **off** (keep paginated blog index pages indexable with self-canonicals). |
| Titles & Meta > Posts | Default schema: Article (type BlogPosting). Our filter adds MedicalWebPage, reviewedBy and citations. |
| Titles & Meta > Pages | Default schema: none (WebPage). Templates add the page-type JSON-LD. |
| Titles & Meta > Categories | Robots: **noindex** by default. Switch a topic archive to index only after it has 5 or more posts and 150+ words of intro. |
| Titles & Meta > Tags | noindex; do not use tags. |
| Titles & Meta > Media / format archives | Disabled |
| Sitemap settings | Include: posts, pages, images. Exclude: `/thank-you/`, every `/research-programs/` URL, any noindexed page (Rank Math does this automatically for noindexed items, but also add the IDs to "Exclude posts"). Categories: only indexed ones. Authors: off. Links per sitemap: 200. |
| Instant Indexing | IndexNow on for posts and pages; key file auto-created. Submit new and updated URLs on publish (Bing, Yandex and others). |
| 404 Monitor | Simple mode for the first 90 days after launch, then off (it writes to the DB). Review weekly (5.9). |
| Redirections | Rules per section 2. "Debug redirections": off on production. Fallback for 404s: **"Default 404"** (never redirect all 404s to home). |
| Per-page Advanced tab | Canonical left **blank** (Rank Math outputs a self-canonical). Only set a canonical for a true duplicate. **Fix post 964 (ERFA) on the live site now**, before migration. |

### 5.2 Core Web Vitals and performance budget

**Targets (p75 mobile, 4G).** Low-traffic sites rarely get CrUX field data, so test with PageSpeed Insights lab runs and confirm with field data when it appears.

| Metric | Budget |
|---|---|
| LCP | ≤ 2.5 s (goal 2.0 s) |
| INP | ≤ 200 ms |
| CLS | ≤ 0.1 |
| TTFB | ≤ 0.8 s from India. Investigate the TLS connection resets (curl error 35) seen during the audit with the host. |
| Homepage total transfer | ≤ 1.5 MB (blueprint). Inner pages ≤ 1.0 MB. |
| JavaScript | ≤ 250 KB compressed in total; no render-blocking JS in `<head>` except the consent default snippet and GTM |
| CSS | ≤ 80 KB compressed; critical CSS inlined; the rest loaded async (LiteSpeed UCSS) |
| Requests | ≤ 50 on the homepage |
| Third-party scripts | GTM only (it loads GA4 after consent). No chat widgets, review widgets or social embeds at launch. |

**Images**

| Rule | Spec |
|---|---|
| Formats | WebP by default; AVIF where LiteSpeed/QUIC.cloud serves it with fallback. Logos and icons as SVG. No PNG photos. |
| Sizes | Hero ≤ 150 KB (1600 px wide source; `srcset` at 480/768/1024/1600). Content images ≤ 100 KB (max 1200 px). Cards and thumbnails ≤ 30 KB (max 600 px). Award and patent-certificate images ≤ 80 KB at 800 px. |
| Uploads | Cap uploads at 2000 px longest side (resize on upload). Strip EXIF. |
| Dimensions | Every `<img>` has `width` and `height` (or CSS `aspect-ratio`) to stop CLS. |
| Lazy-load | `loading="lazy"` on every image below the fold. The **LCP image is never lazy** and gets `fetchpriority="high"` plus a `<link rel="preload" as="image" imagesrcset=…>`. Add it to LiteSpeed's "Lazy Load Image Excludes". |
| Names and alt | Descriptive file names (e.g. `endometrial-biopsy-sample-kit.webp`) and real alt text. Rename all `ChatGPT-Image-*` files. Replace AI stock images with real lab photos from the shoot (blueprint week 3–4). Any AI image kept must be labelled "AI-generated illustration" (brief guardrail 9). |
| Carousels | **Drop heavy sliders** (Prime Slider, Owl, Swiper, UIkit). No carousel above the fold. Show patent-application and award certificates as a static grid of thumbnails that open a lightweight lightbox, or link to `/research/`. |

**Fonts:**
- Exactly 2 variable font files, per the design-system doc (`04-brand-voice-and-design-system.md`, section 8.1): **Inter** (body/UI, `wght` 400–700) and **Source Serif 4** (headings, `wght` 500–700), both roman only, Latin subset, WOFF2.
- Self-host (WordPress Font Library or theme.json `fontFace`); no Google Fonts API calls. `font-display: swap`. Preload **only the Inter file**.
- Remove Font Awesome 4/5, icofont, ekiticons and eicons; use inline SVG icons.

**Other:**
- **Video:** YouTube embeds use a click-to-load facade (lite-youtube pattern); no iframe on load.
- **Maps:** a static map image linking to Google Maps. If an iframe is unavoidable, place it below the fold with `loading="lazy"`.

**LiteSpeed Cache**

| Setting | Value |
|---|---|
| Page cache | On; exclude form `/thank-you/` and logged-in users |
| Browser cache | On; static asset TTL 1 year (versioned filenames) |
| CSS | Minify on; combine on (test it); UCSS on; load CSS async on (with critical CSS) |
| JS | Minify on; defer on. **Exclude the consent-mode default snippet and the GTM loader from delay**, or consent defaults will fire late. |
| HTML | Minify on; remove query strings off |
| Media | Lazy-load images and iframes on (with the LCP exclusion); image optimisation via QUIC.cloud on; WebP/AVIF replacement on; "Add missing sizes" on |
| Object cache | On if the host supports Redis or Memcached |

**Security headers** (hygiene, also trust): HSTS (`max-age=31536000; includeSubDomains`), `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `X-Frame-Options: SAMEORIGIN`. Add a basic CSP after GTM tags are final.

### 5.3 Canonical rules

1. Every indexable page has an absolute, self-referencing canonical: `https://embryogenesis.in/{path}/` (https, no www, trailing slash, lowercase).
2. URLs with parameters (`?utm_*`, `?fbclid`, `?gclid`, `?ref`) canonicalise to the clean URL. Rank Math does this by default; do not override it.
3. Paginated blog pages (`/blog/page/2/`) self-canonicalise. Do not canonicalise them to page 1.
4. Never canonicalise to a URL that redirects or returns 404. The ERFA bug (audit C1) must not recur. QA crawls check "canonical target status = 200".
5. City pages are never canonicalised to each other. If one is too thin, noindex it instead.
6. PDFs (protocols, brochures) get an `X-Robots-Tag: noindex` header if they duplicate page content. Brochures may stay indexable.

### 5.4 Sitemap rules

- Use the Rank Math sitemap index only: `https://embryogenesis.in/sitemap_index.xml`. `/sitemap.xml` and `/wp-sitemap.xml` keep their 301s to it.
- The sitemap contains **only** URLs that are indexable, return 200 and are self-canonical. Nothing that redirects, nothing noindexed, no held pages, no `/thank-you/`, no noindexed topic archives, no author archives.
- `lastmod` must reflect real content changes. Do not bulk-touch posts.
- Image sitemap entries are on (helps the lab-photo and certificate images).
- After launch, resubmit the sitemap in Google Search Console and Bing Webmaster Tools. Check "Submitted vs Indexed" weekly for 6 weeks.

### 5.5 Noindex rules for held and utility pages

| Page | Rule |
|---|---|
| `/research-programs/` and every child (LIT, PBMC, PRP, molecular hydrogen) | Keep as **WordPress Draft or Private** until written legal sign-off. If it must be viewable for the lawyer, use **password protection** plus Rank Math robots `noindex, nofollow` plus "Exclude from sitemap". No internal links, no navigation entries, no social or ad promotion. Do **not** block in robots.txt (Google must be able to see the noindex if it ever finds the URL). |
| Stem cell therapy | **No page at all**, draft or otherwise (NMC advisory of 5 Sep 2026; ICMR). If legal counsel later approves a research description, it goes on `/research/` with a CTRI registration number, never as a service. |
| Lab-training modules on therapies ("PRP Therapy & LIT Therapy", "LIT Therapy & Molecular Hydrogen Therapy", "Molecular Hydrogen Therapy in Health Management", "Stem Cell Processing & Cryopreservation") | Remove them from `/academy/lab-training/` at launch and hold them with the therapy pages pending legal review. These are training courses, but they promote held therapies. Launch with: Biochemistry (semi-auto analyser), Molecular Genetics & Bioinformatics, Tissue Processing & Microtomy, Immunohistochemistry. |
| `/thank-you/` | noindex, follow; excluded from the sitemap |
| `/blog/topic/*` | noindex, follow until the threshold in 5.1 is met |
| Internal search `/?s=` | noindex, follow |
| Staging site | HTTP basic auth (not only "discourage search engines") |
| City page below 400 unique words | noindex, follow until expanded |

### 5.6 robots.txt

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /?s=
Disallow: /*?replytocom=

# AI and answer-engine crawlers are welcome (see section 8)
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: https://embryogenesis.in/sitemap_index.xml
```

**Notes:**
- Do not disallow `/research-programs/`; noindex handles it, and a robots block would hide the noindex.
- Check that the host's firewall, Cloudflare or QUIC.cloud bot protection is not silently blocking Googlebot, Bingbot or the AI crawlers.
- If the client prefers to opt out of AI *training* while staying in AI *search*, set `GPTBot` and `Google-Extended` to `Disallow: /`, and keep `OAI-SearchBot`, `PerplexityBot`, Googlebot and Bingbot allowed. Client decision: `{{AI_TRAINING_OPT_OUT}}`.

### 5.7 GA4 + GTM + Consent Mode v2 (DPDP-safe)

**Install:**
- One GTM container (`{{GTM_ID}}`) in `<head>` and `<body>`, plus a GA4 property (`{{GA4_ID}}`) configured through GTM.
- Do not also install GA via Rank Math, Site Kit or the theme.

**Consent:**
- Use a consent banner that supports Google Consent Mode v2, e.g. Complianz, CookieYes or Cookiebot (`{{CMP_CHOICE}}`). It needs "Accept", "Reject" and "Settings" buttons of equal prominence, and links to `/privacy-policy/`.
- Set defaults **before** GTM loads (an inline snippet, excluded from LiteSpeed JS delay):
  ```js
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent', 'default', {
    'analytics_storage': 'denied',
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'functionality_storage': 'granted',
    'security_storage': 'granted',
    'wait_for_update': 500
  });
  ```
- On "Accept analytics", update `analytics_storage` to `granted`. **The three ad signals stay `denied`**: there are no ad tags at launch.
- Use basic consent mode (GA4 tags do not fire until consent). This is the more conservative choice for a fertility-health site.

**GA4 property settings:**
- Data retention 14 months.
- **Google signals: off.** Ads personalisation: off. No Google Ads link at launch. **User-provided data collection / enhanced conversions: off.**
- Internal-traffic filter for the lab's IP. Unwanted referrals: none needed.
- Content group set from a dataLayer variable `page_section`, taking one of: clinicians, partner, diagnostics, patients, academy, research, about, blog-clinician, blog-patient, blog-academy. The developer sets it per template.

**Event plan**

| Event | Trigger (GTM) | Parameters (allowed) | Key event | DPDP / privacy note |
|---|---|---|---|---|
| `generate_lead` | Forminator success on any lead form except the partner form. Listen for the `forminator:form:submit:success` JS event (confirm the event name in the installed Forminator version) and push `{event:'generate_lead', form_type:…, form_id:…}` | `form_type` (clinician_order, kit_request, academy_application, cme_registration, general_contact), `form_id`, `page_section` | Yes | **Never** push field values (name, phone, email, city, age, symptoms, test interest). Use form IDs only. |
| `partner_enquiry` | Forminator success on the partner form (`/partner-with-us/`) | `form_id`, `partner_city_tier` (metro / tier-2 / other: a dropdown value, not free text), `page_section` | Yes | No business names or contact data in GA4 |
| `tel_click` | Click on links starting `tel:` | `link_location` (header, footer, body, sticky, city_page), `phone_line` (main, admissions, partner_centre) | Yes (secondary) | Send a label, never the dialled number |
| `whatsapp_click` | Click on links to `wa.me/` or `api.whatsapp.com/` | `link_location`, `wa_context` (clinician, partner, academy, general) | Yes | Pre-filled WhatsApp text must be neutral, e.g. "Hello, I have a question for EmbryoGenesis." No health terms in the prefill or URL. |
| `brochure_download` | Click on links to `.pdf` under `/wp-content/uploads/academy/` or `/protocols/` | `file_name`, `file_type` (brochure, protocol, requisition), `programme` | Yes (secondary) | Brochures are not gated. No email capture for minors. |
| `page_not_found` (support) | 404 template view | `page_path` | No | For 404 monitoring alongside Rank Math |
| Enhanced measurement | GA4 default (scrolls, outbound clicks, file downloads, site search off) | default | No | Turn **off** "form interactions" in enhanced measurement (it can read form names). Turn off site search (we noindex search; low value). |

**Rules that protect health data (non-negotiable):**
1. No Meta Pixel, Google Ads tag, LinkedIn Insight Tag or any other ad pixel at launch. If ads start later:
   - B2B pages only (`/partner-with-us/`, `/for-clinicians/*`), after legal review;
   - never on `/patients/*`, `/diagnostics/*` or the blog's patient posts;
   - **never on academy pages** (applicants may be minors; DPDP s.9 bans tracking and targeted ads aimed at children).
2. No remarketing audiences built from health pages. Google Ads policy does not allow health-based personalised ads anyway.
3. No PII or health data in URLs. Forms must not redirect with query strings containing user input.
4. Forms:
   - an **unticked**, required consent checkbox linking to `/privacy-policy/`;
   - a separate, optional marketing-consent checkbox;
   - academy forms ask for date of birth and route under-18s to a parental-consent step;
   - store consent logs (Forminator entries plus a timestamp).
5. Hidden form fields carrying UTM source and medium are fine. Do not pass the GA client ID into CRM records containing health information.
6. GA4 page paths for patient pages are acceptable for aggregate analytics, but are never shared to ad platforms.
7. Document all of this in the privacy policy (purposes, processors: Google, hosting, WhatsApp; retention; grievance officer `{{GRIEVANCE_OFFICER}}`).

### 5.8 Search Console and Bing

1. **Google Search Console:**
   - Add a **Domain property** (DNS TXT at the registrar) plus a URL-prefix property for `https://embryogenesis.in/` (handy for URL inspection). Confirm whether a DNS verification already exists (audit C7).
   - Submit `sitemap_index.xml`.
   - Request indexing for the 15 Tier-1 pages on launch day.
   - Watch the Pages report, Core Web Vitals, HTTPS and Manual actions weekly for 8 weeks.
2. **Bing Webmaster Tools:** import from GSC (one click), submit the sitemap and enable IndexNow (via Rank Math Instant Indexing). Bing's index feeds Copilot and several AI search tools, so do not skip this.
3. **Change of address:** not needed (same domain).
4. **Launch-day checks:**
   - robots.txt live;
   - no stray `noindex` on key pages;
   - canonicals are self and 200;
   - every redirect is a single hop;
   - sitemap shows only 200 URLs;
   - GA4 DebugView receives all 5 events with consent granted, and none with consent denied.

### 5.9 Breadcrumbs and 404 handling

**Breadcrumbs:**
- Visible on every page except the homepage, just under the header: Home › Section › Page.
- Blog: Home › Blog › {Primary topic} › Post. While topic archives are noindexed, the topic crumb is plain text, not a link.
- Rank Math outputs the matching `BreadcrumbList`. Parent pages must be set so the trail matches 1.3.

**404:**
- A custom template that returns a real **404 status** (never 200, never a redirect to home). It contains:
  - a short message;
  - site search;
  - links to For Clinicians, Diagnostics, Collection Network, Academy and Contact;
  - the WhatsApp link.
- Rank Math 404 Monitor (simple) runs for 90 days. Every Monday for 8 weeks:
  - export the 404s;
  - add a 301 **only** where a clearly relevant page exists;
  - ignore bot noise (`/wp-login`, `.env` and similar).
- GA4 `page_not_found` events show which 404s real users hit.

### 5.10 Image restore list (from the audit)

| File (`/wp-content/uploads/…`) | Used on | Action |
|---|---|---|
| `2023/10/EmbryoGenesis.png` | Mobile menu logo on every page | **Replace** with the new SVG logo (and fix the path in the new theme). Highest priority. |
| `2024/03/5742c20dd6.webp`, `2024/03/580488d311.webp`, `2024/03/fallopian_ube_abnormalities_unexplained_infertility.webp`, `2024/03/image.webp`, `2024/03/ivf_unexplained_infertility.webp`, `2024/03/preimplantation_genetic_testing.webp`, `2024/03/sperm_function_abnormalities_unexplained_infertility.webp` | `/unexplained-infertility/` (incl. og:image) | Restore from backup **only if** the rewritten `/blog/unexplained-infertility/` uses them; otherwise make new diagrams. Rename descriptively (fix the "ube" typo). |
| `2024/05/lit-therapy-treatment.webp` | LIT post | **Do not restore** (therapy content held) |
| `2025/07/Endometrial-Immune-Comparison_simple-1024x683.webp` | EIP post | Restore and reuse on `/diagnostics/endo-immune-test/` if the scientific review approves the diagram. Rename to `endometrial-immune-profile-comparison.webp`. |
| `2024/07/3da012aa80.png`, `2024/07/796bc91810.png`, `2024/07/8ab5e35a6b.jpg`, `2024/07/d998ffd2d6.jpg`, `2024/07/stressed-millennial-woman-holding-pregnancy-test.jpg` | Hindi IVF-failure post | **Do not restore** (post redirected). Keep the files in the backup for the Hindi phase. |
| `2024/12/VATSALYA_IVF_CENTER.webp`, `2024/12/DYET_NUTRITION.webp`, `2024/12/ARCHISH.webp` | About page, partner logos | Restore **only after** the client confirms each partnership is current and logo use is permitted (`{{PARTNER_LOGO_PERMISSIONS}}`). |
| `2024/12/GIOSTAR.webp` | About page, partner logo | **Hold.** GIOSTAR is publicly associated with stem cell therapy. Displaying it could read as stem cell promotion; legal review first. |
| `2024/12/Prof-Dr-Neena-Mehta.webp`, `2024/12/Dr-Arunava-Bandyopadhaya.webp`, `2024/12/Dr-Naveen-Chandra-Suryadevara.webp` | About page, expert photos | Restore only with each person's written consent and a current, accurate role description (an implied endorsement otherwise) |
| Homepage carousel `2026/06/ChatGPT-Image-*.png` (7 files, 2.0–2.5 MB each) and `ChatGPT-Image-Jun-19-2026-*.png` (2 files, about 2 MB each) | Homepage "Our Patents" and image boxes | **Retire.** Replace with real certificate scans (≤ 80 KB WebP each) captioned "Indian patent application published (No. …)", and real lab photos |
| `/Clinical_Embryology-Brochure-2025-2026-Bahra_University.pdf` | B.Sc. page | Replace with the 2026–27 brochure at the new path (section 2.2) |

---

## 6. Schema plan and JSON-LD templates

### 6.1 Approach

- Use one connected `@graph` per page, with stable `@id`s:
  - `https://embryogenesis.in/#organization`
  - `https://embryogenesis.in/#website`
  - `https://embryogenesis.in/#founder`
  - `https://embryogenesis.in/{path}/#webpage`
  - `https://embryogenesis.in/{path}/#breadcrumb`
- Rank Math already outputs Organization, WebSite, WebPage, Article and BreadcrumbList. To avoid duplicate or conflicting nodes, the developer adds a small must-use plugin that hooks Rank Math's `rank_math/json_ld` filter (see 6.11). It does three things:
  1. replaces the Organization node with 6.2;
  2. upgrades page nodes to MedicalWebPage where the template says so;
  3. appends page-type nodes from ACF fields (test facts, program facts, event facts).
- Mark up only what is visible on the page. FAQ answers in schema must match the on-page text word for word.
- **No `offers` or `price` on tests.** No `aggregateRating` or `review` (no testimonials; self-serving review markup is not eligible anyway).
- The founder is a `Person`, **never** `Physician`. He is a Ph.D. scientist, not MBBS.
- Validate every template in the Rich Results Test and the Schema.org validator before launch.

**What to expect from Google:**
- **FAQPage:** since 2023, FAQ rich results show only for well-known government and health authority sites, so do not expect FAQ snippets. The markup still helps AI systems parse Q&A, so keep it for visible FAQs.
- **Course info:** Google retired the Course info rich result in 2025. Keep Course and EducationalOccupationalProgram markup for entity clarity and AI answers; expect no rich result.
- **Sitelinks search box:** retired in 2024, so no `SearchAction` is needed.
- **Event:** rich results are still available for event listings and suit CME webinars.

### 6.2 Organization + MedicalOrganization (DiagnosticLab), sitewide (homepage and `/collection-centres/mohali/` in full; other pages reference the `@id`)

`DiagnosticLab` is a subtype of `MedicalOrganization`. Adding `MedicalBusiness` (a `LocalBusiness` subtype) lets the same node carry the address, geo and opening hours that match the Google Business Profile.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["DiagnosticLab", "MedicalBusiness"],
      "@id": "https://embryogenesis.in/#organization",
      "name": "EmbryoGenesis",
      "alternateName": ["EmbryoGenesis Diagnostics", "EmbryoGenesis Infertility Diagnostic & Research Centre"],
      "legalName": "{{LEGAL_ENTITY_NAME}}",
      "url": "https://embryogenesis.in/",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://embryogenesis.in/#logo",
        "url": "https://embryogenesis.in/wp-content/uploads/brand/embryogenesis-logo-600.png",
        "width": 600,
        "height": 600,
        "caption": "EmbryoGenesis logo"
      },
      "image": "{{LAB_PHOTO_URL_1200x630}}",
      "slogan": "Redefining Fertility Evaluation",
      "description": "EmbryoGenesis is an infertility diagnostic and research centre in Mohali, Punjab. It develops endometrial tests in-house, partners with IVF clinics across India, and trains embryologists.",
      "disambiguatingDescription": "EmbryoGenesis (Mohali, India) is an infertility diagnostic and research centre and embryology academy. It is not the biological process of embryogenesis.",
      "foundingDate": "2023-11",
      "founder": { "@id": "https://embryogenesis.in/#founder" },
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Top Floor, Rayat Bahra Dental College & Hospital, {{LOCALITY}}",
        "addressLocality": "Mohali",
        "addressRegion": "Punjab",
        "postalCode": "{{PIN_CODE}}",
        "addressCountry": "IN"
      },
      "geo": { "@type": "GeoCoordinates", "latitude": "{{LAT}}", "longitude": "{{LNG}}" },
      "hasMap": "{{GOOGLE_MAPS_PLACE_URL}}",
      "telephone": "{{PRIMARY_PHONE_E164}}",
      "email": "{{PRIMARY_EMAIL}}",
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
          "opens": "{{OPENS_HH:MM}}",
          "closes": "{{CLOSES_HH:MM}}"
        }
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "contactType": "customer support",
          "name": "Clinician and partner desk",
          "telephone": "{{PRIMARY_PHONE_E164}}",
          "email": "{{PRIMARY_EMAIL}}",
          "areaServed": "IN",
          "availableLanguage": ["English", "Hindi"]
        },
        {
          "@type": "ContactPoint",
          "contactType": "admissions",
          "telephone": "{{ADMISSIONS_PHONE_E164}}",
          "areaServed": "IN",
          "availableLanguage": ["English", "Hindi"]
        }
      ],
      "areaServed": { "@type": "Country", "name": "India" },
      "medicalSpecialty": [
        "https://schema.org/Gynecologic",
        "https://schema.org/Pathology",
        "https://schema.org/LaboratoryScience"
      ],
      "knowsAbout": [
        "Chronic endometritis testing",
        "Endometrial receptivity testing",
        "Uterine natural killer (uNK) cell profiling",
        "Repeated implantation failure",
        "Clinical embryology education"
      ],
      "availableService": [
        { "@id": "https://embryogenesis.in/diagnostics/endometrial-infection-test/#test" },
        { "@id": "https://embryogenesis.in/diagnostics/erfa-endometrial-receptivity-test/#test" },
        { "@id": "https://embryogenesis.in/diagnostics/endo-immune-test/#test" },
        { "@id": "https://embryogenesis.in/diagnostics/receptivity-px/#test" }
      ],
      "sameAs": [
        "{{LINKEDIN_COMPANY_URL}}",
        "{{INSTAGRAM_URL_UNIFIED}}",
        "{{FACEBOOK_URL_UNIFIED}}",
        "{{YOUTUBE_URL_UNIFIED}}",
        "{{X_URL_UNIFIED}}",
        "{{GOOGLE_BUSINESS_PROFILE_CID_URL}}",
        "{{WIKIDATA_URL_WHEN_CREATED}}"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://embryogenesis.in/#website",
      "url": "https://embryogenesis.in/",
      "name": "EmbryoGenesis",
      "inLanguage": "en-IN",
      "publisher": { "@id": "https://embryogenesis.in/#organization" }
    }
  ]
}
```

**Notes:**
- Until the handles are unified (7.3), use the current live URLs: `https://www.instagram.com/embryo_genesis`, `https://www.facebook.com/EmbryoGenesis` and `https://www.youtube.com/@Embryo-Genesis`. Drop the X URL if the `EmbryoGenesiss` account is inactive. Remove any `sameAs` entry that is still a placeholder at launch; never publish a `{{…}}` string.
- `hasCredential` (NABL) and ART Act registration: add only when certificates are supplied (`{{NABL_CERT_NO}}`, `{{ART_REG_NO}}`).

### 6.3 Partner collection centre (city pages; one per real centre)

The partner is **not** an EmbryoGenesis branch, so it keeps its own name. EmbryoGenesis is the `provider` of a sample-collection `Service` delivered at the partner's location. Use `Hospital` for hospitals and `MedicalClinic` for clinics; both are `LocalBusiness` subtypes.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "MedicalWebPage",
      "@id": "https://embryogenesis.in/collection-centres/navi-mumbai/#webpage",
      "url": "https://embryogenesis.in/collection-centres/navi-mumbai/",
      "name": "Endometrial test sample collection in Navi Mumbai",
      "inLanguage": "en-IN",
      "isPartOf": { "@id": "https://embryogenesis.in/#website" },
      "about": { "@id": "https://embryogenesis.in/collection-centres/navi-mumbai/#service" },
      "breadcrumb": { "@id": "https://embryogenesis.in/collection-centres/navi-mumbai/#breadcrumb" },
      "lastReviewed": "{{YYYY-MM-DD}}",
      "reviewedBy": { "@id": "https://embryogenesis.in/#founder" }
    },
    {
      "@type": "Service",
      "@id": "https://embryogenesis.in/collection-centres/navi-mumbai/#service",
      "name": "Endometrial test sample collection, Navi Mumbai",
      "serviceType": "Diagnostic sample collection for endometrial tests",
      "provider": { "@id": "https://embryogenesis.in/#organization" },
      "areaServed": { "@type": "City", "name": "Navi Mumbai" },
      "availableChannel": {
        "@type": "ServiceChannel",
        "serviceLocation": { "@id": "https://embryogenesis.in/collection-centres/navi-mumbai/#collection-point" },
        "servicePhone": { "@type": "ContactPoint", "telephone": "{{PARTNER_PHONE_E164}}" }
      }
    },
    {
      "@type": "Hospital",
      "@id": "https://embryogenesis.in/collection-centres/navi-mumbai/#collection-point",
      "name": "Nirmal Multi Speciality Hospital",
      "url": "{{PARTNER_WEBSITE_URL}}",
      "telephone": "{{PARTNER_PHONE_E164}}",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "{{PARTNER_STREET}}",
        "addressLocality": "Kopar Khairane, Navi Mumbai",
        "addressRegion": "Maharashtra",
        "postalCode": "{{PARTNER_PIN}}",
        "addressCountry": "IN"
      },
      "geo": { "@type": "GeoCoordinates", "latitude": "{{LAT}}", "longitude": "{{LNG}}" }
    }
  ]
}
```

**Per-city values**

| City page | Collection-point `@type` | `name` | `addressLocality` | `addressRegion` | Extra |
|---|---|---|---|---|---|
| navi-mumbai | Hospital | Nirmal Multi Speciality Hospital | Kopar Khairane, Navi Mumbai | Maharashtra | — |
| udaipur | Hospital | Shree B.L. Jain Memorial Hospital | Savina, Udaipur | Rajasthan | — |
| jalandhar | MedicalClinic | Advance Fertility Services & IVF Centre | Jalandhar | Punjab | Add `"containedInPlace": {"@type": "Hospital", "name": "Shakuntala Devi VIG Hospital"}` |
| mohali | — | Uses the Organization node (6.2); the page `about` points to `https://embryogenesis.in/#organization` | | | |

### 6.4 MedicalWebPage with reviewedBy, and MedicalTest (test pages)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "MedicalWebPage",
      "@id": "https://embryogenesis.in/diagnostics/endometrial-infection-test/#webpage",
      "url": "https://embryogenesis.in/diagnostics/endometrial-infection-test/",
      "name": "Endometrial Infection Test: checking for chronic endometritis",
      "description": "{{META_DESCRIPTION}}",
      "inLanguage": "en-IN",
      "isPartOf": { "@id": "https://embryogenesis.in/#website" },
      "publisher": { "@id": "https://embryogenesis.in/#organization" },
      "mainEntity": { "@id": "https://embryogenesis.in/diagnostics/endometrial-infection-test/#test" },
      "medicalAudience": [
        { "@type": "MedicalAudience", "audienceType": "Clinician" },
        { "@type": "Patient" }
      ],
      "datePublished": "{{YYYY-MM-DD}}",
      "dateModified": "{{YYYY-MM-DD}}",
      "lastReviewed": "{{YYYY-MM-DD}}",
      "reviewedBy": [
        { "@id": "https://embryogenesis.in/#founder" },
        { "@id": "https://embryogenesis.in/about/team/#{{RMP_SLUG}}" }
      ],
      "citation": [
        {
          "@type": "ScholarlyArticle",
          "name": "ESHRE good practice recommendations on recurrent implantation failure",
          "datePublished": "2023",
          "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10270320/"
        }
      ],
      "breadcrumb": { "@id": "https://embryogenesis.in/diagnostics/endometrial-infection-test/#breadcrumb" }
    },
    {
      "@type": "MedicalTest",
      "@id": "https://embryogenesis.in/diagnostics/endometrial-infection-test/#test",
      "name": "Endometrial Infection Test (EIT)",
      "alternateName": "Chronic endometritis test",
      "description": "Laboratory assessment of an endometrial biopsy for signs of chronic endometritis. Ordered and interpreted by the treating clinician. Results in 7 to 10 days.",
      "usedToDiagnose": {
        "@type": "MedicalCondition",
        "name": "Chronic endometritis",
        "alternateName": "CE"
      },
      "relevantSpecialty": ["https://schema.org/Gynecologic", "https://schema.org/Pathology"],
      "guideline": {
        "@type": "MedicalGuidelineRecommendation",
        "name": "ESHRE RIF good practice recommendations (2023): assessment for chronic endometritis can be considered",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10270320/"
      }
    }
  ]
}
```

**Values for the other tests:**
- **ERFA:**
  - `name`: "ERFA (Endometrial Receptivity & Function Assay)"; `alternateName`: "The Soil Test".
  - `usedToDiagnose`: omit (it assesses timing, not a disease). Use `"description"` to say what it assesses.
  - `guideline`: the ESHRE RIF wording "insufficient data to recommend the routine use of any commercially available test of endometrial receptivity".
  - Mention the patent application in the page copy (not in schema).
- **Endo-Immune:** `alternateName`: "Endometrial immune profile (uNK / cytokines)"; the guideline line quotes ESHRE "not recommended" for routine uNK testing. Honesty in markup matches honesty on the page.
- **Receptivity PX:** fill `{{RECEPTIVITY_PX_METHOD}}` from the client.

### 6.5 Person: founder (sitewide reference; full node on `/about/pulakes-purkait/`)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://embryogenesis.in/#founder",
  "name": "Pulakes Purkait",
  "honorificPrefix": "Prof. (Dr.)",
  "honorificSuffix": "M.Sc., Ph.D.",
  "jobTitle": "Founder & Director",
  "worksFor": { "@id": "https://embryogenesis.in/#organization" },
  "url": "https://embryogenesis.in/about/pulakes-purkait/",
  "image": "{{FOUNDER_PHOTO_URL}}",
  "description": "Prof. (Dr.) Pulakes Purkait is the Founder and Director of EmbryoGenesis. He is a reproductive scientist with an M.Sc., a Ph.D. and postdoctoral research experience. He is not a medical practitioner.",
  "alumniOf": [
    { "@type": "CollegeOrUniversity", "name": "Vidyasagar University" },
    { "@type": "CollegeOrUniversity", "name": "Andhra University" },
    { "@type": "CollegeOrUniversity", "name": "Panjab University" }
  ],
  "knowsAbout": ["Reproductive genetics", "Endometrial receptivity", "Molecular genetics", "Clinical embryology"],
  "award": [
    "Best Innovator Award, NBHC 2024 (IIT Delhi)",
    "Best Innovator Award for Human Infertility Treatment, Research & Innovation Park, New Delhi (November 2024)"
  ],
  "identifier": {
    "@type": "PropertyValue",
    "propertyID": "ORCID",
    "value": "0000-0002-8814-9939"
  },
  "sameAs": [
    "https://orcid.org/0000-0002-8814-9939",
    "https://www.linkedin.com/in/pulakes-purkait-aa634094/",
    "{{GOOGLE_SCHOLAR_PROFILE_URL}}",
    "{{RESEARCHGATE_PROFILE_URL}}"
  ]
}
```

**Verify before go-live** (design-system doc 04, section 6, items marked [CV]): exact award titles and issuers as printed on the certificates, and the universities for each degree (`alumniOf`). Remove `alumniOf` entries the client has not confirmed. Award names are proper nouns and may be quoted exactly as titled; never paraphrase them into claims like "best innovator in India". The `description` uses the approved founder bio wording. Team members (Dr. Vidhu Wadhwa, Dr. Meenu Bhanot) get the same pattern on `/about/team/` with `@id` `https://embryogenesis.in/about/team/#{slug}`. Use `Physician` only for a team member who holds an MBBS/MD with NMC/SMC registration, and add `"identifier": {"@type":"PropertyValue","propertyID":"NMC/SMC registration","value":"{{REG_NO}}"}`.

### 6.6 FAQPage (any page with a visible FAQ)

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": "https://embryogenesis.in/diagnostics/endometrial-infection-test/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Who usually orders the Endometrial Infection Test?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The test is ordered by the treating fertility specialist, usually after repeated implantation failure or recurrent miscarriage. Patients cannot order it directly; ask your doctor whether it is appropriate for you."
      }
    },
    {
      "@type": "Question",
      "name": "How long do results take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Results usually reach the ordering doctor within 7 to 10 days of the sample arriving at the laboratory."
      }
    }
  ]
}
```

Use 4–6 questions per page. Do not repeat the same FAQ on multiple pages.

### 6.7 Course and EducationalOccupationalProgram

**University program (one node per degree on the program page):**

```json
{
  "@context": "https://schema.org",
  "@type": "EducationalOccupationalProgram",
  "@id": "https://embryogenesis.in/academy/art-clinical-embryology-rayat-bahra-university/#bsc",
  "name": "B.Sc. in ART & Clinical Embryology",
  "description": "Four-year undergraduate program in assisted reproductive technology and clinical embryology, run with ITHS and Rayat Bahra University, Mohali.",
  "url": "https://embryogenesis.in/academy/art-clinical-embryology-rayat-bahra-university/",
  "provider": {
    "@type": "CollegeOrUniversity",
    "name": "Rayat Bahra University",
    "url": "{{RAYAT_BAHRA_UNIVERSITY_URL}}"
  },
  "educationalCredentialAwarded": "B.Sc. (ART & Clinical Embryology), awarded by Rayat Bahra University",
  "programPrerequisites": "Class 12 with Physics, Chemistry and Biology or Mathematics",
  "timeToComplete": "P4Y",
  "termsPerYear": 2,
  "educationalProgramMode": "in-person",
  "occupationalCategory": "Clinical embryologist",
  "applicationStartDate": "{{YYYY-MM-DD}}",
  "applicationDeadline": "{{YYYY-MM-DD}}",
  "startDate": "{{YYYY-MM-DD}}",
  "offers": {
    "@type": "Offer",
    "category": "Tuition",
    "price": "{{FEE_PER_SEMESTER_IF_APPROVED}}",
    "priceCurrency": "INR"
  }
}
```

- Remove `offers` if the client decides not to publish tuition fees (`{{FEE_POLICY}}`).
- M.Sc.: `timeToComplete` `P2Y`; prerequisites "B.Sc./B.Tech in life sciences, MBBS, BDS or equivalent".
- Bahra University program: provider "Bahra University" (current domain `{{BAHRA_UNIVERSITY_URL}}`; the old domain redirects to bushimla.in, so confirm).
- Mention EmbryoGenesis's role in `description` only, exactly as the client documents it (`{{ITHS_EMBRYOGENESIS_ROLE}}`).

**Lab-training module (one Course per module on `/academy/lab-training/`):**

```json
{
  "@context": "https://schema.org",
  "@type": "Course",
  "@id": "https://embryogenesis.in/academy/lab-training/#immunohistochemistry",
  "name": "Hands-on Training in Immunohistochemistry",
  "description": "Three-day practical course in immunohistochemistry techniques for life-science and allied-health graduates. Batch of up to 10.",
  "provider": { "@id": "https://embryogenesis.in/#organization" },
  "educationalCredentialAwarded": "{{CERTIFICATE_NAME}}",
  "coursePrerequisites": "B.Sc. MLT, M.Sc., Ph.D., MBBS, MD, or life-science / allied-health background",
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "Onsite",
    "courseWorkload": "P3D",
    "startDate": "{{YYYY-MM-DD}}",
    "endDate": "{{YYYY-MM-DD}}",
    "maximumAttendeeCapacity": 10,
    "location": {
      "@type": "Place",
      "name": "EmbryoGenesis laboratory, Mohali",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Top Floor, Rayat Bahra Dental College & Hospital, {{LOCALITY}}",
        "addressLocality": "Mohali",
        "addressRegion": "Punjab",
        "postalCode": "{{PIN_CODE}}",
        "addressCountry": "IN"
      }
    }
  }
}
```

Keep the address identical to the master NAP record (7.3); the ACF options page should fill it.

### 6.8 Article (blog posts)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "MedicalWebPage",
      "@id": "https://embryogenesis.in/blog/{{slug}}/#webpage",
      "url": "https://embryogenesis.in/blog/{{slug}}/",
      "name": "{{H1}}",
      "inLanguage": "en-IN",
      "isPartOf": { "@id": "https://embryogenesis.in/#website" },
      "lastReviewed": "{{YYYY-MM-DD}}",
      "reviewedBy": { "@id": "https://embryogenesis.in/#founder" },
      "breadcrumb": { "@id": "https://embryogenesis.in/blog/{{slug}}/#breadcrumb" },
      "mainEntity": { "@id": "https://embryogenesis.in/blog/{{slug}}/#article" }
    },
    {
      "@type": "BlogPosting",
      "@id": "https://embryogenesis.in/blog/{{slug}}/#article",
      "headline": "{{H1_MAX_110_CHARS}}",
      "description": "{{META_DESCRIPTION}}",
      "image": ["{{FEATURED_IMAGE_1200x630}}"],
      "datePublished": "{{YYYY-MM-DDThh:mm:ss+05:30}}",
      "dateModified": "{{YYYY-MM-DDThh:mm:ss+05:30}}",
      "author": {
        "@type": "Person",
        "@id": "https://embryogenesis.in/about/team/#{{AUTHOR_SLUG}}",
        "name": "{{AUTHOR_NAME}}",
        "url": "https://embryogenesis.in/about/team/#{{AUTHOR_SLUG}}"
      },
      "publisher": { "@id": "https://embryogenesis.in/#organization" },
      "mainEntityOfPage": { "@id": "https://embryogenesis.in/blog/{{slug}}/#webpage" },
      "articleSection": "{{For clinicians | Patient education | Embryology careers}}",
      "inLanguage": "en-IN",
      "citation": [
        { "@type": "CreativeWork", "name": "{{REFERENCE_1_TITLE}}", "url": "{{REFERENCE_1_URL}}" }
      ]
    }
  ]
}
```

For academy posts, use `WebPage` instead of `MedicalWebPage` and drop `lastReviewed` (keep `reviewedBy` if reviewed). For the founder as author, use `"author": {"@id": "https://embryogenesis.in/#founder"}`.

### 6.9 BreadcrumbList

Rank Math outputs this when breadcrumbs are on. The template below is for reference and QA.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "@id": "https://embryogenesis.in/diagnostics/endometrial-infection-test/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://embryogenesis.in/" },
    { "@type": "ListItem", "position": 2, "name": "Diagnostics", "item": "https://embryogenesis.in/diagnostics/" },
    { "@type": "ListItem", "position": 3, "name": "Endometrial Infection Test" }
  ]
}
```

### 6.10 Event (CME webinars)

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "@id": "https://embryogenesis.in/for-clinicians/cme-webinars/{{slug}}/#event",
  "name": "{{WEBINAR_TITLE}}",
  "description": "{{ONE_PARAGRAPH_AGENDA}}",
  "startDate": "{{YYYY-MM-DDThh:mm:00+05:30}}",
  "endDate": "{{YYYY-MM-DDThh:mm:00+05:30}}",
  "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {
    "@type": "VirtualLocation",
    "url": "https://embryogenesis.in/for-clinicians/cme-webinars/{{slug}}/"
  },
  "image": ["{{EVENT_IMAGE_1200x630}}"],
  "organizer": { "@id": "https://embryogenesis.in/#organization" },
  "performer": [
    { "@id": "https://embryogenesis.in/#founder" },
    { "@type": "Person", "name": "{{GUEST_SPEAKER_NAME}}", "jobTitle": "{{GUEST_SPEAKER_ROLE}}" }
  ],
  "audience": { "@type": "MedicalAudience", "audienceType": "Clinician" },
  "isAccessibleForFree": true,
  "offers": {
    "@type": "Offer",
    "url": "https://embryogenesis.in/for-clinicians/cme-webinars/{{slug}}/",
    "price": "0",
    "priceCurrency": "INR",
    "availability": "https://schema.org/InStock",
    "validFrom": "{{YYYY-MM-DDThh:mm:00+05:30}}"
  }
}
```

**Notes:**
- `price: 0` here is a free event registration, not a test price.
- Call it "CME" only if the session is accredited by a state medical council (`{{CME_ACCREDITATION}}`); otherwise use "webinar" or "case discussion".
- After the event: leave the Event markup in place (past events are valid; keep `eventStatus` as `EventScheduled` unless it was cancelled or moved), and add the recording as a `VideoObject` on the same page.

### 6.11 Developer note: the Rank Math filter

Create `wp-content/mu-plugins/eg-schema.php`. Hook `add_filter( 'rank_math/json_ld', function( $data, $jsonld ) { … }, 99, 2 );`. In it:

1. Replace `$data['publisher']` / the Organization entity with the 6.2 node, built from an options page (ACF) so NAP is edited in one place.
2. On templates `test`, `clinician-resource`, `city`, `patient` and medical posts, change the WebPage `@type` to `MedicalWebPage` and add `reviewedBy`, `lastReviewed` and `citation` from ACF fields.
3. Append the MedicalTest, Service + partner, EducationalOccupationalProgram, Course, Event or FAQPage nodes from ACF.
4. Never output a node whose required ACF fields are empty. Skip it instead (this prevents `{{placeholders}}` going live).

---

## 7. Entity and brand disambiguation plan

### 7.1 The problem

"Embryogenesis" is a common biology term. Today, searches for the brand return Wikipedia and textbook pages (research doc 02, finding 1). Google and AI assistants need consistent, repeated signals that "EmbryoGenesis" is a specific lab in Mohali.

### 7.2 Naming convention (use everywhere)

| Context | Form |
|---|---|
| Brand name in copy | **EmbryoGenesis**: one word, capital E and G. Never "Embryo Genesis", "Embryogenesis" or "EMBRYOGENESIS" in running text. The ™ appears only in the logo lock-up. |
| First mention on every page and profile | "EmbryoGenesis, an infertility diagnostic and research centre in Mohali, Punjab" (the approved boilerplate wording in `04-brand-voice-and-design-system.md`, section 6). Keep "Mohali" in every first mention. |
| Listing and press descriptions | The 25-, 50- or 100-word boilerplate from doc 04, section 6, **verbatim**. The 100-word version names the partner cities only once each partner has consented. |
| Schema `name` | "EmbryoGenesis"; `alternateName` "EmbryoGenesis Diagnostics" (6.2) |
| Listings that allow a descriptor field | "EmbryoGenesis Diagnostics, Mohali" (matches the blueprint) |
| Google Business Profile **name** | Exactly what is on the signage at the lab (`{{SIGNAGE_NAME}}`). GBP rules forbid adding descriptors or keywords to the name unless they are part of the real-world name. If the signage reads "EmbryoGenesis", the GBP name is "EmbryoGenesis"; the descriptor goes in the category and description. |
| Disambiguation sentence (About page footer note, LinkedIn "About", Wikidata description; add after the boilerplate) | "Not to be confused with embryogenesis, the biological process of embryo development." |
| Founder | "Prof. (Dr.) Pulakes Purkait, Founder & Director". Never "Dr." alone in a context that implies a medical doctor; add "Ph.D." where space allows. |

### 7.3 NAP and handles (one master record)

The client supplies these, and the developer stores them in one ACF options page that feeds the header, footer, contact page and schema.

| Field | Value |
|---|---|
| Name | EmbryoGenesis |
| Address | Top Floor, Rayat Bahra Dental College & Hospital, `{{LOCALITY}}` (audit suggests Sahauran / Kharar; confirm), Mohali, Punjab `{{PIN_CODE}}`, India |
| Primary phone | `{{PRIMARY_PHONE}}`. **One** number, written `+91 XXXXX XXXXX`, used everywhere. Retire the other three from public pages or label them clearly (e.g. "Admissions: …"). |
| WhatsApp | `{{WHATSAPP_BUSINESS_NUMBER}}` |
| Email | `{{PRIMARY_EMAIL}}`. Recommend moving from Gmail to a domain address (e.g. `lab@embryogenesis.in`) for trust and deliverability. Until then: info.embryogenesis@gmail.com. |
| Hours | `{{HOURS}}` |
| Unified social handle | Recommended `@embryogenesisindia` (or the closest available) on LinkedIn, Instagram, Facebook, YouTube and X (`{{HANDLE_DECISION}}`). Keep the old handles and point their bios to the new ones. |

Use the same NAP, character for character, on the site, GBP, Bing Places, Apple Business Connect, Justdial, LinkedIn and every directory below.

### 7.4 Google Business Profile

- **One profile, for the Mohali lab only.** It is the only place EmbryoGenesis staff serve people in person.
- **Primary category:** "Medical laboratory". Secondary: "Research institute". Add "Educational institution" only if academy staff are on-site and serve students at that address during stated hours; otherwise leave it off.
- **Website link:** `https://embryogenesis.in/?utm_source=google&utm_medium=organic&utm_campaign=gbp`. Appointment link: `/contact/`.
- **Description** (750 characters max): the 50-word boilerplate (doc 04) verbatim, then the test names and "Tests are ordered by your doctor". No prices, no superlatives.
- **Photos:** real exterior, signage, entrance (for wayfinding inside the dental college), lab and team. Geotagging is unnecessary. No AI images.
- **Services:** list the 4 tests by name with no prices.
- **Products:** off. **Posts:** monthly (CME, news).
- **Q&A:** seed 3 factual questions (where is the lab inside the campus, who orders tests, turnaround).
- **Reviews:**
  - do not incentivise or bulk-request;
  - reply neutrally, and **never confirm someone was a patient or mention health details** in a reply;
  - do not embed reviews on the site until the legal review of testimonials is complete.
- **Partner centres:** **do not** create GBP listings for Navi Mumbai, Udaipur or Jalandhar under the EmbryoGenesis name (no EmbryoGenesis staff or signage there, which violates GBP rules). Instead, ask each partner to:
  1. add "Sample collection for EmbryoGenesis endometrial tests" to their own GBP services or description;
  2. link to our city page from their website.
- **Also claim:** Bing Places (import from GBP) and Apple Business Connect.

### 7.5 Knowledge-graph profiles

| Profile | Action | Owner |
|---|---|---|
| ORCID (0000-0002-8814-9939) | Add employment "EmbryoGenesis, Mohali" with the website URL; list publications; add the LinkedIn and Scholar links | Prof. Purkait |
| Google Scholar | Create or claim the profile; affiliation "EmbryoGenesis, Mohali"; verified email on the domain once one exists | Prof. Purkait |
| ResearchGate | Fix the profile link (the site currently points to the generic directory); add the institution | Prof. Purkait |
| LinkedIn | Create the company page (Industry: Medical and Diagnostic Laboratories; website; the disambiguation "About"); fix the founder URL (remove `%20`); staff list EmbryoGenesis as employer | Client + TechnoTaau social team |
| Wikidata | Create an item for EmbryoGenesis **only after** 2–3 independent published sources exist (press, university MoU page, conference programme). Statements: instance of "medical laboratory" and "research institute", country India, located in Mohali, founded Nov 2023, founder (link or create a founder item with the ORCID ID), official website. Follow Wikidata's conflict-of-interest guidance and cite sources. **Do not** attempt a Wikipedia article now (notability not yet met). | TechnoTaau Team, month 3–4 |
| Crunchbase | Optional, low priority | Client |

### 7.6 Directory listings

| Directory | Purpose | Notes |
|---|---|---|
| Justdial | Local citation and phone discovery | Category: pathology / diagnostic lab. Same NAP. **Opt out of paid "best" badges.** |
| Sulekha | Local citation | Same NAP |
| IndiaMART / TradeIndia | B2B discovery ("diagnostic lab services", "lab training") | Service listings without prices ("price on request") |
| Practo (lab listing, if eligible) and similar lab directories (e.g. Lybrate) | Patient-side discovery | List only tests; no pricing; check each platform does not add "best" badges |
| LifeLinkr (ART clinic directory) | B2B visibility to the ART ecosystem | Check whether labs or service providers can list; otherwise use it as a prospecting source |
| ivf.net | Already lists the Bahra B.Sc./M.Sc. Add the lab-training events and the lab profile; link to the academy pages. | |
| Careers360, Shiksha, Collegedunia | Academy | These list the *university*. Ask each university to add EmbryoGenesis/ITHS as the lab partner, with a link to the program page. Correct any wrong fees. |
| NABL directory | Only if accredited | Links to the scope certificate |
| ISAR / IFS / ACE member or sponsor directories | B2B authority | Via membership or conference participation (section 10) |

---

## 8. GEO / AI-search visibility plan

AI Overviews appear on a large share of health queries (estimates range from 44% to 88%). ChatGPT, Gemini, Perplexity and Copilot answer clinician and student questions directly. Our goal is to be the **cited source**, not just a ranked link.

### 8.1 Content rules that make pages quotable

1. **Answer-first:** a 40–60 word direct answer under every H1 and at the top of every H2 section (templates in section 4).
2. **One fact per sentence** for key facts: turnaround, sample type, who orders, guideline wording. AI systems lift sentences, not paragraphs.
3. **Tables** for comparisons and "at a glance" facts (test vs what it checks vs sample vs timing vs turnaround).
4. **Named, dated sources** in the text: "ESHRE (2023) states…", with links. Cited pages get cited.
5. **Evidence honesty.** Say plainly what a test cannot do. Balanced pages are preferred for YMYL answers, and this sets us apart from competitors that overclaim.
6. **Consistent entity facts** everywhere (7.2–7.3). The same one-line description on the site, LinkedIn, GBP, directories and press releases.
7. **Author and reviewer bylines** with credentials, linked to Person pages with ORCID.
8. **Freshness:** a visible "Updated" date; review medical pages every 6 months.
9. **Crawlability:** allow AI crawlers (5.6); content in HTML, not in images or PDFs only; no JS-only rendering of key text.
10. **Bing matters.** Several AI search tools rely on Bing's index, so keep IndexNow on and Bing Webmaster Tools clean.

### 8.2 Third-party corroboration (what AI systems read beyond our site)

- University program pages and Careers360/Shiksha listings naming EmbryoGenesis.
- Partner hospital pages naming EmbryoGenesis as their collection lab.
- Press coverage (section 10) using our standard description.
- Conference programmes (ISAR, IFS, ACE) listing our speakers.
- Peer-reviewed publications and abstracts with the EmbryoGenesis affiliation.
- LinkedIn company page posts.

### 8.3 llms.txt (optional, low effort)

`llms.txt` is a proposed convention and no major engine is confirmed to use it. It costs 15 minutes, so publish it at `https://embryogenesis.in/llms.txt`:

```
# EmbryoGenesis
> EmbryoGenesis is an infertility diagnostic and research centre in Mohali, Punjab, established in November 2023. Its lab develops endometrial tests in-house and works with IVF clinicians through partner collection centres. Founded by reproductive scientist Prof. (Dr.) Pulakes Purkait, it also trains embryologists through university-affiliated degree programmes and hands-on lab courses. Tests are ordered and interpreted by the treating doctor. Prices are not published; partner rate card on request.

## Tests
- [Endometrial Infection Test (chronic endometritis)](https://embryogenesis.in/diagnostics/endometrial-infection-test/)
- [ERFA endometrial receptivity test](https://embryogenesis.in/diagnostics/erfa-endometrial-receptivity-test/)
- [Endo-Immune Test](https://embryogenesis.in/diagnostics/endo-immune-test/)
- [Receptivity PX](https://embryogenesis.in/diagnostics/receptivity-px/)

## For clinicians
- [Sample collection protocol](https://embryogenesis.in/for-clinicians/sample-collection-protocol/)
- [Report interpretation](https://embryogenesis.in/for-clinicians/report-interpretation/)
- [Become a collection partner](https://embryogenesis.in/partner-with-us/)

## Academy
- [Academy](https://embryogenesis.in/academy/)

## About
- [Founder: Prof. (Dr.) Pulakes Purkait](https://embryogenesis.in/about/pulakes-purkait/)
- [Editorial policy](https://embryogenesis.in/about/editorial-policy/)
```

### 8.4 20-prompt monitoring panel

**Method:**
- On the first working day of each month, run each prompt in a logged-out or fresh session in these surfaces: ChatGPT (search on), Google AI Overviews and AI Mode (India location), Gemini, Perplexity and Microsoft Copilot.
- Record in a shared sheet:
  - mentioned (Y/N);
  - cited URL (ours or a third party's);
  - accuracy of the facts stated (correct / wrong / outdated);
  - any compliance problem (e.g. an AI calling a test "patented" or "best").
- **Score** = the number of prompts where EmbryoGenesis is mentioned or cited in at least 2 of the 5 surfaces. This matches the blueprint KPI: baseline 0/20, 3/20 at 3 months, 8/20 at 6 months.
- Wrong facts trigger a fix at the source page (clearer wording, an FAQ, a schema field) and on third-party profiles.

| # | Prompt (exact wording) | Audience | Page we want cited |
|---|---|---|---|
| 1 | Which labs in India test for chronic endometritis using CD138 immunohistochemistry? | Clinician | EIT page |
| 2 | Is there an Indian alternative to the ERA endometrial receptivity test? | Clinician | ERFA page |
| 3 | Endometrial receptivity test labs in India with results in under two weeks | Clinician | ERFA page |
| 4 | What does ESHRE recommend for investigating repeated implantation failure? | Clinician | Blog C11 / For Clinicians |
| 5 | When should the endometrial biopsy be taken for a receptivity test in an HRT cycle? | Clinician | Sample collection protocol |
| 6 | How can my IVF clinic become a sample collection centre for a specialist fertility diagnostics lab? | Partner | Partner page |
| 7 | Where can I get uterine NK cell testing in India, and is it recommended? | Clinician | Endo-Immune page |
| 8 | Endometrial testing lab in Punjab for IVF clinics | Clinician | Mohali page / For Clinicians |
| 9 | My IVF failed twice. What tests should I ask my doctor about? | Patient | Repeated IVF failure page |
| 10 | What is chronic endometritis and how is it tested? | Patient | EIT page / blog P2 |
| 11 | Which tests are recommended after recurrent miscarriage? | Patient | Recurrent miscarriage page |
| 12 | Where can I give a sample for an endometrial receptivity test in Navi Mumbai? | Patient / clinician | Navi Mumbai page |
| 13 | Endometrial biopsy test in Jalandhar or Udaipur | Patient / clinician | Jalandhar and Udaipur pages |
| 14 | What is EmbryoGenesis in Mohali? | Brand | Homepage / About |
| 15 | Who is Pulakes Purkait? | Brand | Founder page |
| 16 | What is the ERFA "Soil Test" for IVF? | Brand | ERFA page |
| 17 | Clinical embryology courses in Punjab | Student | Academy hub |
| 18 | How do I become a clinical embryologist in India after Class 12? | Student | Blog A3 |
| 19 | B.Sc. ART and Clinical Embryology at Rayat Bahra University: eligibility and duration | Student | Rayat Bahra program page |
| 20 | Hands-on embryology or lab training courses near Chandigarh | Student / professional | Lab training page |

---

## 9. 90-day editorial calendar (24 articles)

**Window:** launch week (17 Nov 2026) to 4 Feb 2027, publishing Tuesday and Thursday.

**Mix:**
- 12 clinician/B2B (50%) and 6 patient (25%);
- 6 academy (25%), timed for the Jan–Mar career-awareness season.

**Production:**
- Articles 1–4 are written and reviewed before launch (blueprint weeks 2–4) so the blog is not empty at go-live.
- Batch scientific reviews twice a week (blueprint 3.2).
- Every article passes Gates 1–5.
- Author = the EmbryoGenesis expert who contributed (suggested in the last column); scientific reviewer = Prof. Purkait; clinical co-reviewer = `{{RMP_NAME}}` when available.

**Evidence rule for every topic:**
- Quote guidelines (ESHRE, HFEA, NICE, Cochrane) accurately.
- State limits.
- No outcome or success-rate claims.
- No therapy promotion.
- No prices.

| # | Date | Title | Target keyword | Audience | Intent | Internal link target | Suggested author |
|---|---|---|---|---|---|---|---|
| C1 | Tue 17 Nov 2026 | Chronic endometritis testing in repeated implantation failure: what the 2023 ESHRE recommendations say | chronic endometritis diagnosis RIF | Clinician | I (pro) | `/diagnostics/endometrial-infection-test/` | Dr. Vidhu Wadhwa |
| P1 | Thu 19 Nov 2026 | After repeated IVF failure: which tests to discuss with your doctor | tests after failed ivf | Patient | I | `/patients/repeated-ivf-failure/` | Prof. Purkait |
| C2 | Tue 24 Nov 2026 | Becoming a sample collection centre for a specialist endometrial lab: a checklist for IVF clinics | diagnostic collection centre partnership | Partner | C | `/partner-with-us/` | Partner desk + Prof. Purkait |
| C3 | Thu 26 Nov 2026 | Endometrial biopsy timing for receptivity testing: natural cycles and HRT cycles | endometrial biopsy timing for receptivity test | Clinician | I (pro) | `/for-clinicians/sample-collection-protocol/` | Dr. Meenu Bhanot |
| A1 | Tue 1 Dec 2026 | B.Sc. or M.Sc. in clinical embryology? Eligibility, duration and career paths compared | b.sc clinical embryology | Student | C | `/academy/` | Academy team |
| C4 | Thu 3 Dec 2026 | CD138 immunohistochemistry for chronic endometritis: methods, cut-offs and reporting pitfalls | CD138 testing | Clinician (pathology) | I (pro) | `/diagnostics/endometrial-infection-test/` | Dr. Vidhu Wadhwa |
| P2 | Tue 8 Dec 2026 | Chronic endometritis: symptoms, testing and treatment, explained simply | chronic endometritis symptoms | Patient | I | `/diagnostics/endometrial-infection-test/` | Dr. Vidhu Wadhwa |
| C5 | Thu 10 Dec 2026 | ERFA and ERA compared: how two endometrial receptivity tests differ in method, sample and turnaround | ERA test alternative india | Clinician | C | `/diagnostics/erfa-endometrial-receptivity-test/` | Prof. Purkait |
| C6 | Tue 15 Dec 2026 | Endometrial receptivity testing in 2026: what the evidence supports, and where it falls short | endometrial receptivity test evidence | Clinician | I | `/for-clinicians/report-interpretation/` | Prof. Purkait |
| A2 | Thu 17 Dec 2026 | What hands-on lab training covers: immunohistochemistry, microtomy and molecular genetics explained | embryology hands-on training | Student / professional | C | `/academy/lab-training/` | Academy team |
| C7 | Tue 22 Dec 2026 | How to read an endometrial receptivity report: receptive, pre-receptive and post-receptive results | endometrial receptivity report interpretation | Clinician | I (pro) | `/for-clinicians/report-interpretation/` | Prof. Purkait |
| P3 | Thu 24 Dec 2026 | Recurrent miscarriage: which tests the ESHRE guideline recommends, and which it does not | recurrent miscarriage tests | Patient | I | `/patients/recurrent-miscarriage/` | Prof. Purkait + `{{RMP_NAME}}` |
| C8 | Tue 29 Dec 2026 | Uterine NK cells and cytokine testing: what the evidence supports today | uterine NK cell test | Clinician | I (pro) | `/diagnostics/endo-immune-test/` | Prof. Purkait |
| A3 | Thu 31 Dec 2026 | How to become a clinical embryologist in India after Class 12 | how to become an embryologist after 12th | Student | I | `/academy/` | Dr. Meenu Bhanot |
| C9 | Tue 5 Jan 2027 | Send-out endometrial testing for smaller IVF clinics: logistics, quality checks and turnaround | send-out testing for ivf clinics | Clinician / owner | C | `/for-clinicians/` | Partner desk |
| P4 | Thu 7 Jan 2027 | Endometrial biopsy for fertility testing: what to expect on the day | endometrial biopsy procedure | Patient | I | `/patients/how-to-get-tested/` | Dr. Meenu Bhanot |
| C10 | Tue 12 Jan 2027 | CME recap: chronic endometritis in RIF, case discussion and audience Q&A (webinar 1) | chronic endometritis cme | Clinician | I | `/for-clinicians/cme-webinars/` | Prof. Purkait + guest |
| A4 | Thu 14 Jan 2027 | Clinical embryologist salary in India, 2027: what published sources show | clinical embryology salary in india | Student | I | `/academy/` | Academy team |
| C11 | Tue 19 Jan 2027 | A stepwise checklist for investigating repeated implantation failure (aligned with ESHRE 2023) | repeated implantation failure workup | Clinician | I (pro) | `/for-clinicians/` | Prof. Purkait |
| P5 | Thu 21 Jan 2027 | Thin endometrium: common causes and what the evidence says about treatment options | thin endometrium causes | Patient | I | `/patients/repeated-ivf-failure/` | Prof. Purkait + `{{RMP_NAME}}` |
| A5 | Wed 27 Jan 2027 | Is your clinical embryology degree valid? How to check UGC recognition and the awarding university | is clinical embryology degree ugc approved | Student / parent | I | `/academy/admissions/` | Academy team |
| C12 | Thu 28 Jan 2027 | Shipping endometrial biopsy samples: transport media, temperature and chain of custody | endometrial biopsy sample transport | Clinician / nurse | I (pro) | `/for-clinicians/sample-collection-protocol/` | Dr. Vidhu Wadhwa |
| P6 | Tue 2 Feb 2027 | Unexplained infertility: what it means and which tests are worth discussing (rewrite) | unexplained infertility tests | Patient | I | `/patients/` | Prof. Purkait |
| A6 | Thu 4 Feb 2027 | Clinical embryology courses in Punjab: a checklist for comparing programmes | clinical embryology course in punjab | Student / parent | C | `/academy/` | Academy team |

**Dependencies and guardrails per topic**

| Item | Needs | Guardrail |
|---|---|---|
| C2, C9 | Partner programme details (blueprint open item 8) | No revenue promises; "partnership", not "franchise", unless the legal model is a franchise |
| C4, C12 | Lab method and transport SOPs (`{{METHOD}}`, `{{TRANSPORT_SOP}}`) | Cut-offs come from cited literature; state that thresholds vary between studies |
| C5 | ERFA methodology from the client; public information on ERA only | Factual, non-disparaging comparison (ASCI comparative-advertising rules). "ERA" used descriptively. "Patent application published (No. 202431001616 A)". No accuracy-superiority claims without published data. **Fallback if the method is not supplied:** "Questions to ask before choosing an endometrial receptivity test". |
| C6, C8 | — | Quote ESHRE "not recommended" and "insufficient data" lines exactly; HFEA ratings |
| C10 | Webinar 1 held in early December (blueprint: monthly CME) | Speaker consent for the recap; no patient identifiers in case slides |
| P3, P5 | Clinical co-reviewer ideally | P3 states ESHRE's strong recommendation against LIT neutrally. P5 states that ESHRE does not recommend intrauterine PRP. **No links to held therapy pages.** |
| A1, A3, A4, A6 | Verified fee and salary sources with dates | No "100% placement" or salary promises. Sourced ranges only (e.g. AIIMS Nagpur contract post, published fresher ranges). A6 is a checklist plus a sourced fee table, with no ranking. |
| A5 | Documented legal basis of the ITHS + university structure (research doc 01, 4.3) | **Do not publish until the client supplies the documents.** Fallback: "Career options in IVF labs without NEET". |
| P6 | Rewrite of the old post | Remove the uncited "NIH 92%" claim; cite primary sources |

**After 90 days:** repeat the cycle with refreshes of C1, C6 and P1 (6-month review), the first anonymised data piece if ethics-approved, and the Hindi phase if approved.

---

## 10. Off-page and link plan, and KPIs

### 10.1 Principles

- Earn links from the places our audience already trusts: professional societies, universities, journals, partner hospitals and trade press.
- No paid link schemes, PBNs, link exchanges or mass guest posting. Any paid placement (e.g. conference sponsorship pages) is fine but must be `rel="sponsored"` or nofollow on their side; we do not ask otherwise.
- Every press or partner mention uses the standard description (7.2) and links to the most relevant deep page, not only the homepage.

### 10.2 Tactics and timing

| Channel | Tactic | Link / mention target | Timing | Owner |
|---|---|---|---|---|
| **CME webinars** | Monthly 45-minute case discussion with one external speaker (an IVF clinician from a partner or prospect clinic). Co-host with a society chapter where possible. Recording on YouTube and the event page. | Event pages; speakers' clinics link to the event; society chapter pages list it | Webinar 1 early Dec 2026, then monthly | Prof. Purkait + TechnoTaau social |
| **Partner hospitals** | Each partner adds a "Sample collection for EmbryoGenesis endometrial tests" page or section linking to our city page; a co-branded poster has a QR code to the city page | 3 links at launch, plus one per new partner | Launch + ongoing | Partner desk |
| **Conferences** | Submit abstracts or posters (CD138/CE methods, turnaround logistics, education outcomes) to ISAR (Indian Society for Assisted Reproduction), IFS (Indian Fertility Society) and ACE (Academy of Clinical Embryologists) annual meetings. Consider an exhibitor table. Check each 2027 abstract deadline (`{{CONFERENCE_DATES}}`). Consider ESHRE 2027 only with solid data. | Programme pages naming the speaker and EmbryoGenesis | Abstracts Dec 2026–Mar 2027 | Prof. Purkait |
| **Journals** | Case series or methods papers in Indian indexed journals (e.g. Journal of Human Reproductive Sciences (ISAR), Fertility Science and Research (IFS), Journal of Obstetrics and Gynecology of India, Indian Journal of Pathology & Microbiology for CD138 work). The affiliation must read "EmbryoGenesis, Mohali, India". | Journal pages, PubMed and Google Scholar | First submission by month 4–6 | Prof. Purkait |
| **Universities** | Rayat Bahra University, Bahra University, ITHS, and Guru Ghasidas Vishwavidyalaya (MoU Nov 2024) add or update pages naming EmbryoGenesis and linking to the relevant academy or research page. Ask the PJ Embryogenesis Health & Education Foundation (Kolkata) for a link too. | `/academy/` program pages; `/research/` | Month 1–2 | Client |
| **Aggregators** | Careers360, Shiksha, Collegedunia, ivf.net: correct the facts and add the lab-partner link | Academy pages | Month 1–2 | TechnoTaau Team + client |
| **Trade press** | Pitch BioSpectrum India, Medical Dialogues, ET HealthWorld and Express Healthcare. Angles: (1) Indian-developed endometrial tests with patent applications published; (2) the collection-centre network expanding to new cities; (3) university MoUs and the embryology workforce; (4) expert commentary on what ESHRE says about IVF add-ons (evidence-honest, highly quotable); (5) later, an anonymised data report if ethics-approved. | News pages linking to the relevant test page or `/research/` | One pitch per month from launch | TechnoTaau Team |
| **Regional press** | The Tribune (Chandigarh), Hindustan Times Chandigarh and Dainik Bhaskar for academy admissions and MoU news | `/academy/`, `/news-events/` | Admissions season (Apr–Aug) and MoU events | TechnoTaau Team |
| **Journalist requests** | Answer relevant queries on journalist-request platforms (e.g. Qwoted) with evidence-based quotes from Prof. Purkait | Founder page | Ongoing, 2 per month | TechnoTaau Team |
| **LinkedIn** | Founder and company posts summarising each clinician article; share CME recordings. Builds referral traffic and corroboration even though the links are nofollow. | Article URLs | 3–4 posts per week (blueprint) | Social team |
| **Linkable assets** | (1) The sample collection protocol PDF; (2) the RIF investigation checklist (C11); (3) the clinical embryologist salary report (A4), updated each year; (4) the report-interpretation guide | These pages | As published | Writers |

### 10.3 KPIs (3 and 6 months after launch)

**Measurement points:**
- Launch is planned for 12–18 Nov 2026, so the 3-month check is around 18 Feb 2027 and the 6-month check around 18 May 2027.
- The baseline is taken 30 days after GA4/GSC go live, because nothing is measured today.

**How to read the targets:**
- The **blueprint targets** stay as the plan.
- The **SEO floor** is the minimum we would consider healthy for a new, low-authority site in a YMYL niche. If results sit between floor and target, we are on track. Below floor, we review.

| KPI | Baseline (Oct 2026) | 3-month floor | 3-month target | 6-month floor | 6-month target | Source |
|---|---|---|---|---|---|---|
| Qualified partner/clinician enquiries per month (`partner_enquiry` + `generate_lead` with form_type clinician_order or kit_request) | not tracked | 5 | 10 | 15 | 30 | GA4 + CRM |
| New collection-centre partners signed (cumulative) | 3 | +2 | +5 | +8 | +15 | Client |
| Academy enquiries per month | not tracked | 20 | 40 | 60 | 100 | GA4 (academy_application) |
| Organic sessions per month | not tracked (very low) | 600 | 1,500 | 2,500 | 5,000 | GA4 (consented sessions only; true traffic is higher) |
| Indexed pages with impressions | ~20 | 40 | 45 | 70 | 80 | GSC |
| Tier-1 keywords (section 3) ranking top 20 | ~0 | 10 | 15 | 20 | 25 | GSC / rank tracker |
| Non-branded queries with clicks per month | ~0 | 40 | 80 | 150 | 300 | GSC |
| Branded search clicks per month ("embryogenesis" queries landing on our site) | low | 150 | 250 | 300 | 500 | GSC |
| Referring domains (quality, relevant) | `{{BASELINE_RD}}` | +8 | +12 | +20 | +30 | GSC Links / Ahrefs Webmaster Tools (free) |
| GBP actions per month (calls, directions, website) | profile not verified | 20 | 40 | 50 | 100 | GBP Insights |
| AI-answer panel (section 8.4) | 0/20 (assumed) | 2/20 | 3/20 | 5/20 | 8/20 | Monthly panel |
| Core Web Vitals (mobile, key templates) | failing | pass (lab) | pass | pass | pass (field, if CrUX data exists) | PSI / GSC |
| Sitemap URLs indexed | n/a | 85% | 90% | 90% | 95% | GSC |
| Technical errors (5xx, redirect chains, broken canonicals, 404s from internal links) | many | 0 | 0 | 0 | 0 | Screaming Frog monthly |

**Reporting:**
- A monthly report from TechnoTaau Team covering: KPIs, top queries, new and lost pages, the AI panel, link wins, CWV, and next month's priorities.
- Re-baseline the targets after the first 30 days of data. The blueprint also commits to this.

---

## 11. Placeholders and items needing client input

| Placeholder / item | Needed for | Priority |
|---|---|---|
| `{{PRIMARY_PHONE}}` / `{{PRIMARY_PHONE_E164}}`, `{{WHATSAPP_BUSINESS_NUMBER}}`, `{{ADMISSIONS_PHONE_E164}}` | NAP, schema, GBP, tracking labels | Critical, before build |
| `{{PIN_CODE}}`, `{{LOCALITY}}`, `{{LAT}}`/`{{LNG}}`, `{{HOURS}}`, `{{GOOGLE_MAPS_PLACE_URL}}` | NAP, schema, GBP | Critical |
| `{{SIGNAGE_NAME}}` and `{{LEGAL_ENTITY_NAME}}` | GBP name, schema `legalName` | Critical |
| `{{PRIMARY_EMAIL}}`: move to a domain email? | Trust, schema | High |
| `{{HANDLE_DECISION}}` (unified social handle) and the LinkedIn company page | `sameAs`, entity | High |
| Partner details per city: street, PIN, phone, website, collection days and hours, `{{PARTNER_CONSENT}}` to be named and linked | City pages, schema | Critical for city pages |
| Test methodology, sample type, transport and turnaround per test (`{{METHOD}}`, `{{TRANSPORT_SOP}}`, `{{RECEPTIVITY_PX_METHOD}}`); confirm "Receptivity PX" vs "ReceptivityPX" spelling | Test pages, protocol, C4, C5, C12 | Critical |
| `{{RMP_NAME}}`, qualification, `{{NMC/SMC_REG_NO}}` (clinical co-reviewer); registration numbers for Dr. Vidhu Wadhwa and Dr. Meenu Bhanot if applicable | Reviewer lines, Person/Physician schema | High |
| `{{NABL_CERT_NO}}`, `{{ART_REG_NO}}`, other registrations | Trust signals, schema | Medium (only if held) |
| Patent status: grant certificates, if any (otherwise "application published") | Research page, all copy | High |
| `{{FEE_POLICY}}`: may tuition fees be published? (They are on the current site; the brief bans *test* prices only.) | Academy pages, schema `offers` | High |
| `{{ITHS_EMBRYOGENESIS_ROLE}}`, `{{UGC_REFERENCE}}`, awarding-university documents; are the Ph.D. and PG Diploma still offered? | Program pages, A5 | Critical for academy pages |
| `{{PARTNER_LOGO_PERMISSIONS}}` and expert consents (About page images); decision on the GIOSTAR logo (legal) | Image restore | Medium |
| `{{CME_ACCREDITATION}}` (state medical council CME credits?) | Event naming | Medium |
| `{{GTM_ID}}`, `{{GA4_ID}}`, `{{CMP_CHOICE}}`, `{{GRIEVANCE_OFFICER}}` | Tracking, privacy policy | Critical, before launch |
| `{{AI_TRAINING_OPT_OUT}}` (allow or block AI training crawlers) | robots.txt | Low |
| Backup of the 2023–2025 uploads | Image restore list | High |
| WordPress staging access and confirmation of Rank Math Free vs Pro | Build | Critical |

---

*Prepared by TechnoTaau Team*
