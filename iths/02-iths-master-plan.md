# ITHS: Two-Domain Website, SEO and Social Media Master Plan

**Prepared by:** TechnoTaau Team. Team lead and sign-off: Jakhar Singh.
**Client:** Institute of Translational Health Science (ITHS)
**Domains:** translationalhealthscience.in (admissions and ads) and ithsedu.in (official institute site)
**Date:** 27 November 2026 | **Version:** 1.1 (Search Console and GA4 data applied; see `04-baseline-report.md` §5)
**Read with:** `iths/00-iths-brief.md` (direction, facts, guardrails), `iths/01-current-site-audit.md` (audit findings A1–A8, B1–B14, C1–C8), `iths/04-baseline-report.md` (search and analytics baseline), `iths/03-gsc-ga4-data-request-chrome-prompt.md` (data we still need).
**Labels:** **D#** = a decision the client needs to make (section 12). **(E)** = a TechnoTaau Team estimate, re-set once Search Console data arrives. **[VERIFY with counsel]** = needs the client's lawyer. **[DATA]** = waits for the Search Console and GA4 export.

---

## Contents

0. Summary for the client
1. Will this create duplication? The rules that prevent it
2. Domain architecture
3. URL ownership map
4. translationalhealthscience.in: the admissions site
5. ithsedu.in: the official institute site
6. Search, AI answers and local search across both domains
7. Social media architecture
8. Ads and lead management
9. Goals and KPIs
10. Roadmap and the next 30 days
11. Team and RACI
12. Decisions and inputs needed from the client
13. Risks and mitigations
14. If ITHS becomes a university: the merge path
- Appendix A: social handle reservation checklist
- Appendix B: claims checklist for every page, post and ad

---

## 0. Summary for the client

**Your plan works, with one condition: every topic has one home.**

- **translationalhealthscience.in stays the admissions website** for all four campuses. It already holds the pages that rank (programmes, campuses, admission guides). We keep every one of those URLs and improve them. Ads point here.
- **ithsedu.in becomes the official ITHS website**: who ITHS is, leadership, research, partner universities, achievements and announcements. It does **not** copy programme or campus pages. Its "Programmes" and "Apply" buttons go to the admissions site.
- **Social media:** a new official @ithsedu set of accounts for achievements and announcements, and one account set per campus for daily activity. Instagram **Collab posts** put one post on both accounts without duplicating it. We recommend **one** YouTube channel and **one** LinkedIn page (with campus showcase pages), not five of each.
- **Google sees one organisation with two websites**, linked by structured data. A search for "ITHS" should then show both sites at the top: ithsedu.in as the official site and the admissions site for courses.

**What the data says (`04-baseline-report.md`):**
- Organic search brings 44% of visits and 46% of leads.
- Paid search converted at 17.7% in the 2026 season.
- AI assistants already send visitors who convert at 23.6%.
- Bhopal is the strongest campus in search; Shimla and Hoshiarpur barely appear.
- Workshop certificates with participants' names are indexed in Google.

**Fix first (this week):** the admission form shows a Bhopal university bank account for Punjab and Himachal campuses (A1), a link points to a TechnoTaau staging site (A2), a public "note for build" says the Shimla photos are stock (A3), and placement, "first" and patent claims need correcting (A5–A7).

**What we need from you:** twelve decisions (section 12; the biggest is D1, what happens to the existing social accounts), Search Console and GA4 access (or the export from `03-gsc-ga4-data-request-chrome-prompt.md`), and the facts in section 5.3.

**Timeline:** data and decisions by 13 December 2026, ithsedu.in designed and written by 31 January 2027, launch target **9 February 2027** (to be confirmed), 2027–28 admission pages live by 1 March 2027, campaign peak May to August 2027.

---

## 1. Will this create duplication? The rules that prevent it

Duplication happens when two URLs (or two accounts) publish the same thing and compete for the same search or the same audience. Two domains of one organisation are normal (many institutes run an official site and an admissions portal). Problems only start when their content overlaps.

| # | Rule | What it prevents |
|---|---|---|
| R1 | **One topic, one home.** Each page type belongs to one domain (section 3). The other domain links to it and never copies it | Two sites competing for "BSc clinical embryology", split rankings |
| R2 | **ithsedu.in summarises, the admissions site explains.** ithsedu.in may name programmes in 1–3 sentences with a link; full curriculum, eligibility, fees and forms live only on the admissions site | Thin duplicates of programme pages |
| R3 | **One news room.** From ithsedu.in's launch, institutional news is published only on ithsedu.in. Campus daily activity goes on campus social accounts, not on either website as news | The same announcement on two sites |
| R4 | **If something must appear on both sites** (rare, for example a press release), the copy on the admissions site carries `rel=canonical` to the ithsedu.in URL | Duplicate news in Google |
| R5 | **Different search targets.** The admissions site targets course, campus, eligibility, fee and "after 12th" searches. ithsedu.in targets the brand, research, leadership and news | Keyword cannibalisation between domains |
| R6 | **One organisation in structured data.** Both domains point to a single `EducationalOrganization` ID on ithsedu.in (section 6.4) | Google and AI assistants treating them as two different institutes |
| R7 | **Social: share, don't repost.** Use Instagram Collab posts and story reshares. One YouTube channel and one LinkedIn page with showcase pages | Split engagement and five half-empty channels |
| R8 | **Ad landing pages are `noindex`** when they are copies of programme pages for a campaign | Thin near-duplicates in the index |
| R9 | **One fact, one value** across both sites, all accounts, Google Business Profiles and aggregators (section 5.3) | Conflicting facts that confuse users and AI answers |

## 2. Domain architecture

### 2.1 Roles

| | translationalhealthscience.in | ithsedu.in |
|---|---|---|
| Role | Admissions and ads website for **all four campuses** (see D2) | Official website of the institute |
| Audience | Applicants (12th PCB students, graduates, MBBS/BDS/BAMS for PG Diploma), parents | Parents checking credibility, partner universities and hospitals, faculty candidates, media, researchers, future regulators |
| Content | Programmes, campuses, eligibility, fees, scholarships (ITHS-SET), apply forms, campus life, admission and career guides | About, leadership, academic partners, research and patent applications, achievements, news and events, media kit, careers, policies, contact |
| Search target | Non-brand course and location searches ("bsc clinical embryology", "embryology course in chandigarh", "nutrigenetics course") and brand plus course | Brand searches ("ITHS", "Institute of Translational Health Science", "ITHS Prof. Pulakes Purkait"), research and news |
| Main call to action | Enquire, call, WhatsApp, apply, ITHS-SET | Read, contact the office, "Explore programmes" (to the admissions site) |
| Social links in header/footer | Campus accounts for the page's campus, plus @ithsedu | @ithsedu accounts |

### 2.2 How the two sites link

- **Header of ithsedu.in:** About · Leadership · Partners · Research · News & Events · Careers · Contact · button **"Programmes & Admissions"** (to `https://www.translationalhealthscience.in/programs/`).
- **Header/top bar of the admissions site:** a slim line "Official website of ITHS: ithsedu.in". **Footer:** "About ITHS", "News & achievements" and "Careers" link to ithsedu.in.
- **Contextual links:** ithsedu.in partner and achievement pages link to the matching campus or programme page; programme pages link to the relevant faculty and research pages on ithsedu.in.
- **Anchor text** is descriptive ("BSc Clinical Embryology admissions at Bahra University, Shimla"), never "click here".

### 2.3 Before ithsedu.in launches

Keep the current 302 redirect (ithsedu.in → translationalhealthscience.in) until launch day. Two small fixes now: point it straight to `https://www.translationalhealthscience.in/` (one hop instead of two), and keep it a 302 (temporary), because ithsedu.in will have its own content.

## 3. URL ownership map

**Rule:** no URL that gets search clicks is removed or moved without a 301 and Jakhar Singh's approval. Actions marked [DATA] wait for Search Console.

### 3.1 translationalhealthscience.in pages (42)

| URL | Owner | Action |
|---|---|---|
| `/` | Admissions | Keep. Refresh for 2027–28; fix claims (A5–A7); add "Official website: ithsedu.in" |
| `/about/` | Admissions (short) | Keep the URL. Trim to an applicant-focused summary (200–300 words: what ITHS is, partner universities, why study here) with a link to ithsedu.in/about/. ithsedu.in carries the full story, so the two pages say different things |
| `/campuses/`, `/campuses/mohali/`, `/campuses/shimla/`, `/campuses/hoshiarpur/`, `/campuses/bhopal/` | Admissions | Keep. Fix facts and claims; add schema (6.4); name the awarding university at the top. Keep `/campuses/mohali/` as the slug (do not rename) |
| `/programs/` and all programme and level pages (Clinical Embryology ×5, Nutrigenetics ×3, Stem Cell ×3, Cancer Biology ×3, B.Tech, Molecular Medicine ×3, MSc Neuroscience) | Admissions | Keep. Each names the campuses and awarding universities. Molecular Medicine and Neuroscience stay at their current URLs [DATA] |
| `/admission/` | Admissions | Keep as the admissions hub (process, eligibility, dates, scholarships, fees) |
| `/apply-now/` | Admissions | Keep as the enquiry form. Add an H1; fix the `#` buttons |
| `/iths-admission-form-2026-27/`, `/iths-sgsu-admission-form/` | Admissions | `noindex`. Move to evergreen `/admission-form/` and `/admission-form-sgsu/` with 301s (B1). Fix bank details (A1) |
| `/iths-set/` | Admissions | Keep. Add an H1, test dates, eligibility and scholarship rules in text |
| `/clinical-embryology-shimla/`, `/nutrigenetics-admissions/` | Admissions (ad landing pages) | If they get little organic traffic: `noindex`, remove from the sitemap, use only for ads. If they rank: keep indexed and remove the overlap with the campus or programme page [DATA] |
| `/art-and-clinical-embryology-program/` | Admissions (paid landing page) | **Protected.** The top lead page on the site (339 key events in 12 months). Keep `noindex`, out of the sitemap, and use it for the 2027 search ads |
| `/thank-you/` ×3 | Admissions | `noindex`; remove from the sitemap (B2) |
| `/campus-life/` | Admissions | Keep. Monthly curated photos from the campus accounts, with captions and alt text |
| `/news-events/` | Changes at ithsedu.in launch | Keep the URL with the existing items and a banner "Latest news is now on ithsedu.in/news/". After 3 months, if it has few clicks, 301 to `https://ithsedu.in/news/` [DATA] |
| `/careers/` | **ithsedu.in** | Move at launch: publish `https://ithsedu.in/careers/`, then 301 the old URL to it |
| `/contact-us/` | Admissions | Keep, as the admissions contact page (per-campus numbers, WhatsApp, map). Institutional and media contacts live on ithsedu.in |
| `/blog/` | Admissions | Keep for admission and career guides only |

### 3.2 Posts (24)

| Group | Action |
|---|---|
| 19 admission and career guides | Stay on the admissions site. Refresh for 2027–28. Merge overlapping posts by cluster (4.3) [DATA]. Fix "India's leading", "India's 1st", "2025" in titles and body |
| 2 anthropology posts | Confirm whether anthropology is offered (B7). If not, 301 to the closest current page |
| 5 news posts (Aashakiran visit, Teachers' Day, Orientation, Talent Hunt, Nutrition Week) | Stay where they are (no copy on ithsedu.in). New institutional news goes to ithsedu.in from launch |
| 31 category archives (25 indexed), plus 15 date and 2 author archives | `noindex, follow` all except about 5 topic hubs that get written introductions; turn off date archives (baseline §2.8) |
| 17 workshop certificate PDFs with participants' names (indexed) | **P0:** `noindex` (X-Robots-Tag), remove from search, and rebuild `/certificate/` as a verification page (audit C1) |

### 3.3 ithsedu.in pages: see section 5.1.

## 4. translationalhealthscience.in: the admissions site

The client's developer keeps the current WordPress site. No redesign is needed for this plan; if the client wants the new design applied here as well, that is a separate decision (D10).

### 4.1 Protect what ranks

1. Export Search Console data before any change (`03-…-chrome-prompt.md`).
2. Mark every URL with clicks in the last 16 months as **protected**. Protected URLs keep their slug, H1 topic and main content. Edits improve them; they do not replace them.
3. Make changes in batches, one cluster at a time, and note each batch in a change log with the date (so any ranking change can be traced).
4. Watch Search Console weekly for 8 weeks after each batch.

### 4.2 Fix list

Audit items A1–A8 (now) and B1–B14 (before the campaign) in `01-current-site-audit.md`. Owners and dates are in section 10.

### 4.3 Cannibalisation: one primary page per search intent

**Data result (baseline §2.5):** the overlaps are mostly healthy. Posts and programme pages answer different questions, so **nothing with clicks is merged**. Only posts with almost no clicks are merged, after file 01 confirms their numbers.

Method, per cluster:
1. In Search Console, filter queries for the cluster term (for example "shimla") and check the Pages tab: which URLs get impressions and clicks for the same queries.
2. Choose the **primary page** (usually the one with the most clicks and the right intent: programme page for "bsc clinical embryology", campus page for "embryology course in shimla").
3. Other pages either **change angle** (a guide answers a different question and links to the primary) or **merge** into the primary with a 301.
4. Re-check after 6–8 weeks.

| Cluster | Candidate pages | Likely primary (to confirm with data) |
|---|---|---|
| Shimla / Bahra University | `/campuses/shimla/`, `/clinical-embryology-shimla/`, `/bahra-university-shimla-courses-fees-admission/` | `/campuses/shimla/`. Data: 0 clicks from 335 impressions, so this is a visibility problem, not cannibalisation. Deepen the page, add a Google Business Profile, get a Bahra University link |
| BSc clinical embryology | `/programs/clinical-embryology/bsc/`, `bsc-clinical-embryology-scope…`, `exploring-the-possibilities…`, `want-to-become-an-embryologist…`, `bsc-embryology-colleges-in-india…` | Keep the embryologist post (220 clicks in 3 months), the colleges guide and the PhD page. BSc programme page takes "bsc embryology". Merge only `exploring-the-possibilities…` |
| Nutrigenetics | `/programs/nutrigenetics-personalized-nutrition/` (+bsc, msc), `/nutrigenetics-admissions/`, `bsc-and-msc-nutrigenetics-admission-2025`, `join-indias-leading-program…` | Programme page (now position 10–19: strengthen it); merge the 2025 admission post and the "leading" post |
| B.Tech stem cell | `/programs/b-tech-stem-cell-tissue-engineering/`, `study-stem-cell-tissue-engineering…`, `indias-1st-b-tech…`, `stem-cell-tissue-engineering-…-course-india-guide` | Programme page plus the 2026 guide; merge the two older posts |
| Cancer biology | `/programs/cancer-biology/` (+bsc, msc), `want-to-become-a-cancer-research-scientist…`, `bsc-cancer-biology-colleges-in-india…` | Programme page plus the colleges guide; the BSc page takes "bsc cancer biology" and "bsc oncology" queries |

### 4.3a Internal links to level pages (baseline §2.9)

The PhD page (5th-best organic page) has 2 internal links. The MSc embryology page has almost none and is "crawled, not indexed". Several BSc and MSc pages have 0–3 links. Before 1 March 2027:
- add the BSc, MSc, PhD and PG Diploma pages under each programme in the Courses menu;
- add a "Choose your level" block on each programme hub;
- link from each guide to the right level page with descriptive anchors.

### 4.4 Ad landing pages

- Prefer the existing programme and campus pages as ad destinations (relevant, fast, already trusted).
- Build a dedicated landing page only for a specific campaign offer (for example ITHS-SET registration or a campus open day). Dedicated pages are `noindex`, not in the sitemap, and not linked in the menu.
- Every landing page: awarding university and location above the fold, real campus photos, the form with consent text, the campus phone and WhatsApp, and no claims outside Appendix B.

### 4.5 Admissions content calendar (December 2026 to August 2027)

Two guides a month from December to April, then refreshes during the season. Each new guide links to its primary page and does not target that page's main keyword (4.3).

| Month | Publish or refresh | Primary page it supports |
|---|---|---|
| Dec 2026 | NEW: "Clinical embryology course in Punjab: Mohali and Hoshiarpur campuses" ("bsc embryology colleges in punjab" has impressions and no clicks); titles and meta descriptions rewritten on the 6 highest-impression pages (baseline §2.10) | Campus pages; BSc programme page |
| Jan 2027 | Refresh: "Health science courses after 12th PCB" (2027 edition); NEW: "How to check whether a degree is UGC-recognised"; refresh: "BSc embryology colleges in India" | `/programs/`, `/admission/`, BSc page |
| Feb 2027 | NEW: "Clinical embryology course in Bhopal (Madhya Pradesh)"; refresh: Bahra University Shimla guide (2027) | `/campuses/bhopal/`, `/campuses/shimla/` |
| Mar 2027 | NEW: "PG Diploma in Clinical Embryology for MBBS, BDS and BAMS graduates"; NEW: "Nutrigenetics vs nutrition and dietetics: which BSc?" | PGD page; nutrigenetics programme page |
| Apr 2027 | NEW: "PhD in clinical embryology in India: eligibility and process"; ITHS-SET 2027 page update | PhD page; `/iths-set/` |
| May 2027 | Refresh all programme pages for 2027–28 dates and fees; publish ITHS-SET results notice on ithsedu.in | All programme pages |
| Jun 2027 | NEW: "Careers in biology without NEET: options after the NEET result" (factual, no disparaging of NEET) | `/programs/` |
| Jul–Aug 2027 | Refresh "last dates" on campus and admission pages; no new posts | `/admission/` |

Salary and placement sections in guides follow Appendix B.

## 5. ithsedu.in: the official institute site

### 5.1 Sitemap (launch set: 16 pages plus news)

Paths reuse the admissions site's paths where the meaning is the same, so a future merge keeps them (section 14). Paths reserved for the admissions content (`/programs/`, `/campuses/`, `/admission/`, `/apply-now/`, `/iths-set/`, `/blog/`) are **not used** on ithsedu.in.

| Path | Page | Purpose |
|---|---|---|
| `/` | Home | Mission in one line; **an "Admissions 2027–28" band above the fold linking to the admissions site** (brand searches will move to ithsedu.in, and they bring leads today: baseline §5); latest 3 announcements; partner universities; research highlights; leadership; "Programmes & Admissions" button |
| `/about/` | About ITHS | Story, founding year (one value), mission and vision, how the collaboration model works (in words approved by counsel), governance |
| `/leadership/` | Leadership | Founder, Director and the programme heads |
| `/leadership/jyoti-garhewal/`, `/leadership/pulakes-purkait/` | Profiles | Qualifications, ORCID, publications, patent applications (with numbers), awards (exact name, issuer, year) |
| `/faculty/` | Faculty | Faculty by campus and subject, with qualifications. Links to the campus pages |
| `/partners/` | Academic partners | The four universities: what each awards, the campus, approvals (as verified), link to the campus page on the admissions site. Industry and training partners only with permission |
| `/research/` | Research | Research areas, labs, list of publications, patent applications filed and published (numbers and dates) |
| `/research/publications/` | Publications | Full list with DOIs, from ORCID |
| `/achievements/` | Achievements | Awards, student achievements (with consent), milestones by year |
| `/news/` and `/news/<slug>/` | News room | Announcements, achievements, collaborations, events. Each item dated, with real photos |
| `/events/` | Events | Conferences, workshops, guest lectures; past and upcoming |
| `/media/` | Media kit | Logo files, fact sheet (5.3), approved boilerplate, leadership photos, press contact, press coverage list |
| `/careers/` | Careers | Moved from the admissions site (with a 301) |
| `/contact-us/` | Contact | Institute office, media, partnerships; admissions numbers link to the admissions site |
| `/privacy-policy/`, `/terms/`, `/grievance-redressal/` | Policies | DPDP notice; grievance officer; links to each university's anti-ragging and grievance pages |

### 5.2 Page content rules

- Every page names the partner universities as the degree-awarding institutions where programmes are mentioned.
- News items: headline, date, place, 150–400 words, 2–6 real photos with captions and alt text, the people named with consent, and a link to the relevant admissions page only when useful.
- No placement percentages or salary figures on ithsedu.in. They belong, with evidence, on the admissions site (Appendix B).
- Announcements of "firsts" only with a source (for example, a university notification or a government approval letter), linked or quoted with date.

### 5.3 ITHS fact sheet (one fact, one value)

The client fills this in once; TechnoTaau Team applies it to both sites, every bio, Google Business Profiles and aggregator corrections.

| Fact | Current values found | Value to use |
|---|---|---|
| Official name and short name | Institute of Translational Health Science; ITHS | (confirm) |
| Founding year | 2015 and 2023 | (client) |
| Number of campuses | 3 and 4 | 4 (confirm) |
| RBU campus label | Chandigarh, Mohali | Recommend: "Rayat Bahra University, Mohali (Chandigarh region)" — the address stays Mohali; "near Chandigarh" can stay in copy because students search for Chandigarh (D4) |
| RBU campus PIN | 140104 (ITHS site), 140302 (EmbryoGenesis brochure) | (client) |
| Programmes per campus and level | Differ between campus, admission and post pages | (client; one table) |
| Shimla distance from Chandigarh | 60 km, about 80 km | (check on a map; use one) |
| Phone numbers | Main 76966 14978; Hoshiarpur 76966 08683; Shimla 84277 76481; Bhopal 98156 92195; form help 88717 89844 | Keep per campus; confirm the Bhopal number is not shared with EmbryoGenesis |
| Emails | admission.iths@gmail.com; careers@translationalhealthscience.in | Recommend domain emails (admissions@, info@, media@ on ithsedu.in) (D11) |
| Patent applications | "15+", "8+" | List of application numbers and dates |
| Placement data | 95%, 100%, 0% | Latest completed year, with method, or no number |
| Accreditation per university | NAAC badge on the wrong university | Each university's own verified status |
| Fees per programme per campus | Not published | Recommend publishing the university-approved fee per year (D8) |

### 5.4 Design direction

- **Look:** calm, academic and editorial, clearly the "official" voice: generous white space, one serif for headings and a sans serif for text, a restrained palette from the ITHS logo, real photography of labs and people, no sliders, no counters that animate from zero.
- **Shared identity:** the same ITHS logo and colours as the admissions site, so users see one organisation. The admissions site keeps its louder, conversion-focused layout; ithsedu.in is quieter.
- **Key components:** announcement card (date, category, image); partner-university card (logo with permission, campus, link); person card (photo, name, role, ORCID); research card (area, lead, publications); fact strip (numbers only from 5.3); "Programmes & Admissions" handoff band at the foot of every page.
- **Accessibility and speed:** WCAG 2.1 AA, Lighthouse accessibility 100 and performance 90+ on mobile, images in WebP/AVIF under 200 KB, fonts self-hosted with `font-display: swap`.
- **Deliverables from TechnoTaau Team:** sitemap (5.1), wireframes for Home, About, Leadership profile, Partners, Research, News list and News item; a design file or HTML reference build (as for EmbryoGenesis); page copy for the launch set; SEO and schema specification. The client's developer builds in WordPress (D9).

### 5.5 Build and launch specification

- WordPress (separate install from the admissions site), a lightweight theme or block-based build, Rank Math or Yoast with the schema in 6.4 added by hand where the plugin cannot do it.
- **Staging** on a password-protected subdomain with `noindex` (lesson from A2). Never link to staging from a live site.
- `https://ithsedu.in` as the canonical host (non-www, or www: pick one and 301 the other). HTTPS, HSTS, security headers.
- Sitemap, robots.txt, llms.txt (6.8), 404 page, favicon, Open Graph images.
- Launch checklist: remove the 302; submit the sitemap in Search Console; check the Rich Results Test and Schema Markup Validator; test forms; set up the cross-domain GA4 link (6.2); update social bios; add the "Official website" line on the admissions site; 301 `/careers/`.

## 6. Search, AI answers and local search across both domains

### 6.1 Brand search goal

For "ITHS", "Institute of Translational Health Science" and "ITHS Mohali/Shimla/Hoshiarpur/Bhopal": ithsedu.in first (official), the admissions site second with sitelinks, then the campus Google Business Profiles, social profiles and partner-university pages. Two of the organisation's own sites at the top is a strong result, not duplication.

### 6.2 Search Console, Bing and analytics

- **Search Console:** a Domain property for each domain (`translationalhealthscience.in`, `ithsedu.in`), verified by DNS. Same owners on both. TechnoTaau Team gets Full user access.
- **Bing Webmaster Tools:** import both from Search Console. Turn on IndexNow if the SEO plugin supports it.
- **GA4:** one property with one web data stream per site, or one stream covering both, with **cross-domain measurement** set for both domains, so a visitor who goes from ithsedu.in to an admissions form is counted as one journey. Consent Mode v2, default denied. Key events: `generate_lead` (form name and campus only, no personal data), `tel_click`, `whatsapp_click`, `brochure_download`, `iths_set_register`. GA4's "AI Assistant" channel shows visits from AI tools.
- **Fix the current GA4 before 1 March 2027 (baseline §3.3, §3.5):**
  - set event data retention from 2 to 14 months;
  - de-duplicate "Form Submit" (it fires about twice per user);
  - replace the RBU-only phone and WhatsApp events with campus-tagged events;
  - remove the empty `purchase` key event;
  - filter internal and developer traffic (localhost, Tag Assistant);
  - put UTM tags on every link we control.
- **Looker Studio** dashboard with both domains, leads by campus and programme, and ads (section 9).

### 6.3 Internal and cross-domain linking

As in 2.2. Also: each partner-university card on ithsedu.in links to that campus page; each campus page links to the university's own programme page (and we ask each university to link back, 6.6).

### 6.4 Structured data (one organisation, two websites)

On **ithsedu.in** (sitewide):

```json
{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "@id": "https://ithsedu.in/#organization",
  "name": "Institute of Translational Health Science",
  "alternateName": "ITHS",
  "url": "https://ithsedu.in/",
  "logo": "https://ithsedu.in/wp-content/uploads/iths-logo.png",
  "foundingDate": "<from fact sheet>",
  "founder": {"@id": "https://ithsedu.in/leadership/jyoti-garhewal/#person"},
  "sameAs": [
    "https://www.instagram.com/ithsedu",
    "https://www.linkedin.com/company/<ithsedu>",
    "https://www.youtube.com/@<channel>",
    "https://www.facebook.com/<page>"
  ],
  "department": [
    {"@id": "https://www.translationalhealthscience.in/campuses/mohali/#department"},
    {"@id": "https://www.translationalhealthscience.in/campuses/hoshiarpur/#department"},
    {"@id": "https://www.translationalhealthscience.in/campuses/shimla/#department"},
    {"@id": "https://www.translationalhealthscience.in/campuses/bhopal/#department"}
  ]
}
```

On **translationalhealthscience.in**:
- `WebSite` (`@id` `https://www.translationalhealthscience.in/#website`) with `publisher` = `{"@id": "https://ithsedu.in/#organization"}`. Replace Rank Math's separate organisation block with this reference, so there is one organisation, not two.
- Each campus page: `EducationalOrganization` with `@id` `…/campuses/<slug>/#department`, `name` (for example "ITHS at Rayat Bahra University, Mohali"), `parentOrganization` = the ITHS `@id`, `address` (from the fact sheet), `telephone`, and `location` naming the partner university campus.
- Programme pages: `Course` or `EducationalOccupationalProgram` with `provider` = the ITHS `@id`, `educationalCredentialAwarded` naming the degree and the awarding university, and one `CourseInstance` per campus. Google retired Course info rich results (R07 §1), so this markup is for machine reading and AI answers, not for a rich result.
- `BreadcrumbList` on all pages; `BlogPosting` with author and date on guides; `FAQPage` only where a visible FAQ exists (no rich result since 7 May 2026, R07 §1).

Persons (`Person` with `@id` on the leadership profiles, `sameAs` ORCID and LinkedIn) are referenced from both sites.

### 6.5 Local search: Google Business Profiles

- One profile per campus **only if** the ITHS department has its own signage and staff at that address (Google allows departments inside universities to have their own listing when they serve the public separately). Name exactly as on the signage.
- Category: "Educational institution" or the closest education category; website = that campus page on the admissions site (with UTM tags); phone = the campus number.
- Photos: real labs, building, signage. Posts: admission dates and events (monthly in season).
- Reviews: ask students and parents for honest reviews; never offer incentives; reply politely and without personal details.

### 6.6 Partner universities, aggregators and citations

- Ask each university to name ITHS correctly on its programme pages and link to the campus page (and to ithsedu.in from its "collaborations" page). TechnoTaau Team drafts the wording (EmbryoGenesis plan 05 §3.8 has the same ask for the same universities, so we combine them).
- Correct listings on Careers360, Shiksha, Collegedunia, Zollege, CollegeSearch and ivf.net through the universities (they own the college profiles). Use the fact sheet values. Use the spelling "Pulakes" consistently.
- Press: approved news (new programme, ITHS-SET results, a published paper) sent to regional education media in Punjab, Himachal and Madhya Pradesh with a link to the ithsedu.in news item.

### 6.7 Answer-engine questions (to answer on the right page)

| Question students and parents ask | Answer on |
|---|---|
| Is NEET required for BSc clinical embryology? | BSc programme page (FAQ) |
| Which universities offer clinical embryology in Punjab / Himachal / Madhya Pradesh? | Campus pages; Punjab and Bhopal guides |
| Is the ITHS degree UGC-approved? Who awards it? | Programme pages; ithsedu.in `/partners/` |
| What are the fees for BSc clinical embryology at [campus]? | Campus page fee table (if D8 is approved) |
| What is nutrigenetics and what jobs does it lead to? | Nutrigenetics programme page |
| What is the ITHS-SET scholarship test? | `/iths-set/` |
| Who is the Director of ITHS? | ithsedu.in leadership profile |
| What research does ITHS do? Does it hold patents? | ithsedu.in `/research/` (patent applications, with numbers) |

Each answer: a direct 40–60 word answer under a question heading, then detail, with the date of the information.

### 6.8 AI assistants (GEO)

AI assistants sent 195 sessions in 12 months with a 23.6% key-event rate, the best of any channel (baseline §3.1). This work therefore starts in December 2026, not after launch.


- **llms.txt** on both domains: ithsedu.in lists the institute, leadership, partners and research pages; the admissions site lists programmes, campuses, admission and ITHS-SET pages. Facts only, no claims.
- **robots.txt:** allow AI search crawlers (OAI-SearchBot, PerplexityBot, Claude-SearchBot, Bingbot); decide on training crawlers (GPTBot, Google-Extended, ClaudeBot) with the client (D12).
- **Monthly AI prompt panel:** 15 questions (for example "best institute for clinical embryology in Punjab", "is ITHS genuine", "who runs ITHS", "nutrigenetics course in India") asked in ChatGPT, Gemini, Perplexity and Copilot. Record whether ITHS is named, which site is cited, and any wrong facts. Fix wrong facts at the source (our page, a university page or an aggregator).
- **Entity profiles:** LinkedIn company page, YouTube "About", Wikidata item (if the notability rules are met), ORCID for faculty.

## 7. Social media architecture

### 7.1 Accounts

| Account set | Platforms | Role | Posts |
|---|---|---|---|
| **@ithsedu** (official) | Instagram, Facebook, LinkedIn company page, YouTube (the one channel), X (optional), WhatsApp Channel (optional) | Achievements, announcements, collaborations, research, leadership talks, "Admissions open" launch, ITHS-SET, results | 3–4 a week on Instagram; 1–2 a week on LinkedIn; 1 video a month |
| **ITHS at RBU, Mohali** | Instagram, Facebook (LinkedIn showcase page) | Daily campus life, labs, visits, events, student achievements, admission reminders in season | 5–7 a week, plus stories |
| **Clinical Embryology by ITHS · RBPU Hoshiarpur** | Instagram, Facebook (LinkedIn showcase page) | Same, for the campus | 4–6 a week |
| **Clinical Embryology by ITHS · BU Shimla** | Instagram, Facebook (LinkedIn showcase page) | Same | 4–6 a week |
| **Clinical Embryology by ITHS · SGSU Bhopal** | Instagram, Facebook (LinkedIn showcase page) | Same | 4–6 a week |

Suggested handles (check availability, Appendix A): `@ithsedu`, `@iths.rbu`, `@iths.rbpu`, `@iths.bushimla`, `@iths.sgsu`. The department names follow the client's wording once D3 confirms which programmes each campus runs (the Shimla campus page also lists Stem Cell).

### 7.2 What happens to the existing accounts (D1)

The current accounts (Instagram @translationalhealthscience, Facebook /TranslationalHealthScience, X @ITHScience, YouTube @TranslationalHealthScience) carry all of ITHS's followers today.

| | Option A (TechnoTaau Team recommends) | Option B (client's current plan) |
|---|---|---|
| Existing accounts become | The official @ithsedu accounts (rename the handle and name; followers stay) | ITHS at RBU |
| New accounts | ITHS at RBU, plus the three campus accounts | @ithsedu, plus the three campus accounts |
| Official voice starts with | All current followers | Zero followers |
| Brand fit | The handle "translationalhealthscience" already means the whole institute | Followers from Shimla, Hoshiarpur and Bhopal end up on an RBU account |
| Risk | A short notice period ("we are now @ithsedu"); old links redirect on Instagram and YouTube for a while, but update them everywhere | A slow start for the official account; it needs Collab posts and ads to grow |

With either option, the existing **YouTube channel** stays the single ITHS channel (campus videos go into playlists), and the **X account** stays the single official X account.

### 7.3 How a post flows (no duplication)

1. A campus coordinator posts daily activity on the campus account.
2. Anything of institute-level importance (an award, a new collaboration, a result, a published paper) is sent to the central team the same day.
3. The central team posts it on @ithsedu as an **Instagram Collab post** with the campus account (one post, shown on both profiles, shared likes and comments), and as a LinkedIn post on the ITHS page, re-shared by the campus showcase page.
4. If it deserves a web page, it is published on ithsedu.in `/news/`, and the social post links there.
5. Admission posts (dates, ITHS-SET) link to the admissions site with UTM tags (`utm_source=instagram&utm_medium=social&utm_campaign=admissions2027&utm_content=<campus>`).

### 7.4 Content pillars

| Pillar | Campus accounts | @ithsedu |
|---|---|---|
| Learning in the lab | Daily: practicals, equipment, demonstrations (real, consented) | Monthly highlight reel |
| Student life and achievements | Events, competitions, visits | Major awards (Collab) |
| Careers and guidance | Short explainers ("What does an embryologist do?") | Long-form talks by faculty |
| Research and institute news | Share | Original posts |
| Admissions | Reminders in season, campus-specific | Session launch, ITHS-SET, results |

### 7.5 Governance

- **Owners:** one trained coordinator per campus; one central social lead (client side) for @ithsedu; TechnoTaau Team supplies the playbook, templates, calendar and monthly review.
- **Approval:** campus daily posts follow the playbook without pre-approval; anything with a number, a claim, a partner's name or a minor's face goes through the central lead (24-hour turnaround).
- **Templates:** Canva brand kit with one template set; campus accounts use the same look with the campus name in the footer.
- **Consent:** written consent for every identifiable student photo, and a parent's consent for students under 18. Keep a consent log.
- **Bios:** campus bio = campus name, awarding university, campus phone, link to the campus page. @ithsedu bio = official ITHS account, link to ithsedu.in.
- **Monthly report:** followers, reach, saves and shares, profile visits, link clicks, and leads from social (by UTM) per account.

## 8. Ads and lead management

### 8.1 Channels and structure

| Channel | Campaigns | Landing pages |
|---|---|---|
| Google Search | Brand (ITHS, ITHS-SET); programme × location ("bsc clinical embryology punjab", "clinical embryology course chandigarh", "embryology course bhopal", "nutrigenetics course india"); PG Diploma (MBBS, BDS, BAMS) | Programme or campus pages (4.4) |
| Meta (Instagram, Facebook) | Lead forms per campus; awareness video; ITHS-SET registration; retargeting site visitors (adults only) | Instant forms or campus pages |
| YouTube | Short explainers to students and parents | Campus and programme pages |

- **Age:** target **18+** and parents. No targeting or behavioural tracking of under-18s (DPDP s.9; Google already excludes under-18s from personalised ads). 12th-class students are reached through their parents, organic content and search.
- **Geos:** Punjab, Haryana, Himachal, Chandigarh, J&K for RBU, RBPU and BU; Madhya Pradesh and neighbouring states for SGSU; pan-India for PhD and PG Diploma.
- **Ad copy:** Appendix B applies. Name the awarding university in the ad or on the landing page above the fold.

### 8.2 Leads

- **One lead system** for all forms and ad leads (client CRM, or a shared sheet as a minimum). Fields: name, phone, email, campus, programme, level, city, source/medium/campaign (UTM), consent timestamp and wording, and "applicant under 18: parent's consent".
- **Routing:** by campus to that campus's admission counsellor, with a call within 24 hours (the site promises this).
- **Status stages:** new → contacted → counselled → applied → fee paid → enrolled. Weekly export of stages by source.
- **Offline conversion import** into Google Ads and Meta for "applied" and "enrolled", so the campaigns optimise for admissions, not just form fills.

### 8.3 Season calendar (2027–28 intake)

| Period | Focus |
|---|---|
| Dec 2026 – Feb 2027 | Fix the site; 2027–28 pages ready; brand and PG/PhD search; build retargeting audiences |
| Mar – Apr 2027 | ITHS-SET registration; parent-focused awareness; open-day videos |
| May – Jul 2027 | Peak: board results (usually May), NEET result (usually June), university counselling. Highest budget |
| Aug – Sep 2027 | Last dates; lateral entry; PG Diploma |

Budget split by campus and channel is set once the 2025–26 and 2026–27 lead and admission numbers are known (D7).

## 9. Goals and KPIs

Targets are set 30 days after the data export (E). Until then these are the measures and the floors.

| KPI | Measure | Source | Floor or target |
|---|---|---|---|
| K1 Protect organic traffic | Admissions-site **non-brand** organic clicks, and **total leads** (brand clicks are expected to shift to ithsedu.in) | Search Console, CRM | Non-brand clicks no more than 10% below the previous comparable period (no year-on-year data exists before 29 Apr 2026); leads not below the 2026 season |
| K2 Non-brand growth | Non-brand clicks (regex excludes ITHS and translational) | Search Console | Target set from baseline (E) |
| K3 Brand ownership | ithsedu.in and the admissions site in the top 3 for "ITHS" and "Institute of Translational Health Science" | Manual check, Search Console | Within 3 months of launch |
| K4 Leads | Enquiries per campus and programme, per source | CRM, GA4 | Baseline from 2026–27 (D7) |
| K5 Lead quality | Applied ÷ leads; enrolled ÷ applied | CRM | Baseline (D7) |
| K6 Cost | Cost per lead and per admission, by channel | Google Ads, Meta, CRM | Set with budget |
| K7 Social | Followers, reach, link clicks, leads per account | Platform insights, UTM | Monthly trend |
| K8 AI answers | Prompts (of 15) where ITHS is named correctly; GA4 AI Assistant sessions | AI panel; GA4 | Panel baseline in December 2026; sessions above 195 a year |
| K9 Fact consistency | Fact-sheet items that match across sites, bios, profiles and top aggregators | Monthly check | 100% of our own channels; aggregators fixed where the university allows |
| K10 Compliance | Claims outside Appendix B found in the monthly check | Checklist | Zero |

## 10. Roadmap and the next 30 days

### 10.1 Phases

| Phase | Dates | Work | Exit gate |
|---|---|---|---|
| **0. Data and decisions** | 30 Nov – 13 Dec 2026 | GSC/GA4 export; P0 fixes A1–A8; decisions D1–D12; fact sheet; reserve social handles; ithsedu.in redirect fix (2.3) | Export received; A1–A4 fixed; D1–D4 decided |
| **1. Build ithsedu.in, clean the admissions site** | 14 Dec 2026 – 31 Jan 2027 | ithsedu.in wireframes, design and copy; developer build on staging; admissions-site P1 fixes B1–B14; cluster decisions (4.3); schema; GA4 cross-domain; social accounts created and playbook issued | Staging approved by the client |
| **2. Launch** | Target Tue 9 Feb 2027 (TBC) | ithsedu.in live; 301 `/careers/`; "Official website" links; Search Console; social bios updated; launch announcement | Launch checklist (5.5) passed |
| **3. Admissions season** | Mar – Aug 2027 | 2027–28 pages live by 1 Mar; content calendar (4.5); ads (8.3); weekly lead review; monthly SEO, social and AI reports | Monthly KPI review |
| **4. Review** | Sep – Nov 2027 | Season review; next-year plan; decision on the university path (section 14) | Report to the client |

### 10.2 Next 30 days (30 Nov – 29 Dec 2026)

| # | Task | Owner | Due |
|---|---|---|---|
| 1 | Upload the missing Performance exports 01–16 and top pages 01, 02 and 10 (baseline §8) | Jakhar Singh | 2 Dec |
| 2 | Fix A1 (bank details), A2 (staging link), A3 (build note), A4 (NAAC badge), C1 (certificate PDFs), C2 (iths.rbuchd.in), C3 (demo.ithsedu.in password) | Client developer; client confirms facts | 4 Dec |
| 2a | GA4: retention 14 months, de-duplicate Form Submit, internal-traffic filter (C6) | Client developer with TechnoTaau Team | 6 Dec |
| 3 | Decisions D1–D4 and the fact sheet (5.3) | Client | 11 Dec |
| 4 | Reserve all handles (Appendix A) | Client social lead | 6 Dec |
| 5 | Claims rewrite (A5–A7, B9–B11): replacement text for every instance | TechnoTaau Team drafts; client approves | 13 Dec |
| 6 | Baseline report: traffic, top pages, clusters, indexing, AI panel | TechnoTaau Team | 13 Dec |
| 7 | ithsedu.in wireframes and copy for Home, About, Leadership, Partners | TechnoTaau Team | 20 Dec |
| 8 | P1 technical fixes B1–B4, B8, B12, B14 | Client developer | 20 Dec |
| 9 | Social playbook, Canva templates, January calendar | TechnoTaau Team | 22 Dec |
| 10 | Counsel review: collaboration wording, admission form data (Aadhaar), privacy notice | Client's lawyer | 29 Dec |

## 11. Team and RACI

R = responsible, A = accountable, C = consulted, I = informed.

| Work | TechnoTaau Team | Jakhar Singh | Client leadership (Founder, Director) | Client admissions office | Client developer | Campus coordinators | Counsel |
|---|---|---|---|---|---|---|---|
| Strategy, IA, SEO spec | R | A | C | C | I | I | I |
| ithsedu.in design and copy | R | A | C (approve) | C | C | I | C (claims) |
| WordPress build (both sites) | C | A | I | I | R | I | I |
| Fact sheet and claims evidence | C | A | R | R | I | I | C |
| Social playbook and templates | R | A | C | I | I | C | I |
| Daily campus posting | C | I | I | I | I | R | I |
| @ithsedu posting | C | I | A | I | I | C | I |
| Ads | R (or agency) | A | C (budget) | C | C (tracking) | I | I |
| Lead handling | I | I | A | R | C | I | I |
| Legal review | C | I | A | I | I | I | R |

## 12. Decisions and inputs needed from the client

### 12.1 Decisions

| # | Decision | TechnoTaau Team recommendation | Needed by |
|---|---|---|---|
| D1 | Existing social accounts: official @ithsedu (option A) or ITHS at RBU (option B) | Option A (7.2) | 11 Dec 2026 |
| D2 | translationalhealthscience.in for **all four** campuses' admissions, or RBU only | All four (it already ranks for Shimla, Hoshiarpur and Bhopal) | 11 Dec 2026 |
| D3 | Department names per campus, based on the programmes each actually runs | Confirm the programme table first; "Clinical Embryology by ITHS" only where that is the only programme | 11 Dec 2026 |
| D4 | RBU label: Mohali or Chandigarh | Address "Mohali"; copy may say "near Chandigarh" | 11 Dec 2026 |
| D5 | Claims: remove, or provide evidence (placement, firsts, patents, salaries, partner names) | Remove until evidence exists | 13 Dec 2026 |
| D6 | Is the "future university" goal public? | Do not mention it on either site until it is official | 13 Dec 2026 |
| D7 | Share lead, application and admission numbers for 2025–26 and 2026–27, and the ads budget | Needed for targets and budget | 13 Dec 2026 |
| D8 | Publish fees per programme and campus | Yes (aggregators show conflicting fees; parents search for them) | 31 Dec 2026 |
| D9 | Who builds ithsedu.in (same developer?) and where it is hosted | Same developer, separate WordPress install | 13 Dec 2026 |
| D10 | Apply the new design to the admissions site too, or leave it as is | Leave it for the 2027 season; revisit in September 2027 | 31 Jan 2027 |
| D11 | Domain email addresses instead of Gmail | Yes, on ithsedu.in | 31 Jan 2027 |
| D12 | AI training crawlers (GPTBot, Google-Extended, ClaudeBot): allow or block | Allow search crawlers; client decides on training crawlers | 31 Jan 2027 |

### 12.2 Inputs

- Search Console and GA4 access, or the export (`03-…`).
- The fact sheet (5.3), the programme table per campus, the 2027–28 dates, fees and ITHS-SET dates.
- Signed collaboration agreements (for counsel and for the wording on `/partners/` and `/about/`).
- Patent application numbers; publication list (ORCID); awards with issuer and year.
- Real photographs of each campus, lab and the leadership; the logo files.
- Permission to use each university's name and logo; any industry partner permissions.
- Names of the campus coordinators and the central social lead.

## 13. Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Organic traffic drops after changes | Medium | High | Protected URLs (4.1), batches, weekly monitoring, rollback |
| Two sites seen as duplicates or competitors | Low (with section 1 rules) | Medium | Ownership map, canonical for rare shared items, one organisation in schema |
| Followers lost or confused when accounts change | Medium | Medium | Option A; a 2-week notice; Collab posts; bio links |
| Claims complaint (ASCI, CCPA) | Medium today | High | Appendix B; claims rewrite in Phase 0 |
| Collaboration structure questioned (UGC franchise rules) | Unknown | High | Counsel-approved wording; awarding university named everywhere [VERIFY with counsel] |
| Personal data on forms (Aadhaar, minors) | Medium | High | Counsel review; minimised fields; consent; DPDP readiness before May 2027 |
| Wrong payment account on the form | Present now | High | A1 fix this week |
| Campus coordinators post off-brand or risky content | Medium | Medium | Playbook, templates, approval for claims and minors, monthly review |
| ithsedu.in launches late and misses the season | Medium | Medium | Admissions site carries the season either way; ithsedu.in launch is not on the admissions critical path |

## 14. If ITHS becomes a university: the merge path

If ITHS gets university status, one domain is simpler. The plan above keeps that move cheap:

1. ithsedu.in already reuses the admissions site's paths for shared pages and keeps `/programs/`, `/campuses/`, `/admission/`, `/apply-now/`, `/iths-set/` and `/blog/` free.
2. On the move, every admissions URL is copied to the same path on ithsedu.in and 301-redirected one-to-one (one hop).
3. Use Search Console's Change of Address tool for the domain move; keep the old domain registered and redirecting for at least 5 years.
4. Update Google Business Profiles, social bios, university links and aggregator listings.
5. Expect some ranking movement for 4–12 weeks; schedule the move outside the admission season (September to December).

---

## Appendix A: social handle reservation checklist

Reserve every handle now, even on platforms we will not use yet, so nobody else takes them.

| Handle | Instagram | Facebook | LinkedIn | YouTube | X | Threads | WhatsApp Channel |
|---|---|---|---|---|---|---|---|
| ithsedu | ☐ | ☐ | ☐ (company page) | ☐ (or rename existing, D1) | ☐ | ☐ | ☐ |
| iths.rbu | ☐ | ☐ | showcase page | playlist | – | – | – |
| iths.rbpu | ☐ | ☐ | showcase page | playlist | – | – | – |
| iths.bushimla | ☐ | ☐ | showcase page | playlist | – | – | – |
| iths.sgsu | ☐ | ☐ | showcase page | playlist | – | – | – |

Recovery: every account has two admins from the client, two-factor authentication, and a recovery email on a client-owned domain.

## Appendix B: claims checklist for every page, post and ad

| Check | Pass when |
|---|---|
| Superlatives and "firsts" | None, or each has a dated, documented source named next to it |
| Placement and salary | Latest completed academic year, method stated, "Past record is no guarantee of future prospects" in the same font size; never "100%" |
| Patents | "Patent applications filed/published (No. …)"; never "patents" or "patented" without a verified grant |
| University and recognition | Degree-awarding university and location named; "UGC-recognised" said only of the university, as verified on ugc.gov.in |
| Accreditation | Only the institution that holds it, with grade and validity |
| Partner and employer names | Written permission or current evidence on file |
| Photos | Real ITHS campus, lab and people; consent on file; parental consent for minors; AI images labelled |
| Stem cell | Academic and career content only; no therapy promotion |
| Facts | Match the fact sheet (5.3) |
| Forms | Consent checkbox, privacy link, minimal fields, parental consent route for under-18s |

*Prepared by TechnoTaau Team. Sign-off: Jakhar Singh.*
