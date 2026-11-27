# ITHS: Current Website Audit (translationalhealthscience.in)

**Prepared by:** TechnoTaau Team (lead: Jakhar Singh)
**Date:** 27 November 2026
**Method:** the sitemap, robots.txt and about 25 pages were read on 27 Nov 2026 with a web fetcher and `curl` (titles, meta descriptions, robots, canonical, JSON-LD types and redirects). **Search Console and GA4 data are not yet available.** Traffic and ranking statements wait for the export described in `03-gsc-ga4-data-request-chrome-prompt.md`.
**Priority:** P0 = fix now (legal, money or reputation risk, or a live error); P1 = fix before the 2027–28 admission campaign; P2 = fix during the rebuild.

---

## 1. Site inventory

| Item | Finding |
|---|---|
| Platform | WordPress, Elementor, Rank Math SEO (sitemap index), GTM-P795G8W3 |
| Host | `https://www.translationalhealthscience.in` (non-www 301s to www) |
| Sitemap | `sitemap_index.xml`: **97 URLs** = 42 pages, 24 posts, 31 category archives. Last modified 10 Oct 2026 |
| robots.txt | Default WordPress rules plus the sitemap line. No AI-crawler rules |
| Meta | Titles and meta descriptions are written on key pages. `index, follow, max-image-preview:large`. Self-canonicals present |
| Schema (Rank Math) | Home: EducationalOrganization, Person ×2, ContactPoint, PostalAddress, FAQPage, BreadcrumbList. BSc Clinical Embryology: Course + 4 CourseInstance, FAQPage. Blog post: BlogPosting, FAQPage. **No JSON-LD** on the campus pages, the Shimla landing page or the nutrigenetics landing page |
| Navigation | Home, About, Courses (7), Campuses (4), Admission, Life @ ITHS, News, Contact Us; Blog in the footer |
| Social links | Facebook /TranslationalHealthScience, Instagram /translationalhealthscience, X @ITHScience, YouTube @TranslationalHealthScience. No LinkedIn |
| ithsedu.in | 302 redirect (www and non-www) to `https://translationalhealthscience.in/`, which then 301s to www (a two-hop chain) |

### 1.1 Page URLs (42)

- **Core:** `/`, `/about/`, `/contact-us/`, `/careers/`, `/campus-life/`, `/blog/`, `/news-events/`
- **Campuses:** `/campuses/`, `/campuses/mohali/` (labelled "Chandigarh"), `/campuses/shimla/`, `/campuses/hoshiarpur/`, `/campuses/bhopal/`
- **Programmes:** `/programs/`; Clinical Embryology `/programs/clinical-embryology/` + `/bsc/`, `/msc/`, `/phd/`, `/pgd-clinical-embryology/`; Nutrigenetics `/programs/nutrigenetics-personalized-nutrition/` + `/bsc/`, `/msc/`; Stem Cell `/programs/stem-cell-regenerative-medicine/` + `/bsc/`, `/msc/`; Cancer Biology `/programs/cancer-biology/` + `/bsc/`, `/msc/`; `/programs/b-tech-stem-cell-tissue-engineering/`; Molecular Medicine `/molecular-medicine/` + `/bsc-molecular-medicine/`, `/msc-molecular-medicine/` (outside `/programs/`); `/msc-neuroscience/` (outside `/programs/`)
- **Admissions:** `/admission/`, `/apply-now/`, `/iths-admission-form-2026-27/`, `/iths-sgsu-admission-form/`, `/iths-set/`
- **Campaign landing pages:** `/clinical-embryology-shimla/`, `/nutrigenetics-admissions/`
- **Thank-you pages:** `/thank-you/`, `/clinical-embryology-shimla/thank-you/`, `/nutrigenetics-admissions/thank-you/`

### 1.2 Posts (24)

- **Admission and career guides (19):** Bahra University Shimla courses/fees/admission; stem cell & tissue engineering course guide; what is translational health science; BSc clinical embryology scope; transform your career; MSc and BSc clinical embryology; MSc and BSc anthropology; B.Tech/M.Tech stem cell; "India's leading" nutrigenetics programme; want to become an embryologist; want to become a cancer research scientist; BA/BSc and MA/MSc anthropology admission 2025; BSc and MSc nutrigenetics admission 2025; India's 1st B.Tech stem cell; food, nutrition and dietetics career guide; ART course in India guide 2026; BSc cancer biology colleges; BSc embryology colleges in India; health science courses after 12th PCB.
- **News and events (5):** Aashakiran IVF Centre visit; Teachers' Day 2026; Orientation 2026; Sofia Khan Talent Hunt prize; Nutrition Week 2026.

## 2. Findings

### 2.1 P0: fix now

| # | Finding | Where | Why it matters | Fix |
|---|---|---|---|---|
| A1 | The admission form for **RBU, RBPU and BU** shows bank details in the name of **"Registrar Scope Global Skills University"** (ICICI, Hoshangabad Road, Bhopal) | `/iths-admission-form-2026-27/` | Applicants to Punjab and Himachal campuses may pay the Bhopal university's account. Money and trust risk | Client confirms the correct account per campus today; show only the right account for the campus selected |
| A2 | B.Tech "View Details" links to **iths.technotaau.com**, an external staging host | `/campuses/mohali/` | Sends users to a staging site; a public staging copy can be indexed and duplicate the live site | Point the link to `/programs/b-tech-stem-cell-tissue-engineering/`; password-protect and `noindex` the staging host (it did not respond from our network, so check it from a normal browser) |
| A3 | Visible build note: "Note for build: the images below are temporary licensed stock. Replace them with real Bahra University, Shimla campus and lab photos before launch." | `/clinical-embryology-shimla/` | Public text saying the photos are stock; ASCI requires real infrastructure visuals | Remove the note; replace the stock images with real photos |
| A4 | "NAAC Accredited" badge attributed to **Rayat Bahra University** on the **Bahra University (Shimla)** page | `/clinical-embryology-shimla/` | Wrong institution for the accreditation claim | Show only Bahra University's own, verified accreditation, with grade and validity, or remove the badge |
| A5 | Placement claims conflict: **95%** (home, about, admission, programmes), **100%** (Bhopal page, BSc embryology colleges post), counters showing **"0 %"** to crawlers (`/programs/`, `/campuses/`) | Site-wide | "100% placement" is not allowed under ASCI education guidelines; unproven percentages are misleading under the CCPA 2022 guidelines | Replace with "placement support" until audited data for the 2025–26 batch exists; then show the figure with the source and the disclaimer |
| A6 | "Only institute in India" and "only institute **in the world**" offering nutrigenetics, on two copies of the same slide; "#1st", "India's first", "North India's first", "Central India's first", "India's premier", "India's leading" | Home, about, programme pages, posts | Contradictory and unsubstantiated superlatives | Remove, or keep only claims with a dated, documented source |
| A7 | "15+ Patents Filed", "8+ Patents", "15+ Research Patents" | Home, about, programme pages | Must be "patent applications filed/published" with a verifiable list | Reword and publish the list of application numbers on ithsedu.in `/research/` |
| A8 | The admission form makes **Aadhaar** mandatory and collects religion, income and family data | Both admission forms | DPDP data minimisation; restrictions on Aadhaar collection by private bodies | Counsel review; make Aadhaar optional unless a university rule requires it; add consent and a notice **[VERIFY with counsel]** |

### 2.2 P1: before the 2027–28 campaign

| # | Finding | Fix |
|---|---|---|
| B1 | Site still says "Admissions open **2026–27**" (home, admission, meta descriptions); form URL `/iths-admission-form-2026-27/`; posts "…admission 2025" | Update to 2027–28 when the session opens. Move the form to an evergreen slug (`/admission-form/`) with a 301 from the old one, so the URL does not change each year |
| B2 | Thank-you pages are **indexable** (`index, follow`) and in the sitemap | `noindex` and remove them from the sitemap |
| B3 | Form pages (`/iths-admission-form-2026-27/`, `/iths-sgsu-admission-form/`) are indexable and have no H1 | `noindex`; they hold personal-data forms, not search content |
| B4 | `/apply-now/` and `/iths-set/` have no H1; campus "Apply Now" buttons and "Download Prospectus" link to `#` | Add H1s and working links |
| B5 | Inconsistent facts: 3 vs 4 campuses (home stats vs FAQ); founded 2015 vs 2023; Shimla 60 km vs about 80 km from Chandigarh; Stem Cell MSc at Shimla yes/no; RBU called Chandigarh and Mohali | One fact sheet (master plan §5.3), applied everywhere |
| B6 | **Possible keyword cannibalisation** (several URLs for one intent): Shimla (campus page, Shimla landing page, Bahra University post); BSc embryology (programme page and 4 posts); nutrigenetics (programme pages, landing page, 2025 admission post, "leading" post); B.Tech stem cell (programme page and 3 posts); cancer biology (programme pages and 2 posts) | Decide per cluster with Search Console data (master plan §4.3) |
| B7 | Anthropology posts (2), while no anthropology programme appears in the menus | Confirm whether it is offered; update, or 301 to the closest current page |
| B8 | Internal links on plain `http://` (Apply Now slides, BSc embryology post) | Change to `https://www.` |
| B9 | Third-party names: "200+ graduates working at … Nova IVF, Indira IVF, Cloudnine & Apollo Fertility"; "Work with Giostar, Stempeutics" | Remove unless written permission and evidence exist |
| B10 | Salary figures ("₹4–8 LPA", "₹8–12 LPA", "₹15–25 LPA", "$40–80K") | Present as industry ranges with a cited, dated source, not as ITHS outcomes; or remove |
| B11 | "ART Bill Compliant" | The ART (Regulation) Act became law in 2021. Reword to what is actually true (for example, "curriculum covers the ART Act 2021 and ICMR guidelines") |
| B12 | Typos ("Admission Proccess" on three campus pages) | Fix |
| B13 | No schema on the campus pages and the two landing pages; FAQPage earns no rich result since 7 May 2026, and Course info rich results are gone (R07 §1) | Schema plan in master plan §6.4 |
| B14 | Phone numbers: five numbers across the site (main, Hoshiarpur, Shimla, Bhopal, form help) | Keep per-campus numbers but list them in one place; use one main number in sitewide schema |

### 2.3 P2: during the rebuild

- **Template counters** that render "0" without JavaScript: render the real number in HTML.
- **URL pattern:** Molecular Medicine and Neuroscience sit outside `/programs/`. Leave them unless Search Console shows little traffic; any move needs a 301.
- **Campus-life and news galleries** are image grids with no captions: add short captions and alt text (search and accessibility).
- **llms.txt:** none. Add one that lists programmes, campuses, awarding universities and contacts (no claims).
- **robots.txt:** decide on AI search crawlers (allow OAI-SearchBot, PerplexityBot, Claude-SearchBot and Google-Extended per the client's choice; R07 §3).

## 3. What we still need (data)

| Data | Source | Used for |
|---|---|---|
| Clicks, impressions, queries and pages for 16 months | Search Console | Which URLs carry the traffic; the cannibalisation decisions; protecting rankings |
| Indexing, sitemaps, Core Web Vitals, links, crawl stats (any 5xx) | Search Console | Technical fixes; the non-www returned a 503 once during our checks |
| Traffic by channel, landing pages, key events, form submissions | GA4 | Lead baseline per campus; ads plan |
| Lead and admission numbers per campus and programme for 2025–26 and 2026–27 | Admissions office / CRM | KPIs, ads budget, placement-claim evidence |

The step-by-step export prompt is in `03-gsc-ga4-data-request-chrome-prompt.md`.
