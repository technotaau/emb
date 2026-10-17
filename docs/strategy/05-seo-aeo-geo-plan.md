# EmbryoGenesis: SEO, AEO and GEO Plan (next phase, 12 months from launch)

**Prepared by:** TechnoTaau Team (SEO strategy lead, planner). Team lead and sign-off: Jakhar Singh.
**Client:** EmbryoGenesis, Mohali, Punjab (https://embryogenesis.in)
**Date:** 17 October 2026 | **Version:** 1.1 (QC fixes applied)
**Status:** plan for approval. It replaces the parts of `docs/strategy/02-seo-strategy.md` listed in section 9.
**Change history:** v1.0, 17 Oct 2026 (first issue); v1.1, 17 Oct 2026 (QC fixes C1–C20 and lead decisions J1–J16, `docs/qc/qc-seo-plan.md`).

**Read with**
- `docs/00-project-brief.md` (section 0 decisions; section 5 guardrails).
- `docs/strategy/00-business-model.md`.
- `docs/research/07-seo-aeo-geo-landscape-2026.md` and `docs/research/08-keyword-competitor-ai-baseline.md` (the evidence base for this plan).
- `docs/strategy/02-seo-strategy.md` (the technical specification we keep), `docs/strategy/03-social-media-strategy.md` (sections 0, 1 and 4) and `docs/strategy/04-brand-voice-and-design-system.md` (claims dictionary, disclaimer, boilerplate).
- The QC reports in `docs/qc/`.

**How to read references and labels**
- (R07 §x) = research 07, section x. (R08 §x) = research 08; (R08 §1.6) means research 08, section 1, finding 6. (02 §x), (03 §x), (04 §x) = strategy documents. (R03) = `docs/research/03-current-site-audit.md`.
- (QC-SEO), (QC-FE), (QC-DES), (QC-CF) = `docs/qc/qc-seo-aeo-geo.md`, `qc-frontend.md`, `qc-design.md`, `qc-content-fidelity.md`.
- Labels carried over from research 07: **[SECONDARY]** (from a news or vendor report, not the primary text), **[UNVERIFIED]**, **[VERIFY with counsel]**.
- **(E)** = a TechnoTaau Team estimate. Every estimate is re-checked 30 days after launch.
- **NEW** = a page that does not exist yet. Its slug is a proposal and follows the site's existing root-slug pattern.
- **Months:** L = launch day. M1 = the launch month, M2 to M12 the months after it. The indicative calendar assumes launch in the first half of December 2026 (target Tuesday 8 or Wednesday 9 December, **to be confirmed by the client**). So M1 = Dec 2026, M2 = Jan 2027, M3 = Feb, M4 = Mar, M5 = Apr, M6 = May, M7 = Jun, M8 = Jul, M9 = Aug, M10 = Sep, M11 = Oct, M12 = Nov 2027. The academy admission season (roughly April to August) falls in M5 to M9.
- People: **PP** = Prof. (Dr.) Pulakes Purkait (scientific reviewer). **VW** = Dr. Vidhu Wadhwa, MBBS, MD (Pathology) (clinical reviewer, registered medical practitioner). **JS** = Jakhar Singh.

---

## Contents

0. Summary for the client (one page)
1. Baseline (October 2026)
2. Goals and KPIs
3. Strategy pillars
   - 3.1 Launch and technical SEO for the WordPress migration
   - 3.2 Entity, local search and NAP
   - 3.3 Keyword-to-URL map for the existing URLs
   - 3.4 Content plan and 12-month calendar
   - 3.5 AEO (answer engines)
   - 3.6 GEO (generative engines and AI assistants)
   - 3.7 E-E-A-T, YMYL and compliance (includes the pre-launch decisions D1 and D2)
   - 3.8 Off-page and digital PR
   - 3.9 Video and social for search
4. Roadmap and the next 30 days
5. Quality-control system
6. Team and RACI
7. Risks and mitigations
8. Client inputs needed
9. What this plan supersedes in `02-seo-strategy.md`
- Appendix A: KPI definitions
- Appendix B: Monthly report template
- Appendix C: AI prompt panel summary (25 prompts)
- Appendix D: Source map to research 07 and 08

---

## 0. Summary for the client (one page)

Three terms: **SEO** is being found in Google and Bing; **AEO** (answer engine optimisation) is being the direct answer to a question; **GEO** (generative engine optimisation) is being cited by AI assistants.

**Where we are**
- Your new 19-page website is built as a reference for your WordPress developer: the same pages, wording and web addresses, no errors in our quality-control (QC) checks, valid search labels (structured data) and 100/100 for accessibility.
- Search results still show the old site; in our search checks, the Diagnostic page was still listed with the title "Best Infertility Diagnostics in India".
- AI assistants barely know you. A first check of 25 typical questions with one AI search tool cited you 0 times; we repeat it in four assistants this month. Your PIN code appears three ways online, and the only university page that named you has gone.

**The goal for the 12 months after launch**
- More test enquiries and more academy enquiries and applications from your website and Google (search and Maps). Therapy enquiries are counted, but therapies are not promoted during the legal review.
- Be the source Google and AI assistants quote on endometrial testing, IVF failure, recurrent implantation failure (RIF), recurrent miscarriage (RPL) and embryology careers. Clinic chains, journals and education portals answer most of these today, but five gaps are still open, such as ERA versus ERFA and the endometrial biopsy explained for patients.
- All of it inside India's medical-advertising rules, which became stricter on 6 October 2026.

**The eight biggest moves**
1. **A clean WordPress launch:** the same web addresses, one-step redirects, search labels carried over, privacy-safe analytics, and Search Console and Bing from launch day (§3.1).
2. **Therapy pages decided before launch:** we recommend taking the therapy page, the LIT (lymphocyte immunisation therapy) post and the Hindi post offline until your lawyer and reviewers approve evidence-based versions (decision D1, §3.7.1).
3. **Minimum compliance fixes:** "best", "leading", "India's trusted", "patented", the testimonials block, unsourced statistics and the "Source: chat GPT" line (decision D2, §3.7.2).
4. **One identity:** one name, one address with a confirmed PIN code and one phone number everywhere, including your Google Business Profile, directories, ITHS and the universities (§3.2).
5. **Two new reviewed articles a month until April 2027, then one to two a month** (about 19 in 12 months, including reserve and conditional posts): open gaps first, and academy articles live before the April admission season (§3.4).
6. **Trustworthy medical pages:** a named author, Prof. Purkait's dated review, Dr. Wadhwa's registration number for clinical claims, references, a disclaimer and a public editorial policy (§3.7).
7. **Mentions from sources AI systems trust:** universities, ITHS, the Indian Fertility Society, journals and YouTube. A published ERFA validation paper would help most (§3.6, §3.8, §3.9).
8. **Monthly measurement:** Search Console, Bing and Analytics reports, your enquiry log and 25 set questions asked three times in each AI assistant (§2, §5).

**What we need from you** (full list in §8)
- Eight decisions (D1 to D8) between **23 October and 13 November 2026**: therapy content, compliance minimum, refresh pack, address and phone, privacy and consent, launch date, AI crawlers and AI use.
- Your lawyer's review of the therapy content, the privacy policy and forms, AI-made videos and any partner terms.
- Facts: PIN code, one public phone and WhatsApp number, opening hours, the name on your signage, Dr. Wadhwa's registration number and the 2027–28 course details.
- Access: Search Console (if one exists), your Google Business Profile and the staging site.
- **Review time:** from 9 to 27 November, three 90-minute slots a week with Prof. Purkait and a weekly 60-minute slot with Dr. Wadhwa; after launch, one 90-minute slot a week and one 60-minute slot a fortnight.

**How we control quality**
Every page passes seven checks, and nothing goes live without Prof. Purkait's dated review, a compliance check and your written approval. We audit monthly and quarterly, with a set response for ranking drops, wrong AI answers, negative reviews, complaints and outages (§5).

**What realistic progress looks like** (target, with the minimum in brackets; our estimates, reset 30 days after launch; §2)

| By | Test enquiries a month from the website | Academy enquiries a month | AI questions where you appear (of 25) | New quality links |
|---|---|---|---|---|
| Month 3 | 15 (8) | 30 (15) | 4 (2) | 6 (3) |
| Month 6 | 30 (15) | 80 in season (40) | 8 (5) | 12 (6) |
| Month 12 | 50 (25) | 40 off-season (20) | 12 (8) | 20 (12) |

Sources: our research reports 07 and 08 (17 October 2026), the site audit (15 October 2026) and our QC reports; sections 1 to 3 give the reference for each point.

---

## 1. Baseline (October 2026)

### 1.1 Website and rebuild status

| Area | Status on 17 Oct 2026 | Source |
|---|---|---|
| Old live site | WordPress 7.0.4 with Elementor, Astra, Rank Math, Forminator and LiteSpeed Cache. Audit score 38/100; performance 20/100; 14 pages without an H1; homepage images about 21.6 MB | R03 |
| Old site defects that still affect Google | ERFA post canonical points to a 404 URL, so the post is missing from the sitemap; junk `/cache/` post indexed; no analytics; Search Console verification unknown | R03 (C1, H6, C7) |
| Old titles still indexed | `/diagnostic/` shows "Best Infertility Diagnostics in India"; `/unexplained-infertility/` shows "Unraveling unexplained infertility in embryogenesis" | R08 §7 |
| New reference build (`site/`) | 19 pages: 17 indexable pages, a placeholder privacy policy (noindex) and a 404 page. Same URLs as the old site. Old content kept as the client decided (brief §0) | `site/src/llms.txt`, QC-CF |
| Build quality | `qc.py`: 0 errors, 0 warnings. Schema.org validator: 0 problems (59 before fixes). Lighthouse mobile: accessibility 100 on every page; performance about 89 average; 98 to 100 with non-blocking fonts and gzip. axe-core: 0 violations | QC-SEO, QC-FE, QC-DES |
| Redirects | All 28 audited old URLs return 200 or redirect in one hop (`site/src/_redirects`, `site/src/.htaccess`) | QC-SEO §2.5 |
| llms.txt | All therapy facts and therapy page links removed by the lead on 17 Oct 2026 (the therapy page, LIT post and Hindi post are not listed until D1 is decided) | `site/src/llms.txt`; R07 §2 implication 6 |
| Schema constants | `ORG.description` in `site/build.py` no longer mentions therapies (lead fix, 17 Oct 2026), in line with R07 §4.2 | `site/build.py`; R07 §4.2 |
| Forms | 8 pages carry lead forms with a required, unticked consent box. The privacy policy they link to is a placeholder | QC-CF §8.6 |
| WordPress port | Not yet started as far as we know. The client's developer builds; TechnoTaau Team supplies the specification. **Client to confirm status** | brief §1 |
| Launch timing | The blueprint's 12–18 Nov 2026 launch no longer holds. Working assumption: first half of December 2026 (to be confirmed) | lead decision |

### 1.2 Search visibility today
- **Demand exists; the brand does not appear.** People in India search heavily for IVF failure, ERA, chronic endometritis, thin endometrium, recurrent miscarriage and embryology careers, in English and Hinglish. EmbryoGenesis appeared in **none** of the non-branded results checked (R08 §1.1).
- **Brand searches fail.** "EmbryoGenesis Mohali" returns unrelated Mohali IVF directories, and "Pulakes Purkait" returns West Bengal politicians (R08 §1.1).
- **Who owns the answers:** Shree IVF/ImmuRepro on the clinical topics; ESHRE, PubMed Central and university pages on "is it worth it" questions; Apollo, Birla, Indira and Nova on "what is ERA"; Careers360, Shiksha and Zollege on every course and salary query (R08 §1.2, §4).
- **Five open gaps:** ERA vs ERFA and IHC-based receptivity tests; endometrial biopsy explained for patients; Hinglish and Hindi questions; endometrial TB-PCR and genital TB; north-India embryology admissions (R08 §1.3).

### 1.3 Entity footprint

| Asset | Status | Source |
|---|---|---|
| Google Maps place | Exists: "EMBRYOGENESIS - Infertility Diagnostic & Research", Knowledge Graph ID `/g/11y4zwq7dd`. Ownership, category, review count and NAP not verified. Reviews probably exist (the old site embedded a reviews widget) | R08 §7 |
| PIN code | Three versions: **140302** (brochure, site, schema), **140103** (Latrexa; Wikipedia's Sahauran page), **140104** (Rayat Bahra University listings) | R08 §7 |
| Wikidata | No item for the lab or the founder. "embryogenesis" = Q28962, the biological process | R08 §7 |
| Directories | Latrexa lists the lab (PIN 140103, phone 081462 17196). Not found on Justdial or Practo | R08 §7 |
| LinkedIn | Company page exists (about 240 followers); founder profile exists. Neither surfaced in search | brief §2; R08 §7 |
| ORCID | Active (0000-0002-8814-9939), 40 works, including the ERFA, ReceptivityPX and LIT-H2 entries | R08 §7 |
| ResearchGate / Google Scholar | Two different ResearchGate URLs in use; no Scholar profile found | R08 §7 |
| ITHS website | Names Prof. Purkait as Director, says "15+ patents", no link to embryogenesis.in | R08 §7, §8.5 |
| Rayat Bahra University | Programme pages exist; whether they name EmbryoGenesis could not be checked (site returned HTTP 522) | R08 §7 |
| Bahra University | **Citation lost.** The page that named "ITHS, INNR & EMBRYOGENESIS" now redirects (301) to bushimla.in, which does not mention EmbryoGenesis | R08 §7 |
| News | Times of India (3 Jul 2024), Himachal Tonite (6 Jul 2024, verified, names EmbryoGenesis, no link), NewsNation (27 Jul 2024, labelled "brand story") | R08 §7 |
| Aggregators | ivf.net lists the ITHS–Bahra programme; one listing reportedly spells the founder "Pulakesh" (seen in a search summary; not confirmed). Careers360, Zollege and CollegeSearch disagree on fees and durations | R08 §4, §7 |
| YouTube `@Embryo-Genesis` | Did not surface in search | R08 §7 |
| Autocomplete | "pulakes purkait" and "erfa test" appear as suggestions; "embryogenesis mohali" returns none | R08 §7 |

### 1.4 AI-visibility baseline
- **0 of 25** prompts cited EmbryoGenesis in the proxy test (R08 §6.1).
  - It appeared only in a search restricted to its own domain (P6), in one directory (P24), and indirectly through the 2024 Himachal Tonite article (P19).
- **This is a proxy**, not a reading of ChatGPT, Gemini, Perplexity, Copilot or Google AI Mode. It used an AI search tool with a US-based index (R08 §0). We run the real panel in Phase 0 (§4.2, item 7).
- The biggest exposure in AI answers: the only EmbryoGenesis pages an assistant could cite for recurrent miscarriage or IVF failure in Hindi are the LIT post and the Hindi post. The Hindi post says LIT "increases the chance of successful conception" and promotes PRP and stem cell therapy (R08 §1.5).

### 1.5 What is not yet measurable

| Item | Why not | How we fix it | When |
|---|---|---|---|
| Traffic and enquiries | No analytics on the old site (R03 C7) | GA4 with consent at launch; client's enquiry log from now | Log from Nov 2026; GA4 at L |
| Search Console history | Verification status unknown (R03 C7) | Client gives access; we export the history before launch | Phase 0 |
| Search volumes | No credible public source for these Indian keywords (R08 §0) | Google Keyword Planner (India; English and Hindi) | By 30 Oct 2026 |
| SERP features (People Also Ask, AI Overviews, video, local pack) | Google blocks scripted checks (R08 §0) | Manual monthly checks (R08 §6.2) | From Phase 0 |
| True AI visibility | Baseline is a proxy (R08 §0) | Real panel, 3 runs per surface (R07 §3.2) | Week of 26 Oct 2026 |
| Google AI impressions | Search Console's Generative AI report appears only after enough AI impressions (R07 §3.1) | Track; not a failure if absent for months (R07 §3.3) | From L |
| GBP actions and reviews | Ownership unconfirmed (R08 §7) | Claim or confirm ownership | By 2 Nov 2026 |
| Referring domains | No paid tool authorised (R08 §0) | Search Console Links and Bing reports | L+30 |
| Field Core Web Vitals | New site has no field data yet | PageSpeed lab runs until field data exists | From staging |
| Academy pipeline | Client data not shared | 2026 season enquiry and application counts | By L+30 |

### 1.6 Known issues to fix

| # | Issue | Fix | Owner | By |
|---|---|---|---|---|
| 1 | Old title "Best Infertility Diagnostics in India" still indexed for `/diagnostic/`; `/contact-us/` title also says "Best" (R08 §7; R03) | With the client's go-ahead by email, change both titles on the live site now (Rank Math); new titles ship at launch | Client developer | 23 Oct 2026 |
| 2 | PIN code shown as 140302, 140103 and 140104 (R08 §7) | Client confirms with India Post (D4); one PIN everywhere | Client | 23 Oct 2026 |
| 3 | Bahra University citation lost (R08 §7) | Ask the university to restore a programme page that names EmbryoGenesis and links to `/bsc-in-clinical-embryology-in-bahra-university/`; update the footer link to the university's current domain | Client + TechnoTaau | M2 |
| 4 | ITHS site says "15+ patents" (R08 §7, §8.5) | ITHS changes it to "patent applications published" and links to embryogenesis.in | Client (group site) | Before L |
| 5 | ERFA post canonical points to a 404 on the live site (R03 C1) | With the client's go-ahead by email, fix in Rank Math now; correct in the new build | Client developer | 23 Oct 2026 |
| 6 | Address shown in two forms (short visible form vs full schema form) and several phone numbers (QC-CF §8.3; R07 §5.2) | One master NAP record (D4, §3.2) | Client + TechnoTaau | Before L |
| 7 | Residual therapy facts in `llms.txt` and in `ORG.description` (R07 §4.2) | **Done 17 Oct 2026** (lead). Revisit only if D1 approves evidence-based therapy content | TechnoTaau | Done |
| 8 | Privacy policy is a placeholder while 8 forms collect data (QC-CF §8.6) | Real policy and itemised notices (D5) | Counsel + client | 13 Nov 2026 |
| 9 | Kept content contains superlatives, "patented", a testimonials block, unsourced statistics and an AI source line (QC-CF §7) | Compliance minimum (D2, §3.7.2) | Client approval | 10 Nov 2026 |
| 10 | Therapy page, LIT post and Hindi post (R08 §1.5; R07 §1 implication 6) | Decision D1 (§3.7.1) | Client + counsel | 10 Nov 2026 |
| 11 | Course pages say "Admission Open For Session 2025-26" (QC-SEO §4.1 item 12) | Current session and dates (refresh R5) | Client admissions | Before L |
| 12 | Award named two ways: "Best Innovator Award" and "Best Innovation Award" (QC-CF §4) | Client confirms the exact name on the certificate; one form everywhere | Client | 30 Oct 2026 |
| 13 | Organization logo is 403×102, not square (QC-SEO §6.3) | Supply a 512×512 emblem logo | Client designer | Before L |
| 14 | Two ResearchGate URLs; "Pulakesh" spelling reported on ivf.net, not confirmed (R08 §7) | Use the URL that resolves; check the ivf.net listing and ask for a correction if the spelling is confirmed | PP; TechnoTaau | M2 |
| 15 | Fonts load from Google Fonts in the reference build (QC-FE §5) | Self-host in WordPress (§3.1) | Developer | Before L |

---

## 2. Goals and KPIs

### 2.1 Goals
1. **Business outcomes:** grow website-sourced **test enquiries** and **academy enquiries and applications**. Count **therapy enquiries** without promoting therapies (lead decision).
2. **Visibility where people now get answers:** being cited is the new unit of visibility for informational health searches, so we report citations and branded demand alongside clicks (R07 §0, item 2).
3. **Compliance and accuracy:** zero compliance incidents, and wrong AI facts fixed at source within 30 days (R07 §3.3).

### 2.2 Rules for the numbers
- **Re-baseline rule:** at **L+30** we recalculate every baseline from 30 days of data (plus any Search Console history the client can share). We then propose revised floors and targets for client approval. After that, targets change only at the quarterly reviews.
- **Floor and target:** above the target = ahead of plan. Between floor and target = on track. Below the floor = we review the causes and agree a corrective plan.
- **Checkpoints:** 3, 6 and 12 months after launch (about early March, early June and early December 2027 if launch is 8 or 9 December 2026). Each checkpoint uses the 4 weeks before it.
- **Consent caveat:** GA4 counts only visitors who accept analytics, so its traffic and AI-referral figures are floors (R07 §3.1). Search traffic KPIs therefore use Search Console clicks, and business outcomes use the client's enquiry log.
- **What B1 and B2 count (assumption):** every website-sourced enquiry, whether the visit came from branded or non-branded search, the Google Business Profile and Maps, or direct, referral and social visits. In year 1 most enquiries come from branded, direct, GBP and referral visits; non-branded search adds a growing share. The B1 and B2 numbers are placeholders until the client shares 3 to 6 months of enquiry history (§8.2 #21), and they are reset at L+30.

### 2.3 KPI table
All numbers marked (E) are estimates for a small, new entity in a YMYL niche; definitions are in Appendix A.

| # | KPI | Baseline (Oct 2026) | 3 months: floor / target | 6 months: floor / target | 12 months: floor / target | Source | Owner |
|---|---|---|---|---|---|---|---|
| **Business outcomes** | | | | | | | |
| B1 | Website-sourced **test enquiries** per month | Not tracked | 8 / 15 (E) | 15 / 30 (E) | 25 / 50 (E) | Enquiry log; GA4 key events as a floor | Client front desk; TechnoTaau compiles |
| B2 | **Academy enquiries** per month (courses and lab training) | Not tracked | 15 / 30 (E) (pre-season) | 40 / 80 (E) (in season) | 20 / 40 (E) (off-season) | Enquiry log; GA4 form events | Client admissions |
| B3 | **Academy applications** from website-sourced leads, 2027 season (Apr–Aug) | 2026 count needed | n/a | Floor = 2026 count; target = 2026 count + 25% (E) | Reported Sep 2027 | Admissions records | Client admissions |
| B4 | **Therapy enquiries** per month | Not tracked | Track only. No target while therapies are not promoted | Track only | Track only | Enquiry log | Client front desk |
| **Search** | | | | | | | |
| S1 | Non-branded clicks per month | About 0 (R08 §1.1) | 40 / 80 (E) | 120 / 250 (E) | 300 / 600 (E) | Search Console | TechnoTaau SEO lead |
| S2 | Non-branded impressions per month | Unknown | 3,000 / 6,000 (E) | 8,000 / 15,000 (E) | 20,000 / 35,000 (E) | Search Console | TechnoTaau SEO lead |
| S3 | Branded impressions and clicks (brand filter, Appendix A) | Unknown | Upward trend. Numeric target set at L+30 (R07 §3.3) | Set at L+30 | Set at L+30 | Search Console | TechnoTaau SEO lead |
| S4 | Sitemap URLs indexed | New sitemap at L | 85% / 95% (E) | 90% / 100% (E) | 90% / 100% (E) | Search Console Pages report | TechnoTaau QA |
| S5 | Pages with impressions | Unknown | 15 / 20 (E) | 22 / 27 (E) | 30 / 35 (E) | Search Console | TechnoTaau SEO lead |
| S6 | AEO wins (of the 40 questions in R08 §5) | 0 (R08 §1.1) | 1 / 3 (E) | 3 / 6 (E) | 6 / 12 (E) | Quarterly manual check | TechnoTaau QA |
| **AI visibility** | | | | | | | |
| A1 | AI panel score (of 25 prompts; method §3.6.3) | 0/25 proxy (R08 §6.1); real baseline in Phase 0 | 2 / 4 (E) | 5 / 8 (E) | 8 / 12 (E) | Monthly panel | TechnoTaau QA |
| A2 | Brand prompts (P6, P24, P25) visible with correct facts | 0 of 3 | 1 / 2 of 3 (E; R07 §3.3 aims for brand prompts visible by month 3) | 2 / 3 of 3 (E) | 3 / 3 of 3 (E) | Monthly panel | TechnoTaau QA |
| A3 | Pages cited in Bing AI Performance | Not set up | 1 / 2 (E; R07 §3.3 proposes at least 1) | 2 / 4 (E) | 4 / 8 (E) | Bing Webmaster Tools | TechnoTaau SEO lead |
| A4 | AI referrals (GA4 AI Assistant channel and custom AI group) and Google AI impressions | Not set up | Track only, reported as a floor (R07 §3.1, §3.3) | Track only | Track only | GA4; Search Console Generative AI report | TechnoTaau SEO lead |
| A5 | AI factual errors traced and fixed at source within 30 days | n/a | 100% | 100% | 100% (R07 §3.3) | Panel error log | TechnoTaau SEO lead |
| **Local, links, technical, compliance** | | | | | | | |
| L1 | GBP actions per month (calls, directions, website clicks) | Unknown (ownership unconfirmed, R08 §7) | 15 / 30 (E) | 30 / 60 (E) | 50 / 90 (E) | GBP Performance | Client; TechnoTaau reports |
| L2 | New relevant referring domains since launch | To measure at L+30 | +3 / +6 (E) | +6 / +12 (E) | +12 / +20 (E) | Search Console Links; Bing | TechnoTaau SEO lead |
| T1 | Core Web Vitals, mobile, 5 key templates | Old site 20/100 (R03); reference build about 89 (QC-FE) | Pass (lab) | Pass | Pass (field data when it exists) | PageSpeed Insights; Search Console CWV | Developer; TechnoTaau QA |
| T2 | Technical errors (5xx, redirect chains, broken canonicals, internal 404s, links to held pages) | Many on old site (R03) | 0 | 0 | 0 | Monthly crawl; Search Console | TechnoTaau QA |
| C1 | Compliance incidents (ASCI, NMC, platform, consumer) | None logged | 0 | 0 | 0 (R07 §3.3) | Incident log | JS |
| C2 | Median medical-review turnaround (gate G3), reported per reviewer | n/a | ≤ 5 working days for items reviewed by Prof. Purkait only; ≤ 10 working days where Dr. Wadhwa's clinical review is needed | Same | Same | Content tracker | JS |

**A2 is deliberately conservative.** R07 §3.3 aims for brand prompts to be visible by month 3, but the brand name collides with the biology term (R08 §1.6) and the founder's name with other public figures (R08 §1.1), so we plan for 2 of the 3 brand prompts by then.

**Not used as KPIs:** "rank in ChatGPT" (answers rarely repeat), "share of traffic from AI" on its own (undercounted) and raw AI Overview impression totals without page context (R07 §3.3).

### 2.4 Measurement stack (free first)

| Tool | Use | Notes |
|---|---|---|
| Google Search Console | Clicks, impressions, queries, indexing, CWV, Generative AI performance report | Keep the "Search generative AI features" control on **Include** (R07 §1.1, G3). The AI report shows impressions only, no clicks or queries (R07 §3.1) |
| Bing Webmaster Tools | Indexing, IndexNow, **AI Performance** (citations, grounding queries, citation share in preview) | The only first-party view of Copilot citations (R07 §2.5, §3.1) |
| GA4 via Google Tag Manager | Sessions, key events, AI referrals | Consent Mode v2, default denied. Native "AI Assistant" channel since 13 May 2026, confirmed in Google's Analytics Help release notes of that date (https://support.google.com/analytics/answer/9164320); custom AI channel group as backstop (R07 §3.1) |
| Looker Studio | One monthly dashboard | Sources: Search Console, GA4, enquiry log sheet, panel sheet |
| PageSpeed Insights and CrUX | Core Web Vitals | Lab runs until field data exists |
| Rich Results Test and Schema.org validator | Structured data | The Rich Results Test no longer supports FAQ (R07 §1.2); use the Schema.org validator for MedicalWebPage, MedicalTest and DiagnosticLab |
| `site/qc.py` | Automated page checks | Runs on `site/dist/`. We will add an input-folder option so it can check a saved copy of the staging and live WordPress pages |
| Google Keyword Planner | Search volumes (India; English and Hindi) | Replaces the relative tiers in R08 §0 |
| Screaming Frog (free version), an uptime monitor (free tier) | Crawls and outage alerts | Monthly crawl; 5-minute uptime checks |
| Ahrefs, Similarweb | Backlinks, competitor traffic | **Only if the client authorises them** (R08 §0) |

---

## 3. Strategy pillars

Each pillar states its objective, actions, owner, timing and the QC check that proves it is done.

### 3.1 Launch and technical SEO for the WordPress migration

**Objective:** move to the new design on WordPress with no loss of URLs, indexing or tracking, and with a clean technical base, because Google's AI features use the same core ranking systems as Search (R07 §1.1, G1 and G2).

**Key principle:** this is a **design and platform change, not a URL change**. Every live URL keeps its path. Blog posts stay at the root (for example `/unexplained-infertility/`), so the WordPress permalink setting must be `/%postname%/`, not the `/blog/%postname%/` in 02 §5.1.

| # | Item | Specification | Owner | When | QC check |
|---|---|---|---|---|---|
| 1 | URLs | Keep every path in `site/src/llms.txt` plus the held pages as decided in D1. HTTPS, no www, trailing slash, lowercase. Keep each post's original publish date | Developer | Build | Crawl of the URL list: all 200 |
| 2 | Redirects | Port the rules in `site/src/.htaccess` (or Rank Math Redirections), **except three**: do **not** port `/blog/page/*` (WordPress needs blog pagination), the sitemap rule (Rank Math serves `/sitemap_index.xml`) or the feed rule (WordPress serves feeds). Delete the `/cache/` post and return **410**. One hop to a 200 page for every old URL | Developer | Build | Redirect test of the 28 audited URLs plus extras: single 301 or 410 |
| 3 | Category and author archives | Keep them redirected as in `.htaccess`. Set Rank Math breadcrumbs to hide the category level, so breadcrumbs never link to a redirected archive. Disable author archives | Developer | Build | Crawl: no internal links to redirected URLs |
| 4 | Canonicals | Self-referencing, absolute. Leave Rank Math's per-page canonical blank. Check the ERFA post specifically (old bug, R03 C1) | Developer | Build | Crawl: canonical target = self and 200 |
| 5 | Indexing controls | Noindex: internal search, any thank-you page, held pages as decided in D1. Never block a noindexed page in robots.txt | Developer | Build | Crawl: noindex only on the planned list |
| 6 | Schema port | A small must-use plugin on Rank Math's JSON-LD filter (02 §6.11), populated from `ORG`, `PERSON` and `WEBSITE` in `site/build.py` and the page JSON files. Corrections first: no therapy wording in `ORG.description`; NAP from D4; square logo; `WEBSITE.inLanguage` = `en-IN` only if the Hindi post goes offline; `reviewedBy` and `lastReviewed` only once the review line is visible on the page (QC-SEO §4.1 item 23); FAQPage only where a visible FAQ matches word for word; no review or rating markup; the founder is a `Person`, never `Physician` (02 §6.5) | Developer; TechnoTaau validates | Build | Schema.org validator 0 errors on every template; Rich Results Test passes for Organization, Breadcrumb, Article and ProfilePage |
| 7 | robots.txt | As in the reference build: all search and answer bots allowed (OAI-SearchBot, ChatGPT-User, GPTBot, ClaudeBot, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended), `/wp-admin/` blocked except `admin-ajax.php`, internal search blocked. Sitemap line points to the sitemap WordPress actually serves (R07 §2.4, §6.1). AI-training opt-out per D7. Applebot-Extended behaviour is **[UNVERIFIED]** (R07 §2.4) | Developer | Build | Fetch of `/robots.txt` on production |
| 8 | Host and CDN bot protection | Check that firewall or CDN settings do not block Googlebot, Bingbot or the AI crawlers. Whether some CDNs block AI crawlers by default is **[UNVERIFIED]** (R07 §2 implication 1) | Developer | Staging | Host settings screenshot |
| 9 | Sitemaps | Rank Math sitemap index. Only indexable, 200, self-canonical URLs. `lastmod` changes only when content changes (R07 §2 implication 4). Image entries on | Developer | Build | Sitemap vs crawl comparison |
| 10 | IndexNow | Rank Math Instant Indexing, reported to offer IndexNow **[UNVERIFIED; developer to confirm]**. Google does not participate **[SECONDARY]**; treat it as a Bing and Copilot tool (R07 §2.5) | Developer | Build | Key file reachable; submissions log |
| 11 | Core Web Vitals budget | p75 mobile: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, TTFB ≤ 0.8 s from India. Homepage ≤ 1.5 MB, inner pages ≤ 1.0 MB, JS ≤ 250 KB, CSS ≤ 80 KB compressed, GTM the only third-party script (02 §5.2) | Developer | Build | PageSpeed mobile on home, `/diagnostic/`, a course page, a blog post and `/contact-us/` |
| 12 | Fonts | **Self-host** the fonts the design uses (Work Sans 500/600/700 and Lato 400/700) as WOFF2, Latin subset, `font-display: swap`, preload one file. No Google Fonts request. This removes the render-blocking request that capped the reference build near 90 (QC-FE §3, §5) | Developer | Build | No request to fonts.googleapis.com |
| 13 | Images | Upload through the media library so WordPress writes `srcset`. Phones get an 800 px hero (about 41 KB instead of 145 KB, QC-FE §3). LCP image not lazy-loaded, `fetchpriority="high"`. Width and height on every image. WebP | Developer | Build | PageSpeed: no "properly size images" warning on home |
| 14 | Embeds | YouTube with a click-to-load facade; static map image linking to the Maps place (02 §5.2) | Developer | Build | No iframe on first load |
| 15 | Search Console | Domain property (DNS) plus URL-prefix property. Generative AI control on **Include** (R07 §1.1, G3). Submit the sitemap. Inspect the key URLs on launch day | TechnoTaau SEO lead | L | Sitemap "Success"; inspection results saved |
| 16 | Bing | Import from Search Console, submit the sitemap, IndexNow on, AI Performance report read monthly, Bing Places with the same NAP (R07 §2.5, §5.1) | TechnoTaau SEO lead | L | Bing shows the sitemap processed |
| 17 | GA4 and consent | GTM with Consent Mode v2, basic mode, default denied (02 §5.7). Google signals off, no ad links, no ad pixels on any page, never on academy pages (applicants may be minors) (R07 §4.7). Events: `generate_lead` (form ID and page section only), `whatsapp_click`, `tel_click`, `brochure_download`, `page_not_found`. **No field values or "interest" choices sent to GA4**; the enquiry type is recorded in the client's enquiry log. GA4's native "AI Assistant" channel (13 May 2026, Google Analytics Help release notes: https://support.google.com/analytics/answer/9164320) counts visits from AI assistants; the custom channel group "AI search" above Referral, with the regex in R07 §3.1, is the backstop. Internal-traffic filter | Developer; TechnoTaau | Build | GA4 DebugView: no events before consent; events after consent |
| 18 | Forms (DPDP) | Itemised notice above the submit button; required, unticked consent box; separate optional marketing box; withdrawal as easy as consent; academy forms ask "Are you 18 or older?" and route under-18s to parental consent; consent log; "please do not include medical reports" line (04 §5.6; R07 §4.7). Substantive DPDP duties start about 13–14 May 2027; check the Gazette, because an earlier date was proposed but not notified as of September 2026 (R07 §4.7) | Developer; counsel approves text | Build | Test submission per form; consent log entry |
| 19 | 404 and security | Real 404 status with helpful links; never redirect all 404s to the home page; HSTS and basic security headers (02 §5.2, §5.9) | Developer | Build | `curl -I` on a random URL returns 404 |

**Go-live runbook (staging noindex removal checklist)**

Staging sits behind HTTP basic authentication and "Discourage search engines" (02 §5.1). On launch day, in this order:
1. Take a full backup and agree the rollback plan.
2. Remove HTTP basic authentication.
3. WordPress, Settings > Reading: untick "Discourage search engines from indexing this site".
4. Rank Math global robots: `index, follow`. Only the planned pages carry noindex.
5. Check headers on 5 URLs for any `X-Robots-Tag: noindex` from the server or CDN.
6. Check `/robots.txt` is the production version (no `Disallow: /`) and its Sitemap line is right.
7. Search and replace the staging domain with `https://embryogenesis.in` in the database, including serialized data. Check canonicals, Open Graph tags, schema, sitemap and internal links for staging URLs.
8. Run the redirect test file. `/cache/` returns 410. Held pages behave as decided in D1.
9. Crawl the site: no broken internal links, no links to held pages, canonicals self and 200.
10. GA4: production stream, internal-traffic filter on, consent default denied, events only after consent.
11. Submit sitemaps to Search Console and Bing; inspect the home page, `/diagnostic/`, `/courses/`, both university course pages, the founder profile and the three refreshed posts.
12. Test every form end to end, including the consent log and the enquiry routing by "I am interested in".
13. Spot-check structured data on 5 templates and PageSpeed mobile on the same 5.
14. Post-launch checks at 48 hours and 7 days (gate G6, §5).

Launch rules: no new articles on launch day (they follow from week 2, so migration effects can be read on their own), and launch on a Tuesday or Wednesday so working days follow.

**QC check for pillar 3.1:** two staging QA passes by TechnoTaau (16 Nov 2026, and 25 Nov, two working days before the 27 Nov freeze), a signed go-live runbook, and the go/no-go meeting (4 Dec 2026) chaired by JS with the client.

### 3.2 Entity, local search and NAP

**Objective:** one consistent identity that Google, Bing and AI systems can match to "EmbryoGenesis, an infertility diagnostic and research centre in Mohali, Punjab", and that is not confused with the biological process. Microsoft lists consistent entities and Bing Places among its citation advice, and Google tells local businesses to keep Business Profile data current (R07 §1.5, §2.5).

**One master record (D4).** The developer stores it once (an options page) and the header, footer, contact page and schema read from it (02 §7.3).

| Field | Value | Status |
|---|---|---|
| Name | EmbryoGenesis. Alternate: "EmbryoGenesis – Infertility Diagnostic & Research" (R07 §5.2) | Agreed |
| Address | Top Floor, Rayat Bahra Dental College & Hospital, Rayat Bahra University Campus, VPO Sahauran, Tehsil Kharar, Dist. Mohali, Punjab **[PIN to confirm]** | PIN: 140302 vs 140103 vs 140104 (R08 §7). Client confirms with India Post |
| Phone | One public number for the lab and WhatsApp. Proposed +91 81462 17196 (brief §2). Admissions numbers labelled as "Admissions" | Client to confirm, including whether +91 98156 92195 is the admissions line (site) or the Delhi regional centre (brief §2) |
| Email | Public email; we recommend a domain address over Gmail (02 §7.3) | Client to decide |
| Hours | Not in any source (R07 §5.1) | Client to supply |
| Map pin | The client's own Maps place (KG `/g/11y4zwq7dd`; about 30.78099, 76.61935) (R08 §7) | Agreed |

**Naming rules** (02 §7.2, kept): "EmbryoGenesis" in running text; first mention on every page and profile is "EmbryoGenesis, an infertility diagnostic and research centre in Mohali, Punjab"; listings use the 50-word boilerplate in 04 §6 verbatim; the founder is "Prof. (Dr.) Pulakes Purkait, Founder & Director", with "Ph.D." where space allows, never "Dr." alone where it could imply a medical doctor; the spelling is always "Pulakes".

| # | Action | Rule or reason | Owner | When | QC check |
|---|---|---|---|---|---|
| 1 | Confirm the PIN and the master record | One PIN everywhere: site, schema, GBP, Bing Places, directories (R08 §7) | Client | 23 Oct 2026 | Signed record |
| 2 | Google Business Profile: claim or confirm ownership of the existing place | Name = the real-world name on the signage, no keywords (keyword-stuffed names breach Google's guidelines and arguably NMC clause 8.1(xii)). Primary category: the most precise "IS a" category, likely "Medical laboratory" **[check the exact list in the GBP interface]**; never "Fertility clinic" or "IVF clinic". One profile, for the Mohali lab only. Phone under the client's direct control. Accurate hours including holidays (R07 §1.5, §5.1) | Client (owner) + TechnoTaau | 2 Nov 2026 | Profile matches the master record |
| 3 | Check GBP eligibility inside the campus | A department inside an institution may have its own profile if it is public-facing with its own signage and staffed hours **[check on site]** (R07 §5.1). Verification in India is often by video **[UNVERIFIED]**; prepare a short video of the signage, entrance and lab (R07 §5 implication 1) | Client | Before L | Verification complete |
| 4 | No profiles at partner hospitals; no practitioner profiles | They are not EmbryoGenesis locations (R07 §5.1) | Client | Always | Monthly check |
| 5 | GBP posts | Treated as advertising under NMC clause 3.2: factual updates only; clinical posts carry the RMP credential line (R07 §5.1, §4.1) | TechnoTaau drafts; client posts | Monthly from M2 | G4 on every post |
| 6 | Reviews | No review requests aimed at patients, no QR drives, no staff, student or partner-clinic reviews, no incentives. Reply factually without confirming that anyone was a patient. Report suspicious reviews through GBP tools. One-page reply policy for staff (R07 §5.3) | Client; TechnoTaau writes the policy | Policy by L | Monthly review audit |
| 7 | Bing Places | Same data as GBP, published at launch (R07 §5.1) | TechnoTaau | L | Listing live |
| 8 | Apple Business Connect | Optional, same data. Not researched in R07 **[UNVERIFIED]** | TechnoTaau | M3 | Listing live |
| 9 | Directories | Consistency hygiene, not volume (R07 §5.2): correct Latrexa's PIN once confirmed (R08 §7); claim or correct Justdial (whether free listings are still offered is **not verified**; avoid paid "top placement"); Practo, Sulekha and IndiaMART low priority (R07 §5.2) | TechnoTaau | M2 | NAP spot check |
| 10 | Knowledge-graph profiles | ORCID: add EmbryoGenesis employment and website. Google Scholar: create and claim papers. ResearchGate: use the URL that resolves. LinkedIn company and founder pages: align the description and address (R08 §7; 02 §7.5) | PP (ORCID, Scholar); TechnoTaau (LinkedIn wording) | M2 | `sameAs` lists only live URLs |
| 11 | Wikidata | Organisation item and founder item (ORCID as P496), strictly factual, conflict of interest declared, references such as the Times of India item, ORCID and IP India records. Low-cost hygiene; no evidence it raises AI citations for a small organisation **[UNVERIFIED benefit]**. **No Wikipedia article** (notability not met) (R07 §2.2; R08 §7) | TechnoTaau | M2–M3 | Items live; COI declared |
| 12 | Disambiguation | "Not to be confused with embryogenesis, the biological process of embryo development." Already in `llms.txt` and schema; add to the About page (client approval), LinkedIn "About" and the Wikidata description (02 §7.2; R08 §1.6) | TechnoTaau; client approves | Before L | Present on all four |
| 13 | ITHS and universities | ITHS: "patent applications published", a link to embryogenesis.in. Rayat Bahra University: name EmbryoGenesis and its role on programme pages, with a link. Bahra University: restore a programme page that names EmbryoGenesis. Aggregator facts corrected through the universities, never through an EmbryoGenesis "college" profile (R07 §5.4; R08 §7) | Client asks; TechnoTaau drafts the wording | Phase 0 to M2 | Pages checked by hand |

**QC check for pillar 3.2:** a monthly NAP spot check (site footer, contact page, schema, GBP, Bing Places, LinkedIn and the top three directories) with zero mismatches; the entity audit in each quarterly deep audit.

### 3.3 Keyword-to-URL map for the existing URLs

**Objective:** give each existing URL one clear job, using research 08's clusters (K1 to K22), without changing the client's wording. Titles and meta descriptions are SEO metadata. The old site had no H1 on 14 pages, including most of the main pages (R03), so most current H1s were written by our builders and we may improve them. All changes still need client approval. Volumes are relative tiers until Keyword Planner data arrives (R08 §0).

| URL | Job | Clusters (R08 §2) | Query focus: primary; secondary | Title (current → proposed) | H1 (current → proposed) | Notes and guardrails |
|---|---|---|---|---|---|---|
| `/` | Brand and entity hub; routes three audiences | K22 | EmbryoGenesis Mohali; infertility diagnostic centre Mohali, endometrial tests | Keep "EmbryoGenesis Mohali \| Infertility Diagnostics & Research" (57) | Keep "Advanced Fertility Solutions at EmbryoGenesis, Mohali" | D1 and D2 removals (therapy cards, testimonials block, "India's trusted"). FAQ already de-duplicated |
| `/about/` | Entity facts, team | K22 | about EmbryoGenesis; EmbryoGenesis lab Mohali | Keep "About EmbryoGenesis \| Infertility Diagnostic Centre, Mohali" (59) | "About Us" → "About EmbryoGenesis" | The entity answer box (QC-SEO §4.1 item 4) is already in the build: take "therapeutic services" out of it while D1 is open, because answer boxes are written to be quoted and therapy facts stay out of machine-readable summaries (R07 §4.2). Add the disambiguation line (client approval). D2 superlatives |
| `/pulakes-purkait-profile/` | Founder E-E-A-T page; fixes the "Who is Prof. Pulakes Purkait?" gap (P25) | K22 | pulakes purkait; prof pulakes purkait, pulakes purkait embryogenesis | "Prof. (Dr.) Pulakes Purkait, Founder \| EmbryoGenesis Mohali" → "Prof. (Dr.) Pulakes Purkait, PhD \| Founder, EmbryoGenesis" (57) | Keep | Add "reproductive scientist; not a medical practitioner" from the approved bio (04 §6), ORCID and Scholar links, and "patent applications published" wording |
| `/diagnostic/` | Main page for the three tests | K4, K6, K8, K9; K5 only as a no-figure FAQ | endometrial receptivity test (ERFA); chronic endometritis test, endometrial immune profile, ERFA test, ERFA soil test | Keep "Endometrial Receptivity Test (ERFA), Mohali \| EmbryoGenesis" (59) | "Diagnostic Services" → "Diagnostic Services: Endometrial Tests (ERFA, Endo-Immune, EIT)" | Refresh R1: evidence status per test (reviewer decisions, R08 §8), reviewer lines, references, the FAQ "What affects the cost of endometrial testing?" answered without figures (R08 §3, K5). Links to N3, N4, N5 when live |
| `/advanced-fertility-therapies/` | **Held** | K14 | None | No optimisation | – | Decision D1. Therapy keywords excluded during the legal hold |
| `/courses/` | Academy hub | K15, K16 | clinical embryology courses Punjab and Himachal; embryology course Chandigarh, BSc and MSc clinical embryology | Keep "Clinical Embryology Courses in Punjab & HP \| EmbryoGenesis" (58) | "Courses" → "Clinical Embryology Courses" | Current session (R5); question-style H2 (QC-SEO §4.1 item 11); links to N9 to N12 |
| `/art-and-clinical-embryology-in-rayat-bahra-university/` | Rayat Bahra programmes | K16, K17 | Rayat Bahra University clinical embryology; BSc and MSc ART and clinical embryology | "ART & Clinical Embryology at Rayat Bahra \| EmbryoGenesis" → "BSc & MSc ART & Clinical Embryology, Rayat Bahra University" (59) | Keep | The page shows no fees. Autocomplete shows "rayat bahra … clinical embryology fees" (R08 §2.2); add fees only exactly as the university publishes them (client input). Awarding university named prominently (R07 §4 checklist) |
| `/bsc-in-clinical-embryology-in-bahra-university/` | Bahra University programmes | K16 | Bahra University clinical embryology; clinical embryology course Himachal Pradesh | "BSc Clinical Embryology, Bahra University \| EmbryoGenesis" → "BSc & MSc Clinical Embryology, Bahra University, Himachal" (57) | Keep | Restore the lost university citation (§3.2 item 13) |
| `/skill-development-training/` | Hands-on lab training | K20 | hands-on lab training Mohali; immunohistochemistry training, tissue processing and microtomy training, molecular genetics training | Keep "Skill Development Lab Training in Mohali \| EmbryoGenesis" (56) | "Skill Development Training" → "Skill Development Lab Training, Mohali" | New meta (153): "Hands-on lab training at EmbryoGenesis, Mohali: biochemistry, molecular genetics, tissue processing and microtomy, and immunohistochemistry. 1 to 5 days." Never target ICSI or IVF-lab terms: not offered (R08 §1.9) and a keyword trap (R08 §1.6). Therapy modules per D1 |
| `/blog/` | Blog hub | All | EmbryoGenesis blog | Keep (56) | Keep | New meta without the LIT mention (157): "Articles from EmbryoGenesis, Mohali, on endometrial receptivity, ERFA – The Soil Test, endometrial immune profiling, IVF failure and unexplained infertility." |
| `/media-event/` | Press, awards, MoUs (third-party corroboration) | K22 | EmbryoGenesis news; ERFA launch | Keep (51) | "Media & Event" → "Media & Events" | One award name (§1.6 item 12); exact name, issuer and date (R07 §4.1, 8.1(ix)) |
| `/contact-us/` | NAP and local | K22; P12 (local) | contact EmbryoGenesis; endometrial test Mohali | Keep "Contact EmbryoGenesis \| Book a Test or Course, Mohali" (53) | "Contact Us" → "Contact EmbryoGenesis, Mohali" | Full address with the confirmed PIN; one phone; map link to the Maps place |
| `/privacy-policy/` | Legal (DPDP) | – | – | Keep (38) | Keep | Replace the placeholder before launch (D5); then make it indexable |
| `/erfa-the-soil-test-endometrial-receptivity-analysis-optimize-fertility-success/` | Receptivity basics; branded ERFA | K4 (Q7), K6 | what is endometrial receptivity; window of implantation, ERFA test | Keep "ERFA – The Soil Test & Embryo Implantation \| EmbryoGenesis" (58) | Keep (client's) | Refresh R2 |
| `/endometrial-immune-profiling-what-it-is-why-it-matters-and-who-should-consider-it/` | Endometrial immune profiling | K9 (Q21–23) | endometrial immune profiling; uterine NK cells, NK cell test IVF | Keep (56) | Keep | Refresh R3 (ESHRE status on uNK testing) |
| `/unexplained-infertility/` | Unexplained infertility | K13 (Q33) | unexplained infertility; meaning, causes, diagnosis | Keep (59) | Keep | Refresh R4 |
| `/exploring-lit-therapy-treatment-for-recurrent-pregnancy-loss/` | **Held** | K14 | None | – | – | D1 |
| `/tips-and-treatments-for-pregnancy-after-ivf-failure/` (Hindi) | **Flagged** | K2 (Q6) | – | – | – | D1. A Hindi version of N1 only if the client lifts "English only" (R08 §3) |
| `/404.html` | Utility | – | – | Keep | Keep | New meta without "therapies" (142): "Sorry, this page could not be found. Visit the EmbryoGenesis home page, diagnostic tests, courses, lab training, blog or contact page instead." |

**Keyword traps and exclusions**

| Do not target | Why | Use instead | Source |
|---|---|---|---|
| "embryogenesis" on its own | The biology term (Wikidata Q28962) | "EmbryoGenesis Mohali", "ERFA", "Pulakes Purkait" | R08 §1.6 |
| "ICSI course", "ICSI training" | Means the Institute of Company Secretaries of India; and no ICSI course exists | "ICSI training for embryologists", only if a course is launched | R08 §1.6, §1.9 |
| "RIF test" | Means rifampicin resistance (TB) | "recurrent implantation failure" | R08 §1.6 |
| "ERA cost", any cost or price term (K5) | A crypto token; and the no-price rule makes these unwinnable | A no-figure FAQ: "What affects the cost of endometrial testing?" | R08 §1.6, §1.7 |
| "soil test" on its own | Means agriculture | "ERFA – The Soil Test", "ERFA endometrial test" | R08 §1.6 |
| "PBMC therapy" and all therapy terms (K14: LIT, PRP for thin endometrium, stem cell, endometrial scratching) | Physical-therapy intent; therapies on legal hold | None until the hold is lifted | R08 §1.6, §2.1 |
| "ERA test" as a title or H1 | ERA is Igenomix's test | Refer to it only as Igenomix's test, in body text | R08 §3 (K4); 02 §3.3 |
| "IVF centre Mohali", "best IVF …" | Wrong intent (a lab, not an IVF centre) and superlatives | Lab and test terms | 02 §3.3; R07 §4.1 |
| City "ERA test cost" pages | Programmatic copies (Birla runs 39), doorway risk, no-price rule | Depth and accuracy on one page | R08 §4; R07 §5.5 |
| "andrology course", "IVF lab training" | Product gap, not a content gap | Only if the academy adds such a course | R08 §1.9 |
| "good colleges", "top colleges" | Monitoring prompts only; superlatives in copy | Factual programme pages | R08 §6.1 |
| Any sex-selection term, in any language | ART Act s.32 and PCPNDT s.22 | Never | R07 §4.3, §4.4 |

**QC check for pillar 3.3:** the keyword map lives in the content tracker; gate G0 rejects any brief whose primary query is already owned by another URL (cannibalisation check); the monthly crawl flags duplicate titles.

### 3.4 Content plan and 12-month calendar

**Objective:** publish a small number of deep, reviewed pages that answer the questions nobody in India answers well, and keep existing medical pages current. Google names original, non-commodity content as the lever for both Search and its AI features (R07 §1.1, §1 implication 2).

#### 3.4.1 Topic clusters

| Cluster | Pillar page | Spokes (existing and NEW) | Audiences | R08 clusters |
|---|---|---|---|---|
| A. Endometrial testing | `/diagnostic/` (service) and NEW N3 `/endometrial-receptivity-tests-explained/` (explainer; slug provisional) | ERFA post, EIP post, NEW N4 biopsy, NEW N5 chronic endometritis, NEW N13 immunohistochemistry, NEW N8 genital TB (conditional) | Couples; treating doctors | K4, K6, K7, K8, K9, K12 |
| B. IVF failure, RIF and RPL patient education | NEW N1 `/ivf-failed-what-next/` | NEW N2 RIF tests, NEW N6 RPL tests, NEW N7 thin endometrium, `/unexplained-infertility/`; Hindi post per D1 | Couples (doctors for N2) | K1, K2, K3, K10, K11, K13 |
| C. Embryology careers and admissions | `/courses/` | Both university course pages, `/skill-development-training/`, NEW N9, N10, N11, N12 | Students, parents, trainees | K15 to K20 |

Internal linking (adapted from 02 §1.5): each spoke links to its pillar in the first 150 words; each pillar links to all its spokes; academy pages link lightly to the diagnostic cluster and never into patient pages; **nothing links to held pages**.

#### 3.4.2 Cadence and review budget

Prof. Purkait's review time is the bottleneck, so the cadence is set by review slots, not by writing capacity.

- **Review slot:** one 90-minute slot a week with PP on a fixed weekday, and one 60-minute slot a fortnight with VW for clinical claims (E; we time the first reviews in Phase 0 and recalibrate).
- **What one slot covers (E):** one new medical post (two review rounds), or one refresh or re-review of a medical page, or two academy posts or small updates.
- **Pre-launch review surge (9 to 27 Nov 2026):** the Phase 0 review set (the D2 replacement text, R1 to R5, T1 and T2) needs about 7 of PP's slot-equivalents in three weeks, against 3 normal slots (QC estimate, `docs/qc/qc-seo-plan.md` §5.3). We ask the client for three 90-minute slots a week with PP and a weekly 60-minute slot with VW in that window. N4 and N9 are reviewed from 1 to 11 Dec 2026, after the freeze; they publish from week 2 of M1 anyway.
- **If the surge is not granted:** the minimum pre-launch review set is the D2 replacement text, R1, T1, T2 and the R5 facts (the admissions team checks the facts; PP approves the wording only). R2 to R4 move to M1, and their pages launch with only the D2 minimum edits.
- **Cadence: 2 new posts a month until April 2027 (M1 to M5), then 1 to 2 a month; about 19 in 12 months including reserve and conditional posts.** M1 to M4 normally pair one medical and one academy post. M11 has no new post, because its review time goes to the academy refresh (R8b). Refreshes and re-reviews follow the calendar in §3.4.5: the test page every 6 months, articles every 12 months, sooner when a guideline changes (04 §5.4).
- **Step-up, from M4 at the earliest:** up to **1 new post a week**, the level first discussed, only if all of these hold for 8 weeks: median G3 turnaround within the C2 targets (§2.3); no more than 2 posts waiting for review; no repeated G4 failures; at least 4 approved topics with sources in the backlog; and PP confirms a second weekly slot. Step-up posts come from the reserve list W1 to W5 or from new questions found in Search Console.
- **Step-down:** if more than 3 items wait for review or turnaround exceeds 10 working days, drop to 1 new post a month and protect corrections and re-reviews first.
- **Social review is separate.** Reels and posts (03 §4.4) need their own review time; the web slot is not shared.

**Why we do not start at one medical post a week**
1. **The reviewer's time is already committed** to the launch: four framing decisions (R08 §8), the refresh pack and the trust pages all need him before L.
2. **Three of the five priority-1 posts wait on those decisions:** N3 and N4 on biopsy-timing wording, N5 on how CD138 testing is described (R08 §8.1, §8.3).
3. **The niche supports about 13 strong new URLs now** (our judgement). R08 maps 40 real questions onto 10 new posts and the existing pages (R08 §3, §5); we add 3. Mass-producing pages for query variations falls under Google's scaled content abuse policy, and R07 advises against fragmenting content into thin pages (R07 §1.1, §1.2).
4. **YMYL quality:** every medical post needs references, a dated scientific review and, for clinical claims, a named registered doctor (brief §5.7; R07 §1.3, §4.1).

#### 3.4.3 Refresh of existing pages (refresh pack, subject to client approval under D2 and D3)

Original publish dates stay. Each refreshed page gains "Reviewed on" and "Next review due" dates; dates never change without a real content change (R07 §2 implication 4). If the pre-launch review surge is not granted, R2 to R4 move to M1 (their pages launch with only the D2 minimum edits), and R5 is checked for facts by the admissions team with PP approving the wording only (§3.4.2).

| ID | Page | Current issues | Proposed refresh | Reviewer | Approval |
|---|---|---|---|---|---|
| R1 | `/diagnostic/` | No references or review line; FAQ answer "Absolutely. Our diagnostic tests are particularly beneficial…" implies every IVF patient needs testing (NMC 8.1(i), R07 §4.1); "groundbreaking", "forefront" (QC-CF §7.1) | Evidence status per test with exact guideline wording (ESHRE 2023 on chronic endometritis "can be considered"; on receptivity tests "insufficient data to recommend the routine use"; on uNK testing "not recommended"), wording chosen by the reviewers (R08 §8); "what the test can and cannot tell you"; reviewer lines; references; reframed FAQ answer; new no-figure cost FAQ; H1 | PP + VW | D2, D3 |
| R2 | ERFA post (published 7 Jun 2024) | "a patented groundbreaking … tool"; "greatly improve the chances of successful pregnancy"; no references; headings end in colons (QC-CF §7.2, §7.5; QC-SEO §4.1 item 19) | "Patent application published (No. 202431001616 A)"; remove the outcome sentence; question headings; references; named author and review line; link to N3 and N4 | PP | D2, D3 |
| R3 | Endometrial immune profiling post (28 Jul 2025) | "often leads to better outcomes"; no ESHRE status; no references (QC-CF §7.5; R08 §8.2) | Add ESHRE 2023 "uterine NK cell testing is not recommended" to the existing Limitations section (wording by the reviewers); blood vs uterine NK distinction (R08 Q22); references; review lines | PP + VW | D2, D3 |
| R4 | `/unexplained-infertility/` (1 Apr 2024) | Uncited "NIH … 92%" statistic; "Source: chat GPT, google gemini" line; colon headings (QC-CF §7.5, §7.6) | Remove the statistic or cite its primary source; replace the AI source line with real references; named author; question headings; review lines | PP + VW | D2, D3 |
| R5 | `/courses/`, both university pages, `/skill-development-training/` | "Admission Open For Session 2025-26" (QC-SEO §4.1 item 12) | Current session and dates; fees and eligibility exactly as each university states them; question-style H2s; awarding university named prominently | PP + client admissions | Client data |
| – | LIT post (21 May 2024), Hindi post (9 Jul 2024), therapy page | Therapy promotion; uncited "8–10%" and "5%"; LIT benefit claim in Hindi (QC-CF §7.3, §7.5; R08 §8.4) | Decision D1. If counsel later approves evidence-based versions: ESHRE's RPL position stated neutrally, statistics removed unless cited, no booking calls to action, Hindi version reviewed by a Hindi-fluent medical reviewer | PP + VW + counsel | D1 |

#### 3.4.4 New posts, prioritised

All NEW posts follow the blog template in 02 §4.5 (kept), the rules in §3.5 and §3.7, and the guardrails: no prices, no superlatives, no therapy promotion, no outcome promises.

| ID | NEW slug | Title tag (≤ 60) | Cluster | Audience | Questions answered (R08 §5) | Priority (R08 §1.10) | Month |
|---|---|---|---|---|---|---|---|
| N4 | `/endometrial-biopsy-for-fertility-tests/` (provisional) | Endometrial Biopsy for Fertility Tests: What to Expect (provisional) | K7 | Couples | 8, 34 | 1 | M1 |
| N9 | `/how-to-become-a-clinical-embryologist/` | How to Become a Clinical Embryologist in India | K19 | Students, parents | 35, 36, 37 | 1 | M1 |
| N3 | `/endometrial-receptivity-tests-explained/` (provisional) | Endometrial Receptivity Tests Explained \| EmbryoGenesis (provisional) | K4, K6 | Couples, doctors | 9, 10, 11 | 1 | M2 |
| N10 | `/clinical-embryology-career-and-salary-india/` | Clinical Embryologist Career and Salary in India | K18 | Students | 39 | 1 | M2 |
| N5 | `/chronic-endometritis-testing/` (provisional) | Chronic Endometritis Testing, Explained \| EmbryoGenesis (55 characters; provisional) | K8 | Couples, doctors | 15 to 20 | 1 | M3 |
| N11 | `/bsc-vs-msc-clinical-embryology/` | BSc or MSc in Clinical Embryology? The Routes Compared | K15 | Students, parents | – (K15 hub topic, R08 §3) | Added (pre-season) | M3 |
| N2 | `/recurrent-implantation-failure-tests/` | Recurrent Implantation Failure: Tests and What ESHRE Says | K3 | Doctors, couples | 2, 4 | 2 | M4 |
| N12 | `/msc-clinical-embryology-eligibility/` | MSc Clinical Embryology Eligibility: Which Degrees Qualify | K17 | Students | 38 | Added (pre-season) | M4 |
| N1 | `/ivf-failed-what-next/` | IVF Failed? What to Discuss With Your Doctor Next | K1 | Couples | 1, 3, 5 | 2 | M5 |
| N6 | `/recurrent-pregnancy-loss-tests/` | Recurrent Miscarriage: Which Tests Guidelines Support | K10 | Couples | 24 to 27 | 2 | M6 |
| N7 | `/thin-endometrium-causes-and-evaluation/` | Thin Endometrium: Causes and How Doctors Evaluate It | K11 | Couples | 28 to 31 | 2 | M7 |
| N13 | `/immunohistochemistry-endometrial-testing/` | Immunohistochemistry in Endometrial Testing, Explained | K6 (P16) | Doctors | – (prompt P16) | Added (GEO asset) | M7 |
| N8 | `/genital-tuberculosis-and-infertility/` | Genital Tuberculosis and Infertility: How It Is Tested | K12 | Couples, doctors | 32 | 3, conditional | M8 |

The N3, N4 and N5 titles and slugs are provisional until the reviewers' decisions of 28 Oct 2026 on biopsy timing and CD138 framing (R08 §8.1, §8.3). N5 uses a neutral slug and title so that the page does not pre-empt how chronic endometritis testing is described.

N11, N12 and N13 are our additions to R08's list. R08 assigns the B.Sc. vs M.Sc. comparison (K15) to the `/courses/` hub and the eligibility question (K17) to a course-page FAQ that needs client approval (R08 §3); a new post covers both without changing the client's kept course pages, and is timed before the admission season. N13 is the clinician-level source for "Are there IHC-based endometrial receptivity tests developed in India?" (R08 §6.1, P16), where no Indian source surfaced.

**Reserve list for step-up and the second wave** (each needs a G0 check that it does not compete with its parent page)

| ID | NEW slug | Topic | Parent page | R08 evidence |
|---|---|---|---|---|
| W1 | `/is-an-embryologist-a-doctor/` | Is an embryologist a doctor? | N9 | K19; Q36 (7 autocomplete variants) |
| W2 | `/non-receptive-endometrium-meaning/` | What a "non-receptive" result means | N3 | K4; Q11 |
| W3 | `/bad-obstetric-history-meaning/` | Bad obstetric history: meaning and tests | N6 | K10; Q26 |
| W4 | `/chronic-endometritis-biopsy-or-hysteroscopy/` | Chronic endometritis: biopsy or hysteroscopy? (for doctors) | N5 | K8; Q16 |
| W5 | `/embryology-internship-and-hands-on-training/` | Embryology internships and hands-on training after a BSc (existing courses only) | `/skill-development-training/` | K20; Q40 |

#### 3.4.5 12-month content calendar (prioritised)

Reviewer codes: PP, VW, Adm = client admissions team (facts), Counsel = legal counsel. "Dependency" must be cleared before gate G1.

| Month | ID | Type | Working title | Cluster | Audience | Target URL | Reviewer | Dependency |
|---|---|---|---|---|---|---|---|---|
| Phase 0 (Nov 2026) | R1 | Refresh | Diagnostic page: evidence status, references, review lines, FAQ | K4, K6, K8, K9 | Couples, doctors | `/diagnostic/` | PP + VW | D2, D3; reviewer decisions (R08 §8.1–8.3) |
| Phase 0 | R2 | Refresh | ERFA post: patent wording, references, headings | K4, K6 | Couples | ERFA post | PP | D2, D3; moves to M1 if the review surge is not granted (§3.4.2) |
| Phase 0 | R3 | Refresh | EIP post: ESHRE uNK status, references | K9 | Couples, doctors | EIP post | PP + VW | D2, D3; R08 §8.2; moves to M1 if the review surge is not granted |
| Phase 0 | R4 | Refresh | Unexplained infertility: statistic and AI source line, references | K13 | Couples | `/unexplained-infertility/` | PP + VW | D2, D3; moves to M1 if the review surge is not granted |
| Phase 0 | R5 | Update | Course and training pages: session, fees, eligibility | K15–K17, K20 | Students, parents | `/courses/`, both university pages, `/skill-development-training/` | PP + Adm | Academy facts by 30 Oct (§8.2 #15); without the surge, Adm checks the facts and PP approves the wording only |
| Phase 0 | T1 | NEW trust page | Editorial policy | E-E-A-T | All | NEW `/editorial-policy/` | PP; Counsel (AI-use wording) | D3, D8 |
| Phase 0 | T2 | NEW trust page | Clinical reviewer profile | E-E-A-T | All | NEW `/vidhu-wadhwa-profile/` | VW | Drafted only after VW's registration number and consent arrive (§8.1 #11, due 6 Nov) |
| M1 Dec 2026 | N9 | New | How to become a clinical embryologist in India | K19 | Students, parents | NEW `/how-to-become-a-clinical-embryologist/` | PP + Adm | IFS certification requirements; each university's eligibility; reviewed 1–11 Dec 2026 |
| M1 | N4 | New | Endometrial biopsy for fertility tests: what to expect | K7 | Couples | NEW `/endometrial-biopsy-for-fertility-tests/` (provisional) | PP + VW | Timing wording (R08 §8.3); VW's procedure notes; reviewed 1–11 Dec 2026 |
| M2 Jan 2027 | N3 | New | Endometrial receptivity tests explained | K4, K6 | Couples, doctors | NEW `/endometrial-receptivity-tests-explained/` (provisional) | PP + VW | ERFA method facts; R08 §8.3; ERA named only as Igenomix's test; no superiority claim |
| M2 | N10 | New | Clinical embryologist career and salary in India | K18 | Students | NEW `/clinical-embryology-career-and-salary-india/` | PP + Adm | Dated, sourced salary ranges; no placement promises |
| M3 Feb 2027 | N5 | New | Chronic endometritis testing, explained | K8 | Couples, doctors | NEW `/chronic-endometritis-testing/` (provisional) | PP + VW | **CD138 decision** (R08 §8.1) |
| M3 | N11 | New | BSc or MSc in clinical embryology: the routes compared | K15 | Students, parents | NEW `/bsc-vs-msc-clinical-embryology/` | PP + Adm | 2027–28 programme facts |
| M4 Mar 2027 | N2 | New | Recurrent implantation failure: tests and what ESHRE says | K3 | Doctors, couples | NEW `/recurrent-implantation-failure-tests/` | PP + VW | ESHRE 2023 wording verbatim, in a table |
| M4 | N12 | New | MSc Clinical Embryology eligibility | K17 | Students | NEW `/msc-clinical-embryology-eligibility/` | PP + Adm | Each university's published eligibility |
| M4 | R6 | Check | Pre-season fact check of all academy pages and N9 to N12 | K15–K19 | Students | Existing + N9–N12 | Adm | University documents |
| M5 Apr 2027 | N1 | New | IVF failed? What to discuss with your doctor next | K1 | Couples | NEW `/ivf-failed-what-next/` | PP + VW | N2, N3, N5 live; no links to held pages |
| M5 | W1 | New (reserve) | Is an embryologist a doctor? | K19 | Students, parents | NEW `/is-an-embryologist-a-doctor/` | PP + Adm | G0 check against N9 data |
| M6 May 2027 | N6 | New | Recurrent miscarriage: which tests guidelines support | K10 | Couples | NEW `/recurrent-pregnancy-loss-tests/` | PP + VW | ESHRE RPL 2022, MoHFW guideline; tests only, no therapies; no link to the LIT post |
| M6 | R7 | Re-review | 6-month review of the diagnostic page | K4–K9 | Couples, doctors | `/diagnostic/` | PP + VW | Guideline watch |
| M7 Jun 2027 | N7 | New | Thin endometrium: causes and evaluation | K11 | Couples | NEW `/thin-endometrium-causes-and-evaluation/` | PP + VW | Evidence status only; no PRP or stem cell promotion |
| M7 | N13 | New | Immunohistochemistry in endometrial testing | K6 | Doctors | NEW `/immunohistochemistry-endometrial-testing/` | PP + VW | Lab method description from the client |
| M8 Jul 2027 | N8 | New (conditional) | Genital tuberculosis and infertility: how it is tested | K12 | Couples, doctors | NEW `/genital-tuberculosis-and-infertility/` | PP + VW | Client confirms TB-PCR is offered; otherwise general education at lower priority |
| M8 | W5 | New (reserve) | Embryology internships and hands-on training | K20 | Students | NEW `/embryology-internship-and-hands-on-training/` | PP + Adm | Only courses that exist |
| M9 Aug 2027 | W2 | New (reserve) | What a "non-receptive" result means | K4 | Couples | NEW `/non-receptive-endometrium-meaning/` | PP + VW | G0 check against N3 |
| M9 | X1 | Expansion | Add sections to the 3 posts with most impressions, for questions seen in Search Console and People Also Ask | By post | By post | Existing URLs | PP (+ VW) | Search Console data |
| M10 Sep 2027 | W3 | New (reserve) | Bad obstetric history: meaning and tests | K10 | Couples | NEW `/bad-obstetric-history-meaning/` | PP + VW | G0 check against N6 |
| M10 | H1 | New (conditional) | Hindi version of N1 | K2 | Couples (Hindi) | NEW `/ivf-fail-hone-ke-baad-kya-kare/` | Hindi-fluent medical reviewer + PP | Client lifts "English only"; D1 outcome for the existing Hindi post; hreflang pair with N1 |
| M10 | R8a | Refresh | Academy refresh for the 2028 cycle: course and training pages | K15–K17, K20 | Students, parents | `/courses/`, both university pages, `/skill-development-training/` | PP + Adm | New university data |
| M11 Oct 2027 | R8b | Refresh | Academy refresh for the 2028 cycle: posts N9 to N12 | K15, K17–K19 | Students | N9–N12 | PP + Adm | New university and salary data |
| M12 Nov 2027 | W4 | New (reserve) | Chronic endometritis: biopsy or hysteroscopy? | K8 | Doctors | NEW `/chronic-endometritis-biopsy-or-hysteroscopy/` | PP + VW | G0 check against N5 |
| M12 | R9 | Re-review | 12-month review of N4 and N9; annual content audit; year-2 plan | All | – | N4, N9 | PP + VW | – |
| M12 | R10 | Re-review | 12-month review of the diagnostic page (6 months after R7) | K4–K9 | Couples, doctors | `/diagnostic/` | PP + VW | Guideline watch |

The 12-month re-reviews of R2 to R4 fall in M13 (December 2027, 12 months after the refreshed pages go live) and open the year-2 plan.

**Totals:** about 19 new posts in 12 months including reserve and conditional posts (13 core posts, N1 to N13, with N8 conditional; up to 5 reserve posts, W1 to W5; and 1 conditional Hindi post, H1), or about 1.6 a month on average; 18 without H1 (1.5 a month). The cadence is 2 new posts a month until April 2027 (M1 to M5), then 1 to 2 a month; M11 has none, because its review time goes to the academy refresh (R8b). Alongside them run 11 refresh, check or re-review items (R1 to R10, with R8 split into R8a and R8b), the trust pages T1 and T2 and the expansion X1. A step-up adds reserve or data-led topics, never more than one new post a week.

| New posts | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Count | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 (incl. H1, conditional) | 0 | 1 | 19 (18 without H1) |

**QC check for pillar 3.4:** every item passes gates G0 to G6 (§5); the content tracker shows the review date and the next review due date for every medical page; the quarterly content audit confirms no two URLs compete for the same main query.

### 3.5 AEO (answer engines)

**Objective:** make each target page the clearest direct answer to the real questions in R08 §5, so it can be shown in People Also Ask, featured answers and AI answers, without fragmenting the site into thin pages.

**Question bank usage.** Each of the 40 questions in R08 §5 has one main target URL. Where the table names a second page (questions 10, 20, 35 to 38 and 40), that page gives only a short answer and links to the main one; all other pages link to it.

| Target URL | Questions (R08 §5) | When |
|---|---|---|
| NEW N1 `/ivf-failed-what-next/` | 1, 3, 5 | M5 |
| NEW N2 `/recurrent-implantation-failure-tests/` | 2, 4 | M4 |
| NEW N3 `/endometrial-receptivity-tests-explained/` (provisional) | 9, 10, 11 | M2 |
| `/diagnostic/` | 10, 12, 13, 14 (no figures), 20 | Refresh R1 (approval) |
| ERFA post | 7 | Refresh R2 |
| NEW N4 `/endometrial-biopsy-for-fertility-tests/` (provisional) | 8, 34 | M1 |
| NEW N5 `/chronic-endometritis-testing/` (provisional) | 15 to 20 | M3 |
| EIP post | 21, 22, 23 | Refresh R3 |
| NEW N6 `/recurrent-pregnancy-loss-tests/` | 24 to 27 (27 answered in English) | M6 |
| NEW N7 `/thin-endometrium-causes-and-evaluation/` | 28 to 31 (31 answered in English) | M7 |
| NEW N8 `/genital-tuberculosis-and-infertility/` | 32 | M8 (conditional) |
| `/unexplained-infertility/` | 33 | Refresh R4 |
| Hindi post | 6 | Held (D1) |
| NEW N9 and `/courses/` | 35, 36, 37 | M1 |
| Course pages and NEW N12 | 38 | M4 |
| NEW N10 | 39 | M2 |
| `/skill-development-training/` (and W5) | 40 | Existing; W5 in M8 |

**Answer-first rules** (from 02 §4.5 and §8.1, updated with R07 §1.2 and §2)
1. Each question becomes an H2 or H3 written the way people ask it.
2. The first sentence answers it directly. The answer block is 40 to 60 words and self-contained: it names the subject ("ERFA – The Soil Test is…"), not "it". Bing recommends self-contained one- or two-sentence answers (R07 §1.2, M3).
3. Clinical answers name the source and year in the text and quote guideline wording exactly ("ESHRE (2023) states that…").
4. Numbers appear only with a named, dated source (R07 §2 implication 4).
5. Clinical answers end with the doctor pathway where relevant ("Your doctor decides whether this test is right for you").
6. Comparisons go in tables (test, what it measures, sample, timing, turnaround, evidence status).
7. Key answers are in visible HTML text, not only in images, PDFs, tabs or collapsed panels (R07 §1.2, M3). Accordions are for secondary FAQs.
8. No "best", "only" or "first" in any answer (R07 §4.1, clause 8.1(ix); 04 §5.1).

**FAQ policy after the 2026 rich-result change**
- FAQ rich results stopped showing for every site on 7 May 2026, and HowTo and Course info results are gone too (R07 §1.2).
- FAQ sections stay where they help readers. FAQPage markup is optional: keep it only where a visible FAQ exists and matches word for word, and never repeat the same FAQ on two URLs (R07 §1 implication 3, §6.1).
- FAQs on existing pages are old content, so adding questions there needs client approval (R08 §3).

**People Also Ask and featured answers.** These cannot be observed by script (R08 §0). The QA analyst checks the 22 cluster head terms monthly and all 40 questions quarterly in Google India, incognito, and records the questions shown, whether an AI Overview appears and which domains it cites (R08 §6.2, step 5). An "AEO win" is defined in Appendix A.

**Video answers.** YouTube is the most-cited domain in AI Overviews (R07 §1.1, R3 vendor study). For five questions we add a 60- to 120-second answer video by a named, qualified person, with the transcript on the target page and VideoObject markup: Q8 (biopsy: what happens, does it hurt), Q7 (endometrial receptivity), Q10 (how receptivity tests differ), Q24 (when testing starts after miscarriages) and Q36 (is an embryologist a doctor). Rules in §3.9.

**Hinglish and Hindi (later, with approval).** Hindi and Hinglish queries currently return English foreign pages; no Hindi page surfaced, including EmbryoGenesis's own (R08 §2.1, K2). This is a real gap, but the site is English-only by decision. Conditions for a Hindi phase: the client lifts "English only"; a Hindi-fluent medical reviewer is appointed; D1 is resolved for the existing Hindi post; reciprocal hreflang pairs; no unreviewed machine translation (02 §3.4). First candidates: Hindi N1 (K2), then "bar bar miscarriage" (K10) and "bachedani ki parat patli" (K11) topics.

**QC check for pillar 3.5:** gate G2 checks question headings, answer length and visible answers; the quarterly AEO check reports wins against the 40-question bank.

### 3.6 GEO (generative engines and AI assistants)

**Objective:** be mentioned, correctly, when people ask AI assistants about endometrial testing, IVF failure and embryology careers in India, and fix wrong facts at their source.

**Principle:** for Google, AI search is still Google SEO. Google says AI Overviews and AI Mode use its core ranking and quality systems, and that llms.txt, "chunking", AI-specific rewrites and extra markup are not needed (R07 §0 item 1, §1.1). There is no separate GEO budget for Google. The GEO work below targets the other assistants and the off-site signals all of them read.

#### 3.6.1 What the evidence says gets cited

| Finding | Strength | Source |
|---|---|---|
| Branded web mentions had the strongest correlation with brand visibility in AI Overviews (0.664). Only domains with DR above 40 were studied, so this may not hold for small brands | Vendor study, correlation | R07 §2.2 (R4) |
| YouTube is the most-cited domain in AI Overviews; in German health queries it was the top cited domain | Vendor studies | R07 §1.1 (R3, R8) |
| Adding quotations, statistics and cited sources raised visibility by about 40% in a lab pipeline; keyword stuffing did worse | Peer-reviewed, experimental, dated | R07 §2.2 (R1) |
| AI assistants such as ChatGPT cited newer pages than organic results did; Google AI Overviews cited slightly older ones | Vendor study, correlation | R07 §2.2 (R5) |
| Health answers in one engine came mostly from established institutions; proposed "authority signals" are author credentials, institutional affiliation, quality assurance and digital authority | Academic preprint | R07 §2.2 (R9) |
| AI answers rarely repeat; visibility % across runs is more stable than lists or order | Vendor-partnered study | R07 §2.2 (R11) |
| Only 37.9% of URLs cited in AI Overviews ranked in the top 10 for the same query; likely cited for sub-questions | Vendor study | R07 §1.1 (R3) |
| Microsoft advises clear, self-contained sections, tables, claims backed by data, fresh content notified by IndexNow, consistent entities and Bing Places | First-party guidance | R07 §2.5 (M1, M3) |

#### 3.6.2 GEO actions

| # | Action | Why | Owner | When | QC check |
|---|---|---|---|---|---|
| 1 | Third-party mentions: universities, ITHS, INNR, IFS, conference programmes, journals and earned press, each using the standard one-line description | Mentions correlate most with AI visibility (R07 §2.2); entity corroboration is the gap (R07 §0 item 4) | Client + TechnoTaau (§3.8) | Phase 0 to M12 | Mentions log |
| 2 | YouTube explainers with transcripts on the matching page | Most-cited domain (R07 §1.1) | TechnoTaau video (§3.9) | From M2 | Videos live and embedded |
| 3 | Entity consistency: master NAP, naming rules, `sameAs`, boilerplate | Microsoft guidance (R07 §2.5); brand collision (R08 §1.6) | TechnoTaau | Phase 0, then monthly | NAP spot check |
| 4 | Citable facts on our pages: key-facts lists (sample, timing, turnaround), evidence-status tables with exact ESHRE wording, patent application numbers and dates, references | R07 §2.2 (R1, R9); R07 §1.2 (M3) | Content team | Every page | G1 and G2 |
| 5 | **Publish ERFA validation data** in an indexed journal | The single strongest AI-citation and E-E-A-T asset; the AI proxy summarised ERFA as having "no independent evaluation" (R08 §6.1 P6, §7) | PP | Submission target M6 (E) | Submission record |
| 6 | Freshness through real reviews, not date changes | R07 §2.2 (R5); R07 §2 implication 4 | Content team | Review cycle | Review log |
| 7 | Bing Webmaster Tools, IndexNow and the AI Performance report every month | First-party Copilot citation data (R07 §2.5) | TechnoTaau SEO lead | From L | Monthly report block |
| 8 | Keep every search and answer crawler allowed | Blocking OAI-SearchBot removes the site from ChatGPT search answers; blocking Google-Extended also blocks Gemini app grounding (R07 §2.4, §2 implication 1) | Developer | L | robots.txt check |
| 9 | llms.txt: low priority hygiene. Keep it only as an exact, reviewed subset of on-site facts (therapy lines removed 17 Oct 2026); regenerate when facts change | Google does not use it; 97% of llms.txt files got no requests in Ahrefs' study; no other lab has said it reads the file **[UNVERIFIED]** (R07 §2.3) | TechnoTaau | 30 Oct 2026, then on change | Diff against the master record |
| 10 | Wikidata items (org and founder) | Low-cost hygiene; benefit **[UNVERIFIED]** (R07 §2.2) | TechnoTaau | M2–M3 | Items live |

**What we will not do:** Wikipedia articles (notability not met), Reddit or Quora seeding, paid "best lab" list placements, AI-specific rewrites or thin "chunked" pages. Named experts may answer clinical questions in public forums under their real names, with the affiliation disclosed and without self-promotion (R07 §1.1, §2.2, §2 implications 3 and 7).

#### 3.6.3 Monthly AI prompt panel

**Prompts:** the 25 prompts in R08 §6.1, pasted exactly (summary in Appendix C). P2 is run in Hinglish and in Devanagari (R08 §6.2).

**Method** (R07 §3.2 method fix, applied to R08's panel)
1. Surfaces, minimum four: ChatGPT (search on), Google AI Mode, Perplexity and Microsoft Copilot. Also record AI Overviews when they trigger, and Gemini when time allows.
2. **Three runs per prompt per surface**, each in a fresh logged-out session or clean account, located in India (Chandigarh or Mohali if possible), a new chat every time.
3. **Surface hit:** EmbryoGenesis is mentioned or cited in at least **2 of 3** runs.
4. **Prompt visible:** a surface hit on at least **2 surfaces**.
5. **Panel score:** visible prompts out of 25. P5 (test cost) is monitor-only by design, and P22 and P23 depend on product decisions, so 22 is the realistic maximum.
6. Record per run: mentioned (Y/N); URL cited; where the mention sits; facts correct, wrong or outdated (name, Mohali, tests, "patent application published", founder's qualifications); compliance problems (for example "patented", "best", stem cell therapy listed); competitors named; top 3 cited domains; screenshot (R07 §3.2; R08 §6.2).
7. Effort: 25 × 4 × 3 = 300 runs, about 6 hours a month for one person (E, scaled from R07 §3.2).
8. Run in the first working week of each month. Prompts stay fixed within a quarter so trends stay comparable.

**Expected order of wins (E):** brand and navigational prompts first (P24, P25, P6), then the academy primary-source prompts (P18, P19) and the local prompt (P12, through the Business Profile), then niche clinician prompts (P14, P16). Category and patient prompts (P1, P3, P4, P8 to P11) are slow because chains, YouTube and medical literature dominate them (R07 §3 implication 4; R08 §6.1).

#### 3.6.4 How wrong AI answers get corrected
1. **Log** the error with screenshot, surface, prompt and date.
2. **Classify:** S1 safety or compliance (says EmbryoGenesis offers stem cell therapy, calls a test "patented" or "best", presents the founder as a medical doctor, attributes medical advice to us); S2 wrong facts (address, phone, tests, programmes); S3 omission or confusion with the biology term or another person.
3. **Trace** the URL the assistant cited: our page, a third-party page, or none.
4. **Fix at source:** our page wording, key facts, schema or llms.txt; or the third-party owner (ITHS, a university, an aggregator, a directory, Wikidata).
5. **Request recrawl:** Search Console URL inspection; IndexNow for Bing. Use the assistant's own feedback option where it has one.
6. **Recheck** in the next panel run. Close when the error is gone in 2 of 3 runs.
7. **Deadlines:** S1 within 7 days; S2 within 30 days (R07 §3.3); S3 at the next quarterly entity review. Incident playbook I2 in §5.5.

**QC check for pillar 3.6:** AI-panel QC (§5.4); the "AI visibility" block in every monthly report (R07 §3 implication 3).

### 3.7 E-E-A-T, YMYL and compliance

**Objective:** meet Google's standard for "Your Money or Your Life" health content, where trust is the most important part of E-E-A-T (R07 §1.3, G9), and India's medical-advertising rules, which treat promotional search-engine and AI-assisted communication as advertising (R07 §4.1, clause 3.2). Whether the NMC guidelines formally cover a standalone diagnostic lab is **[VERIFY with counsel]**; we treat them as binding on everything EmbryoGenesis publishes (R07 §4.1, §6.2 item 9).

#### 3.7.1 Pre-launch legal decision on therapy content (D1)

**In scope:** `/advanced-fertility-therapies/`; the LIT post `/exploring-lit-therapy-treatment-for-recurrent-pregnancy-loss/`; the Hindi post `/tips-and-treatments-for-pregnancy-after-ivf-failure/`; the therapy cards and "Book Now" therapy links on the home page; the therapy line on `/diagnostic/`; the "Therapeutic" item in the header and footer; the builder-added "Personalized therapy" care-pathway step on the home page; the builder-added therapy links in the "Related at EmbryoGenesis" boxes; the therapy mentions and links our builders added or placed on `/about/` (the answer-box sentence naming "therapeutic services" and the "Explore our … therapeutic services" link), `/contact-us/` (the "ask about therapies" link), `/blog/` (the LIT and Hindi post cards and the sidebar "Therapeutic" link) and the 404 page (the "Therapeutic" link); the therapy option in forms; and the four therapy-related lab-training modules (PRP & LIT; LIT & molecular hydrogen; molecular hydrogen in health management; stem cell processing & cryopreservation).

**Why a decision is needed before launch**
- The NMC advisory of 5 Sep 2026: promoting stem cell therapy beyond approved indications is professional misconduct (R07 §4.2).
- NMC clause 8.1(vi): no promotion of unproven therapies; clause 8.1(iii): no success rates; penalties fall personally on the registered doctor named on the content (R07 §4.1).
- The Drugs and Magic Remedies Act covers products or kits claimed to treat "sterility in women" (R07 §4.5).
- Google's YMYL standard is strictest on unproven treatments, and these pages are what AI assistants could quote for recurrent miscarriage in Hindi (R07 §1 implication 6; R08 §1.5).
- ESHRE's 2022 RPL guideline recommends against LIT for unexplained RPL; the Hindi post says LIT increases the chance of conception (R08 §8.4).

| Option | What happens | Search and AI exposure | Legal exposure | Effort and timing | Our view |
|---|---|---|---|---|---|
| 0. Keep as is (the client's current decision) | Pages stay live and indexed | Highest; AI assistants can quote them | Highest | None | **Not recommended** |
| A. Edit to evidence-based wording before launch | Counsel, PP and VW rewrite: stem cell content removed entirely; benefit, safety and outcome claims removed; guideline positions stated neutrally; no "Book Now" | Lower, and accurate | Lower, if counsel approves | 2 to 4 weeks; must finish by code freeze (27 Nov 2026) | Good end state, but **unlikely before launch** |
| B. Noindex | Pages stay public but leave Google's index and AI features (AI features need an indexed page, R07 §1.1, G1). Out of sitemap and llms.txt. No first-party statement for other engines | Lower on Google | **Still public advertising** under NMC clause 3.2 (R07 §4.1) | Hours | **Fallback only**, and only together with removing the stem cell content and the outcome and safety claims |
| C. Unpublish until reviewed | WordPress draft. The URLs return 404 (not redirected to unrelated pages). Navigation, home cards, form option, related links, sitemap, schema and llms.txt cleaned. Text kept for counsel | None | Lowest | Hours | **Recommended now** |

**Our recommendation**
1. **Before launch: Option C** for the therapy page, the LIT post and the Hindi post, with the clean-up listed above. Hold the four therapy-related training modules from public listing until counsel clears them; keep the four lab-technique modules (biochemistry, molecular genetics and bioinformatics, tissue processing and microtomy, immunohistochemistry).
2. **Then Option A, fast-tracked:** counsel, PP and VW agree evidence-based descriptions of LIT, PBMC, PRP and molecular hydrogen. Republish at the same URLs when approved (target M2 to M3, E), still without SEO, link building or social promotion while the hold applies.
3. **Stem cell therapy never returns as a service page** (brief guardrail 4; R07 §4.2).
4. **Revenue note:** therapy enquiries that start on the website may fall while the page is offline. Doctors still refer patients directly; the contact form keeps a neutral "Other enquiry" option; the enquiry log records therapy enquiries (KPI B4, no target).

#### 3.7.2 Compliance minimum in the kept content (D2)

These are the client's own words, kept under brief section 0. Each item conflicts with the NMC guidelines or the brief's guardrails. We supply exact replacement text from the claims dictionary (04 §5.1); the client approves.

| # | Item (location) | Problem | Basis |
|---|---|---|---|
| 1 | "As the best fertility centre, we believe…" (footer, every page) | Superlative on 19 pages | NMC 8.1(ix); brief guardrail 1 (R07 §4.1) |
| 2 | "best fertility diagnostic centre in India", "the leading force", "a leader in…" (About; BSc page) | Superlatives and leadership claims | NMC 8.1(iii), (ix) |
| 3 | "India's trusted infertility diagnostic and research center", "Leaders in Fertility Diagnostics and Research", "Learn from top experts" (home; courses) | Superlatives | NMC 8.1(ix) |
| 4 | "Patented diagnostic test" (home), "(Patented)/(Patent)" (About road map), "a patented groundbreaking…" (ERFA post), "patented technologies" (Rayat Bahra page), "14 patent" and "Patent No." (profile) | Patent applications described as patents | Brief guardrail 2 |
| 5 | "Real Stories, Real Smiles: Our Patients Speak", "Testimonials" and the "Read our reviews on Google" button (home) | Patient reviews used for promotion | NMC 6.2, 8.1(v), Explanation V (R07 §4.1); brief guardrail 6 |
| 6 | "NIH … 92%" (Unexplained post); "8–10%" and "5%" (LIT post, under D1) | Uncited statistics | R07 §2 implication 4; brief guardrail 3 (evidence honesty) |
| 7 | "Source: chat GPT, google gemini" (Unexplained post) | AI tools given as the source on a medical page; Google says AI-assisted content must be fact-checked and automation disclosed where readers would ask (R07 §1.3, G9 and G10) | R07 §1.3; §3.7.6 below |
| 8 | "improve IVF success" (home ERFA card), "greatly improve the chances of successful pregnancy" (ERFA post), "often leads to better outcomes" (EIP post), "Absolutely. Our diagnostic tests are particularly beneficial…" (diagnostic FAQ) | Outcome claims; implying every IVF patient needs testing | NMC 8.1(i), (iii) (R07 §4.1) |
| 9 (recommended, not minimum) | "groundbreaking", "forefront", "world-class", "globally renowned", "top fertility clinics" | Hype that needs substantiation | ASCI (R07 §4.6); 04 §5.1 |

#### 3.7.3 Trust elements on every medical page

| Element | Specification | Basis |
|---|---|---|
| Byline | "Written by [real person, role]". Drafting support by TechnoTaau Team is disclosed in the editorial policy. No invented authors or AI headshots | R07 §1.3 (G9: bylines; fabricated creator profiles are deception) |
| Scientific review line | "Scientifically reviewed by Prof. (Dr.) Pulakes Purkait, M.Sc., Ph.D., Founder & Director (reproductive scientist) · Reviewed on [date] · Next review due [date]" (04 §5.4) | Brief guardrail 7 |
| Clinical review line | "Clinically reviewed by Dr. Vidhu Wadhwa, MBBS, MD (Pathology), [SMC/NMR] Reg. No. [number]" on pages with clinical claims | Brief guardrail 7; NMC Explanations III–IV (R07 §4.1, §4 implication 5) |
| References | Numbered, linked, primary sources first (ESHRE, PubMed Central, MoHFW guideline, IFS), with dates | R07 §2 implication 4; R07 §2.2 (R1, R9) |
| Evidence box | "What the evidence says ([Month YYYY])" with exact guideline wording (04 §5.3) | Brief guardrail 3 |
| Disclaimer | The full medical disclaimer in 04 §5.2; the short version on cards | Brief guardrail 7 |
| Dates | Published, Reviewed on, Next review due. Changed only with real changes | R07 §2 implication 4 |
| Structured data | MedicalWebPage or BlogPosting with `reviewedBy`, `lastReviewed` and `citation` only when visible on the page | QC-SEO §4.1 item 23; R07 §1.2 |

#### 3.7.4 Author and reviewer pages

| Page | Status | Contents |
|---|---|---|
| `/pulakes-purkait-profile/` | Exists | Approved founder bio (04 §6), "reproductive scientist; not a medical practitioner", ORCID, Scholar, publications, awards by exact name, issuer and date, patent applications with numbers |
| NEW `/vidhu-wadhwa-profile/` | Proposed (title tag: "Dr. Vidhu Wadhwa, MD (Pathology) \| EmbryoGenesis, Mohali", 56) | Qualifications, registration status and number, role (Consultant Pathologist & Quality Manager), reviewer role. A website doctor directory with registration details is patient information, not advertising (NMC 9.1). NMC 9.2 bars RMP photos used as self-advertisement; in our reading a plain directory photo is not self-promotion (R07 §4.1). Needs VW's consent |
| Other authors (for example Dr. Meenu Bhanot for academy posts) | Optional | Same pattern, only if they author content |

The slugs follow the existing `/pulakes-purkait-profile/` pattern.

#### 3.7.5 Editorial policy page (NEW `/editorial-policy/`)

Linked from every review line. Contents: who writes and who reviews (scientific and clinical); how sources are chosen (guidelines first); the review cycle (test page every 6 months, articles every 12 months, sooner when guidelines change; 04 §5.4); the corrections policy and contact; how AI tools are used and checked (D8); conflict of interest (EmbryoGenesis offers some of the tests it writes about); no sponsored content; the full medical disclaimer.

#### 3.7.6 AI use (D8)
- **Rule (lead decision):** AI-generated content is published only with legal sign-off and labelling.
- **NMC clause 7.2:** an "AI Generated promotional campaign for furtherance of commercial interest is prohibited"; permitted AI content must carry a source mark; no synthetic patients, doctors or endorsements. The clause pairs a prohibition with labelled permission, so its reach is **[VERIFY with counsel]** (R07 §4.1).
- **Google:** AI-assisted content must meet Search Essentials and the spam policies and must be fact-checked, including titles, meta descriptions, structured data and alt text (R07 §1.3, G10).
- **ASCI guidelines on synthetic content in advertising** apply from 29 Dec 2026 **[SECONDARY]**; the IT Rules amendment on synthetic labelling is in force from 20 Feb 2026 **[SECONDARY]** (R07 §4.6).
- **Until counsel decides:** every published sentence is written or rewritten by a named person and fact-checked against sources; AI tools may help with research and outlines; no AI images on medical pages unless labelled "AI-generated illustration" (04 §5.5); no AI reels until sign-off (§3.9). Counsel confirms whether AI-assisted drafting that is rewritten and expert-reviewed counts as "AI-generated content", and approves the disclosure wording for the editorial policy.

#### 3.7.7 Must and must not (condensed from R07 §4 checklist)

| Topic | Must | Must not |
|---|---|---|
| Test pages | What the test is, who orders it, sample, timing, turnaround, limits, references, "ordered and interpreted by your doctor" | Superiority claims, accuracy percentages, outcome or pregnancy promises, "only in India" |
| Superlatives | – | best, No. 1, leading, top, most trusted, unmatched, revolutionary, miracle, cure, 100%, painless |
| Awards | Exact name, issuer and date | Implying an award covers test accuracy or the whole lab |
| Patents | "Patent application published (No. …)" | "Patented" |
| Patient stories | Anonymised, journal-style case reports only | Testimonials, success stories, before/after, patient videos, even with consent |
| Reviews | Let them arrive; reply politely without confirming patient status | Incentives, gating, staff or partner reviews, bought engagement |
| RMP identity | Name, qualifications, registration on clinical electronic posts; directory with registration details | RMP photos as self-promotion; RMP endorsing products |
| AI media | Educational, labelled, legal sign-off | AI promotional campaigns; synthetic doctors, patients, testimonials or outcomes |
| Therapies | Held | Stem cell promotion; unproven therapy promotion; ads; therapy facts in llms.txt or schema |
| Necessity and fear | Evidence-graded indications ("may be discussed with your doctor if…") | Fear-based copy; implying every IVF patient needs testing; discounts, free tests, camps |
| Referral economics | Counsel-approved partner terms | Commission, referral or lead fees for patients **or specimens** [VERIFY with counsel] |
| Sex selection | – | Any reference in any language |
| Products and kits | – | Claims that a product treats or cures infertility, impotence or miscarriage |
| Education | Degree-awarding university named prominently; placement or salary only with latest-year evidence | "100% placement", unsupported salary claims |
| Data | Itemised notice, unticked consent, withdrawal, parental consent for minors | Health data in ad pixels; personalised ads or tracking aimed at under-18s; identifiable patient data |

#### 3.7.8 Proposed additions to the brief (for client approval; not changed by this plan)
Research 07 proposes four additions to brief section 5: (a) the RMP's name, qualifications and registration number on clinical posts; (b) no AI promotional campaigns, AI content labelled, no synthetic people; (c) no fear-based or "unnecessary diagnostics" framing and no discounts; (d) counsel review of partner economics under clause 8.1(vii). It also proposes extending guardrail 9 with NMC clause 7.2 and the ASCI synthetic-content guidelines (R07 §4 implication 1, §6.1). We recommend the client approves them with D2.

**QC check for pillar 3.7:** gate G4 on every page and post; the monthly compliance scan of new and changed pages; zero compliance incidents (KPI C1).

### 3.8 Off-page and digital PR

**Objective:** earn factual mentions and links from institutions that already trust EmbryoGenesis, because corroboration of the brand, not markup, is the gap (R07 §0 item 4).

**Principles** (02 §10.1 kept, updated)
- Earned, never bought. No paid links, link schemes, PBNs, link exchanges, mass guest posts, paid "best lab" lists or paid "brand stories" presented as news (NMC 8.1(ix), (xi), (xii); R07 §2 implication 3). Any sponsorship link must be marked `rel="sponsored"` or nofollow.
- Every mention uses the standard description (04 §6) and links to the most relevant deep page.
- Paid advertorials on news or university sites also touch Google's site reputation abuse policy (R07 §1.3).
- **Partner hospitals and collection centres:** no partner-facing copy, outreach or "become a collection centre" content until counsel reviews NMC clause 8.1(vii) (lead decision; R07 §0 item 7). Any later mention by a partner must be factual and disclose the relationship (R07 §4.1, 8.1(xi)). GIOSTAR is excluded until counsel gives a view (brief §2).

| Target | Ask | Link target | Timing | Owner |
|---|---|---|---|---|
| ITHS (translationalhealthscience.in) | "Patent applications published" instead of "15+ patents"; link to embryogenesis.in (R08 §7) | `/`, `/pulakes-purkait-profile/` | Phase 0 | Client (group site) |
| Rayat Bahra University | Name EmbryoGenesis and ITHS's role on the programme pages; link; correct aggregator facts (R08 §7; R07 §5.4) | `/art-and-clinical-embryology-in-rayat-bahra-university/` | M1–M2 | Client asks; TechnoTaau drafts |
| Bahra University (bushimla.in) | Restore a programme page that names EmbryoGenesis (R08 §7) | `/bsc-in-clinical-embryology-in-bahra-university/` | M1–M2 | Client; TechnoTaau drafts |
| INNR (nutrigenetics.in) | Consistent founder description; link | `/pulakes-purkait-profile/` | M2 | Client |
| Guru Ghasidas Vishwavidyalaya (MoU Nov 2024) | Factual MoU mention with link | `/media-event/` | M3 | Client |
| PJ Embryogenesis Health & Education Foundation | Link, if it has a website | `/about/` | M3 | Client |
| Indian Fertility Society | Membership listing (IFS-2900) with the standard name (R07 §5.2) | `/` | M2 | Client |
| ISAR, IFS and ACE meetings | Abstracts and posters (methods, turnaround logistics, education); check 2027 deadlines | Programme pages naming the speaker and EmbryoGenesis | M2–M6 | PP |
| Indian indexed journals (02 §10.2) | **ERFA validation data**; methods papers. Affiliation "EmbryoGenesis, Mohali, India" | Journal, PubMed, Scholar | Submission target M6 (E) | PP |
| Trade press: BioSpectrum, Medical Dialogues, ET HealthWorld, Express Healthcare (02 §10.2; R08 §7) | Earned stories only when there is news: a publication, a programme launch, an MoU; evidence-based expert comment. Never therapy angles | Relevant deep page | When news exists, from M2 | TechnoTaau |
| Regional press (Chandigarh, Himachal) | Academy and programme news | `/courses/` and the course pages | Admission season M5–M9 | TechnoTaau |
| Aggregators (Careers360, Shiksha, Collegedunia, Zollege, CollegeSearch, ivf.net) | Correct fees, durations and the founder's spelling, through the universities (R07 §5.4; R08 §4, §7) | Course pages | M2–M3 | TechnoTaau + client |
| Journalist-request platforms | Evidence-based quotes in Prof. Purkait's own name (02 §10.2) | Profile | Ongoing, about 2 a month | TechnoTaau |

**Linkable assets:** N2's ESHRE investigations table; N10's dated salary sources table (updated yearly); N4's biopsy explainer; N13's method explainer; the ERFA validation paper.

**QC check for pillar 3.8:** a mentions-and-links log reviewed monthly; quarterly link audit; every outreach text passes G4.

### 3.9 Video and social for search

**Objective:** use YouTube as a search and AI-citation surface, and use social channels to build branded demand and mentions, within the AI and medical-advertising rules.

| # | Action | Rule or reason | Owner | When |
|---|---|---|---|---|
| 1 | Claim and align the YouTube channel (`@Embryo-Genesis`): name, description with the standard boilerplate, link to the site; keep it in `sameAs` | Channel did not surface in search (R08 §7); entity consistency | TechnoTaau + client | M1 |
| 2 | Educational answer videos (60 to 120 seconds; longer explainers later) for N4, N3, N5, N9 and N10 and the five questions in §3.5, by named, qualified staff, filmed in the lab with real footage | YouTube is the most-cited domain in AI Overviews (R07 §1.1); video by named qualified staff with transcripts is the main new format worth considering (R07 §1 implication 5) | TechnoTaau video; PP, VW on camera | From M2, one per month (E) |
| 3 | Transcript on the matching page, VideoObject markup, click-to-load player | Video is still a supported rich result (R07 §1.2); CWV (02 §5.2) | Content team; developer | With each video |
| 4 | Clinical videos and posts carry the RMP credential line (name, qualifications, registration number) | NMC Explanations III–IV (R07 §4.1) | TechnoTaau | Every clinical item |
| 5 | Education must not promote personal practice; RMP photos not used as self-advertisement | NMC 5.1, 9.2 (R07 §2.2, §4.1) | TechnoTaau | Always |
| 6 | YouTube health source features for registered healthcare professionals in India: Dr. Wadhwa may apply once eligible. India thresholds **[UNVERIFIED]** | R07 §2.2 (G21) | VW; TechnoTaau | M6 review |
| 7 | **AI-produced reels** (03 §4): educational only, labelled "AI-generated visuals", no synthetic doctors, patients or outcomes, no therapy topics, **legal sign-off before the first reel**, plus the RMP credential line on clinical reels (an update to 03 §4.1's end card, which names only Prof. Purkait) | NMC 7.2 [VERIFY with counsel]; ASCI synthetic-content guidelines from 29 Dec 2026 [SECONDARY]; IT Rules labelling [SECONDARY] (R07 §0 item 6, §4.1, §4.6) | TechnoTaau social; counsel | After D8 |
| 8 | Every social post and video description links to the matching page; consistent naming | Branded mentions correlate with AI visibility (R07 §2.2, R4) | TechnoTaau social | Ongoing |
| 9 | Re-align `03-social-media-strategy.md` to this plan. Its status note of 17 Oct 2026 pauses the AI reels and all partner-facing posts and outreach until D8 and counsel's view on NMC clause 8.1(vii); non-AI educational posts continue through G4. Its partner-recruitment goals and "Become a collection partner" calls to action are superseded by the client's decision | Lead decision; brief §0; §4.2 item 2 | TechnoTaau social (JS accountable) | Pause from 19 Oct 2026; 03 §7 calendar re-issued after 13 Nov 2026 |

**QC check for pillar 3.9:** the reel QC checklist in 03 §4.7 plus gate G4; a video log showing the review date, the RMP line, the AI label (if any) and the page it supports.

---

## 4. Roadmap and the next 30 days

### 4.1 Phases

| Phase | Window (indicative) | Deliverables | Owner | Exit criteria |
|---|---|---|---|---|
| **0. Pre-launch** | Now to L (17 Oct to about 8 Dec 2026) | Decisions D1 to D8; pause of AI reels and partner-facing posts (§4.2 item 2); live-site quick fixes; real AI-panel baseline and SERP checks; Keyword Planner volumes; reviewer decision session; WordPress SEO handover pack v1 (30 Oct) and v2 (11 Nov); reference-build fixes in our remit; GBP ownership; master NAP record; privacy policy and consent; the D2 replacement text, refresh pack R1 to R5 and trust pages T1 and T2 reviewed during the review surge of 9 to 27 Nov. Fallback without the surge: only the minimum set (D2 text, R1, T1, T2 and the R5 facts) is reviewed before launch, and R2 to R4 move to M1 (§3.4.2). N9 and N4 drafted for review from 1 to 11 Dec; two staging QA passes (16 and 25 Nov); code and content freeze 27 Nov; go/no-go 4 Dec | JS (coordination); client (decisions); developer (build); TechnoTaau (spec, QA, content) | D1 to D8 in writing and implemented on staging; NAP confirmed; privacy policy and forms approved by counsel; the agreed pre-launch review set signed off; redirect test passes; schema validator 0 errors; PageSpeed within budget on 5 templates; GA4 fires nothing before consent; go/no-go signed |
| **1. Launch month** | M1 (Dec 2026) | Go-live runbook; Search Console and Bing submissions; Bing Places; GBP live; 48-hour and 7-day checks; N9 and N4 reviewed 1 to 11 Dec and published from week 2; R2 to R4 if they moved from Phase 0; 404 monitoring; NAP clean-up starts; first monthly report | Developer; TechnoTaau | Runbook complete; no critical errors in Search Console or Bing; GBP verified; at least 80% of sitemap URLs indexed by L+30 (E); re-baseline done and new targets approved |
| **2. Foundation** | M2–M3 (Jan–Feb 2027) | N3, N10, N5, N11; university and ITHS fixes; directories; Wikidata; ORCID and Scholar; course pages ready for 2027–28; first videos; monthly panel; quarterly deep audit at the end of M3 | TechnoTaau; client; PP | 3-month KPIs at or above floor, or a corrective plan agreed; at least 2 of 4 institutional pages corrected and linking; step-up decision recorded |
| **3. Growth and admission season** | M4–M6 (Mar–May 2027) | N2, N12, N1, W1, N6; pre-season academy check (R6); regional academy PR; ERFA paper submission target; DPDP readiness check before mid-May 2027; 6-month re-review of `/diagnostic/` (R7); quarterly deep audit at the end of M6 | TechnoTaau; client; PP | 6-month KPIs at or above floor; DPDP readiness confirmed; decision on the Hindi phase; therapy content outcome (Option A) known |
| **4. Scale and consolidate** | M7–M12 (Jun–Nov 2027) | N7, N13, N8 (conditional), W5, W2, W3 and W4 (M12); expansion X1; Hindi N1 (conditional); academy refresh for 2028 (R8a, course and training pages, in M10; R8b, posts N9 to N12, in M11); 12-month re-reviews (R9 for N4 and N9; R10 for `/diagnostic/`); quarterly audits at M9 and M12; year-2 plan, opened in M13 by the 12-month re-reviews of R2 to R4 | TechnoTaau; client; PP; VW | 12-month KPIs reviewed; every medical page within its review cycle; year-2 plan approved |

### 4.2 Next 30 days (19 Oct to 16 Nov 2026)

| # | Date (2026) | Action | Owner | Done when |
|---|---|---|---|---|
| 1 | Mon 19 Oct | Send this plan and the decision sheet (D1 to D8) to the client; book a 60-minute decision call for the week of 26 Oct | JS | Call booked |
| 2 | Mon 19 Oct | Pause the AI reels and all partner-facing posts and outreach in 03 §7 until D8 and counsel's view on NMC 8.1(vii); non-AI educational posts continue through G4; re-issue the 03 calendar after 13 Nov | TechnoTaau social (JS accountable) | Pause in place and recorded in 03; calendar re-issued after 13 Nov |
| 3 | Wed 21 Oct | Request access: existing Search Console property (if any), Google Business Profile (owner or manager), WordPress staging, LinkedIn page and YouTube channel | TechnoTaau SEO lead; client grants | Access granted, or "does not exist" confirmed |
| 4 | Wed 21 Oct | Book legal counsel for D1, D5, D8 and the NMC clause 8.1(vii) partner note | Client | Counsel engaged; dates agreed |
| 5 | Fri 23 Oct | Confirm the master NAP record (D4): PIN with India Post, address form, one public phone and WhatsApp, hours, signage name, legal entity name, public email; and whether +91 98156 92195 is the admissions line or the Delhi regional centre (the brief and the site disagree) | Client; TechnoTaau compiles | Signed record |
| 6 | Fri 23 Oct | With the client's go-ahead by email, on the old live site (about one hour): remove "Best" from the `/diagnostic/` and `/contact-us/` titles and the `/about/` meta in Rank Math; fix the ERFA post canonical; delete `/cache/` with a 410; resubmit the sitemap if Search Console exists (R03 C1; R08 §7) | Client developer | Go-ahead email on file; TechnoTaau checks the live titles |
| 7 | Mon 26 Oct | Real AI-panel baseline: 25 prompts × 4 surfaces × 3 runs, plus AI Overviews and Gemini where possible; manual SERP-feature check of the 22 cluster head terms (R07 §3.2; R08 §6.2) | TechnoTaau QA | Baseline sheet and screenshots saved |
| 8 | Wed 28 Oct | Reviewer decision session (90 min): EIT and CD138 framing and biopsy day; uNK status wording; ERFA vs ERA timing wording; founder descriptions; approved claims bank (R08 §8; 03 §4.4). These decisions settle the provisional N3, N4 and N5 titles and slugs (§3.4.4) | PP and VW decide; JS facilitates | Written decisions |
| 9 | Fri 30 Oct | WordPress SEO handover pack v1 to the developer: URL and redirect list, schema port spec, robots, sitemap, GA4 and consent spec, CWV budget, go-live runbook (§3.1). The rules that depend on D1 are written for both options (unpublish or noindex), and robots.txt follows the D7 default (allow all) | TechnoTaau SEO lead | Developer confirms receipt and questions |
| 10 | Fri 30 Oct | Keyword Planner volumes (India; English and Hindi) for the 22 clusters, added to the keyword map | TechnoTaau SEO lead | Map updated |
| 11 | Fri 30 Oct | Reference-build fixes in our remit (no client wording changed): therapy names out of the "Related at EmbryoGenesis" boxes; the therapy mentions and links our builders added on `/about/`, `/contact-us/`, `/blog/` and the 404 page taken out (§3.7.1), with the blog cards for the LIT and Hindi posts following D1; builder headings "Our Patents" changed to "Patent applications"; blog and 404 meta without therapy terms. (`ORG.description` and llms.txt were already fixed on 17 Oct 2026.) | TechnoTaau front-end builder + QA | `qc.py` 0 errors; schema validator 0 problems |
| 12 | Fri 30 Oct | Confirm the launch week (D6) once the developer has given a written build estimate (if the estimate does not fit, the launch moves, not the QA passes); the AI crawler policy (D7); the exact award name; the academy facts for R5 (§8.2 #15) | Client; developer (estimate) | Written confirmation |
| 13 | Mon 2 Nov | Google Business Profile: claim or confirm ownership of the existing place; check name, category and NAP against D4; prepare Bing Places for launch (R07 §5.1; R08 §7) | Client (owner) + TechnoTaau | Owner access confirmed |
| 14 | Fri 6 Nov | Drafts to the reviewers: the D2 replacement text, the refresh pack R1 to R5 and trust page T1 (if D3 is approved in principle); new posts N9 and N4 (through G0 to G2), queued for review from 1 to 11 Dec | TechnoTaau content writer | Drafts in the review queue |
| 15 | Tue 10 Nov | Written decisions D1, D2 and D3, with counsel's view | Client + counsel | Decision record signed |
| 16 | Wed 11 Nov | WordPress SEO handover pack v2, updated for the D1 to D3 decisions (and for D7 if the client chose other than the default) | TechnoTaau SEO lead | Developer confirms receipt and questions |
| 17 | Fri 13 Nov | Trust page T2 to the reviewers, drafted only after Dr. Wadhwa's registration number and consent arrive (§8.1 #11, due 6 Nov) | TechnoTaau content writer | Draft in the review queue |
| 18 | Fri 13 Nov | Privacy policy, form notices and consent text final (D5); AI-use wording (D8) | Counsel; client | Texts approved |
| 19 | Fri 13 Nov | Staging ready for SEO QA pass 1 | Client developer | Staging URL shared behind basic authentication |
| 20 | Mon 16 Nov | QA pass 1 on staging: crawl, redirect test, canonicals, schema, robots, sitemap, PageSpeed mobile, consent and GA4 DebugView | TechnoTaau QA | Issue list sent |

Dates avoid Dussehra (20 Oct), Diwali (8 Nov), Vishwakarma Day (9 Nov) and Gurpurab (24 Nov); review slots in the surge of 9 to 27 Nov are booked around them.

After this window: the review surge runs to Fri 27 Nov (§3.4.2); QA pass 2 on Wed 25 Nov, two working days before the code and content freeze and reviewer sign-off on Fri 27 Nov (Gurpurab is Tue 24 Nov); go/no-go Fri 4 Dec; launch Tue 8 or Wed 9 Dec 2026 (to be confirmed); N9 and N4 reviewed from Tue 1 to Fri 11 Dec and published from week 2 of M1.

---

## 5. Quality-control system

### 5.1 Gates for every page and post

| Gate | What is checked | Pass criteria | Who signs | Evidence |
|---|---|---|---|---|
| **G0 Brief and keyword** | Cluster, target URL (existing or NEW slug), primary and secondary queries (R08), questions to answer (R08 §5), audience, intent, cannibalisation, topic allowed (not therapy, price or sex selection), sources started, reviewer booked, video candidate | One URL per main query; topic inside the guardrails; reviewer slot booked; dependency cleared or dated | TechnoTaau SEO lead | Brief in the content tracker |
| **G1 Draft with sources** | Answer-first blocks; question headings; every factual claim sourced (guidelines first); exact guideline wording; "what it can and cannot tell"; named author; plain English, short sentences; 1 link to the pillar in the first 150 words and 2 to 4 related links; no links to held pages | No unsourced statistic; no claim from the "must not" list; all sources open and dated | TechnoTaau SEO lead (editorial check by someone other than the writer) | Draft with a source table |
| **G2 SEO, AEO and GEO technical** | Title ≤ 60 characters and meta 140 to 160; one H1; heading order; canonical; schema (BlogPosting or MedicalWebPage plus BreadcrumbList; FAQPage only if a visible FAQ matches); images (alt, size, WebP); internal links resolve; entity naming and facts match the master record; `qc.py` 0 errors on the build or a saved copy; Schema.org validator; Rich Results Test for supported types | All checks pass; `qc.py` exit code 0; validator 0 errors | TechnoTaau QA (SEO lead accountable) | Check sheet and tool output |
| **G3 Medical review** | Scientific accuracy, references, framing (PP); clinical claims (VW, as the registered doctor) | Written approval with a date; reviewer decisions recorded; next review date set | PP; VW where clinical claims exist | Approval email or document comment |
| **G4 Compliance and legal** | §3.7.7 must and must-not list; brief §5 guardrails; scripted claims scan (04 §5.1 dictionary); RMP line; AI label if any synthetic media; DPDP for any form; ASCI education rules for academy content. Counsel is triggered for anything therapy-related, AI-generated content, patient cases, partner-facing copy and comparative claims (ERA vs ERFA) | Zero "must not" hits; counsel's written approval where triggered | TechnoTaau compliance check (JS accountable); counsel when triggered | Checklist and counsel note |
| **G5 Sign-off and approval** | All earlier gates complete | JS signs; the named client approver approves in writing | JS; client approver | Approval record |
| **G6 Post-publish checks** | **48 hours:** URL returns 200, indexable, canonical self, schema renders, in the sitemap, IndexNow sent, Search Console inspection requested, hub links added, GA4 events after consent only. **7 days:** indexed in Google and Bing; no errors; video and social cross-links live. **30 days:** impressions and queries in Search Console; cannibalisation check; CTR against position; People Also Ask and AI check on its target questions; lessons added to the brief template | All 48-hour items pass; 7-day items pass or are explained; 30-day review filed | TechnoTaau QA | G6 log |

### 5.2 Monthly audit checklist
1. Search Console: Pages report errors; sitemaps; Core Web Vitals; HTTPS; manual actions and security issues; enhancements (breadcrumbs, profile page, videos); Generative AI performance report if it has appeared.
2. Bing Webmaster Tools: crawl errors; IndexNow submissions; AI Performance (citations, cited pages, grounding queries).
3. Crawl: status codes, redirect chains, canonicals, noindex, titles and metas, H1s, orphan pages, and **zero links to held pages**.
4. `qc.py` on a saved copy; Schema.org validator on changed templates.
5. Compliance scan of new and changed pages; llms.txt and schema facts against the master record.
6. NAP spot check: footer, contact page, schema, GBP, Bing Places, LinkedIn and the top three directories.
7. GBP: hours (including holidays), posts, questions, reviews answered within 2 working days per the reply policy, suspicious reviews reported.
8. Analytics: consent default works; no events before consent; no personal data in URLs or events.
9. Content: review due dates; G6 30-day checks; cannibalisation; queries without a good answer become briefs.
10. AI panel and error log.
11. Google Search Status Dashboard: any core or spam update during the month, read before interpreting changes (R07 §1.4, §1 implication 7).
12. Uptime log, SSL expiry, plugin updates (developer).
13. KPI dashboard and the monthly report (Appendix B).

### 5.3 Quarterly deep audit (end of M3, M6, M9 and M12)
- Full technical audit of every template; PageSpeed lab runs on all templates; field data where it exists.
- Content inventory: performance, freshness, guideline changes, merge or prune decisions.
- Entity audit: Wikidata, ORCID, Scholar, LinkedIn, YouTube, directories, university and ITHS pages, aggregator listings.
- Link audit: new and lost referring domains; any unnatural links.
- Legal watch with counsel: NMC guidance, DPDP dates (substantive duties about 13–14 May 2027; R07 §4.7), ASCI synthetic-content guidelines (from 29 Dec 2026; R07 §4.6), stem cell advisory updates.
- GA4 referrer review for the AI channel group (quarterly, R07 §3.1).
- Prompt-panel review: prompts stay fixed; up to 5 "watch" prompts may be added from Bing grounding queries, at the quarter boundary only.
- KPI review and the cadence decision (step up, hold or step down).
- Access review: who holds admin rights to Search Console, GA4, GBP, WordPress and the domain.

### 5.4 AI-panel QC
- Standard set-up every run: logged-out or clean account, India location, new chat per prompt, exact wording, date, surface and model name where shown (R07 §3.2; R08 §6.2).
- Three runs per surface; the 2-of-3 rule; a prompt counts when visible on 2 surfaces.
- A screenshot of every run that mentions EmbryoGenesis, and one per prompt per surface otherwise.
- A second person re-checks a random 10% of runs each month; the SEO lead settles disagreements.
- Report visibility % and trends, never "rank in ChatGPT" (R07 §3.3).
- Every factual or compliance error is logged with severity and the cited URL; S1 and S2 open incident I2.

### 5.5 Incident playbooks

| ID | Trigger | First 24 to 48 hours | Within 7 days | Owner (R); sign-off (A) |
|---|---|---|---|---|
| **I1 Ranking or traffic drop** | Non-branded clicks down more than 30% over 14 days against the previous 14 (E), a key page loses indexing, or a key page leaves the top 20 for its main query | Check the Search Status Dashboard for updates (R07 §1.4); check Search Console and Bing (Pages, manual actions, security, robots, sitemaps); check recent deploys (robots, noindex, canonicals, redirects, plugins); fix technical causes within 48 hours | Compare with seasonality and with AI Overview presence (impressions steady but clicks down suggests a CTR change; R07 §1.1); during a core update, wait for rollout to finish before content changes, then review the E-E-A-T of affected pages; report cause and plan to the client within 3 working days | R: SEO lead; A: JS |
| **I2 Wrong AI answer** | Panel or client finds a wrong fact or compliance problem about EmbryoGenesis in an AI answer | Log, screenshot, classify S1, S2 or S3 (§3.6.4); for S1 inform JS and, if there is legal exposure, counsel | Trace the cited source; fix at source; request recrawl; use the assistant's feedback option; recheck at the next run. S1 within 7 days, S2 within 30 (R07 §3.3) | R: SEO lead; A: JS; C: PP, counsel |
| **I3 Negative review** | A negative review on GBP or a directory | Reply within 2 working days using the reply policy: thank, no confirmation that the person was a patient, no medical detail, invite offline contact (R07 §4.7, §5.3) | Report through GBP tools only if it breaches Google policy (fake or conflict of interest); never offer incentives, never ask staff, partners or patients for counter-reviews (R07 §5.3); escalate allegations of harm to the client lead and defamation to counsel | R: client; A: client; C: JS, counsel |
| **I4 Compliance complaint** | A complaint or notice from ASCI, the NMC, a platform, a consumer or a competitor | Acknowledge; unpublish or edit the content pending review; do not argue in public; preserve evidence; notify counsel, VW (personal risk for the named RMP; R07 §4.1, clause 10) and PP | Counsel-led response; root cause; update the G4 checklist; log the incident | R: counsel; A: client; coordination: JS |
| **I5 Site outage or hack** | Uptime monitor alert or reports of errors | Developer and host contacted within 1 hour; for extended maintenance, serve a maintenance page with a temporary 503 status, never a 200 error page or a redirect to the home page (our standard practice); for a hack, take the site offline, restore from backup, rotate credentials | Check Search Console and Bing for crawl errors and security issues; inspect key URLs; check robots.txt, SSL and redirects; incident note in the monthly report | R: developer; A: client; C: TechnoTaau QA |

---

## 6. Team and RACI

**Roles**
- **JS:** Jakhar Singh, TechnoTaau Team lead (coordination, sign-off, client communication).
- **SEO:** TechnoTaau SEO lead (strategy, keyword map, briefs, reporting).
- **QA:** TechnoTaau technical SEO and QA analyst (staging and launch QA, crawls, schema, AI panel).
- **CW:** TechnoTaau content writer and editor (drafts, sources, first compliance pass).
- **SV:** TechnoTaau social and video producer.
- **Builder:** TechnoTaau front-end builder (reference build).
- **PP:** Prof. (Dr.) Pulakes Purkait, scientific reviewer.
- **VW:** Dr. Vidhu Wadhwa, clinical reviewer (registered medical practitioner).
- **CL:** Client management, front desk and admissions team (decisions, approvals, enquiry log, GBP replies).
- **DEV:** Client's WordPress developer and host.
- **LC:** Legal counsel.

R = does the work; A = accountable, signs off (one per row; for incident response, one per incident type, as in §5.5); C = consulted; I = informed.

| Activity | JS | SEO | QA | CW | SV | PP | VW | CL | DEV | LC |
|---|---|---|---|---|---|---|---|---|---|---|
| Pre-launch decisions D1 to D8 | R | C | I | I | I | C | C | A | I | C |
| Legal opinions (therapy, privacy, AI use, partner terms) | C | C | – | – | – | C | C | A | I | R |
| WordPress build and technical implementation | I | C | C | – | – | – | – | A | R | – |
| Staging and launch QA | I | A | R | – | – | – | – | I | C | – |
| Go/no-go and go-live | R | C | C | – | – | I | I | A | R | – |
| Schema port and validation | I | A | R | – | – | – | – | – | R | – |
| Analytics, consent, Search Console and Bing set-up | I | A | R | – | – | – | – | C | R | C |
| Master NAP record, GBP and Bing Places | I | R | C | – | – | – | – | A | – | – |
| Directories, Wikidata and knowledge-graph profiles | I | R | C | – | – | R | – | A | – | – |
| University, ITHS and institutional outreach | A | R | – | C | – | C | – | R | – | C |
| Briefs and keyword mapping (G0) | I | A/R | C | C | – | C | – | I | – | – |
| Drafting with sources (G1) | I | A | – | R | – | C | C | – | – | – |
| SEO, AEO and GEO checks (G2) | I | A | R | C | – | – | – | – | – | – |
| Medical review (G3) | I | I | – | C | – | A/R | R | I | – | – |
| Compliance and legal check (G4) | A | C | – | R | – | C | C | I | – | C |
| Publication approval (G5) | R | C | – | – | – | C | – | A | I | – |
| Publishing and post-publish checks (G6) | I | A | R | C | – | – | – | I | C | – |
| Monthly AI panel and error log | I | A | R | – | – | C | – | I | – | – |
| Monthly report and KPI dashboard | A | R | C | – | – | I | – | I | – | – |
| Enquiry log by type | – | C | – | – | – | – | – | A/R | – | – |
| GBP review replies | C | C | – | – | – | – | – | A/R | – | C |
| Video and reels | A | C | – | C | R | C | C | I | – | C |
| Digital PR | A | R | – | C | – | C | – | C | – | C |
| Journal publication (ERFA validation) | I | C | – | – | – | A/R | C | I | – | – |
| Incident response (A and R per §5.5) | A: I1, I2 | R: I1, I2 | C | – | – | C | C | A: I3 to I5; R: I3 | R: I5 | R: I4; C: I2, I3 |

Notes: the client's front desk keeps the enquiry log (R and A sit with CL). Incident response follows §5.5: JS is accountable for I1 and I2, the client for I3 to I5. The builder makes the reference-build fixes (§4.2 item 11), checked by QA. Prof. Purkait is both a client principal and the scientific reviewer; we keep the two roles separate so a review is never skipped to meet a date.

---

## 7. Risks and mitigations

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| 1 | Review bottleneck: Prof. Purkait's time | High | High | Pre-launch review surge 9 to 27 Nov, or the minimum pre-launch review set if it is not granted (§3.4.2); N4 and N9 reviewed 1 to 11 Dec; weekly slot after launch; batching; approved claims bank (03 §4.4); step-up and step-down rules (§3.4.2); hold publication rather than skip review | JS, PP |
| 2 | Therapy content stays live as it is | Medium | High | D1 with counsel; panel watch on P1, P2 and P10 for therapy mentions | Client, counsel |
| 3 | Superlatives and "patented" stay in kept content | Medium | High | D2 minimum edits with exact replacement text | Client |
| 4 | Migration errors (noindex left on, sitemap loop, lost pagination, broken redirects) | Medium | High | Go-live runbook; two QA passes; the three redirect rules not ported; no new content on launch day; rollback plan | Developer, QA |
| 5 | A core update during launch month (one ran 11–29 Dec 2025) | Medium | Medium | Read data against the Search Status Dashboard; no reactive rewrites mid-rollout (R07 §1.4) | SEO lead |
| 6 | Brand collisions: the biology term; other people named Purkait | High | Medium | Disambiguation line, consistent naming, Wikidata, ORCID and Scholar (R08 §1.1, §1.6, §7) | SEO lead |
| 7 | New evidence weakens how EIT and Endo-Immune are described (CD138 in Human Reproduction 2026; ESHRE on uNK) | High | Medium | Reviewer decisions (R08 §8); evidence-based wording builds trust with doctors | PP, VW |
| 8 | Measurement gaps: no history; consent-mode floors | High | Medium | Search Console for traffic; enquiry log for outcomes; re-baseline at L+30 (R07 §3.1) | SEO lead, client |
| 9 | AI answers unstable or wrong | High | Medium | Visibility %, 2-of-3 rule, fix-at-source loop (R07 §3.2, §3.3) | QA |
| 10 | Uncertainty over whether NMC guidelines cover a standalone lab | Medium | High | Treat as binding; counsel view (R07 §4.1) [VERIFY with counsel] | Counsel |
| 11 | DPDP duties brought forward | Low to medium | High | Build to the consent standard now; check the Gazette before launch (R07 §4.7) | Developer, counsel |
| 12 | Partner economics under NMC clause 8.1(vii) | Medium | High | No partner copy or outreach until counsel reviews; never mention incentives (R07 §0 item 7) | Client, counsel |
| 13 | Academy data conflicts; a possibly competing "Origin LIFE" programme on the RBU campus | Medium | Medium | Primary-source course pages; corrections through the universities; client confirms (R08 §1.9, §4) | Client, SEO lead |
| 14 | Host or CDN blocks crawlers, or slow server response | Low to medium | Medium | Check settings and TTFB on staging (R07 §2 implication 1, [UNVERIFIED] default behaviour) | Developer |
| 15 | AI-made media breaches NMC 7.2 or the ASCI rules | Medium | High | Counsel sign-off (D8); labels; no synthetic people (R07 §4.1, §4.6) | SV, counsel |
| 16 | Review gating or fake reviews | Low | High | Reply policy; no solicitation (R07 §5.3) | Client |
| 17 | Single reviewer unavailable for weeks | Medium | Medium | Pause new medical publication; never publish unreviewed; the client may name a second scientific reviewer | Client |
| 18 | Old-site negative signals linger (the "Best" title) | High now | Medium | Live-site fixes this month; recrawl requests after launch | Developer, SEO lead |
| 19 | Eight client decisions in three weeks | Medium | High | One decision call; a recommended default for each decision; JS escalates | JS |
| 20 | Topic inventory runs thin after M8 | Medium | Low | Reserve list W1 to W5; topics from Search Console queries; Hindi phase if approved | SEO lead |

---

## 8. Client inputs needed

Items marked "02 §11" carry over from the earlier strategy and are still relevant.

### 8.1 Critical before launch

| # | Input | Why | Needed by |
|---|---|---|---|
| 1 | D1 therapy decision (§3.7.1), with counsel | Legal and AI exposure; site structure | 10 Nov 2026 |
| 2 | D2 compliance minimum (§3.7.2) | NMC and brief guardrails | 10 Nov 2026 |
| 3 | D3 refresh pack and trust pages (§3.4.3, §3.7.4, §3.7.5) | E-E-A-T at launch | 10 Nov 2026 |
| 4 | D4 master NAP: PIN confirmed with India Post, locality, phone and WhatsApp, admissions labels, hours, signage name, legal entity name (02 §11); whether +91 98156 92195 is the admissions line or the Delhi regional centre (the brief and the site disagree) | Schema, GBP, directories | 23 Oct 2026 |
| 5 | D5 privacy policy, grievance officer, retention period, consent texts; consent banner choice (02 §11) | DPDP; forms | 13 Nov 2026 |
| 6 | D6 launch week and code freeze | Planning | 30 Oct 2026 |
| 7 | D7 AI crawler policy (allow all recommended; 02 §11 `{{AI_TRAINING_OPT_OUT}}`) | robots.txt | 30 Oct 2026 |
| 8 | D8 AI-use policy (counsel) | Editorial policy; reels | 13 Nov 2026 |
| 9 | Access: existing Search Console, GBP owner, Bing (if any), GA4 and GTM IDs or permission to create them (02 §11) | Baseline and launch | 21 Oct 2026 |
| 10 | WordPress staging access; Rank Math Free or Pro; WordPress port status (02 §11); the developer's written build estimate before D6 is confirmed (if the estimate does not fit, the launch moves, not the QA passes) | Build; launch date | 30 Oct 2026 |
| 11 | Dr. Wadhwa's SMR/NMR registration number and consent to be the clinical reviewer (02 §11) | Clinical review lines; NMC Explanations III–IV | 6 Nov 2026 |
| 12 | Review time: a pre-launch review surge from 9 to 27 Nov (PP three 90-minute slots a week; VW a weekly 60-minute slot), then a weekly 90-minute slot (PP) and a fortnightly 60-minute slot (VW). If the surge is not granted, only the minimum pre-launch review set is reviewed before launch (§3.4.2) | Pre-launch review set; cadence | 23 Oct 2026 |

### 8.2 High

| # | Input | Why | Needed by |
|---|---|---|---|
| 13 | Exact award name as printed on the certificate | Entity consistency | 30 Oct 2026 |
| 14 | Which collection centres are active (website vs brochure lists) | Factual consistency | 30 Oct 2026 |
| 15 | Academy: 2027–28 session dates; fees and eligibility per university; ITHS and EmbryoGenesis role; whether the Ph.D. and PG Diploma are still offered; the "Origin LIFE" programme (02 §11; R08 §1.9) | R5, N9 to N12 | 30 Oct 2026 |
| 16 | Test facts: ERFA method description, Receptivity PX method and spelling, sample and transport details (02 §11) | N3, N4, N13 | 6 Nov 2026 |
| 17 | Whether TB-PCR is offered | N8 | M6 |
| 18 | Patent status: any grant certificates (02 §11) | Wording | 30 Oct 2026 |
| 19 | Square 512×512 logo and a 1200×630 default social image (QC-SEO §6.3) | Schema; sharing | 13 Nov 2026 |
| 20 | Real lab photos and a short entrance video | GBP verification; pages; video | 13 Nov 2026 |
| 21 | Historic enquiry counts by type (3 to 6 months) and 2026 admission numbers | KPI baselines | L+30 |
| 22 | Public email decision (domain address?) and which director mailbox is live (02 §11; QC-CF §9) | NAP | 30 Oct 2026 |
| 23 | Which number the "Call Now" buttons on course pages dial (QC-CF §9) | NAP | 30 Oct 2026 |
| 24 | ResearchGate URL that resolves; agreement to create Google Scholar (R08 §7) | Entity | M2 |
| 25 | Contacts at Rayat Bahra University, Bahra University, ITHS, INNR and Guru Ghasidas Vishwavidyalaya | Outreach | 30 Oct 2026 |
| 26 | ERFA validation data and ethics status | Journal paper | M3 |
| 27 | Unified social handle decision (02 §11) | `sameAs`; video | M1 |

### 8.3 Medium

| # | Input | Why | Needed by |
|---|---|---|---|
| 28 | Partner logo permissions, expert photo consents, GIOSTAR decision with counsel (02 §11) | About page images | M2 |
| 29 | CME accreditation, if webinars are planned (02 §11) | Event wording | When planned |
| 30 | ISO, MSME and NABL or ART registration numbers, only if held (02 §11; brief §2) | Accreditation lines | M2 |
| 31 | Backup of 2023–2025 uploads (02 §11) | Image restore | M2 |
| 32 | Hindi phase decision and a Hindi-fluent medical reviewer | Hindi N1 | M6 |
| 33 | Staff willing to appear on camera, with consent | Video | M1 |
| 34 | Authorisation for Ahrefs or Similarweb (optional) | Backlink and competitor data | Any time |

Superseded from 02 §11 and no longer needed: partner details per city for city pages, and partner consent for city pages (city pages are parked).

---

## 9. What this plan supersedes in `02-seo-strategy.md`

| 02 section | Status | What changes |
|---|---|---|
| §1.1 Principles | **Kept in part** | "One page, one job", held content out of the index and navigation, and city pages only where a real centre exists (parked) still hold. The navigation and the B2B header call to action are superseded |
| §1.2 Changes from the draft | **Superseded** | Except the editorial policy, which becomes NEW `/editorial-policy/` |
| §1.3 Sitemap tree and §1.4 page table | **Superseded** | The site keeps the old URLs (`site/src/llms.txt`). The sections 02 proposed (Diagnostics, For Clinicians, Partner With Us, Collection Centres, Patients, Academy and Research hubs, and city pages) were never built and are not used |
| §1.5 Internal linking rules | **Updated** | New hubs and clusters (§3.4.1); never link to held pages |
| §2 301 redirect map | **Superseded** | Replaced by `site/src/_redirects` and `.htaccess`, minus three rules for WordPress (§3.1 item 2). Kept: one hop to a 200 page; 410 for `/cache/`; never redirect broken images to pages |
| §3.1–3.2 Keyword map | **Superseded** | By R08 §2–3 and §3.3 of this plan, including its B2B keyword focus |
| §3.3 Excluded keywords | **Kept and extended** | With R08's traps (§3.3 table) |
| §3.4 Hindi and Hinglish list | **Kept as parked input** | For a possible Hindi phase (§3.5) |
| §4 On-page template rules; §4.1 test page; §4.5 blog article | **Kept** | URL formulas updated to root slugs; the test-page template applies to sections of `/diagnostic/` |
| §4.2 Clinician resource; §4.3 city page | **Superseded / parked** | Client dropped these pages |
| §4.4 Academy programme page | **Kept** | For updates to the existing course pages; its URL formula is superseded |
| §5.1 WordPress and Rank Math settings | **Updated** | Permalinks `/%postname%/`, not `/blog/%postname%/`; category archives redirected and hidden from breadcrumbs; no topic archives. Other settings kept |
| §5.2 CWV budget | **Kept and updated** | Self-host Work Sans and Lato (the fonts actually used), not Inter and Source Serif 4; responsive image findings from QC-FE |
| §5.3 Canonicals | **Kept** | – |
| §5.4 Sitemaps | **Updated** | Use what WordPress serves and align robots.txt (R07 §6.1) |
| §5.5 Noindex rules | **Updated** | 02's proposed research-programme and city pages were never built; held pages per D1; the therapy training modules per D1 |
| §5.6 robots.txt | **Updated** | Bot list as in the built file (adds Claude-SearchBot, Claude-User, ChatGPT-User, Perplexity-User); Google-Extended also controls Gemini app grounding; Search Console AI control on Include (R07 §6.1) |
| §5.7 GA4, GTM and Consent Mode | **Updated** | Native "AI Assistant" channel (13 May 2026, confirmed in Google's Analytics Help release notes, https://support.google.com/analytics/answer/9164320), custom group kept (R07 §6.1); `partner_enquiry` and B2B form types removed; enquiry type kept out of GA4 |
| §5.8 Search Console and Bing | **Kept and extended** | Generative AI performance report; Bing AI Performance report (R07 §3.1) |
| §5.9 Breadcrumbs and 404 | **Kept** | 404 links point to the existing navigation |
| §5.10 Image restore list | **Kept in part** | Items tied to dropped pages are void |
| §6.1 Schema approach | **Kept and updated** | Values from `site/build.py`; FAQ rich results gone for all sites since 7 May 2026, FAQPage optional (R07 §6.1) |
| §6.2 Organization | **Updated** | Use the built `ORG` node, minus therapy wording |
| §6.3 Partner collection centre | **Parked** | – |
| §6.4 MedicalTest; §6.5 Person; §6.8 Article; §6.9 Breadcrumb | **Kept** | `@id`s from `site/build.py` (for example `/pulakes-purkait-profile/#person`); root URLs |
| §6.6 FAQPage | **Updated** | Optional; no rich result (R07 §1.2) |
| §6.7 Course | **Kept** | No Course info rich result; Course list remains in Google's gallery (R07 §1.2) |
| §6.10 Event | **Kept, conditional** | Only if webinars happen; "CME" only if accredited |
| §6.11 Rank Math filter | **Kept** | – |
| §7.1–7.3 Entity, naming, NAP | **Kept** | PIN now a known conflict (R08 §7) |
| §7.4 Google Business Profile | **Updated** | R07 §5.1 rules (category check, video verification [UNVERIFIED], posts as advertising); partner GBP requests on hold until counsel |
| §7.5 Knowledge-graph profiles | **Kept, timing updated** | Wikidata in M2–M3 with COI declared (R07 §2.2) |
| §7.6 Directories | **Updated** | Priorities per R07 §5.2; IndiaMART and LifeLinkr de-prioritised |
| §8 intro statistic ("44% to 88%") | **Updated** | Only verified figure: more than 82% of German health searches (SE Ranking); no India data (R07 §1.1, §6.1) |
| §8.1 Quotable content rules | **Kept** | Extended in §3.5 |
| §8.2 Third-party corroboration | **Updated** | Partner hospital pages on hold until counsel |
| §8.3 llms.txt | **Updated** | Google does not use it; 97% of files never requested; reviewed subset only; the residual therapy wording in lines 23 and 34 was removed on 17 Oct 2026 (R07 §2.3, §6.1) |
| §8.4 20-prompt panel | **Superseded** | R08's 25 prompts with 3 runs per surface and the 2-of-3 rule (R07 §3.2, §6.1) |
| §9 90-day calendar (24 articles) | **Superseded** | By §3.4.5, including its 50% clinician and B2B mix |
| §10.1 Off-page principles | **Kept** | – |
| §10.2 Tactics | **Updated** | Partner outreach on hold; universities, journals and press kept; CME optional |
| §10.3 KPIs | **Superseded** | Partner KPIs removed; new table in §2.3. The floor-and-target format is kept |
| §11 Placeholders | **Merged** | Into §8 of this plan |

**Research 07 §6.1 updates and where they land:** FAQ note (§3.5, §9); AI Overview statistic (§9); llms.txt (§3.6.2 item 9); prompt panel (§3.6.3); robots.txt (§3.1 item 7); GA4 channel (§3.1 item 17); sitemap mismatch (§3.1 items 2 and 7); brief section 5 additions (§3.7.8, for client approval); the `01-industry-research.md` citation update (outside this plan).

---

## Appendix A: KPI definitions

| KPI | Definition and formula | Source and filter | Frequency | Notes |
|---|---|---|---|---|
| B1 Test enquiries | Count per month of (a) form submissions where "I am interested in" = Diagnostic test, plus (b) calls and WhatsApp chats that the front desk logs as "found us on the website or Google" and "test" | Client enquiry log (Google Sheet); GA4 `generate_lead`, `tel_click` and `whatsapp_click` as a floor | Monthly | No health details in the log beyond the enquiry type |
| B2 Academy enquiries | Same method for course and lab-training enquiries | Enquiry log; GA4 form events on academy pages | Monthly | Seasonal: compare with the same month a year earlier from 2028 |
| B3 Academy applications | Applications in the 2027 season whose lead source is the website | Admissions records | Season total | Floor = 2026 count; target = 2026 count + 25% (E) |
| B4 Therapy enquiries | Enquiries logged as therapy | Enquiry log | Monthly | Track only |
| S1, S2 Non-branded clicks and impressions | All Search Console queries minus the brand filter | Search Console, Web search, all countries, then India split | Monthly | The brand filter below |
| S3 Branded demand | Queries containing "embryogenesis" together with Mohali, ERFA, Purkait, test, lab, Kharar, Rayat Bahra or course; plus queries containing "erfa" or "purkait"; plus "embryogenesis.in". "embryogenesis" on its own is excluded (biology term) (R07 §3.3; R08 §1.6) | Search Console query filter or export | Monthly | Numeric target set at L+30 |
| S4 Sitemap URLs indexed | Indexed URLs ÷ URLs in the sitemap | Search Console Pages and Sitemaps reports | Monthly | – |
| S5 Pages with impressions | URLs with at least 1 impression in the 28 days before the checkpoint | Search Console Pages tab | Monthly | – |
| S6 AEO win | A question from R08 §5 for which an EmbryoGenesis page is shown as a People Also Ask answer source, a featured answer, or a cited source in an AI Overview, in the manual check (Google India, incognito) | Quarterly manual check (R08 §6.2) | Quarterly | Count each question once |
| A1 AI panel score | Prompts visible on at least 2 surfaces, where "visible on a surface" = mentioned or cited in at least 2 of 3 runs (R07 §3.2) | Panel sheet | Monthly | Out of 25 |
| A2 Brand prompts with correct facts | P6, P24 and P25 visible with no wrong facts | Panel sheet | Monthly | R07 §3.3 |
| A3 Bing cited pages | Distinct EmbryoGenesis URLs with at least 1 citation in the month | Bing AI Performance | Monthly | Sampled data (R07 §3.1) |
| A4 AI referrals and Google AI impressions | GA4 sessions in the "AI Assistant" channel and the custom AI group; Search Console Generative AI impressions by page | GA4; Search Console | Monthly | Floors only |
| A5 AI errors fixed in 30 days | S1 and S2 errors closed within deadline ÷ errors opened | Panel error log | Monthly | – |
| L1 GBP actions | Calls + direction requests + website clicks | GBP Performance | Monthly | – |
| L2 New referring domains | Relevant domains linking for the first time since L | Search Console Links; Bing backlinks | Monthly | Exclude spam and scraper domains |
| T1 Core Web Vitals | LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 on 5 templates | PageSpeed lab; field data when available | Monthly | – |
| T2 Technical errors | 5xx, redirect chains, broken canonicals, internal links to 404s or held pages | Crawl; Search Console | Monthly | Target 0 |
| C1 Compliance incidents | Complaints or notices received | Incident log | Monthly | Target 0 |
| C2 Review turnaround | Working days from "sent to G3" to written approval, median, reported per reviewer | Content tracker | Monthly | ≤ 5 working days for items reviewed by Prof. Purkait only; ≤ 10 working days where Dr. Wadhwa's clinical review is needed |

## Appendix B: Monthly report template

Delivered by the 7th of each month as a short document plus the Looker Studio dashboard link.

1. **Summary:** three wins, three issues, three priorities for next month.
2. **KPI table:** every KPI in §2.3 with this month, last month, floor, target and a red, amber or green status.
3. **Business outcomes:** enquiries by type (test, academy, training, therapy tracked only); academy pipeline in season.
4. **Search:** branded and non-branded clicks and impressions; top 10 queries; top 10 pages; new pages and their G6 30-day results; indexing.
5. **AI visibility** (R07 §3 implication 3): Search Console Generative AI impressions by page; Bing citations, cited pages and top grounding queries; GA4 AI sessions and key events; the panel score with the per-surface breakdown; the error log with status.
6. **Local:** GBP actions; reviews received and answered; NAP fixes made.
7. **Technical:** Core Web Vitals; crawl errors; schema and `qc.py` results; uptime.
8. **Content:** items published, refreshed and re-reviewed; gates passed; review turnaround; next month's calendar.
9. **Off-page:** mentions and links earned; outreach status.
10. **Compliance:** incidents (if any); checks run; legal watch notes.
11. **Decisions needed from the client.**

## Appendix C: AI prompt panel summary (25 prompts from R08 §6.1)

"Earliest realistic visibility" is a TechnoTaau estimate (E). Prompts with "good colleges" or similar are monitoring prompts only, never copy (R08 §6.1).

| # | Prompt (paste exactly) | Audience | Asset that should earn the citation | Scored? | Earliest realistic visibility (E) |
|---|---|---|---|---|---|
| P1 | What should I do after a failed IVF cycle in India? | Couple | N1 | Yes | M9+ |
| P2 | IVF fail hone ke baad kya karna chahiye? (also in Devanagari: आईवीएफ फेल होने के बाद क्या करें?) | Couple | Hindi post after D1; N1; Hindi N1 if approved | Yes (Hinglish run) | After the Hindi phase |
| P3 | Which tests should I ask for after three failed embryo transfers? | Couple | N2 | Yes | M9+ |
| P4 | Is the ERA test worth it for repeated IVF failure? | Couple | N3 | Yes | M9+ |
| P5 | How much does an ERA test cost in India? | Couple | None (no-price rule) | Monitor only | – |
| P6 | What is the ERFA "Soil Test" for IVF, and how is it different from the ERA test? | Couple, doctor | N3, `/diagnostic/`, a validation paper | Yes (brand) | M3 |
| P7 | Which labs in India offer endometrial receptivity testing? | Couple, doctor | `/diagnostic/`, entity work | Yes | M9+ |
| P8 | How is chronic endometritis diagnosed, and does a CD138 test matter for IVF? | Couple, doctor | N5 | Yes | M9+ |
| P9 | Should I get a uterine NK cell test after IVF failure? | Couple | EIP post | Yes | M9+ |
| P10 | What tests are done for recurrent miscarriage in India? | Couple | N6 | Yes | M12 |
| P11 | My endometrium is 6 mm. What does a thin endometrium mean for IVF? | Couple | N7 | Yes | M12 |
| P12 | Where can I get an endometrial biopsy test for IVF failure near Chandigarh or Mohali? | Couple (local) | GBP, `/contact-us/`, `/diagnostic/` | Yes | M4–M6 |
| P13 | What does ESHRE recommend for investigating recurrent implantation failure? | Doctor | N2 | Yes | M9+ |
| P14 | Is there a lab in India that does endometrial immune profiling (uNK, plasma cells, cytokines) on a biopsy? | Doctor | `/diagnostic/`, EIP post | Yes | M4–M6 |
| P15 | When should the endometrial biopsy be taken for receptivity testing (LH+7, P+5)? | Doctor | N4, `/diagnostic/` | Yes | M9+ |
| P16 | Are there immunohistochemistry-based endometrial receptivity tests developed in India? | Doctor | N3, N13, patent applications on the profile page, publication | Yes | M6–M9 |
| P17 | Which are good colleges for clinical embryology in Punjab? | Student | `/courses/`, corrected aggregator profiles | Yes (monitoring wording) | M9+ |
| P18 | What are the eligibility and fees for B.Sc./M.Sc. ART & Clinical Embryology at Rayat Bahra University, Mohali? | Student | `/art-and-clinical-embryology-in-rayat-bahra-university/` | Yes | M3–M6 |
| P19 | Is there a clinical embryology course in Himachal Pradesh? | Student | `/bsc-in-clinical-embryology-in-bahra-university/` | Yes | M3–M6 |
| P20 | What is the salary of a clinical embryologist in India? | Student | N10 | Yes | M9+ |
| P21 | How do I become an embryologist after 12th in India? | Student | N9 | Yes | M6–M9 |
| P22 | Where can I do hands-on ICSI or IVF lab training in north India? | Student, trainee | `/skill-development-training/` only if such a course is offered | Product-dependent | – |
| P23 | Is there an andrology or semen analysis hands-on course in India? | Trainee | Product decision | Product-dependent | – |
| P24 | What is EmbryoGenesis in Mohali? | Brand | `/about/`, GBP, Wikidata | Yes (brand) | M3 |
| P25 | Who is Prof. Pulakes Purkait? | Brand | `/pulakes-purkait-profile/`, ORCID, Wikidata, Scholar | Yes (brand) | M3 |

**Baseline:** 0 of 25 in the proxy test (R08 §6.1). The real baseline is taken in the week of 26 Oct 2026.

## Appendix D: Source map to research 07 and 08

| Plan section | Research 07 | Research 08 |
|---|---|---|
| §1 Baseline | §0; §2.3 (llms.txt); §4.2 | §1, §6.1, §7 |
| §2 KPIs and measurement | §0 item 2; §3.1–3.3 | §0 (no volumes; connectors), §6 |
| §3.1 Technical | §1.1 (G1–G3), §1.2, §2.4, §2.5, §3.1, §4.7, §6.1 | – |
| §3.2 Entity and local | §1.5, §2.2 (Wikidata), §5.1–5.4 | §1.8, §7 |
| §3.3 Keyword map | §4.1 (claims), §5.5 | §1.6, §1.7, §2, §3 |
| §3.4 Content | §1.1 (scaled content), §1.3, §2 implication 4 | §1.3, §1.10, §3, §5, §8 |
| §3.5 AEO | §1.2, §2.2 | §0, §5, §6.2 |
| §3.6 GEO | §0, §1.1, §2.1–2.5, §3.2, §3.3 | §6 |
| §3.7 E-E-A-T and compliance | §1.3, §4.1–4.7, the must and must-not checklist, §6.1 | §1.5, §8 |
| §3.8 Off-page | §0 items 4 and 7, §1.3 (site reputation), §2 implication 3, §5.2, §5.4 | §4, §7 |
| §3.9 Video and social | §1.1, §1 implication 5, §2.2 (YouTube), §4.1, §4.6 | §7 (YouTube) |
| §5 QC and incidents | §1.4, §3.2, §3.3, §5.3 | §6.2 |
| §9 Supersedes | §6.1 | §3 |

The prioritised content calendar is inline in §3.4.5, and the prompt panel summary is inline in Appendix C. Research 07's list of unverified facts (R07 §6.2) applies wherever this plan marks an item [UNVERIFIED] or [SECONDARY].

---

*Prepared for EmbryoGenesis by TechnoTaau Team, 17 October 2026. This is a search and content plan, not legal advice: items marked [VERIFY with counsel] need the client's lawyer or medical-council adviser before anyone acts on them.*

*TechnoTaau Team*
