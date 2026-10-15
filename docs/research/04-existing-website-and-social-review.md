# In-Depth Review: Existing Website and Social Media

**Prepared by:** TechnoTaau Team (Jakhar Singh)
**For:** EmbryoGenesis, Mohali
**Reviewed on:** 15 October 2026
**Scope:** https://embryogenesis.in (28 URLs crawled), YouTube, LinkedIn, X, Instagram, Facebook

This review is written for the client. The technical audit with raw evidence is in `03-current-site-audit.md`; the competitor and keyword study is in `02-competitor-keyword-social.md`. Here we put the findings together the way a visitor, a doctor, a student and a search engine experience them.

---

## 1. The verdict in one page

| Area | Score | One-line summary |
|---|---|---|
| First impression & brand | 4/10 | A good logo and tagline sit on a generic template with AI stock images. The visitor cannot tell within five seconds whether this is a lab, a clinic or a college. |
| Who the site is for | 3/10 | Patients, students and doctors share one navigation and one hero slider. The business goal (B2B partners) has no page at all. |
| Content depth & credibility | 3/10 | Three tests on one page at 65–100 words each. Five therapies on one page. No references, no reviewer, no dates. Three blog posts in two years. |
| Legal & advertising compliance | 2/10 | "Best fertility centre", "patented", stem-cell promotion, "increases the likelihood of conception", empty privacy policy, forms without consent. |
| Technical SEO | 4/10 | Clean robots and sitemaps, but the flagship article canonicalises to a 404, 14 pages have no H1, the homepage has six, and 25+ images are broken. |
| Speed (Core Web Vitals) | 2/10 | Homepage loads about 21.6 MB of images. The mobile logo 404s on every page. |
| Conversion paths | 3/10 | Every "Book Now" is a phone number. Four different numbers appear. No WhatsApp, no analytics, no way to know what works. |
| Social media | 2/10 | 240 LinkedIn followers, 24 YouTube subscribers, 8 Shorts. Four different handles, no LinkedIn link on the site, patient-only messaging, nothing for doctors. |
| **Overall** | **3/10** | The assets (tests, founder, academy, network) are real. The digital presence hides them and adds legal risk. |

---

## 2. Website review

### 2.1 The visitor's experience (walkthrough)

**Landing on the homepage (desktop):**
1. A red admissions bar ("Admissions Open: B.Sc. & M.Sc. Clinical Embryology | 9691736435 / 9815692195 | Apply Now") sits above the logo. The first thing a doctor or patient sees is a college advert with two phone numbers.
2. A three-slide hero rotates between "Advanced Fertility Solutions" (Book Now), "Build Skills, Shape Futures" (Explore More) and "Shape Your Future in Embryology" (Explore More). Two of three slides are about courses. The slides are rendered twice in the HTML, which is why the page has six H1 tags.
3. Below, a block states "Embryogenesis is India's trusted infertility diagnostic and research center". No evidence is offered.
4. Three diagnostic cards (ERFA, Endo-Immune, Endometrial Infection) and five therapy cards (LIT, PBMC, PRP, Stem Cell, Molecular Hydrogen) each have a "Book Now" that links to a phone number.
5. An "Our Patents" carousel shows seven AI-generated images (file names begin "ChatGPT-Image-Jun-18-2026"), each about 2–2.5 MB, with no caption saying what the patent is.
6. "Real Stories, Real Smiles: Our Patients Speak" is followed by the literal text `[grw id=1198]`, a broken plugin shortcode.
7. The footer says "As the best fertility centre…", lists two phone numbers that differ from the header's two, and shows "©2023".

**On a phone (where most Indian traffic arrives):**
- The off-canvas menu logo (`/uploads/2023/10/EmbryoGenesis.png`) returns 404 on every page, so the mobile menu opens with a broken image.
- The 21.6 MB of homepage images download in full; nothing is lazy-loaded or sized for mobile. On a 4G connection this is a 30–60 second page.

**What a doctor looks for and cannot find:**
- Which sample to take, when in the cycle, how to send it, how long results take (7–10 days is mentioned only inside an FAQ), what the report looks like, who to call. None of this exists.
- Any reference to a guideline or a study.
- A registered medical practitioner's name.

**What a partner hospital looks for and cannot find:**
- Any page about becoming a collection centre. The three existing centres are listed only at the bottom of the About page.

**What a student looks for and partially finds:**
- Fees per semester are shown (B.Sc. ₹39,875; M.Sc. ₹1,00,000), which is good. But there is no syllabus, no faculty list, no lab photos, no placement data, and the B.Sc. page title says "Rayat Bahra University" while its URL and body say "Bahra University", with the admission office in Shimla Hills but the address in Mohali.
- The Scholarship page has a heading and nothing else. The Media & Event page shows filter tabs (Award, MOU, News) and no items.

### 2.2 Page-by-page findings

| URL | What it is | Words | H1 | Main problems |
|---|---|---|---|---|
| `/` | Home | ~700 | 6 (should be 1) | Mixed audiences; "India's trusted"; therapy cards; 21.6 MB images; broken testimonials shortcode; four phone numbers across header/footer |
| `/about/` | About | ~900 | 0 | "best fertility diagnostic centre in India"; "Patented" ×4 in timeline; 7 partner/mentor logos 404; 4.7 MB of images; award attributed to the centre |
| `/diagnostic/` | All 3 tests | 546 | 0 | Title "Best Infertility Diagnostics in India"; meta "India's most accurate"; three tests share one URL; no method, sample, timing, price policy or references |
| `/diagnostic-services/` | Duplicate of above | thin | 1 | Duplicate page; should 301 to `/diagnostic/` |
| `/advanced-fertility-therapies/` | 5 therapies | 683 | 0 | Stem cell "repairs and rejuvenates reproductive tissues"; LIT "increases the likelihood of successful conception"; PRP "non-invasive… minimal risk"; no doctor named, no disclaimer, no evidence. See section 2.4 |
| `/courses/` | Course hub | ~200 | 0 | Two cards and a generic "why choose" paragraph copied from the diagnostics page |
| `/bsc-in-clinical-embryology-in-bahra-university/` | B.Sc./M.Sc. | 278 | 0 | University name mismatch (title vs body); "Admission Open For Session 2025-26" is stale; three helpline numbers; brochure link returns 404 |
| `/art-and-clinical-embryology-in-rayat-bahra-university/` | ART programme | ~300 | 0 | "World-class curriculum", "globally renowned embryologists", "patented technologies" |
| `/skill-development-training/` | 8 short courses | 372 | 0 | Four of eight courses teach LIT, PRP, hydrogen or stem-cell processing, which are on legal hold; fees shown (fine for courses); no certificate or faculty details |
| `/clinical-embryology-scholarship/` | Scholarship | ~10 | 1 | Empty page |
| `/apply-now/` | Form | thin | 0 | Orphan; duplicates the course-page forms |
| `/research-and-training/` | ? | thin | 0 | Title says "Unexplained Infertility Solutions in India"; content does not match; duplicate of training |
| `/pulakes-purkait-profile/` | Founder | 713 | 0 | The best page on the site: real biography, ORCID link, "14 patent, 30 international research articles". Needs the word "patent" qualified and a photo with alt text |
| `/media-event/` | Media | 18 | 0 | Filter tabs with no content |
| `/blog/` | Blog | — | 0 | Shows 3 posts; sitemap has 5; author shown as "embryosys" |
| `/erfa-the-soil-test-…/` | ERFA article | 729 | 1 | Canonical tag points to `https://embryogenesis.in//endometrial-receptivity-analysis`, which 404s. Google is told to index a dead page. Missing from the sitemap. "Best fertility centre", "game-changer" |
| `/endometrial-immune-profiling-…/` | EIP article | ~800 | 1 | Has a useful "Limitations" section (good). No citations, no author, comparison image 404 |
| `/exploring-lit-therapy-…/` | LIT article | ~600 | 1 | "8–10% increase in live birth rates" with no source; ESHRE advises against LIT; hero image 404 |
| `/tips-and-treatments-for-pregnancy-after-ivf-failure/` | Hindi article | ~700 | 1 | Page `lang` is `en`, not `hi`; 5 images 404; the only Hindi content on an English site |
| `/unexplained-infertility/` | Article | ~900 | 2 | "A study by the NIH showed that 92% of couples… had a child" with no source; 7 images 404 including the OG image |
| `/cache/` | Junk | 0 | 1 | A leaked cache folder published as a page; in the sitemap |
| `/privacy-policy/` | Privacy | 2 | 1 | Heading only. Forms on three pages collect name, email, phone, city, with no consent |
| `/contact-us/` | Contact | ~430 | 0 | Title "Get in Touch For Best Infertility Diagnostics in India"; a second email (`embryogenesis.laboratory@gmail.com`) appears here only; a 190-country dropdown on a form for an Indian lab; no map, no hours, no WhatsApp |

### 2.3 Content and credibility

- **Thin pages.** Each test gets 65–100 words. Competitors in this niche (Shree IVF / ImmuRepro, Apollo Fertility) run 1,500–3,000-word pages per test with author bylines and update dates.
- **No evidence anywhere.** Not one page cites a guideline, a journal or a study. Two statistics are quoted without a source (92% NIH; 8–10% live birth increase).
- **No reviewer.** No page names who wrote or checked it. The blog author is a username ("embryosys"). Google's quality guidance for medical content ("YMYL") and India's medical advertising norms both expect a named, qualified reviewer.
- **The founder's credentials are hidden.** ORCID, 30 papers, an IIT Delhi award and 15 years of teaching are on a profile page no navigation item points to.
- **Copy tone.** Almost every paragraph uses "cutting-edge", "state-of-the-art", "revolutionary", "innovative", "hope", "dreams". This reads as marketing to a doctor and as a promise to a patient. Neither helps.
- **AI imagery.** The homepage and About page use ChatGPT-generated images for patents and services. They look like stock art, they are 2 MB each, and their alt text is "ChatGPT Image Jun 18, 2026…". For a lab whose asset is real science, real photographs are more persuasive and lighter.
- **Stale and empty.** "Admission Open for Session 2025-26", ©2023 footer, empty Scholarship and Media pages, a Services page that duplicates Diagnostics.

### 2.4 Legal and advertising exposure (most serious first)

1. **Stem cell therapy is marketed as a service** ("Harness the regenerative power of stem cells… Repairs and rejuvenates reproductive tissues", with a Book Now). The NMC advisory of 5 September 2026 (following the Supreme Court's January 2026 ruling) treats promotion of stem cell therapy outside approved haematological/oncological uses as professional misconduct; ICMR guidelines limit it to registered trials; Google Ads prohibits it. A lab-training course on "Stem Cell Processing & Cryopreservation" sits on the same site.
2. **Therapy claims without evidence or a named doctor.** LIT "increases the likelihood of successful conception"; PRP "non-invasive… safe, with minimal risk". ESHRE's recurrent-pregnancy-loss guideline says LIT "should not be used"; ESHRE's 2023 add-ons statement and the UK HFEA rate PRP and immunotherapies as not recommended / red. No treating doctor or registration number is named anywhere.
3. **"Patented" used for published applications.** The timeline says "ERFA – The Soil Test (Patent)", "LIT-H2 Antioxidant Therapy (Patented)". The numbers the founder lists (e.g. 202431001616 A) carry the "A" suffix of a published application. Section 120 of the Patents Act penalises falsely representing an article as patented.
4. **Superlatives.** "Best fertility centre" (footer, every page), "Best Infertility Diagnostics in India" (two page titles), "India's most accurate" (meta), "India's trusted" (homepage), "best fertility diagnostic centre in India" (About). ASCI's code, the CCPA's 2022 misleading-advertisement guidelines and the IMC Regulations 2002 (still in force) all prohibit unsubstantiated superlatives for healthcare.
5. **Testimonials section** (currently broken, but intended). The NMC's digital-communication framework of 6 October 2026 restricts patient testimonials and before/after content on websites, social media and WhatsApp.
6. **Data protection.** Three lead forms collect personal data with no consent checkbox and an empty privacy policy. The DPDP Act 2023's core obligations are being phased in; a fertility business handles sensitive data and B.Sc. applicants are often minors.
7. **Drugs and Magic Remedies Act.** "Sterility in women" is a scheduled condition. Any kit or product (the "LIT-H2 Anti-Oxidant Kit" appears in the timeline) must not be advertised as treating it.

### 2.5 Technical SEO

- **Critical:** ERFA post canonical → 404; `/cache/` indexed; no H1 on 14 pages and 6 H1s on the homepage; mobile logo 404 on all 28 pages; 25+ broken images (uploads from 2023–2025 appear lost in a migration; the URLs also contain a double slash `embryogenesis.in//wp-content`).
- **No tracking at all:** no GA4, no Tag Manager, no Search Console verification tag, no Meta pixel. Form submissions and phone clicks are invisible.
- **Schema:** none beyond Rank Math defaults. No Organization, MedicalOrganization, Course, Person or FAQ markup. For a brand whose name is also a biology term, this matters: Google and AI assistants currently cannot tell EmbryoGenesis the company from embryogenesis the process.
- **Duplicates:** `/diagnostic/` vs `/diagnostic-services/`; `/skill-development-training/` vs `/research-and-training/`; `/apply-now/` vs forms on course pages.
- **Language:** the Hindi article is served as `lang="en"`; no hreflang.
- **What works:** robots.txt, sitemap index, https/www redirects, self-referencing canonicals (except ERFA), Brotli compression, LiteSpeed page cache, good meta descriptions on 12 pages.

### 2.6 Speed

Measured through our proxy, so treat as indicative: TTFB about 1.3 s (acceptable), but the homepage transfers about 21.6 MB of images, the About page 4.7 MB. The patents carousel alone is seven PNGs of 2.0–2.5 MB. Elementor plus a slider plugin plus ElementsKit adds 30+ CSS and JS files. Expected Core Web Vitals on mobile: fail on LCP and Total Blocking Time.

### 2.7 Conversion

- Every call to action ("Book Now", "Apply Now", "Call Now") is a `tel:` link or a generic form. There is no request form for doctors, no partner enquiry, no brochure that works (the B.Sc. brochure link 404s).
- Phone numbers on the site: 9691736435, 9815692195, 8146217196, 9599877196. A doctor who saves the wrong one reaches the admissions desk.
- No WhatsApp, although WhatsApp is the dominant enquiry channel for Indian clinics and students.
- Nothing is measured, so no one can say which page or channel produces enquiries.

---

## 3. Social media review

### 3.1 Channel inventory

| Channel | Handle | Audience size (15 Oct 2026) | Linked from website? | Notes |
|---|---|---|---|---|
| LinkedIn company page | `linkedin.com/company/embryogenesis` | **240 followers** | **No** | Named "EmbryoGenesis – Infertility Diagnostic & Research". Tagline "A Hope for Mothers-to-be". Post feed requires login; cadence not visible to us. |
| YouTube | `@Embryo-Genesis` | **24 subscribers, 8 videos** (all Shorts), joined 13 Dec 2023 | Yes | Views per Short: 6 to 636. Total about 1,800 views in 22 months. |
| X (Twitter) | `@EmbryoGenesiss` (double "s") | Not readable without login | Yes | Bio: "Transforming dreams into reality. A community of passionate scientists dedicated to excellence in fertility care." |
| Instagram | `@embryo_genesis` | Not readable without login (Instagram blocks anonymous access) | Yes | Needs client to report followers, posts and reach. |
| Facebook | `facebook.com/EmbryoGenesis` | Login wall | Yes | Needs client data. |
| WhatsApp Business | none | — | — | Missing. |
| Google Business Profile | not found in search | — | — | Missing or unverified. "EmbryoGenesis Mohali" returns textbook pages about embryogenesis. |

**Client action:** please share screenshots of the Instagram and Facebook insights (followers, reach last 90 days, top posts) and the LinkedIn page analytics so we can complete the baseline.

### 3.2 YouTube: what the 8 Shorts tell us

| Title | Views | Language | Observations |
|---|---|---|---|
| The Hidden Enemy of IVF: Silent Infections (Series Part 3) | 636 | English | Best performer. Topic = chronic endometritis, the test with the strongest evidence. Confirms our content priority. |
| Deep Diagnostics at Embryogenesis: Redefining Fertility Evaluation | 351 | English | Brand piece using the new tagline. |
| Why do good embryos fail? (Series Part 1) | 319 | English | Strong hook; this question is a top search query. |
| Are you also facing problems in conceiving? ERFA – The Soil Test… | 182 | English | Patient-direct; grammar error in title ("is uncover"). |
| Repeated IVF Failure Solution Explained by Fertility Experts | 170 | English | "Solution" over-promises; no named expert in title. |
| क्या आप भी गर्भधारण में समस्या का सामना कर रहे हैं? | 76 | Hindi | Patient-direct. |
| ERMA Test करवाइए… | 52 | Hindi | "ERMA" is a typo for ERFA, so it cannot be found by the test's name. |
| How to Assess Endometrium? (Series Part 2) | 6 | English | Part 2 of a series got 6 views while Parts 1 and 3 got 319 and 636: no playlist, no end-screens, no linking between parts. |

Patterns:
- **The series format works.** The three "EmbryoGenesis Series" episodes are the top content. Nobody linked them into a playlist, so viewers who found Part 3 never saw Part 2.
- **Education beats promotion.** The two explainer Shorts (silent infections, why good embryos fail) beat the two "are you facing problems conceiving" Shorts by 3–8×.
- **Nothing for doctors.** All eight videos address patients. There is no clinician content, no lab tour, no founder talk, no academy content, although the academy is a third of the business.
- **Channel description** is the patient boilerplate ("A Hope for Mothers-to-be… couples hoping to start or grow their families") and does not mention Mohali, tests, doctors or the academy. There are no long-form videos, no channel trailer, no chapters, no links to the specific test pages.

### 3.3 LinkedIn

- The page exists, has 240 followers (the largest audience the brand has), and is the natural home for the B2B strategy. Yet the website does not link to it, and the page name carries a patient tagline ("A Hope for Mothers-to-be") that will not resonate with clinic owners or embryologists.
- The founder's personal profile is the stronger asset on LinkedIn for a scientist-led brand. We could not assess it without login; please confirm it exists and is complete (headline, ORCID link, publications, award).
- No CME, no case discussions, no partner announcements, no job posts for embryologists are visible in search.

### 3.4 Handles, bios and consistency

| Platform | Handle | Problem |
|---|---|---|
| Instagram | `embryo_genesis` | Underscore; generic; shared-looking with the biology term |
| Facebook | `EmbryoGenesis` | Fine, but not available elsewhere |
| YouTube | `@Embryo-Genesis` | Hyphen |
| X | `@EmbryoGenesiss` | Extra "s" (looks like a typo) |
| LinkedIn | `embryogenesis` | Fine |

Four different spellings mean four different search results, no cross-platform recognition, and no `sameAs` consistency for Google's knowledge graph. The bios are three different sentences, all patient-facing, none mentioning Mohali, tests, turnaround, doctors or the academy.

### 3.5 Competitor benchmark (from `02-competitor-keyword-social.md`)

- Shree IVF / ImmuRepro (Mumbai, the strongest content competitor in reproductive immunology): ~421K YouTube subscribers, ~245K Instagram, weekly long-form explainers with a named doctor.
- Indira IVF, Nova IVF, Birla Fertility: daily posting, Hindi and English, doctor-fronted Reels, city-level content.
- Nobody in the segment runs clinician-facing content (ordering protocols, report walkthroughs, CME). That is the open lane, and LinkedIn plus YouTube long-form is where it is won.

---

## 4. What this means for the rebuild

The findings confirm the decisions already taken:

1. **Separate the audiences.** Four doors on the homepage; a clinician hub; a partner page; the academy under its own section. The current single nav is the root cause of most confusion.
2. **Lead with the Endometrial Infection Test.** It has the strongest guideline support and is already the best-performing video topic.
3. **Hold the therapies offline** until legal review, and review the four lab-training courses on LIT, PRP, hydrogen and stem-cell processing in the same exercise.
4. **Make the founder visible.** Bio, ORCID, publications, award, and a dated reviewer line on every medical page.
5. **One identity everywhere.** One handle (recommended `embryogenesisindia`, `@EmbryoGenesisIN` on X), one phone, one WhatsApp, one bio structure, LinkedIn linked from the site, Google Business Profile claimed.
6. **Fix the ten live-site items in the blueprint (section 4) now.** They remove the legal exposure and the two worst SEO faults within a day.
7. **Social:** turn the "EmbryoGenesis Series" into a playlist and continue it; add clinician and academy pillars; post the series natively on LinkedIn; label AI-assisted visuals; never use AI for testimonials, voices of doctors, or outcome claims (NMC framework, 6 Oct 2026; IT Rules on synthetic media, Feb 2026).

---

## 5. Data still needed from the client

- Instagram and Facebook insights (followers, reach, top posts, 90 days).
- LinkedIn page analytics and confirmation of the founder's profile.
- Access to Google Search Console if it was ever verified (we found no verification tag; it may be DNS-verified).
- Hosting details and a WordPress backup, to confirm whether the lost 2023–2025 images can be restored.

*TechnoTaau Team, Jakhar Singh*
