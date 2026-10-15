# Copy notes: priority pages 01 to 05

**Prepared by:** TechnoTaau Team (Senior Medical Content Writer), for Jakhar Singh
**Date:** 15 October 2026
**Covers:** `01-home.md`, `02-partner-with-us.md`, `03-endometrial-infection-test.md`, `04-for-clinicians.md`, `05-about.md`
**Sources used:** `docs/00-project-brief.md`, `docs/strategy/01-project-blueprint.md`, `docs/research/01` to `03`, the saved current-site HTML (home, about, diagnostic, courses, skill-development-training, founder profile, course and contact pages), the founder's public ORCID record, and primary sources checked on 15 Oct 2026 (listed in section 5).

This file lists every placeholder, every fact the client must verify, and every claim we softened from the current site. Nothing marked here should go live until it is resolved.

---

## 1. Placeholders

### 1.1 How placeholders work

- `{{NAME}}` is a value the client must supply.
- `{{CONFIRM}}` after a sentence means the sentence describes something we believe is planned but have not confirmed. If it is not confirmed by launch, the developer deletes the sentence.
- `{{CONFIRM_X}}` is a specific yes/no or detail question for the client.
- `{{LEGAL_REVIEW}}` means the client's legal adviser must approve the wording.
- The developer must never publish brace text. A pre-launch search for `{{` across all pages is part of QA Gate 5.

### 1.2 Contact, entity and site-wide

| Placeholder | What we need | Pages | Owner |
|---|---|---|---|
| `{{PRIMARY_PHONE}}` | One primary phone number in +91 format. The current site shows four (9691736435, 9815692195, 8146217196, 9599877196). | 01, 02, 05 | Client |
| `{{WHATSAPP}}` | WhatsApp Business number (digits only, with 91) | 01, 02, 04, 05 | Client |
| `{{SCIENTIFIC_TEAM_PHONE}}`, `{{SCIENTIFIC_TEAM_EMAIL}}` | Direct line and email for clinician queries | 04 | Client |
| `{{PARTNERSHIPS_EMAIL}}` | Inbox for partner enquiries | 02 | Client |
| `{{KIT_REQUEST_EMAIL}}` | Inbox for kit requests | 03, 04 | Client |
| `{{CONFIRM_PRIMARY_EMAIL}}` | Keep info.embryogenesis@gmail.com, or move to a domain email (recommended) | 01 | Client |
| `{{LOCALITY}}`, `{{MOHALI_PIN}}` | Full postal locality and PIN code of the Mohali lab | 01, 02, 05 | Client |
| `{{UDAIPUR_PIN}}`, `{{JALANDHAR_PIN}}` | PIN codes for these collection centres | 01, 02, 05 | Client / partners |
| `{{LAB_HOURS}}` | Lab and phone hours | 01, 02, 04, 05 | Client |
| `{{LEGAL_ENTITY_NAME}}` | Registered legal name of the data fiduciary (company / LLP / trust) | 02 | Client |
| `{{GRIEVANCE_OFFICER_NAME}}`, `{{GRIEVANCE_EMAIL}}` | DPDP grievance contact | 02 (reused on 04) | Client |
| `{{RETENTION_PERIOD}}` | How long enquiry data is kept (we suggest 24 months) | 02 | Client + legal |
| `{{RESPONSE_TIME}}` | Committed reply time (we suggest 2 working days) | 02, 04 | Client |
| `{{LINKEDIN_URL}}`, `{{INSTAGRAM_HANDLE}}`, `{{FACEBOOK_URL}}`, `{{YOUTUBE_URL}}` | Unified social handles (current handles are inconsistent; no LinkedIn page yet) | 01 | Client |
| `{{FOUNDER_LINKEDIN_URL}}` | Correct LinkedIn URL (current one ends in `%20`) | 05 | Client |
| `{{GOOGLE_BUSINESS_PROFILE_URL}}` | Verified Google Business Profile link | 05 | Client |
| `{{CURRENT_YEAR}}` | Dynamic year in footer | 01 | Developer |
| `{{PARTNER_COUNT}}` | Number of active collection centres (3 today) | 01 | Client |

### 1.3 Clinical, reviewer and accreditation

| Placeholder | What we need | Pages |
|---|---|---|
| `{{RMP_NAME}}`, `{{RMP_QUALIFICATION}}`, `{{NMC_REG_NO}}` | A registered medical practitioner to co-review clinical pages, with NMC or State Medical Council registration number (brief guardrail 7). Dr. Vidhu Wadhwa (MD Pathology) may be suitable. | 01, 03, 04 |
| `{{NMC_REG_NO_VIDHU_WADHWA}}` | Dr. Wadhwa's registration number | 04, 05 |
| `{{REPORTING_PATHOLOGIST}}`, `{{REPORTING_SIGNATORIES}}` | Who signs reports, with registration numbers | 03, 04, 05 |
| `{{REVIEW_DATE}}`, `{{NEXT_REVIEW_DATE}}` | Date Prof. Purkait signs off; next review date | all |
| `{{CLINICAL_REVIEW}}` | RMP to check the patient description of the biopsy procedure | 03 |
| `{{LAB_ACCREDITATION}}` | NABL certificate number and scope, or a statement that it is in progress | 04, 05 |
| `{{LAB_REGISTRATION}}`, `{{LAB_REGISTRATIONS}}` | Clinical establishment registration, bio-medical waste authorisation | 01, 05 |
| `{{CONFIRM_EQA_PARTICIPATION}}` | Whether the lab takes part in external quality assessment | 05 |
| `{{VALIDATION_STATUS}}` | Status of validation data for ERFA, EIT, Endo-Immune, Receptivity PX | 01, 04, 05 |
| `{{LEGAL_ADVISER}}`, `{{LEGAL_REVIEW_DATE}}` | Legal sign-off on partner terms | 02 |

### 1.4 Test specifications (blueprint open item 5)

| Placeholder | What we need | Pages |
|---|---|---|
| `{{METHOD}}`, `{{METHOD_DESCRIPTION}}` | EIT method: CD138 IHC, culture, PCR, or a combination. 2 to 3 sentence description. | 03 |
| `{{THRESHOLD}}` | Plasma-cell threshold the lab uses (for example ≥5 CD138+ cells per 10 HPF) | 03 |
| `{{REPORT_FIELDS}}` | What the EIT report shows (count, categories) | 03 |
| `{{IF_PCR_OR_CULTURE}}`, `{{SHOW_ONLY_IF_METHOD_IS_PCR_OR_MICROBIOME}}` | Conditional content, shown only if the method includes organism detection | 03 |
| `{{SAMPLE_EIT}}`, `{{SAMPLE_ERFA}}`, `{{SAMPLE_ENDO_IMMUNE}}`, `{{SAMPLE_RPX}}` | Sample type and container for each test | 03, 04 |
| `{{TIMING_EIT}}`, `{{TIMING_ERFA}}`, `{{TIMING_ENDO_IMMUNE}}`, `{{TIMING_RPX}}` | Cycle timing for each test (for example LH+7 / P+5 for receptivity) | 03, 04 |
| `{{BIOPSY_METHOD}}`, `{{MIN_SAMPLE_SIZE}}`, `{{FIXATIVE_OR_MEDIUM}}`, `{{RATIO}}`, `{{TIME_TO_FIXATION}}` | Collection details | 02, 03, 04 |
| `{{STORAGE}}`, `{{STORAGE_CONDITIONS}}`, `{{TRANSPORT_CONDITIONS}}`, `{{MAX_TRANSIT_HOURS}}` | Storage and transport | 01, 02, 03, 04 |
| `{{CONFIRM_ANTIBIOTIC_WASHOUT}}` | Any washout period after antibiotics before EIT biopsy | 03 |
| `{{CONFIRM_ERFA_MARKERS}}`, `{{CONFIRM_ENDO_IMMUNE_MARKERS}}` | What each assay measures, in one line | 01, 04 |
| `{{CONFIRM_RECEPTIVITY_PX_STATUS}}`, `{{CONFIRM_RECEPTIVITY_PX}}`, `{{CONFIRM_RECEPTIVITY_PX_INDICATION}}` | Is Receptivity PX a separate orderable test, or part of ERFA / Endo-Immune? It has no planned URL in the sitemap. | 01, 04 |
| `{{CONFIRM_COMBINED_SAMPLE}}` | Can one biopsy serve more than one test? | 04 |
| `{{CONFIRM_CLIENT_INDICATIONS}}` | Any extra EIT indications the lab supports | 03 |
| `{{CONFIRM_TAT_START}}` | Is 7 to 10 days counted from sample receipt (our assumption) or from collection? | 01 |
| `{{SAMPLE_REPORT_PDF}}`, `{{REQUISITION_FORM_PDF}}`, `{{CONSENT_FORM_PDF}}`, `{{SOP_PDF}}` | Anonymised sample report, forms and SOP | 03, 04 |
| `{{REPORT_CHANNEL}}` | How reports are delivered (portal, encrypted email) | 02, 03, 04 |
| `{{CONFIRM_REPORT_TO_PATIENT_POLICY}}` | Do reports go only to the ordering clinician, or also to patients? | 02, 04 |
| `{{CONFIRM_REJECTION_CRITERIA}}`, `{{CONFIRM_REJECTION_POLICY}}` | Sample rejection rules | 02, 04 |

### 1.5 Partner programme (blueprint open item 8)

| Placeholder | What we need | Pages |
|---|---|---|
| `{{CONFIRM}}` items in partner Section 5 table | Training format, kits (free or at cost), logistics (courier, who pays), report support, CME, co-branded leaflets, talent pipeline, rate card | 02 |
| `{{CONFIRM_KIT_PROVIDED}}` | Whether we supply collection kits | 01 |
| `{{COURIER_PARTNER}}`, `{{PICKUP_DAYS}}`, `{{PICKUP_CUTOFF_TIME}}`, `{{PICKUP_BOOKING_CONTACT}}`, `{{CONFIRM_COURIER_ARRANGEMENT}}` | Pickup logistics | 02, 03, 04 |
| `{{CONFIRM_NON_PARTNER_ORDERING}}` | Can non-partner doctors order? | 03, 04 |
| `{{CONFIRM_TEST_LIST}}` | Tests partners can collect for | 02 |
| `{{CONFIRM_ANY_ONBOARDING_FEE}}` | Any onboarding fee | 02 |
| `{{CONFIRM_EXCLUSIVITY_POLICY}}` | City exclusivity | 02 |
| `{{CONFIRM_NOTICE_PERIOD}}` | Exit terms | 02 |
| `{{CONFIRM_TIMELINE}}`, `{{REVIEW_FREQUENCY}}` | Onboarding timeline; partner review cadence | 02 |
| `{{CONFIRM_DIRECT_PATIENT_POLICY}}` | Can patients self-refer? We assumed no (doctor order only). | 01 |

### 1.6 CME, academy and about

| Placeholder | What we need | Pages |
|---|---|---|
| `{{CME_FREQUENCY}}`, `{{CME_ACCREDITATION}}`, `{{CME_REGISTRATION_URL}}`, `{{YOUTUBE_PLAYLIST_URL}}` | CME programme details | 04 |
| `{{ACADEMY_ROLE}}` | EmbryoGenesis's exact role in the degree programmes (ASCI requires the awarding university to be named prominently) | 01 |
| `{{CONFIRM_CURRENT_COURSE_LIST}}` | Current short courses (we listed only the four non-therapy courses) | 01 |
| `{{CONFIRM_AWARD_DETAILS}}`, `{{CONFIRM_FULL_AWARD_NAME_AND_ISSUER}}`, `{{CONFIRM_RELATION_TO_NBHC_2024_AWARD}}` | Exact award names, issuers, dates, and whether these are one award or two | 01, 05 |
| `{{CONFIRM_PUBLICATION_DATES}}` | Publication dates of the two patent applications | 05 |
| `{{CONFIRM_DATE_AND_ROLE}}` | Date and role of PJ Embryogenesis Health & Education Foundation, Kolkata | 05 |
| `{{CONFIRM_START_DATE}}`, `{{DATE}}`, `{{CONFIRM_DATES}}`, `{{OPTIONAL}}` | Timeline dates (Rayat Bahra programme start; collection partners added) | 05 |
| `{{YEARS_EXPERIENCE}}`, `{{STUDENTS_SUPERVISED}}`, `{{CONFIRM_CURRENT_ROLES}}`, `{{CONFIRM_SELECTION}}` | Founder bio facts | 05 |
| `{{CONFIRM_TITLE}}`, `{{QUALIFICATION}}` | Team titles and qualifications | 05 |
| `{{CONFIRM_SCOPE}}`, `{{CONFIRM_CURRENT_LIST}}` | MoU scope; training and placement partner list | 05 |
| `{{CLIENT_TO_REVIEW_WORDING}}` | Endo-Immune FAQ answer on the clinician hub | 04 |

---

## 2. Facts that need client verification

1. **Patent status.** Both numbers shown (ERFA 202431001616 A; Receptivity PX 202411059621 A) are published applications. The founder's ORCID lists Receptivity PX in Patent Office Journal No. 39/2024. Please check both on IP India InPASS and send any grant certificate. Until then, the copy says "patent application published".
2. **Awards.** The brief lists two awards: "Best Innovator Award, NBHC 2024 (IIT Delhi)" and "Best Innovator Award for Human Infertility Treatment, Research & Innovation Park, New Delhi, Nov 2024". The Research & Innovation Park is part of IIT Delhi, so these may be the same award. ASCI requires the exact name, issuer and year. We also state the award went to Prof. Purkait, not to the company.
3. **Turnaround.** We assumed 7 to 10 days runs from sample receipt at the lab.
4. **Founder bio.** "More than 15 years of research and teaching", "supervised more than 50 students", "14 patents" and "30 international research articles" come from the current profile page. ORCID currently lists 40 items: about 27 journal articles and reviews, 9 patent or design entries, 1 book and 2 book chapters. We did not repeat the "30 articles" or "14 patents" figures. Please confirm what you want stated.
5. **Founder's titles and affiliations** (ITHS director roles, INNR co-founder) need to be current.
6. **Team list.** Every name, qualification and title is taken from the current About page. Please confirm each person still works with EmbryoGenesis and has given written consent to be listed with a photo.
7. **Mentors and advisors.** Same as above. Several are senior officials at other institutions (AIIMS Patna, Vanderbilt, Astellas). Get written consent and confirm current affiliations.
8. **Dr. Anand Shrivastava (Chairman, GIOSTAR-USA).** GIOSTAR is publicly associated with stem cell therapy. Listing him is factual, but with stem cell therapy on legal hold under the NMC advisory of 5 Sep 2026, ask your legal adviser whether to keep this listing and the GIOSTAR training-partner logo.
9. **Academic structure.** Confirm that Bahra University (Shimla Hills) awards the B.Sc./M.Sc. Clinical Embryology degree, that Rayat Bahra University (Mohali) awards the B.Sc./M.Sc. ART & Clinical Embryology degree, where classes are held, and EmbryoGenesis's exact role. The current Rayat Bahra page also lists a Ph.D. and a PG Diploma; we left these out of the home teaser until confirmed.
10. **Timeline.** The current About page places all four patent entries and the PJ Embryogenesis Foundation under "Feb 2024". We used "2024" pending dates.
11. **Collection centres.** Confirm all three are active, each centre's legal registration, and permission to show their names and logos.
12. **Lab accreditation and registrations.** NABL status, clinical establishment registration and bio-medical waste authorisation (blueprint open item 6).
13. **Receptivity PX.** Whether it is a separate product.
14. **Short courses.** We listed only Biochemistry (semi auto analyser), Molecular Genetics & Bioinformatics, Tissue Processing & Microtomy, and Immunohistochemistry. The other four current courses train in therapies on legal hold and are not mentioned.
15. **Validation data.** We found no peer-reviewed validation study of ERFA, EIT, Endo-Immune or Receptivity PX on the founder's ORCID record. If such data exists, send it; it will strengthen every clinician page. If not, we suggest the line "Validation studies are in preparation for peer review", only if true.

---

## 3. Claims softened or removed (before → after)

| # | Where (current site) | Before | After (our copy) | Why |
|---|---|---|---|---|
| 1 | Footer, every page | "As the best fertility centre, we believe that every dream of starting a family is worth pursuing, and we are here to turn those dreams into reality." | "EmbryoGenesis Diagnostics is a specialised endometrial and reproductive diagnostics lab and academy in Mohali, Punjab. We partner with IVF clinics across India." | Superlative (ASCI, CCPA 2022, IMC 2002 cl. 6.1); not a fertility centre; outcome promise |
| 2 | Home, intro | "Embryogenesis is India's trusted infertility diagnostic and research center, pioneering personalized fertility treatments…" | "EmbryoGenesis is a specialised endometrial and reproductive diagnostics lab and academy. We work with IVF clinicians and hospitals across India…" | Unverifiable "trusted"; therapy reference removed |
| 3 | Home, ERFA card | "Patented diagnostic test to assess endometrial health, improve IVF success…" | "Our in-house assay profiles markers of endometrial receptivity and function. Indian patent application published (No. 202431001616 A)." plus evidence chip "Evidence: emerging. Not for routine use." | "Patented" is inaccurate (Patents Act s.120); "improve IVF success" is not supported (ESHRE, Doyle 2022 RCT) |
| 4 | Home, Endo-Immune card | "Detect immune imbalances affecting pregnancy… offering tailored treatments for recurrent miscarriage" | "Profiles immune markers in the endometrium, including uterine NK cells and cytokines." plus "Evidence: limited." | Treatment promotion removed; ESHRE does not recommend uNK/cytokine testing |
| 5 | Home, EIT card | "Identify and treat hidden infections… ensuring a healthier environment for successful implantation." | "Looks for chronic endometritis, a low-grade inflammation of the uterine lining that often causes no symptoms." plus guideline chip | "Ensuring successful implantation" is an outcome promise |
| 6 | Home, therapy section | Five therapy cards (LIT, PBMC, PRP, Stem Cell, Molecular Hydrogen) with "Book Now" | Removed entirely | Legal hold; NMC stem cell advisory 5 Sep 2026; ESHRE/HFEA |
| 7 | Home, "Why choose" | "Leaders in innovative reproductive health diagnostics… we transform infertility journeys into paths of hope and success" | "Why IVF clinics partner with us" with six factual points | Superlative and outcome language |
| 8 | Home, testimonials | "Real Stories, Real Smiles: Our Patients Speak" + broken `[grw]` shortcode | Removed | No testimonials (brief guardrail 6; NMC framework Oct 2026) |
| 9 | Home, academy | "Learn from top experts"; "state-of-the-art laboratory" | Factual list of programmes, awarding universities and course topics | Superlatives; ASCI education guidelines |
| 10 | About, hero | "a leader in cutting-edge infertility research and diagnostics" | "a specialised endometrial and reproductive diagnostics lab and academy" | Unverifiable leadership claim |
| 11 | About, vision | "To be the leading force in infertility diagnosis… As the 'Best Innovation Awardee' and best fertility diagnostic centre in India… making dreams of the family a tangible reality for all." | "A fertility evaluation in India where every couple's doctor can access specialised endometrial testing close to home, choose tests on the basis of evidence, and work with well-trained embryology teams." | Superlative; award misapplied to the centre; outcome promise |
| 12 | About, "Who we are" | "state-of-the-art facility… stands as a beacon of hope" | "We are a young organisation. We say clearly what our tests can and cannot do…" | Puffery |
| 13 | About, timeline | "ERFA – The Soil Test (Patent)", "LIT-H2 Antioxidant Therapy (Patented)", "LIT-H2 Anti-Oxidant Kit (Patent)", "Receptivity PX test (Patent)" | "Indian patent applications published for ERFA (No. 202431001616 A) and Receptivity PX (No. 202411059621 A)". LIT-H2 entries removed. | "Patented" inaccurate; LIT/H2 on legal hold |
| 14 | About, award heading | "'Best Innovation Award for Human Infertility Treatment'" shown as a company headline | Award listed under the founder's name, with issuer and date, pending confirmation | ASCI awards guideline: name, issuer, year; must not imply it covers the whole centre |
| 15 | About, team | "Stem Cell Scientist" (Dr. Kumar Abhiram Jha); "Stem Cell Biologist" (Ms. Nancy Saini) | "Research Scientist"; "Research Biologist", each marked `{{CONFIRM_TITLE}}` | Avoids any implied stem cell service while on legal hold. Client to confirm or choose other neutral titles. |
| 16 | Diagnostic page, ERFA | "a groundbreaking diagnostic tool… pinpoint factors affecting fertility and implantation success" | "Endometrial Receptivity and Function Assay… for selected cases on clinician advice", with ESHRE/HFEA status | "Groundbreaking" puffery; unsupported claim |
| 17 | Diagnostic page, Endo-Immune | "Offers targeted insights for immune-modulatory treatments" | No treatment reference; evidence status "Limited" | Therapy link; ESHRE "not recommended" |
| 18 | Diagnostic page, EIT | "Ensure your endometrium is prepared for a healthy pregnancy with our EIT." | "The test does not tell you why a past cycle did not work, and it cannot promise a better result next time." | Outcome promise |
| 19 | Diagnostic page, FAQ | "Will these tests help if I've already had IVF treatments? Absolutely." | "Will these tests improve my chance of pregnancy? No test can promise that." | Overclaim |
| 20 | Diagnostic page, "Why choose" | "Cutting-Edge Technology… at the forefront of reproductive science"; "ensuring accurate, individualized results" | Not used. Quality section states what we actually do (signed reports, QM, SOPs). | Unverifiable |
| 21 | Diagnostic page, CTA | "Book Your Test Today" (tel: link aimed at patients) | Patients: "Our tests are ordered by your doctor." Clinicians: "How to order". | Doctor-ordered model; IMC 2002 cl. 6.1 solicitation |
| 22 | Courses / ART page | "World-Class Curriculum", "globally renowned embryologists", "patented technologies", "Strong Collaborations: Partnerships with top fertility clinics" | Not used on these pages. Academy teaser lists programmes factually. | Superlatives; "patented"; ASCI education guidelines |
| 23 | Titles and meta | "Best Infertility Diagnostics in India"; "India's most accurate infertility diagnostics"; "Best Infertility Diagnostic Center in India" | New titles and meta descriptions on each page, with no superlatives | ASCI / CCPA |

---

## 4. Compliance decisions in this copy

1. **Evidence chips.** Every test card and the clinician test menu carries an evidence status that matches ESHRE: EIT "guideline-supported"; ERFA and Receptivity PX "emerging"; Endo-Immune "limited". This follows brief guardrail 3 and research doc section 2.2. If the client wants softer wording on the Endo-Immune chip, it still cannot claim support that ESHRE does not give.
2. **Antibiotics.** The EIT evidence box quotes ESHRE's line "If CE is diagnosed, treatment with antibiotics can be considered", and summarises two outcome studies. This is guideline content, not an EmbryoGenesis therapy. On the patient side we say only that the doctor decides on treatment. Flag for Prof. Purkait in case he prefers to drop the antibiotic quote.
3. **No referral commissions.** The partner page states that we do not pay commissions for referrals, and that any fees relate to defined services. IMC Regulations 2002, clause 6.4 (still in force while the 2023 NMC regulations are in abeyance) prohibits rebates and commissions for patient referral. **Legal adviser must approve this wording and the actual partner fee model.**
4. **Founder title.** We use "Prof. (Dr.) Pulakes Purkait, M.Sc., Ph.D." as in the brief, and add a line on the About page that he is a research scientist, not a registered medical practitioner. We do not use the `Physician` schema type for him.
5. **DPDP.** The partner and clinician forms carry a full itemised notice, a required unticked consent box, an optional unticked marketing box, withdrawal and grievance routes, and a "no patient data" warning. No form values go to analytics or ad pixels.
6. **Prices.** None anywhere. "Partner rate card on request" for clinics; "ask your clinic" for patients.
7. **Therapies.** Not mentioned on any of the five pages, including the four therapy-related short courses.
8. **Signature line.** Each file ends with the exact line requested, "Draft prepared by TechnoTaau Team — scientific review pending: Prof. (Dr.) Pulakes Purkait". It contains the only em dash in the drafts, kept verbatim as instructed.

---

## 5. Evidence checked on 15 Oct 2026 (primary sources)

| Statement used in copy | Source checked | Result |
|---|---|---|
| ESHRE: CE assessment "can be considered"; antibiotics "can be considered"; diagnosis by hysteroscopy, H&E and CD138; lack of standardisation | ESHRE RIF GPR 2023, Hum Reprod Open hoad023 (PMC10270320) | Confirmed verbatim |
| ESHRE RIF definition | Same | Confirmed (paraphrased) |
| ESHRE: insufficient data for routine commercial receptivity tests; uNK, pNK and blood cytokine testing not recommended | Same | Confirmed |
| ESHRE RPL 2022: CE prevalence 7 to 58% by method; research needed before screening can be recommended; CD138 IHC "seems to be" the gold standard | ESHRE RPL guideline 2022, full PDF, section 1.4 and anatomy chapter | Confirmed |
| ESHRE RPL 2022: cytokine testing should not be used (strong); insufficient evidence for NK testing (strong) | Same | Confirmed |
| ESHRE add-ons: receptivity tests not recommended; peripheral immune and uNK testing not recommended; definition of "not recommended" | ESHRE add-ons GPR 2023, Hum Reprod dead184 (PMC10628516) | Confirmed. The paper makes no recommendation on CE testing. |
| HFEA ratings: endometrial receptivity red; microbiome testing grey; page last reviewed 28 Sep 2026 | hfea.gov.uk treatment add-ons page | Confirmed |
| Doyle 2022 RCT: 58.5% vs 61.9% live birth, no benefit | JAMA 2022;328:2117 (secondary summaries; JAMA key points) | Confirmed. Sources quote 767 randomised; JAMA key points cite 978 enrolled. We say "767 patients". Reviewer may prefer "a 2022 randomised trial" without the number. |
| Vitagliano 2018 meta-analysis: higher live birth when CE cured vs persistent; 5 studies, 796 patients; observational | Fertil Steril 2018;110:103 (abstract-level sources) | Confirmed at abstract level |
| Huang 2026 cohort: 1,401 women, 3,041 cycles, no significant live-birth improvement with antibiotics | Front Cell Dev Biol 2026;14:1749173 (PMC12910471) | Confirmed |
| Santoro 2023: no agreed threshold; ≥5/10 HPF associated with miscarriage risk | Biomedicines 2023;11:1714 (PMC10296269) | Confirmed |
| CE often has few symptoms | Kitaya 2016, Am J Reprod Immunol 75:13 (abstract) | Confirmed at abstract level |
| Founder publications, patent entries | ORCID public API, 0000-0002-8814-9939 | 40 items listed; no assay validation paper found |

Not verified, and therefore not used: specific CE symptom lists; the effect of cycle phase on CD138 counts (studies vary, so timing is left to the client's protocol); any EmbryoGenesis outcome or accuracy figures.

---

## 6. Style and QA self-check

- One H1 per page; SEO titles 54 to 59 characters; meta descriptions 143 to 155 characters (counted by script).
- No "best", "No. 1", "leading", "trusted", "guaranteed", "revolutionary", "cutting-edge", "state-of-the-art" or "patented" in page copy. Exceptions: the proper names of the founder's awards ("Best Innovator Award"), and disclaimers that say we do "not guarantee" outcomes. Otherwise these words appear only in section 3 of this file and in developer notes, as quotes of the old text.
- No prices, testimonials, therapy names (outside notes), sex-selection terms, or pregnancy promises.
- Every medical page has a reviewer line, references and a disclaimer.
- Items for Prof. Purkait's review are marked `{{CONFIRM}}` or listed in section 2.

---

Draft prepared by TechnoTaau Team — scientific review pending: Prof. (Dr.) Pulakes Purkait
