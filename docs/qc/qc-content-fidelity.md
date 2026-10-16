# QC: Content Fidelity & Compliance

**Prepared by:** TechnoTaau Team (Content Fidelity & Compliance Controller), for Jakhar Singh
**Date:** 16 October 2026
**Scope:** the 19 built pages in `site/src/pages/*.html`, checked against the old live pages (`content/source/old-site-html/`, saved 15 Oct 2026), `website-content-doc-2024.txt`, `company-brochure-2024.txt` and `erfa-brochure.txt`.
**Client rule:** keep the old website's content as it is; only the design changes.
**Result:** after fixes, every substantive sentence, list item, fee, eligibility line, phone number and address from the old pages is on the new site. `python3 site/build.py` builds 19 pages; `python3 site/qc.py` reports **0 errors, 0 warnings**. Nothing committed.

---

## 1. Method

- **Extractor** (`/tmp/claude-0/-home-user-emb/b14c7f6e-a696-51d0-a38b-d172266186db/scratchpad/fid/extract.py`): parses the old WordPress HTML and the built `site/dist/` pages (run with `python3 -I`, data only). It takes only the `<main>` element and skips scripts, styles, SVG and `<select>` options. Block elements become separate text blocks.
- **Sentence diff** (`/tmp/claude-0/-home-user-emb/b14c7f6e-a696-51d0-a38b-d172266186db/scratchpad/fid/diff.py`): splits blocks into sentences (abbreviation-aware: Dr., Prof., M.Sc., etc.) and normalises them (NFKC, curly quotes, dashes, `&`→`and`, punctuation removed, lower case, whitespace collapsed).
  - **Coverage:** each old sentence is searched for in the new page's text.
  - **Additions:** each new sentence is searched for in the matching old page, then in all old pages, then in the three text sources. A sentence found nowhere is flagged `NOT-IN-SOURCES`.
- **Strict pass** (`/tmp/claude-0/-home-user-emb/b14c7f6e-a696-51d0-a38b-d172266186db/scratchpad/fid/strict.py`): repeats the check with only whitespace and quotes normalised, to catch case and punctuation edits.
- **Claim scan** (`/tmp/claude-0/-home-user-emb/b14c7f6e-a696-51d0-a38b-d172266186db/scratchpad/fid/risk.py`): keyword scan for superlatives, "patent", stem cell, testimonials, statistics and AI sources.
- I reviewed every `MISSING` and every `NOT-IN-SOURCES` line by hand. The outputs are `out_all.txt` (before fixes) and `out_after.txt` (after fixes) in the same folder.

## 2. Coverage per page (after fixes)

"Raw" is the script's figure. "Content" excludes WordPress template text that is not page content:
- the "By embryosys" bylines;
- Previous/Next post links;
- the comment form;
- the `[grw id=1198]` shortcode;
- `<select>` options, which the extractor skips although they are present;
- headings that were rephrased as questions, which is allowed.

| Page (old → new) | Old sentences | Raw coverage | Content coverage | Notes on what is not matched |
|---|---|---|---|---|
| home | 58 | 98.3% | 100% | `[grw id=1198]` Google Reviews shortcode. The section and heading are kept with a placeholder (see 8.4). |
| about | 122 | 99.2% | 99.2% | Heading "Our Patents". On the old site this was an image-only carousel of seven AI-generated images with no captions, so there was no text to carry over. Patents remain in the Road Map and on the founder page. Not restored: decision for the client. |
| diagnostic | 56 | 98.2% | 100% | "Who is it for?" is now "Who is ERFA for?" (allowed). |
| advanced-fertility-therapies | 66 | 100% | 100% | |
| courses | 8 | 100% | 100% | |
| bsc-in-clinical-embryology-in-bahra-university | 44 | 95.5% (was 90.9%) | 100% | The two unmatched lines are `<select>` options that are present. "GET Location" and "Call Now" are restored. |
| art-and-clinical-embryology-in-rayat-bahra-university | 58 | 100% (was 98.3%) | 100% | "Call Now" restored. |
| skill-development-training | 38 | 100% (was 97.4%) | 100% | "Call Now" restored. Tissue Processing eligibility corrected. |
| blog | 9 | 66.7% (was 55.6%) | 100% | The old listing excerpts ended in "…". The new cards carry longer excerpts from the same posts. The only parts not reused are the auto-excerpt labels "परिचय (Introduction)" and "Introduction:" and the truncated word "Uncover…". |
| Endometrial Immune Profiling post | 69 | 97.1% | 100% | Byline "By embryosys" is now "By EmbryoGenesis". Prev/Next links are not used. |
| ERFA post (`x_erfa`) | 50 | 94.0% | 100% | Same. |
| Hindi IVF-failure post | 70 | 95.7% | 100% | Same. |
| LIT post | 30 | 90.0% | 100% | Same. |
| Unexplained Infertility post | 93 | 88.2% | 100% | Same, plus the WordPress comment form. |
| pulakes-purkait-profile | 75 | 98.7% | 100% | "Brief Biography:" is now "Who is Prof. (Dr.) Pulakes Purkait?" (allowed). |
| media-event | 2 | 100% | 100% | The old gallery loaded by JavaScript and is not in the saved HTML. The new items come from the "Media & Event" section of `website-content-doc-2024.txt`. |
| contact-us | 15 | 100% (was 93.3%) | 100% | Address restored to the old wording. |
| privacy-policy | 1 | 100% | n/a | The old page had a heading only (see 8.5). |

Not in scope (old pages with no new page; for the client to decide): `p_diagnostic-services`, `p_research-and-training`, `p_apply-now`, `p_clinical-embryology-scholarship`.

## 3. What I restored or fixed (page bodies only)

| # | Page | Change | Why |
|---|---|---|---|
| 1 | skill-development-training | Tissue Processing & Microtomy eligibility is now "B.Sc. MLT, M.Sc., Ph.D., **MBBS, MD**, Faculty of Life Science, Allied Health Science", in the card and in the comparison table. I removed the extra answer-box line that said this course excludes MBBS/MD. | The old live page shows MBBS, MD for all eight programmes. The builder had followed the 2024 content doc, which differs. Old site wins. |
| 2 | bsc-in-clinical-embryology… | Restored "GET Location" (old link `maps.app.goo.gl/MzufZM8oX22hSCQi9`) under the Admission Office. | Missing from the new page. |
| 3 | bsc…, art…, skill-development-training | Restored the "Call Now" button in the ADMISSION HELP LINE box, dialling **+91 9599877196** as on the old site. | Missing from the new pages. Note: on the old site this button dials the director's number, which is not one of the listed help-line numbers on the BSc and ART pages. **Client to confirm** which number "Call Now" should dial. |
| 4 | contact-us | Visit address is now "Top Floor, Rayat Bahra Dental College & Hospital, Mohali, Punjab" (old wording, same as the footer). | The builder's "…, Rayat Bahra University Campus, Kharar, Mohali, Punjab" matched no source exactly. |
| 5 | about | Key facts "Location" now uses the same old-site address. | One address form everywhere in the page bodies. |
| 6 | blog | Removed the invented tagline "Infertility Research Centre - Get Informed". | Not in any source. Category (c). |
| 7 | blog | The featured Endometrial Immune Profiling card now uses the old blog-listing excerpt: "Discover Endometrial Immune Profiling - advanced fertility testing for IVF failures & recurrent pregnancy loss." | Restores the old listing text. The home page already uses it. |
| 8 | blog, Hindi post | Date "9 जुलाई 2024" is now "July 9, 2024" (marked `lang="en"`). | The old site shows the English date. The builder had translated it. |
| 9 | media-event | Himachal Tonite item restored to the content-doc wording: "Bahra University, Waknaghat (HP), in partnership with the Institute of Translational Health Science (ITHS) and EmbryoGenesis – Infertility Diagnostic & Research, has announced the launch of Himachal Pradesh's first comprehensive Clinical Embryology program." | The builder had rewritten and shortened it. |
| 10 | about | Alt text on `lab.jpg` is now "Diagnostic laboratory bench with microscopes and lab equipment". | It is an Unsplash stock photo (Trnava University). The alt claimed it was the EmbryoGenesis laboratory, which is misleading. |
| 11 | home | Alt text on `lab-bench.jpg` is now "Gloved hand pipetting a sample into test tubes in a laboratory". | Stock photo (CDC). The alt claimed "the EmbryoGenesis laboratory". |

## 4. Factual consistency (all page bodies)

| Item | Value on site | Status |
|---|---|---|
| Lab / main phone | +91 8146217196 | Consistent. Same as old site and brochure. |
| Director phone | +91 9599877196. The profile page shows "+91 95998 77196", the old format. | Consistent. |
| Admissions | +91 9691736435, +91 9815692195 | Consistent. |
| Emails | info.embryogenesis@gmail.com, embryogenesis.laboratory@gmail.com (contact); director@embryogenesis.in, director@translationalhealthscience.in, purkaitpulakes@gmail.com (profile) | Consistent with the sources (see 6.2 for the profile). |
| Centre address | "Top Floor, Rayat Bahra Dental College & Hospital, Mohali, Punjab" | Consistent in all bodies after fixes 4 and 5. Home also has the brochure-based line "…at the Rayat Bahra University campus in Mohali". |
| ITHS admission office | "Institute of Translational Health Science, Top Floor, Rayat Bahra Dental College & Hospital, Rayat Bahra University, Mohali, Punjab, India" | Consistent (courses, art, skill). |
| Established | Nov 2023 / November 2023 | Consistent. |
| Award | "Best Innovator Award for Human Infertility Treatment…, 27th Nov 2024" (Road Map, keyfacts, media) and "Best Innovation Award for Human Infertility Treatment" (hero cards) | Both forms are the client's own wording. **Client to choose one.** |
| ERFA patent application | 202431001616 A | Consistent (diagnostic, profile). |
| Fees | BSc ₹39,875 per semester; MSc INR 1,00,000/- Per Semester; training 1000/-, 7000/-, 5000/-, 20,000/-, 20,000/-, 25,000/-, 15,000/-, 35,000/- | Identical to the old pages everywhere. |
| Durations | BSc 4 Years; MSc 2 Years (4 Semesters); ART B.Sc. 4 / M.Sc. 2 / Ph.D. 3-4 / PG Dip 1 Years; training 1–5 Days | Identical. |
| Names and titles | "Prof. (Dr.) Pulakes Purkait, Founder & Director"; "Dr Vidhu Wadhwa, MBBS MD Pathology" | Consistent. |
| Collection centres | Mumbai (Navi Mumbai address), Udaipur, Jalandhar | Consistent with the old site. |

## 5. Builder typos

- I found **no builder-introduced typos** in the added text.
- Builders made two small corrections to the client's punctuation. I kept both:
  - closed the bracket in "recurrent pregnancy loss (RPL)";
  - changed "B Sc." to "B.Sc." on the course card.

**Client wording kept as-is (list for the client to correct if they wish):**
- "ERFA – The SoiL Test" (diagnostic page quote).
- "1 Days", "1 Years".
- "14 patent".
- "He established many premier institute…".
- "reputed organization".
- "contributed to the scientific world at his best".
- "Vishakhapatnam" (profile) vs "Visakhapatnam" (about).
- "Mareland Hills, Ohio" (probably Moreland Hills).
- "Kochin".
- "Sedeer Medical, Doha".
- "Pro. (Dr.) Simerjit Kaur".
- "Robotize Smart waste management system".
- "Batsalya IVF, Bikaner" (the brochure says "Vatsalya").
- "Dr.Pulakes Purkait".
- "Innovation" vs "Innovator" (see section 4).
- The Courses page's "Why Choose Embryogenesis?" text talks about diagnostic services, not courses.

## 6. Additions register (sentences on new pages that are not on the old page)

### 6.1 Category (a): allowed, UI and structure (not listed one by one)

- Breadcrumbs.
- Eyebrows and section labels, e.g. "Key facts", "Admissions", "Compare", "Test 1/2/3", "Contents" / "विषय-सूची (Contents)".
- Question-style headings that rephrase existing headings. This covers 31 headings, for example:
  - "Who is ERFA for?"
  - "What are the key benefits of LIT Therapy?"
  - "Who can apply for the BSc in Clinical Embryology?"
  - "How long is the Ph.D. in ART & Clinical Embryology?"
  - "Who is Prof. (Dr.) Pulakes Purkait?"
- Form labels ("Name (required)", "I am interested in", "Select test/therapy/programme"), consent lines ("I agree to the Privacy Policy.", "By clicking "Book Now", you agree to our Privacy Policy.") and form status messages ("Thank you. We will contact you shortly.", "Our admissions team will call you.").
- Buttons and links: "Book Now", "View Course", "Read more", "Apply Now", "Download Brochure (PDF)", "View all…", "See all media & events", "← Blog".
- Hidden link context ("Read more: …").
- Table caption and hint ("Swipe/Scroll the table sideways…").
- "Related at EmbryoGenesis" boxes on the 5 posts.
- Team-member initials avatars (JG, JN, RS…).
- Blog filter chips. "Reproductive Immunology" and "Fertility Testing & Diagnostics" are real WordPress categories of the Endometrial Immune Profiling post. The builder also assigned them to the Hindi, LIT and Unexplained posts, which were "Uncategorized" on the old site.
- Section headings: "Our Patents & Recognition", "Media Coverage & Events", "Explore more programmes", "Latest articles" (hidden), "EmbryoGenesis at a glance", "Education and experience at a glance".
- Media lead: "News, awards, MOUs and appreciation of EmbryoGenesis – Infertility Diagnostic & Research, Mohali".
- Courses note: "Fees are shown where they are published; for other programmes, please contact the admission office."

### 6.2 Category (b): acceptable factual additions taken from the sources

| Page | Added text | Source |
|---|---|---|
| home | "EmbryoGenesis – Infertility Diagnostic & Research is an infertility diagnostic and research centre at the Rayat Bahra University campus in Mohali, Punjab, India." | Brochure (name and address). |
| home | Key facts: "November 2023, Mohali, Punjab"; test list; "Typically within 7-10 days, depending on the test"; "Navi Mumbai, Udaipur, Jalandhar" | Old About Road Map, old diagnostic FAQ, old collection centres. |
| home | Care pathway: "Comprehensive consultation / Each test includes a comprehensive consultation."; "Simple collection process / A simple collection process."; "Results in 7-10 days / A detailed explanation of results."; "Personalized therapy / Therapies at our Mohali centre." | Split from the old FAQ answer. "Therapies at Mohali" was confirmed by Jakhar Singh on 15 Oct (`docs/strategy/00-business-model.md` §6) but is **not in the client sources**. Client to confirm. |
| home | Tiles "Our Patents: ERFA – The Soil Test"; "Scientific Team: MBBS MD Pathology"; "Visit our Mohali centre …"; "Our Collection Centre: Mumbai · Udaipur · Jalandhar" | Old site facts. |
| home | FAQ (3 Q&As) | Old diagnostic page, verbatim. |
| about | "What is EmbryoGenesis?" (heading); "Explore our diagnostic services, therapeutic services and academic programs." (internal links) | Navigation sentence. |
| about | Key facts: Established, Location, Founder, Consultant Pathologist, Collection centres, Academic partners ("Rayat Bahra University, Bahra University (with ITHS)"), Recognition | Old About and brochure. |
| about | Hero card "27th Nov 2024 · Research & Innovation Park, New Delhi"; "Appreciation of EMBRYOGENESIS" | Old Road Map; content doc. |
| diagnostic | "EmbryoGenesis, an infertility diagnostic and research centre in Mohali, Punjab, offers three endometrial tests: ERFA – The Soil Test, the Endo-Immune Test and the Endometrial Infection Test (EIT)." | Old page plus the brief's entity line. |
| diagnostic | ERFA key facts: sample type; "Curettage procedure (D&C) or needle biopsy"; Day 21–23 (Preferred 21st day); LH+7 to LH+9; P+6 to P+8; "7 endometrial factors…"; "Patent application No. 202431001616 A"; "A complete pathology report requires an accurate time for biopsy sampling…" | `erfa-brochure.txt`, verbatim or near-verbatim. |
| therapies | "…also offers immunomodulation, antioxidant and regenerative therapeutics: LIT Therapy, PBMC Therapy, PRP Therapy, Stem Cell and Molecular Hydrogen therapy." | `website-content-doc-2024.txt` line 211. |
| therapies | "Therapies are given at our Mohali centre." | Client answer of 15 Oct, not in the sources. Client to confirm. |
| courses | Entity sentence; "Which courses does EmbryoGenesis offer?" answer; programme cards; comparison table; "1 to 4 Years, depending on the programme"; "B.Sc. · M.Sc. · Ph.D. · PG Diploma · Shimla Hills & Mohali"; both admission offices; "ADMISSION HELP LINE: +91 9691736435 / 9815692195" | Old BSc and ART pages; content doc. |
| bsc / art / skill | Entity sentences, key-facts lists, hero fact chips ("Seat in Batch: 10 · 1 to 5 Days · 8 programmes"), "Fee: 1000/- to 35,000/-" | Old pages. |
| blog | Entity sentence ("Articles from EmbryoGenesis, an infertility diagnostic and research centre in Mohali, Punjab, on …"); sidebar "Prof. (Dr.) Pulakes Purkait, Founder & Director, Reproductive Geneticist." | Old posts and profile. |
| blog | Two extra cards (LIT, Unexplained) with excerpts from the posts | Old posts. |
| posts | Byline "By EmbryoGenesis" (old: "By embryosys", a WordPress user name) | Acceptable; the client may prefer the founder as author. |
| profile | "Prof. (Dr.) Pulakes Purkait is the Founder & Director of EmbryoGenesis, an infertility diagnostic and research centre in Mohali, Punjab. He is a Reproductive Geneticist with more than 15 years of research and teaching experience in Molecular and Medical Genetics." | Merges two existing sentences of the biography. |
| profile | "Education and experience at a glance" key facts ("Vidyasagar University, West Bengal" expands "WB"); "Best Innovator Awardee: NBHC 2024 at IIT Delhi" also added to the Award list | Old biography. |
| profile | Official Emails show **director@embryogenesis.in**, info.embryogenesis@gmail.com, director@translationalhealthscience.in | `website-content-doc-2024.txt`. The old page listed director@translationalhealthscience.in twice, and the first link actually opened **drpurkait@embryogenesis.in**. Client to confirm which mailbox is live. |
| profile | ResearchGate link `researchgate.net/profile/Pulakes-Purkait` | The old link went to a generic directory page. Builder-supplied URL; verify. |
| profile | "The ERFA test is offered at EmbryoGenesis as ERFA – The Soil Test; read more in …"; "(see B.Sc. / M.Sc. …)" link notes; CTA "Contact EmbryoGenesis to learn more about our diagnostic services, courses and lab training." | Internal links. |
| media | Ten items: Times of India (3 Jul 2024), Himachal Tonite (6 Jul 2024), News Nation (27 Jul 2024), Award (27 Nov 2024), MOUs (Guru Ghasidas Vishwavidyalaya, GIOSTAR USA, Indira IVF Udaipur, Batsalya IVF Bikaner, Parul IVF Ahmedabad), Appreciation | Content doc "Media & Event" and the old About Road Map. Publication names are taken from the article URLs. |
| contact | "Contact EmbryoGenesis – Infertility Diagnostic & Research, Mohali, Punjab, to book a diagnostic test, ask about therapies, or enquire about courses and lab training."; "Admissions: 9691736435 / 9815692195"; "I am interested in" field | Entity line and old phone numbers. |

### 6.3 Category (c): not allowed, fixed

1. Blog tagline "Infertility Research Centre - Get Informed": removed.
2. Himachal Tonite headline rewritten by the builder: restored.
3. Tissue Processing eligibility changed from the live site: restored.
4. Stock-photo alt texts claiming "EmbryoGenesis laboratory": neutralised.
5. Hindi date translation: restored.

### 6.4 Category (c), pending: added by TechnoTaau Team builders, kept, **needs client approval**

| Page | Exact text |
|---|---|
| diagnostic | "Information only. Testing is ordered and interpreted by your treating doctor." |
| advanced-fertility-therapies | "Information only. Treatment decisions are made with your treating doctor." |
| endometrial-immune-profiling…, erfa-the-soil-test…, exploring-lit-therapy…, unexplained-infertility | "Information only. Testing and treatment are ordered and interpreted by your treating doctor." |
| tips-and-treatments… (Hindi) | "यह जानकारी केवल शैक्षिक उद्देश्य के लिए है। कोई भी टेस्ट या उपचार आपके डॉक्टर की सलाह पर ही कराएँ।" |
| contact-us | "WhatsApp: +91 8146217196". The old site had no WhatsApp. The header and footer partials also use it. The brief lists it as "proposed, to confirm". |
| home, therapies | "Therapies at our Mohali centre." / "Therapies are given at our Mohali centre." (see 6.2) |
| privacy-policy | Placeholder: "The Privacy Policy of EmbryoGenesis – Infertility Diagnostic & Research, Mohali, Punjab, is being prepared and will be published on this page. Until then, … please email info.embryogenesis@gmail.com." |
| home | Visible text "Google Reviews widget (to be reconnected in WordPress after legal review)". This internal note shows on the public page (see 8.4). |

## 7. Compliance register (risky claims kept as the client instructed; not changed)

### 7.1 Superlatives and unverifiable leadership claims

| Page | Exact text |
|---|---|
| about | "As the "Best Innovation Awardee" and best fertility diagnostic centre in India, we aspire to redefine possibilities, pioneer breakthroughs, …" |
| about | "To be the leading force in infertility diagnosis, …" |
| about | "Our infertility diagnostic centre is a leader in cutting-edge infertility research and diagnostics, …" |
| about | "… our diagnostic centre stands as a beacon of hope …"; "With years of experience, a state-of-the-art facility …" |
| home | "Embryogenesis is India's trusted infertility diagnostic and research center, pioneering personalized fertility treatments and education programs for global excellence." |
| home, therapies | "Our center leads in reproductive health diagnostics, …" |
| home | "As a leader in advanced infertility diagnostics and research, …"; "Leaders in innovative reproductive health diagnostics."; heading "Leaders in Fertility Diagnostics and Research" |
| home, courses | "Learn from top experts." |
| diagnostic | "… our diagnostics are at the forefront of reproductive science."; "The ERFA, or Endometrial Soil Test, is a groundbreaking diagnostic tool …" |
| therapies | Heading "Explore Our Pioneering Therapeutic Solutions for Reproductive Health"; "… supported by the most advanced medical science available." |
| bsc | "… a leader in infertility diagnostics and ART research." |
| art | "Guidance from globally renowned embryologists, researchers, and clinicians."; "Partnerships with top fertility clinics, IVF centers, and research institutes worldwide."; "World-Class Curriculum" |
| Hindi post | "… आपको सर्वोत्तम डायग्नोस्टिक और थेराप्यूटिक टेस्ट प्रदान करते हैं …" ("best") |
| media | "… Himachal Pradesh's first comprehensive Clinical Embryology program." This quotes a news item. |

### 7.2 "Patent" / "patented" (the brief requires "patent application published")

| Page | Exact text |
|---|---|
| home | "Patented diagnostic test to assess endometrial health, improve IVF success, …" (ERFA card) |
| about (Road Map, Feb 2024) | "ERFA - The Soil Test (Patent)"; "LIT -H2 Antioxidant Therapy (Patented)"; "LIT -H2 Anti-Oxidant Kit (Patent)"; "Receptivity PX test ( Patent)" |
| ERFA post | "The ERFA – The Soil Test, a patented groundbreaking endometrial tissue (biopsy) assessment tool …" |
| art | "Opportunity to engage in cutting-edge research projects and patented technologies." |
| profile | "14 patent"; heading "Patent"; application numbers shown as "Patent No.202411059621 A", "Patent No.202411037742 A", "Patent No.202431001616 A", "Patent No.202211073981 A", "Patent No.202311076252 A", "Patent No.202421004316 A" (these are application numbers); five "Applied on …" entries |
| media | "Cutting-Edge Digital Biothesiometer Gains Design Patent, …" (news headline) |
| home | Section heading "Our Patents & Recognition"; tile "Our Patents: ERFA – The Soil Test". **Builder-added wording**; the diagnostic page correctly says "Patent application". Recommend "Patent application published". |

### 7.3 Therapy promotion, including stem cell (therapy pages are held pending legal review)

| Page | Exact text |
|---|---|
| advanced-fertility-therapies | The whole page, including: |
| | "Stem Cell Therapy is at the forefront of regenerative medicine, offering new hope for those facing gynecological disorders or infertility. Human mesenchymal stem cells (hMSCs) can differentiate and repair damaged tissues, making them invaluable for treating conditions like premature ovarian failure and primary ovarian insufficiency." |
| | "Repairs and rejuvenates reproductive tissues" |
| | "Offers solutions for both male and female infertility" |
| | "Find out how our revolutionary stem cell therapy can make a difference in your fertility journey." |
| | PRP: "Non-invasive and safe, with minimal risk" (PRP involves an injection) |
| | LIT: "Increases the likelihood of successful conception" |
| | Hydrogen: "Recent studies have shown hydrogen's significant benefits in reproductive health, including enhanced tissue support and improved embryo quality." (unreferenced) |
| | FAQ: "Yes, all of our therapies are designed with safety and efficacy in mind. They are supported by extensive research and performed by experienced medical professionals." |
| home | All five therapy cards with "Book Now", including "Harness the regenerative power of stem cells … Our advanced therapy offers hope for couples seeking innovative solutions." |
| home, diagnostic | "Explore advanced therapies like LIT Therapy, Stem Cell Therapy, PRP, and Molecular Hydrogen Therapy." |
| skill-development-training | "Hands-on Training on Stem Cell Processing & Cryopreservation" (35,000/-); PRP/LIT and Hydrogen therapy trainings |
| Hindi post | LIT, PRP and Stem Cell Therapy described as EmbryoGenesis treatments ("स्टेम सेल थेरेपी से प्रजनन अंगों की मरम्मत और पुनर्निर्माण में मदद मिलती है।") |
| LIT post | The whole post promotes LIT (see 7.5). |
| 5 posts | "Related at EmbryoGenesis" box: "Therapeutic: LIT, PBMC, PRP, Stem Cell and Molecular Hydrogen Therapy". **Builder-added** cross-link that names stem cell therapy on posts that did not mention it (e.g. ERFA, Unexplained). Recommend shortening to "Therapeutic Services" if legal advises. |
| about, media | GIOSTAR (stem-cell company): "Dr. Anand Shrivastava, Chairman, GIOSTAR-USA"; "MOU with GIOSTAR, USA"; image alt "EmbryoGenesis brochure handed over at GIOSTAR" |

### 7.4 Testimonials

| Page | Exact text |
|---|---|
| home | Heading "Real Stories, Real Smiles: Our Patients Speak", label "Testimonials", and the reviews widget slot (old `[grw id=1198]`). No reviews are shown. |

### 7.5 Unreferenced statistics and outcome claims

| Page | Exact text |
|---|---|
| LIT post, blog excerpt | "… recurrent pregnancy loss (RPL), affecting approximately 5% of women." |
| LIT post | "… certain groups of patients have shown promising outcomes with an 8-10% increase in live birth rates. This suggests a significant potential for LIT in improving pregnancy success rates …" |
| LIT post | "Increased Live Birth Rates: …"; "With studies indicating a rise in live birth rates and a profile of minimal invasiveness and low side effects, …" |
| Unexplained post | "A study by the National Institute of Health (NIH) showed that 92% of couples with unexplained infertility who received fertility treatment had a child." |
| home | ERFA card "… improve IVF success …" |
| ERFA post | "… we can greatly improve the chances of successful pregnancy and implantation." |
| Endometrial Immune Profiling post | "… which often leads to better outcomes in subsequent IVF cycles or natural conceptions." |
| Hindi post | LIT "… सफल गर्भधारण की संभावना बढ़ाती है।" |

### 7.6 AI-generated source and missing references

| Page | Exact text |
|---|---|
| Unexplained post | "Source : chat GPT , google gemini" |
| All 5 posts and the therapy page | No references. CLAUDE.md requires references and a disclaimer reviewed by Prof. (Dr.) Pulakes Purkait. The disclaimers are pending (6.4); references are missing. |

## 8. Changes needed in files I do not own

1. **`site/src/pages/skill-development-training.json`** (Course schema): Tissue Processing & Microtomy eligibility should read "B.Sc. MLT, M.Sc., Ph.D., MBBS, MD, Faculty of Life Science, Allied Health Science" to match the restored page.
2. **`site/src/pages/media-event.json`**: the Himachal Tonite headline in the schema still has the shortened builder wording. Use the restored content-doc sentence from fix 9.
3. **Address (NAP):**
   - Visible text (footer partial and all bodies) uses the old-site form: "Top Floor, Rayat Bahra Dental College & Hospital, Mohali, Punjab".
   - `build.py` ORG schema now uses the brochure form ("…Rayat Bahra University Campus, VPO Sahauran, Tehsil Kharar…").
   - `contact-us.json` description says "Rayat Bahra campus, Kharar".
   - Recommendation: the client confirms one full address (brochure, PIN 140302), then the footer, schema, Google Business Profile and Contact page all use it.
4. **WhatsApp**: `partials/header.html` and `partials/footer.html` show WhatsApp +91 8146217196, and `contact-us.json` says "call or WhatsApp". This was not on the old site; client to confirm.
5. **Home testimonials placeholder**: the visible text "Google Reviews widget (to be reconnected in WordPress after legal review)" should become a developer comment or a hidden slot (core group, CSS/markup decision). The section heading stays until the client decides.
6. **Privacy policy**: the forms link to a placeholder page. The client must supply a real policy before launch (lead forms collect health-adjacent personal data).

## 9. Decisions for the client (summary)

1. Approve or remove the "Information only…" disclaimer lines (6.4).
2. Legal review of every item in section 7, especially stem-cell and therapy claims, "patented", the 5% / 8-10% / 92% statistics and "Source: chat GPT".
3. Which number "Call Now" dials on the course and training pages (old site: +91 9599877196).
4. Which director mailbox is live: director@embryogenesis.in, or drpurkait@embryogenesis.in (the old link target).
5. "Best Innovation Award" vs "Best Innovator Award".
6. WhatsApp number; that therapies are given only in Mohali; the full address.
7. Whether to bring back an "Our Patents" section on About. The old one showed AI-generated images only.

*TechnoTaau Team, Jakhar Singh*
