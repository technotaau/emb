# EmbryoGenesis: Competitor, Keyword and Social Landscape Report
**Prepared by SearchFit.ai for the TechnoTaau Team, 2026-10-15**

**Method and limits.** I used WebSearch and WebFetch, plus Google Autocomplete (`suggestqueries.google.com`, gl=in) to check which queries real people type. I had no access to a keyword-volume tool, so all volume and difficulty figures are qualitative estimates and are labelled that way.

Several sources could not be fetched:
- Instagram returned 429 and X returned 402.
- Facebook showed a login wall, and YouTube rendered no channel data.
- igenomix.in returned 503.

Because of this, I could not collect social follower counts. A team member needs to check those by hand while logged in. The schema checks are also limited: WebFetch cannot see the `<head>` of a page, so JSON-LD needs confirming with Google's Rich Results Test or Screaming Frog.

---

## 0. Executive summary: the 12 findings that matter most

1. **EmbryoGenesis barely exists as a search entity.** Searches for "EmbryoGenesis Mohali", the founder's name with the brand, and the Instagram handle found nothing about the brand. The results were Wikipedia and generic biology pages, because "embryogenesis" is also a common science term. Making the brand distinct (an entity name like "EmbryoGenesis Fertility Diagnostics, Mohali", Organization schema with `sameAs`, a Google Business Profile, matching social handles) is step zero.
2. **The site is very thin.** It has 17 pages and 5 posts in the Rank Math sitemaps:
   - One of the posts is a junk `/cache/` URL.
   - Three tests share one page at about 65–100 words each.
   - Five therapies share one page at about 85–95 words each.
   - The blog shows only 3 posts, written by "embryosys", with no citations and no medical reviewer.
3. **No competitor owns "IVF failed, what next?" in Hindi or Hinglish.** Autocomplete shows heavy Hinglish demand: "ivf fail hone ke baad kya kare", "era test kya hota hai", "bar bar miscarriage kyu hota hai", "endometrium patla hone ke karan", "garbh nahi thaharta hai to kya kare". The big chains publish general Hindi IVF content. None of the visible Birla Hindi titles covers IVF failure, ERA or the endometrium.
4. **The strongest national content competitor in this niche is Shree IVF Clinic / "ImmuRepro Solutions" (Dr Jay Mehta, Mumbai).** It has deep RIF, LIT, ERA/EMMA/ALICE, reproductive immunology and NK-cell articles. Its pages carry author bylines, update dates and "honest recommendation" framing, and the clinic reports 421K YouTube subscribers and 245K Instagram followers. This is the template to beat, not Indira or Nova.
5. **Apollo Fertility owns the cost-intent keywords.** It has an ERA page with an FAQ quoting ₹35,000–40,000 and Chandigarh cost blogs with a named medical reviewer and dates. Indira, Nova and Birla run large city-page systems (`/ivf-cost-in-chandigarh`, `/ivf-centre/zirakpur/...`) and dominate local "IVF centre" searches. EmbryoGenesis should not compete for "IVF centre in Mohali"; it is a lab, so the intent does not match.
6. **There is a clear differentiator to market: speed and a single biopsy.** EmbryoGenesis states a 7–10 day turnaround. Shree IVF says ERA/EMMA/ALICE results take 3–4 weeks and the panel costs about ₹80,000. If EmbryoGenesis publishes a transparent price, that becomes a second advantage.
7. **Evidence and regulation risk is the biggest strategic constraint, and also the biggest opportunity.**
   - ESHRE's 2023 RIF recommendations say peripheral and uterine NK testing, intrauterine PRP, intrauterine PBMC, IVIG, intralipids and G-CSF are "not recommended". They also say there is insufficient data for routine commercial receptivity tests.
   - ESHRE's 2022 RPL guideline (strong recommendation) says LIT should not be used for unexplained RPL.
   - Google Ads bans ads for most stem-cell and cellular therapies.
   - On 6 Oct 2026 the NMC issued an advertising and digital-communication framework that restricts testimonials, before/after content, and "100% success" or "best" claims. It covers websites, social media and WhatsApp.
   - The current site's claims ("best fertility centre", "game-changer", "safe, with minimal risk", "supported by extensive research" with no citations) are a liability. Content that is open about the evidence, in the Shree IVF style, will rank better, survive the YMYL quality bar, and get cited by AI answer engines.
8. **Check the patent claims before using the word "patented".** The founder's profile lists numbers such as 202411059621 A and 202431001616 A. An "A" suffix normally marks a *published application*, not a granted patent. Verify grant status on IP India before using "patented" in copy or ads. Otherwise use "patent application published / patent-pending".
9. **Clinical embryology education is a winnable, lower-risk traffic engine.**
   - Rival pages are weak. LPU's M.Sc page has empty sections, stale 2021–22 labels and a six-year curriculum tab for a two-year course. Chitkara claims "assured placement" with no salary data. Careers360 Q&A threads rank for salary questions with conflicting anecdotes.
   - EmbryoGenesis's own course pages are about 200–250 words. The scholarship and media pages are empty.
10. **There is an untapped B2B audience nearby.** LifeLinkr lists 21 registered ART clinics in SAS Nagar (Mohali) and 200 in Punjab. No competitor in this segment publishes clinician-facing content such as ordering protocols, biopsy timing, report interpretation, CME, or case series.
11. **Social handles are inconsistent** (`embryo_genesis`, `EmbryoGenesis`, `@Embryo-Genesis`, `EmbryoGenesiss` with a double "s"). There is no LinkedIn link and no WhatsApp. The site shows four different phone numbers: 9691736435, 9815692195, 8146217196 and 9599877196.
12. **The site mixes audiences.** A course "Apply Now" button sits in the header of clinical pages, and patients and students share one navigation. Split them into two clear hubs: patient diagnostics and the academy.

---

## 1. EmbryoGenesis baseline audit (observable)

| Area | Finding | Source |
|---|---|---|
| Sitemap | Rank Math; 17 pages and 5 posts. Posts: endometrial-immune-profiling (2025/2026), `/cache/` (junk), LIT for RPL (2024), pregnancy after IVF failure (Hindi, 2024), unexplained-infertility (2024) | https://embryogenesis.in/sitemap_index.xml, /post-sitemap.xml, /page-sitemap.xml |
| Duplicate or orphan pages | `/diagnostic/` and `/diagnostic-services/`; `/research-and-training/` and `/skill-development-training/`; `/apply-now/` (2024); `/clinical-embryology-scholarship/` has no scholarship details | page-sitemap.xml |
| Diagnostics page | ERFA about 100 words, Endo-Immune about 75, EIT about 65. 3 FAQs. Results in 7–10 days. No price, no author, no references. "Book" goes to a phone number only | https://embryogenesis.in/diagnostic/ |
| Therapies page | LIT, PBMC, PRP, stem cell and H2 at about 85–95 words each on one URL. No H1, citations, disclaimer or risks. Claims such as "non-invasive and safe, with minimal risk" and "supported by extensive research" | https://embryogenesis.in/advanced-fertility-therapies/ |
| Blog quality | ERFA post: about 650 words, no references, no alt text, "best fertility centre" and "game-changer" claims. EIP post: about 800 words with a useful *Limitations* section (a good sign) but no citations or named author | /erfa-the-soil-test-.../, /endometrial-immune-profiling-.../ |
| E-E-A-T assets (underused) | Founder Prof. (Dr.) Pulakes Purkait (Ph.D., Postdoc; ORCID 0000-0002-8814-9939; 30 papers claimed; NBHC 2024 Best Innovator at IIT Delhi). Team includes Dr. Vidhu Wadhwa (Consultant Pathologist and Quality Manager) and Dr. Meenu Bhanot (Consultant Embryologist), who could act as medical reviewers. No Google Scholar link; no NABL or ART-registration badge visible | /about/, /pulakes-purkait-profile/ |
| Courses | /courses/ about 200–250 words. The B.Sc page title says "Rayat Bahra University" but the URL says "bahra-university"; admission office in Shimla Hills but address in Mohali. Fees listed: B.Sc ₹39,875/semester, M.Sc ₹1,00,000/semester. No curriculum, faculty, placement data, FAQs or salary information | /courses/, /bsc-in-clinical-embryology-in-bahra-university/ |
| Lab training | 8 short courses with fees (₹1,000–35,000), 10 seats each. No ICSI, vitrification or andrology modules, and no certificate details | /skill-development-training/ |
| Media page | Filter tabs (Award, MOU, News) but no items render | /media-event/ |
| Third-party listings | ivf.net lists "B.Sc/M.Sc Clinical Embryology – ITHS Bahra University". Careers360 lists the Rayat Bahra Mohali B.Sc/M.Sc ART and Clinical Embryology | https://ivf.net/ivf/b-sc-m-sc--clinical-embryology--iths-bahra-university-himachal-pradesh-o13759.html |
| Other | Footer © 2023; no WhatsApp; no visible language switcher; no prices; no Google Map or NAP block on every page |  |

---

## 2. Competitor analysis

### 2A. Endometrial receptivity and reproductive immunology testing

| Competitor | Positioning | Site structure and content | Trust signals | CTAs | Schema / technical | Social |
|---|---|---|---|---|---|---|
| **Igenomix (Vitrolife Group): ERA / EMMA / ALICE / OpERA** | Global originator of ERA (patented 2011); sells to clinics, not directly to patients | Global product pages; India regional site igenomix.in (returned 503 during this audit). No India pricing published | Peer-reviewed literature, brand ownership of "ERA" | Clinic-referral led | Could not inspect | Mostly B2B |
| **Neuberg Centre for Genomic Medicine (NCGM)** | Indian genomics lab running OpERA-type receptivity sequencing | Visible mainly through an Indian retrospective study (158 RIF patients) | Publications | B2B | – | – |
| **Shree IVF Clinic / "Dr Jay Mehta's ImmuRepro Solutions" (Mumbai)**: *main content rival* | "India's leading reproductive immunology center"; reproductive immunology and RIF specialist | Dedicated pages for RIF, LIT/PLI, reproductive immunology and recurrent IVF failure, plus long blogs (ERA/EMMA/ALICE guide about 1,250 words; BCL-6/uNK; immune-related infertility). Question-style H2s, "My honest recommendation", an India cost section (₹80k panel; 3–4 week TAT) and contextual internal links | Author and "medically reviewed by" with MBBS, DNB and council registration; "Updated on" dates; 4.9 rating badge; "50,000+ patients" | 24/7 toll-free 1800-268-4000, WhatsApp, Book, Pay Now, online consults | Breadcrumbs; no visible FAQ schema; brand names inconsistent (Shree IVF / ImmuRepro) | YouTube 421K+, Instagram 245K (self-reported on site) |
| **Delhi IVF (Dr Anoop Gupta et al.)** | Claims "first IVF centre in India to start LIT"; failed-IVF specialist | Pages for LIT, RIF, multiple failed IVF cycles, PRP for thin endometrium and personalized embryo transfer; large category blog | "Since 1993", "25k+ IVF babies" | Call, WhatsApp "Free Video Consultation", Book | No visible schema; broken internal links | YouTube channel active |
| **Apollo Fertility** | Pan-India chain; ERA as an "advanced treatment" | ERA page (1,000–1,200 words, 5 FAQs incl. "How much does an ERA test cost in India?" giving ₹35–40k). Language selector with 11 languages including Hindi and Punjabi | ERA page has no author; its city blogs carry named reviewers | Book form, OTP call-back, WhatsApp, 1860 number | FAQ layout (schema unconfirmed) | Brand channels |
| **Metropolis / Dr Lal PathLabs** | Mass-market labs offering *peripheral* NK cell (CD16/CD56) tests at about ₹4,360 (Metropolis Delhi) | City "parameter" pages; "nk cell test dr lal pathlabs" appears in autocomplete | Brand scale | Book home collection | Product/lab-test pages | – |
| **ARGI (Association of Reproductive Genetics & Immunology)** | New professional body for RIF/RPL with 350+ specialists | PR (The Quint brand studio) | – | – | – | Potential *partner* or speaking venue, not a rival |

**Takeaways for 2A**
- No Indian lab publishes patient-friendly, evidence-graded explainers *plus* clinician-ordering pages for its own receptivity, immune and infection panels. EmbryoGenesis can be "the lab that explains".
- Price is unclear across the whole market. The only published numbers are Apollo's ₹35–40k (ERA) and Shree IVF's about ₹80k (ERA+EMMA+ALICE). A clear ERFA price and turnaround page would be unusual and very linkable.
- Searchers ask for prices and lab names: "nk cell test price", "nk cell test dr lal pathlabs", "endometrial biopsy test price", "era test cost in [city]". Labs win these with plain lab-test pages.

### 2B. Fertility/IVF brands (digital and SEO approach only)

| Brand | Site architecture | Content types | Local Punjab footprint (URLs) | Trust and CTAs | Notes |
|---|---|---|---|---|---|
| **Indira IVF** | Treatment, condition, centre, cost and doctor pages for each city; Resources hub | Blog, FAQs, research papers, newsroom, 5 calculators plus a "Pregnancy Success Rate" calculator, homepage quiz, YouTube success-story playlist | `/ivf-cost-in-chandigarh`, `/best-ivf-doctor-in-chandigarh`, `/punjab/best-ivf-center-in-ludhiana`. LifeLinkr also lists an Indira clinic in SAS Nagar | "2,00,000+ couples", "72%+ success" (with definition), awards, 0% EMI; toll-free number, WhatsApp, call-back | YouTube about 299K subscribers and about 2.24K videos (vidIQ, Jul 2025). Indira Fertility Academy trains embryologists (direct education competitor) |
| **Nova IVF** | `/ivf-centre/{city}/...` and `/ivf-doctor/{city}` pairs; locality pages in metros | Topic-sorted blog, FAQs, ovulation / due-date / PCOS calculators, ₹999 fertility test package, "Doctors Speak", case studies | Chandigarh, Ludhiana, Jalandhar, Amritsar and Zirakpur ("Mohali-Zirakpur") centre and doctor pages | "1L pregnancies", fellowship programs; call, booking, WhatsApp | AI WhatsApp bot handles 70% of queries; more than 5% of WhatsApp users book (vendor case study) |
| **Birla Fertility & IVF** | State → centre locator; `/chandigarh/` | Blogs in English **plus Hindi, Marathi, Tamil, Telugu, Kannada, Malayalam and Bengali**; risk-assessment quiz; calculators; video testimonials | `/chandigarh/` (no Punjab, Mohali or Ludhiana pages seen) | Fixed-price packages, 0% EMI, awards, "230,000+ patients" | Hindi blog is broad (IVF steps, TSH, cysts). No visible Hindi titles on IVF failure, ERA or thin endometrium |
| **Apollo Fertility** | City hubs, hospital and doctor pages | Cost blogs with tables and FAQs, "top clinics in Chandigarh" listicles, named medical reviewer, updated dates | `/chandigarh/sector-22a/...`, "IVF cycle cost in Chandigarh" | Booking, OTP call-back, WhatsApp | Ranks for Chandigarh-intent queries with listicles |
| **Local Mohali/Chandigarh** (Fortis Bloom, Dr Sodhi's, Simran IVF, Singla/Ivy, Kore, Pink Lines, Motherhood, Cloudnine, etc.) | Mostly thin sites; directory-dependent (WhatClinic, ClinicSpots, Latrexa, Credihealth) | Little original content found | 21 ART clinics registered in SAS Nagar (LifeLinkr) | – | These are **B2B prospects** for EmbryoGenesis, not rivals |

**Takeaways for 2B**
- The chains win on city × service × cost × doctor pages, calculators and EMI messaging. EmbryoGenesis should not copy the city-page model for IVF. Location pages only make sense where it actually has a lab or a sample-collection partner (for example "ERFA test in Chandigarh / Ludhiana / Jalandhar via partner clinics"). Otherwise they risk being treated as doorway pages.
- None of the chains publishes deep content on RIF diagnostics, because they sell IVF cycles. That middle-funnel gap is where EmbryoGenesis fits.
- **Worth copying:**
  - an interactive "IVF failure next-step checker" (quiz-style lead tool);
  - visible review dates and medical reviewers;
  - a Hindi section;
  - a WhatsApp bot.

### 2C. Clinical embryology education

| Institution | Programs | Page quality (SEO) | Trust and CTAs | Exploitable weakness |
|---|---|---|---|---|
| **Chitkara University (Punjab)** | 4-yr B.Sc; 2-yr M.Sc (with Neelam Hospital) | Strong: keyword H1, fee table (about ₹5.7L total), 10 FAQs, curriculum list, careers, recruiter logos, blog ("What is Clinical Embryology?") | Apply, Brochure, WhatsApp, phone | "Assured placement" with no data; no salary figures; recruiter logos unrelated to IVF (Deloitte, PwC) |
| **LPU (Phagwara)** | M.Sc with CooperSurgical/Origio; B.Sc (about ₹9.6L) | Weak: empty sections, stale 2021–22 labels, six-year curriculum tabs, empty FAQ | Many CTAs (WhatsApp, video counselling, scholarship predictor) | The Origio tie-up is never explained |
| **Rayat Bahra University (Mohali), Hoshiarpur campus, Bahra University (Shimla)** | B.Sc/M.Sc ART and Clinical Embryology; Clinical Embryology and Reproductive Genetics (Careers360 lists about ₹2.9L B.Sc fee) | Mainly aggregator listings | – | EmbryoGenesis *is* the lab partner here. It should be the main source, so the aggregators link to it |
| **Amity (Mohali / Bengaluru)** | M.Sc (about ₹10.16L per Careers360) | Aggregator-led | – | Fees are high; EmbryoGenesis can compete on fees |
| **Lamrin Tech Skills Univ., Dolphin PG College, MRSPTU Bathinda** | B.Sc / M.Sc | Low visibility | – | – |
| **National**: Yenepoya × Momsoon (integrated B.Sc–M.Sc, 1-month ICSI certificate), Adamas × GDIFR ("Eastern India's 1st M.Sc", AY 2026-27), Navrachana, Marwadi, MGUMST, Malla Reddy, Pacific (Udaipur, about ₹3.05L) | Programs and certificates | Careers360 and Shiksha aggregators rank above most university pages | – | Southern-state queries dominate autocomplete (Tamil Nadu, Kerala, Bangalore, Chennai), so Punjab/North India is less contested |
| **Training academies**: Indira Fertility Academy (embryology course about US$5,000 in 2020; 200+ embryologists trained; FNB seats), Fertilis Academy (Gurugram, 12-day micro-batch at Artemis), Lifeinvitro/IIT Hyderabad (ICSI/andrology), Nova "Embryo-Tech" (unverified) | Hands-on ICSI, IVF and vitrification | Event listings on ivf.net | – | EmbryoGenesis's lab courses (IHC, microtomy, molecular, PRP/LIT, stem cell) do not include core IVF-lab skills (ICSI, vitrification, andrology) that students search for |

**Takeaways for 2C**
- Nobody in Punjab publishes honest, sourced salary data. The AIIMS Nagpur 2026 contract embryologist post paid ₹96,134/month. Fresher ranges on Careers360 and CareerPlanB are ₹15–30k/month, or ₹3–6 LPA. Other missing pieces: ART Act career pathways, IFS certification requirements (B.Sc/M.Sc/MBBS, 3 years of hands-on work, a 50-case logbook, an MCQ exam), and "day in the IVF lab" video.
- The 2026–27 admission cycle is live, with new entrants such as Adamas/GDIFR.

---

## 3. Head-to-head content comparison (estimates)

| Metric | EmbryoGenesis | Shree IVF / ImmuRepro | Apollo Fertility | Indira IVF | Chitkara (edu) |
|---|---|---|---|---|---|
| Blog posts | 4 real (plus a junk URL) | Hundreds (est.) | Hundreds (est.) | Hundreds (est.) | Blog present |
| Publishing frequency | About 1/year | Monthly or more (June 2025 posts seen; © 2026) | Ongoing (updated Jul 2026) | Ongoing | Periodic |
| Avg depth on RIF/ERA topics | 65–800 words, no citations | 1,200–1,500 words, author, dates | 1,000–1,300 words, FAQs | General | 1,200–1,400 words/course page |
| Hindi/Hinglish | 1 Hindi post | Hinglish only in reviews | Language selector | No switcher seen | No |
| Tools/calculators | None | None | Ovulation calculator | 6 calculators and a quiz | Scholarship predictor (LPU) |
| Price transparency | Training fees only | ERA panel about ₹80k | ERA ₹35–40k | City cost pages | Full fee table |
| WhatsApp | No | Yes | Yes | Yes | Yes |
| Named medical reviewer | No | Yes | Yes (blogs) | Partly | n/a |

---

## 4. Keyword landscape (English + Hindi/Hinglish)

Each row's "intent" is one of: I = informational, C = commercial investigation, T = transactional, N = navigational, L = local.
Volume and difficulty (KD) are qualitative and relative within the niche. Every query marked with \* was confirmed in Google Autocomplete for India.

### Cluster 1: IVF failure / implantation failure (top of the "what next" hub)

| Keyword | Intent | Vol | KD | Notes / target page |
|---|---|---|---|---|
| ivf failure reasons\* / ivf failure\* / ivf failure what next\* | I | High | High | Pillar: "IVF Failed – What Next? (Complete guide)" |
| ivf fail hone ke karan\* / ivf fail kyu hota hai\* / ivf fail hone ke baad kya kare\* / ivf fail hone ke lakshan\* | I | High (Hinglish) | **Low–Med** | Hindi pillar `/hi/ivf-fail-hone-ke-baad-kya-kare/` (strong opportunity) |
| आईवीएफ फेल होने के बाद क्या करें\* / आईवीएफ फेल होने के कारण\* / आईवीएफ फेल होने के लक्षण\* | I | Med | **Low** | Devanagari version of the same page; Hindi search results are thin and dominated by foreign English pages |
| repeated ivf failure\* / multiple ivf failure what next\* / repeated embryo transfer failure\* | I/C | Med | Med | RIF pillar |
| repeated implantation failure\* / implantation failure reasons\* / implantation failure symptoms (in hindi)\* | I | Med | Med–High | RIF explainer, with Hindi FAQ |
| implantation failure symptoms after embryo transfer\* | I | Med | Med | Two-week-wait FAQ page |
| repeated ivf failure with donor eggs\* | I | Low | Low | Niche explainer (endometrial factor focus) |
| garbh nahi thaharta hai to kya kare\* / garbh kyu nahi thaharta hai\* | I | Med | Low | Hindi explainer that leads into receptivity testing |

### Cluster 2: Recurrent miscarriage (RPL)

| Keyword | Intent | Vol | KD | Notes |
|---|---|---|---|---|
| recurrent miscarriage causes / treatment / testing\* | I/C | Med | Med–High | RPL pillar (be faithful to ESHRE) |
| recurrent miscarriage meaning in hindi\* | I | Med | Low | Hindi glossary page |
| bar bar miscarriage kyu hota hai\* / bar bar miscarriage ho to kya kare\* / bar bar miscarriage hone se kaise roke\* | I | High (Hinglish) | **Low** | Hinglish article and reel series |

### Cluster 3: ERA test, endometrial receptivity, ERFA

| Keyword | Intent | Vol | KD | Notes |
|---|---|---|---|---|
| era test\* / era test in ivf\* / era test procedure\* / era test means\* | I | Med | Med–High (Igenomix, Apollo, Shree) | "ERA vs ERFA" comparison and explainer |
| era test cost\* / era test cost in india\* / era test ivf cost\* | C | Med | Med | **Transparent price page**: ERFA price and what is included |
| era test cost in delhi / mumbai / pune / bangalore / hyderabad / chennai\* | C/L | Low–Med each | Low–Med | Only if partner collection exists in that city |
| era test kya hota hai\* / ईआरए टेस्ट क्या है | I | Med | **Low** | Hindi explainer |
| era test ivf success rate\* / era test report\* | I | Low–Med | Med | "How to read your receptivity report" (good for AI answers) |
| endometrial receptivity test / analysis / assay\* / endometrial receptivity test cost in india\* | I/C | Low–Med | Med | Hub page |
| erfa test / soil test for ivf / receptivity px | N | Very low now | None | Branded; grows with social and PR |
| endometrial biopsy test price / cost in india\* / kaise hota hai\* / in hindi\* | C/I | Med | Low–Med | "Endometrial biopsy for fertility testing: procedure, pain, cost" |

### Cluster 4: Reproductive immunology / NK cells

| Keyword | Intent | Vol | KD | Notes |
|---|---|---|---|---|
| nk cell test price\* / nk cell test ivf\* / nk cell test for pregnancy\* / nk cell test results\* | C/I | Low–Med | Low–Med (Metropolis/Dr Lal win "price") | Explain blood vs uterine NK, and ESHRE's "not recommended" |
| nk cell test dr lal pathlabs\* | N | Low | – | Shows lab-brand demand. Get listed on aggregator marketplaces |
| uterine nk cells / cd56 uNK test | I | Low | Low | Clinician-facing page |
| immune infertility treatment / reproductive immunology india | C | Low | Med (Shree IVF) | Endo-Immune test page |

### Cluster 5: Chronic endometritis

| Keyword | Intent | Vol | KD | Notes |
|---|---|---|---|---|
| chronic endometritis symptoms / treatment / causes / ultrasound\* | I | Med | Med | EIT pillar. ESHRE says CE assessment "can be considered", so this is the **best-supported test to lead with** |
| chronic endometritis in hindi\* | I | Low–Med | Low | Hindi page |
| cd138 test / chronic endometritis panel\* / pathology outlines\* | I (pro) | Low | Low–Med | Clinician/pathology page (Dr. Vidhu Wadhwa as author) |

### Cluster 6: Thin endometrium / PRP (handle carefully)

| Keyword | Intent | Vol | KD | Notes |
|---|---|---|---|---|
| thin endometrium treatment / causes / meaning in hindi\* / in ayurveda\* | I | Med–High | Med | Evidence-graded guide |
| endometrium patla hone ke karan\* / endometrium ka patla hona\* | I | Med | Low | Hinglish |
| prp for thin endometrium\* / prp treatment for uterine lining\* | C | Low–Med | Low–Med (Delhi IVF) | Must state that ESHRE does not recommend intrauterine PRP for RIF; position it as investigational |
| prp ovarian rejuvenation\* / cost in india\* / success rate\* / side effects\* | C | Med | Med | Same evidence caveats; Google Ads likely restricted |

### Cluster 7: LIT / PBMC / stem cell / molecular hydrogen

| Keyword | Intent | Vol | KD | Notes |
|---|---|---|---|---|
| lit therapy in ivf\* / lit therapy cost (in india)\* / procedure\* / side effects\* / success stories\* / in ivf in hindi\* | C/I | Low–Med | Low–Med (Shree, Delhi IVF) | Very high YMYL risk: ESHRE strongly recommends against LIT for unexplained RPL. Content must be balanced; no testimonials (NMC 2026) |
| pbmc therapy\* | – | Low | – | Autocomplete shows **no fertility intent** ("pbmc physical therapy"). Use "PBMC intrauterine infusion for implantation failure" |
| stem cell therapy for infertility in india\* | C | Low–Med | Med | ICMR treats stem cells as investigational (trials only); Google bans ads. Reframe as research or clinical-trial content |
| molecular hydrogen therapy\* (benefits / cost / side effects) | I/C | Med (general wellness) | Med | Little fertility-specific intent; low priority |

### Cluster 8: Clinical embryology education

| Keyword | Intent | Vol | KD | Notes |
|---|---|---|---|---|
| clinical embryology courses (in india)\* / clinical embryology colleges in india\* | C | Med–High | High (Careers360, Shiksha, universities) | Course hub |
| bsc clinical embryology\* / course details\* / syllabus\* / colleges\* | C | Med | Med–High | B.Sc page with full syllabus, fees and FAQ schema |
| msc clinical embryology\* / eligibility\* / government colleges in india\* | C | Med | Med–High | M.Sc page |
| embryologist course\* / duration\* / eligibility\* / fees in india\* | C | Med | Med | "How to become an embryologist" guide |
| clinical embryology salary (in india)\* / bsc clinical embryology salary per month\* / msc … salary per month\* / embryologist salary in india per month\* | I | **High** | Med (Careers360 Q&A) | **Salary report with sources**: strong traffic and link magnet |
| embryologist salary in dubai / abroad / usa\* | I | Med | Med | Global career page |
| embryology course in punjab\* / msc embryology in punjab\* / clinical embryology courses in punjab\* | C/L | Low–Med | **Low** | Punjab landing page (primary local education keyword) |
| clinical embryology course chandigarh / mohali | C/L | Low | Low | Same page or sub-sections |
| embryologist kaise bane / clinical embryology kya hai | I | Med (YouTube-heavy) | Low | Hindi YouTube and blog |
| embryology course in udaipur\* | – | ~0 (autocomplete empty) | – | Do not build. Udaipur only matters as Indira IVF's home base |
| icsi training course / embryology hands-on training / vitrification course | C | Low | Low–Med | Add an ICSI/vitrification module if capacity allows |

### Cluster 9: Local terms

| Keyword | Intent | Vol | KD | Fit for EmbryoGenesis |
|---|---|---|---|---|
| ivf centre / hospital / clinic in mohali\*; best ivf centre in mohali\*; ivf hospital mohali sector 71\* | L/T | Med | High (chains and directories) | **Poor fit** (IVF intent). Do not target |
| ivf cost in chandigarh\*; ivf treatment cost in pgi chandigarh\* | C/L | Med | High | Poor fit |
| ivf centre in jalandhar\* (+ "test tube baby centre in jalandhar", "nova ivf centre in jalandhar") | L | Med | High | Poor fit |
| ERA / endometrial test in Chandigarh / Mohali / Punjab / Ludhiana / Jalandhar | L/C | Low | **Low (no local provider pages found)** | **Good fit**: one Punjab page, plus city sections only where samples are actually accepted |
| ERA test cost in Mumbai\* | C/L | Low–Med | Med (Shree IVF is in Mumbai) | Only with a real Mumbai partner or courier logistics |
| fertility diagnostic lab Mohali / endometrial biopsy test near me\* | L | Low | Low | Google Business Profile plus a lab page |

**Language note:** For "ivf failure reasons" and "implantation failure", autocomplete also suggests Tamil and Kannada versions, but no Punjabi ones. Hindi (Devanagari) plus Hinglish should come first; Punjabi (Gurmukhi) is a later, local-trust layer for social, not SEO.

---

## 5. Social media landscape

### What works for fertility and embryology accounts in India

| Format | Evidence or observation | Use for EmbryoGenesis |
|---|---|---|
| **Doctor/scientist explainer Reels (30–60s, Hinglish)** | Doctor creators reach six figures: Dr Tanushree Pandey (@gynae_guru) about 202K, Dr Sargam Soni about 161K. Healthcare Reels average about 2.7% engagement (Hootsuite via Webtonic). Educational content gets about 2.3× the engagement of promotional content | Weekly "Myth vs Science" and "Why did my IVF fail?" Reels with Prof. Purkait and Dr. Bhanot. Hinglish captions and subtitles |
| **YouTube long-form, Hindi** | Indira IVF has about 299K subscribers and about 2.24K videos; Ideal Fertility (Hindi) has about 428K; Shree IVF says 421K. Long explainers build search equity and trust | 8–15 min Hindi explainers: "IVF fail hone ke baad kaunse test?", "ERA vs ERFA", "Chronic endometritis", "Embryologist kaise bane". Cut each into 3–5 Shorts |
| **Patient stories / testimonials** | Vendor data says testimonial videos beat static posts by 40–60% on Meta. **However**, the NMC's 6 Oct 2026 framework restricts testimonials ("patient consent shall not, by itself, make permissible any testimonial"), before/after content and success claims, across websites, social media and WhatsApp | Replace them with anonymised "case explainers" (what was tested, what was found, what the evidence says), no outcome promises. Get legal review |
| **Carousels with text overlays** | Ranked as top Instagram formats for fertility clinics (Arrow Marketing case via Webtonic) | "Your RIF test checklist", "ERA vs ERFA vs EMMA", "Embryology career roadmap" |
| **WhatsApp** | Nova IVF's bot handles 70% of queries, and more than 5% of WhatsApp users book. Every major rival shows a WhatsApp CTA | WhatsApp click-to-chat on every page, a WhatsApp Channel for updates, a bot for "Book test / Course admission / Clinician order" |
| **LinkedIn** | Not linked by EmbryoGenesis. This is where IVF clinicians, embryologists and lab managers spend time | Company page plus founder posts: case series, CME, MOUs, patent news |
| **Education-specific** | Careers360 dominates text search, but Hindi YouTube for "embryologist kaise bane" is underserved (no strong results surfaced) | "Day in the IVF lab", student vlogs, admissions Q&A lives, alumni placements, salary breakdown videos |

### EmbryoGenesis's current presence (what is publicly visible)
- **Instagram (`embryo_genesis`), Facebook (`/EmbryoGenesis`), YouTube (`@Embryo-Genesis`), X (`EmbryoGenesiss`):** none of the four was reachable through the fetch tools (429, login wall, empty render, 402), and none came up in web search for the brand or handle. That suggests low reach and engagement, but **a logged-in manual audit is needed** to record followers, post frequency, top posts and last-post date.
- **Handles are inconsistent.** The X handle has a double "s", YouTube uses a hyphen, Instagram an underscore. Reserve a single handle (e.g., `embryogenesisindia`) wherever possible.
- **Gaps:** no LinkedIn, no WhatsApp, and no social proof embedded on the site. The Media & Event page is empty.

---

## 6. Evidence and regulatory guardrails (must shape all content)

| Topic | Authoritative stance | Content implication |
|---|---|---|
| Receptivity tests (ERA-type) | ESHRE 2023 RIF: "insufficient data to recommend the routine use of any commercially available test of endometrial receptivity". RCTs are mixed (NBC report; Frontiers 2023 review) | Present ERFA as a diagnostic option for *selected* RIF cases, with a limitations section. Publish your own outcome data |
| NK cells (peripheral and uterine) | ESHRE: "not recommended" | Endo-Immune page needs balanced framing and a clinician-facing evidence page |
| Chronic endometritis | ESHRE: assessment "can be considered"; antibiotics "can be considered" | **Lead with EIT**: it has the strongest guideline support |
| PRP, PBMC, IVIG, intralipid, G-CSF | ESHRE RIF: "not recommended" | Call them investigational; no outcome claims; informed-consent language |
| LIT | ESHRE RPL 2022: should not be used for unexplained RPL (strong) | Highest risk. Consider moving it to a research page, not a "Book Now" service card |
| Stem cell therapy | ICMR 2017: investigational, clinical trials only. Google Ads bans most stem cell and cellular therapy ads | Present as research or a clinical trial, not a service |
| Advertising | NMC framework (public notice 6 Oct 2026): no misleading claims, guaranteed cures, "best", testimonials, before/after; AI-generated promotional content restricted. Applies to websites, blogs, social media and WhatsApp | Remove "best fertility centre", "game-changer" and "safe, minimal risk" language. Add a medical disclaimer. Get legal sign-off on testimonials |
| "Patented" | Founder profile lists A-suffix application numbers | Verify grant status on IP India; otherwise say "patent application published" |

---

## 7. Content gaps and opportunities EmbryoGenesis can own

### 7.1 Blue-ocean (no competitor covers them well)
1. **"IVF Failed – What Next?" hub in English, Hindi and Hinglish.** One pillar with 10–15 spokes:
   - causes, organised as embryo, endometrium, immune, infection, anatomy and male factors;
   - a test-selection decision tree;
   - ERA vs ERFA vs EMMA/ALICE;
   - a CE guide;
   - a thin-endometrium guide;
   - the two-week wait;
   - when to stop;
   - emotional and financial planning.

   Interactive lead tool: an "RIF Next-Step Checker" (5 questions that suggest which tests to discuss with your doctor).
2. **Transparent ERFA / EIT / Endo-Immune price and turnaround page.** Show what is included, biopsy timing, 7–10 day results versus the market's 3–4 weeks, and that one biopsy covers several panels. No Indian lab does this clearly.
3. **"How to read your endometrial receptivity report"** (receptive / pre-receptive / post-receptive, what changes at transfer). Very useful for AI answers.
4. **Hindi/Hinglish RPL and endometrium series** ("bar bar miscarriage", "endometrium patla", "garbh nahi thaharta"). Demand is high and competition is low.
5. **Original data.** An annual "EmbryoGenesis Implantation Report" (anonymised), for example the share of displaced windows in N tested patients from Punjab and North India. Indian data is scarce (the OpERA paper itself says so), which makes this highly citable by journalists, clinicians and LLMs.

### 7.2 B2B content for IVF clinics (21 in Mohali, 200 in Punjab)
- **"For Clinicians" hub:**
  - test menu with indications;
  - biopsy timing protocols (natural cycle and HRT, LH+7 / P+5);
  - sample kit and courier logistics;
  - report samples;
  - turnaround times;
  - references;
  - a "refer a patient" form.
- **Monthly CME webinars or case discussions** (ISAR/IFS/ARGI-style), posted on YouTube and LinkedIn.
- **Embryologist upskilling bundle**: lab-training courses aimed at clinic staff, plus a placement pipeline for B.Sc/M.Sc graduates. This makes "We supply trained embryologists" a B2B hook.
- **Partner-clinic directory**, showing where ERFA samples can be collected in Chandigarh, Ludhiana, Jalandhar and so on. This legitimately supports local landing pages.

### 7.3 Education gaps
- A **"Clinical Embryologist Salary in India 2026" report** with sources: AIIMS Nagpur ₹96,134/month contract; fresher ₹15–30k/month; 3–6 LPA ranges; Gulf and abroad. Update it each year.
- A **"How to become an embryologist after 12th"** roadmap covering B.Sc vs B.Sc+M.Sc vs fellowship, ART Act staffing, and IFS certification (3 years of hands-on work, a 50-case logbook).
- **Full course pages**: syllabus by semester, fee table with total cost, scholarship rules, eligibility, lab photos and video, faculty profiles, placement list, FAQ plus Course/EducationalOccupationalProgram schema.
- **"Embryology course in Punjab" page** comparing options neutrally, with a fee comparison table (Chitkara about ₹5.7L, LPU about ₹9.6L, Amity about ₹10.16L, Rayat Bahra about ₹2.9L). EmbryoGenesis looks cheaper on fees.
- **Add ICSI / IVF / vitrification / andrology** hands-on modules, the skills people actually search for.

### 7.4 AI search / GEO answerability
- **Fix the entity first:**
  - Organization + MedicalOrganization/DiagnosticLab JSON-LD with `sameAs` (all socials, LinkedIn, ORCID);
  - a Google Business Profile at "Top Floor, Rayat Bahra Dental College & Hospital, Mohali";
  - consistent NAP and a single phone number;
  - "EmbryoGenesis (Mohali)" disambiguation text on the About page.
- **Answer-first page format:**
  - a 40–60 word direct answer;
  - definition boxes;
  - tables (test vs indication vs sample vs TAT vs cost);
  - "Evidence status" boxes citing ESHRE;
  - dated "Medically reviewed by Dr. X" lines;
  - FAQPage, MedicalWebPage and Person schema.
- **Third-party corroboration that LLMs read:**
  - Careers360, Shiksha and Collegedunia profiles linking to EmbryoGenesis course pages;
  - ivf.net listings;
  - PubMed-indexed case series;
  - press in BioSpectrum, Medical Dialogues and ET HealthWorld;
  - ARGI/IFS conference talks.
- **Bilingual parity**: matching Hindi pages with `hreflang` (en-IN / hi-IN) so Hindi-language AI answers can cite EmbryoGenesis.
- **Monitor** prompts such as "What to do after failed IVF in India", "ERA test cost India", "best clinical embryology course in Punjab" across ChatGPT, Gemini, Perplexity and AI Overviews.

---

## 8. Our competitive advantages
- **Proprietary branded tests** (ERFA, ReceptivityPX, Endo-Immune, EIT): branded keywords no one else can rank for.
- **Speed and convenience**: 7–10 day results, local Indian lab, versus the 3–4 weeks reported for imported ERA/EMMA/ALICE panels.
- **A real scientist-founder** with ORCID, 30 publications and an IIT Delhi innovator award, plus a pathologist and an embryologist on the team. This is genuine E-E-A-T, currently unused.
- **University affiliations** (Rayat Bahra, Bahra) with stated fees well below Chitkara, LPU and Amity.
- **Diagnostics, education and lab training under one roof**, which gives a natural B2B flywheel with Punjab's 200 ART clinics.
- **Low local competition** for receptivity testing and for "embryology course in Punjab".

## 9. Their weaknesses we can exploit
- **Shree IVF/ImmuRepro:** Mumbai-based with a confused brand (three names), no FAQ schema, reviews unrelated to immunology. North India is open.
- **Apollo ERA page:** no author or date.
- **Chains:** no depth on RIF diagnostics in Hindi; Birla's Hindi blog does not visibly cover IVF failure or ERA.
- **LPU:** empty and stale course page. **Chitkara:** unsupported "assured placement" and no salary data. **Careers360:** conflicting Q&A answers.
- **The market overall:** almost no Indian lab publishes clear pricing or report-interpretation guides.

---

## 10. Action plan (priority order)

**Days 0–30: foundation and risk removal**
1. **Compliance clean-up.** Remove superlatives and unsupported safety claims; add a medical disclaimer and evidence-status notes. Verify patent grant status. Move LIT and stem cell to "research" framing. Do not use testimonials until legal review under the NMC framework. *Removes YMYL and regulatory exposure.*
2. **Technical and entity fixes.**
   - Delete `/cache/`; merge `/diagnostic-services/` into `/diagnostic/` and `/research-and-training/` into the training page (301 redirects).
   - Use one phone number and add WhatsApp click-to-chat.
   - Add Organization, MedicalOrganization and Person schema with `sameAs`.
   - Claim the Google Business Profile, unify social handles, add LinkedIn, update the © year.
   - Split the navigation into "Patients", "Clinicians" and "Academy".
3. **One URL per test and per therapy**, 1,200+ words each with a named reviewer, references, FAQ schema, sample/TAT/price and a clinician section. Start with ERFA, EIT (best evidence) and Endo-Immune.

**Days 30–90: own the gaps**
4. **Launch the "IVF Failed – What Next?" hub** in English and Hindi/Hinglish (pillar plus 10 spokes, and the RIF Next-Step Checker). *Fills the biggest gap left by every competitor.*
5. **Publish the ERFA price and turnaround page** and an "ERA vs ERFA vs EMMA/ALICE" comparison. *Targets Apollo's and Shree IVF's cost-intent pages.*
6. **Rebuild the course pages** (B.Sc, M.Sc, lab training) with syllabus, total fees, FAQs and Course schema. Add the "Embryology Course in Punjab" page and the "Embryologist Salary in India 2026" report. *Exploits weak LPU/Chitkara pages and thin Careers360 answers.*
7. **Launch the Clinicians hub** and begin LinkedIn and email outreach to the 21 Mohali and 200 Punjab ART clinics with a CME webinar series.

**Days 90–180: compounding**
8. **YouTube Hindi long-form** (2 per month) plus 3 Reels/Shorts per week; WhatsApp Channel and bot.
9. **Publish anonymised outcome data** (an "Implantation Report") and submit a case series to an indexed journal. *Builds GEO citations and links.*
10. **Partner-clinic pages** for Chandigarh, Ludhiana and Jalandhar, only where sample collection really exists. Track a 20-prompt AI-visibility panel every month.

---

## Sources
- EmbryoGenesis: https://embryogenesis.in/ · /diagnostic/ · /advanced-fertility-therapies/ · /blog/ · /about/ · /pulakes-purkait-profile/ · /courses/ · /bsc-in-clinical-embryology-in-bahra-university/ · /skill-development-training/ · /clinical-embryology-scholarship/ · /media-event/ · /erfa-the-soil-test-endometrial-receptivity-analysis-optimize-fertility-success/ · /endometrial-immune-profiling-what-it-is-why-it-matters-and-who-should-consider-it/ · /sitemap_index.xml · /post-sitemap.xml · /page-sitemap.xml
- Shree IVF / ImmuRepro: https://www.shreeivfclinic.com/blogs/era-emma-alice-endometrial-testing-ivf/ · https://www.shreeivfclinic.com/reproductive-immunology-center-in-india · https://www.shreeivfclinic.com/recurrent-implantation-failure-rif/ · https://www.shreeivfclinic.com/paternal-lymphocyte-immunization-therapy-pli/ · https://www.shreeivfclinic.com/blogs/endometrial-immune-testing-bcl6-nk-cells-profiling/
- Delhi IVF: https://delhi-ivf.com/lymphocyte-immunization-therapy · https://delhi-ivf.com/repeated-implantation-failure · https://delhi-ivf.com/prp-therapy-for-thin-endometrium-in-delhi · https://delhi-ivf.com/personalized-embryo-transfer
- Apollo Fertility: https://www.apollofertility.com/treatment/era-endometrial-receptivity-array · https://www.apollofertility.com/blog/ivf/ivf-cycle-cost-in-chandigarh-what-to-expect-in-2025 · https://www.apollofertility.com/blog/ivf/top-ivf-clinics-in-chandigarh-with-highest-success-rate
- Indira IVF: https://www.indiraivf.com/ · https://www.indiraivf.com/ivf-cost-in-chandigarh · https://vidiq.com/youtube-stats/channel/UCZFyFHkeoHX_RyCZxbhMF6w · https://www.biospectrumindia.com/news/98/15975/ifa-all-set-for-its-clinical-fellowship-art-training-course-.html · https://news.careers360.com/nbe-accredited-reproductive-health-courses-begin-at-indira-ivf
- Nova IVF: https://www.novaivffertility.com/ · https://www.engati.ai/nova-ivf
- Birla Fertility: https://birlafertility.com/ · https://birlafertility.com/hi/blogs/ · https://birlafertility.com/chandigarh/
- Igenomix: https://www.igenomix.com/our-services/era-endometrial-receptivity-analysis/ · https://www.igenomix.com/genetic-solutions/emma-clinics/
- OpERA / NCGM study: https://pmc.ncbi.nlm.nih.gov/articles/PMC10967671/ · Indian ERA study: https://doaj.org/article/55eeb32135884d2fad44604d52d2ea96
- Metropolis NK test: https://www.metropolisindia.com/parameter/delhi/natural-killer-cells
- ARGI: https://www.thequint.com/brandstudio/partner-argi-fertility-care
- Local ART clinics: https://www.lifelinkr.com/art-clinics/punjab/sas-nagar/ · https://whatclinic.com/fertility/india/mohali · https://www.clinicspots.com/hospitals/ivf-in-vitro-fertilization/mohali · https://www.datanyze.com/companies/ivf-centre/397923119
- Education: https://www.chitkara.edu.in/healthscience/b-sc-clinical-embryology/ · https://www.lpu.in/programmes/msc-clinical-embryology · https://medicine.careers360.com/colleges/list-of-clinical-embryology-colleges-in-punjab · https://www.careers360.com/university/amity-university-bengaluru/msc-clinical-embryology-course · https://medicine.careers360.com/articles/adamas-university-and-gdifr-launch-eastern-indias-1st-msc-clinical-embryology-admission-open-for-ay-2026-27 · https://www.mrsptu.ac.in/uploads2024/syllabus/M.SC.%20(Clinical%20Embryology)%20(Sem.%201-4%20scheme%20and%20syllabus)%202023%20batch%20onwards.pdf · https://ivf.net/ivf/b-sc-m-sc--clinical-embryology--iths-bahra-university-himachal-pradesh-o13759.html · https://ivf.net/ivf/embryology-hands-on-training-program-o14025.html · https://ivf.net/ivf/intensive-certificate-course-in-intra-cytoplasmic-sperm-injection-icsi-o13896.html · https://www.careers360.com/colleges/rayat-bahra-university-school-of-medical-and-allied-sciences-mohali/bsc-art-and-clinical-embryology-course
- Salary: https://www.careers360.com/question-what-will-be-the-salary-for-an-freshly-graduated-embryologist-msc-embryology · https://www.careerplanb.co/bsc-embryology-salary-in-india-2025-in-hand-average-and-fresher-salary-breakdown/ · https://centralstatejobs.in/hi/jobs/aiims-nagpur-clinical-embryologist-recruitment-2026 · IFS certification: https://www.indianfertilitysociety.org/requirements
- Evidence and regulation: ESHRE RIF 2023 https://pmc.ncbi.nlm.nih.gov/articles/PMC10270320/ · https://www.eshre.eu/Guidelines-and-Legal/Guidelines/RIF · ESHRE RPL 2022 https://www.eshre.eu/-/media/sitecore-files/Guidelines/Recurrent-pregnancy-loss/2022/ESHRE-RPL-Guideline-_-Update-2022_-Final-Version-January-2023_v2.pdf · LIT recommendation summary https://richtlijnendatabase.nl/richtlijn/adaptatietraject_internationale_richtlijn_herhaalde_miskraam/prognose_en_behandeling_bij_koppels_met_herhaalde_miskramen/behandeling_van_onbegrepen_herhaalde_miskramen/lymfocyten_immunisatie_therapie.html · ERA evidence https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8045470/ · https://nbcwashington.com/news/local/study-shows-test-used-for-some-ivf-patients-not-likely-worth-pain-cost/3308730 · Google Ads unproven treatments https://SUPPORT.GOOGLE.COM/google-ads/answer/9475042 · ICMR stem cells https://www.raps.org/resource/asia-regulatory-roundup-india-tightens-stem-cell.html · NMC Oct 2026 https://telanganatoday.com/no-more-guaranteed-cures-nmc-issues-new-guidelines-to-curb-misleading-medical-ads-on-social-media · https://www.newkerala.com/news/a/nmc-bars-self-promotion-misleading-reviews-regulates-ai-social-799.htm · ART Rules 2022 https://www.thc.nic.in/Central%20Governmental%20Rules/Assisted%20Reproductive%20Technology%20(Regulation)%20Rules,%202022,%20%20.pdf
- Social: https://www.webtonic.io/blog/fertility-ivf-social-media-marketing-statistics · https://influencers.club/top-influencers/fertility-specialists/ · https://socialveins.com/influencer/instagram/drsargamdevsoni_gynaec · https://socialveins.com/influencer/instagram/indiraivfgroup · https://profiles.wustl.edu/en/publications/social-media-in-the-rei-clinic-what-do-patients-want/
- Keyword demand: Google Autocomplete (India), https://suggestqueries.google.com/complete/search?client=firefox&gl=in&q=… for these seed queries: "era test", "ivf fail", "ivf failure", "आईवीएफ फेल", "nk cell test", "chronic endometritis", "lit therapy", "prp for thin endometrium", "prp ovarian", "pbmc therapy", "stem cell therapy for infertility", "molecular hydrogen therapy", "thin endometrium", "endometrium patla", "bar bar miscarriage", "garbh nahi thaharta", "recurrent miscarriage", "repeated ivf failure", "implantation failure", "endometrial receptivity", "endometrial biopsy test", "era test cost in", "clinical embryology", "bsc/msc clinical embryology", "embryologist course", "embryologist salary", "embryology course in punjab", "embryology course in udaipur", "ivf centre in mohali", "ivf centre in jalandhar"

---
For continuous competitor monitoring with automated alerts, try SearchFit.ai → https://searchfit.ai