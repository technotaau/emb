# Page copy: For Clinicians (hub)

| Field | Value |
|---|---|
| **URL** | `/for-clinicians/` |
| **SEO title** (54 chars) | Endometrial Testing for IVF Clinicians \| EmbryoGenesis |
| **Meta description** (147 chars) | Test menu, sample requirements, ordering, transport and report support for IVF clinicians. Evidence status for every test. Reports in 7 to 10 days. |
| **Primary keyword** | endometrial testing for IVF clinicians |
| **Secondary keywords** | endometrial biopsy timing protocol; chronic endometritis test lab; endometrial receptivity test India for clinics; uterine NK cell test evidence; refer patient for endometrial biopsy test |
| **Audience** | IVF specialists, gynaecologists, embryologists, clinic lab managers |
| **Page template** | Hub page with sticky in-page nav: Test menu · Ordering · Sample collection · Reports · CME · Contact |
| **Schema** | `MedicalWebPage` (`audience`: `MedicalAudience` "Clinician"), `ItemList` of `MedicalTest`, `FAQPage` |
| **Status** | Draft v1, 15 Oct 2026. Test specifications pending client confirmation. Gate 4 pending |

**Reading this file.** `[H1]`, `[H2]`, `[H3]` mark heading levels. `{{...}}` is a placeholder. `{{CONFIRM}}` means EmbryoGenesis must confirm the sentence, or it is removed. `[n]` refers to the References list.

---

## Section 1: Hero

**Eyebrow:** For IVF clinicians and gynaecologists

**[H1]** Endometrial testing for your patients, with the evidence in view

**Sub-heading:**
Order specialised endometrial tests from our Mohali lab, collect at your clinic or a partner centre, and receive a signed report in 7 to 10 days. Our scientific team is available to discuss every case.

**[Button, primary]** See the test menu → `#test-menu`
**[Button, secondary]** Request the partner rate card → `/partner-with-us/#rate-card`

**Note box (under hero, neutral):**
We show the evidence status of each test, citing ESHRE and other primary sources. Most endometrial and immune tests are not recommended for routine use. Chronic endometritis assessment is the exception that ESHRE says "can be considered" in repeated implantation failure [1]. We would rather you order the right test for the right patient than more tests.

---

## Section 2: Test menu (anchor `#test-menu`)

**[H2]** Test menu

**Intro:** All tests use an endometrial biopsy. Where the timing allows, one biopsy can be used for more than one test. {{CONFIRM_COMBINED_SAMPLE}}

| Test | What it assesses | When clinicians consider it | Evidence status | Sample | Cycle timing | Turnaround |
|---|---|---|---|---|---|---|
| **Endometrial Infection Test (EIT)** | Chronic endometritis | Repeated implantation failure; selected recurrent pregnancy loss | **Guideline-supported:** ESHRE RIF 2023, assessment "can be considered" [1]. RPL: more research needed before screening [2] | Endometrial biopsy in {{SAMPLE_EIT}} | {{TIMING_EIT}} | 7 to 10 days |
| **ERFA, The Soil Test** (Endometrial Receptivity & Function Assay) | Markers of endometrial receptivity and function {{CONFIRM_ERFA_MARKERS}} | Selected RIF cases, after other causes are assessed, on clinician judgement | **Emerging:** ESHRE does not recommend the presently available receptivity tests for routine use [1][3]. HFEA rates receptivity testing red [4] | Endometrial biopsy in {{SAMPLE_ERFA}} | {{TIMING_ERFA e.g. LH+7 or P+5}} | 7 to 10 days |
| **Endo-Immune Test** | Endometrial immune profile, including uterine NK cells and cytokines {{CONFIRM_ENDO_IMMUNE_MARKERS}} | Selected RIF or RPL cases, on clinician judgement, ideally within a research or audit protocol | **Limited:** ESHRE does not recommend uNK or blood cytokine testing [1][3]; RPL guideline advises against cytokine testing [2] | Endometrial biopsy in {{SAMPLE_ENDO_IMMUNE}} | {{TIMING_ENDO_IMMUNE}} | 7 to 10 days |
| **Receptivity PX** | Biomarkers of endometrial receptivity and immune competency {{CONFIRM_RECEPTIVITY_PX}} | {{CONFIRM_RECEPTIVITY_PX_INDICATION}} | **Emerging:** as for receptivity and immune testing above [1][3] | {{SAMPLE_RPX}} | {{TIMING_RPX}} | 7 to 10 days |

**Under the table (small):** Turnaround is counted from sample receipt at our Mohali lab. Prices are not published. Clinics can request the partner rate card.

**[H3]** Test pages
- [Endometrial Infection Test (EIT)](/diagnostics/endometrial-infection-test/)
- [ERFA, The Soil Test](/diagnostics/erfa-endometrial-receptivity-test/)
- [Endo-Immune Test](/diagnostics/endo-immune-test/)
- [All diagnostics](/diagnostics/)

**[H3]** How we describe evidence
- **Guideline-supported:** a major guideline says the test "can be considered" for a defined group.
- **Emerging:** there is a biological rationale and some data, but guidelines do not recommend routine use.
- **Limited:** guidelines advise against routine use. Consider only in selected cases, with full patient counselling.

---

## Section 3: Ordering process (anchor `#ordering`)

**[H2]** How to order

**Step 1. Set up your clinic.** Partner clinics are set up during onboarding. Other clinics can register with a short call. {{CONFIRM_NON_PARTNER_ORDERING}}

**Step 2. Get kits and forms.** Request collection kits, requisition forms and patient consent forms from {{KIT_REQUEST_EMAIL}} or your scientific contact.

**Step 3. Decide and counsel.** Choose the test that answers your clinical question. Explain to the patient what the test can and cannot show. Our patient leaflets can help.

**Step 4. Complete the requisition.** Include the patient's details, clinical indication, cycle day and protocol (natural or HRT), the date and time of biopsy, and your registration number.

**Step 5. Collect and dispatch.** Take the biopsy at the required timing, fix and label it, and book a courier pickup. Details are below.

**Step 6. Receive the report.** We send the signed report to you within 7 to 10 days of receipt.

**[Link]** Download the requisition form (PDF) → `{{REQUISITION_FORM_PDF}}`
**[Link]** Download the patient consent form (PDF) → `{{CONSENT_FORM_PDF}}`

---

## Section 4: Sample collection and transport (anchor `#sample-collection`)

**[H2]** Sample collection and transport

**Intro:** Good samples give reliable reports. Please follow these steps. Our full collection SOP is part of every kit and partner training. {{CONFIRM}}

**[H3]** Timing
- Each test has its own cycle timing (see the test menu). Record the cycle day, the protocol (natural cycle or HRT) and the LH surge or progesterone start date on the requisition.
- If a patient's cycle changes, please call us before taking the biopsy.

**[H3]** Collection
- Biopsy method: {{BIOPSY_METHOD e.g. pipelle or hysteroscopy-guided}}.
- Minimum tissue: {{MIN_SAMPLE_SIZE}}.
- Place the tissue in the container supplied, in {{FIXATIVE_OR_MEDIUM}}, within {{TIME_TO_FIXATION}} of collection.

**[H3]** Labelling
- Two patient identifiers on the container (full name and date of birth or clinic ID).
- Date and time of collection.
- Test(s) requested.
- Unlabelled or mislabelled samples cannot be tested.

**[H3]** Storage and packing
- Store at {{STORAGE_CONDITIONS}} until pickup. Do not freeze unless the test protocol says so. {{CONFIRM}}
- Pack using the triple packaging supplied, with the requisition and consent forms in the outer sleeve.

**[H3]** Transport
- Book a pickup at {{PICKUP_BOOKING_CONTACT}} by {{PICKUP_CUTOFF_TIME}} on {{PICKUP_DAYS}}.
- Samples should reach our lab within {{MAX_TRANSIT_HOURS}} hours of collection.
- Courier: {{COURIER_PARTNER}}. Each shipment has a tracking number and chain-of-custody record.

**[H3]** Sample acceptance
We may not be able to test a sample that is unlabelled, leaking, received outside the transit window, without a requisition or consent form, or too small. We will tell you the same day and advise on recollection. {{CONFIRM_REJECTION_CRITERIA}}

**[Link]** Download the collection SOP (PDF, partners only) → `{{SOP_PDF}}`

---

## Section 5: Reports and interpretation support (anchor `#reports`)

**[H2]** Reports and interpretation support

**[H3]** What the report includes
- Patient and sample identifiers, dates of collection and receipt.
- Sample adequacy.
- Method used.
- Findings, with the thresholds or reference ranges used.
- An interpretive comment that states the limits of the result.
- Signature of the reporting pathologist or scientist, with registration number where applicable.

**[H3]** How reports are sent
By {{REPORT_CHANNEL e.g. secure clinician portal / encrypted email}} to the ordering clinician. {{CONFIRM_REPORT_TO_PATIENT_POLICY}}

**[H3]** Talk to us about a report
Book a call with our scientific team to discuss a result or plan further testing. We will explain how the result was reached and what it does and does not show. Treatment decisions remain with the treating clinician.

**[Link]** Download a sample report (PDF) → `{{SAMPLE_REPORT_PDF}}`

---

## Section 6: CME webinars (anchor `#cme`)

**[H2]** CME webinars and case discussions

**Copy:**
We hold {{CME_FREQUENCY e.g. monthly}} online sessions for IVF clinicians and embryologists. Each session reviews the evidence on one topic and discusses anonymised cases.

**Planned topics (Developer: render as a list of upcoming sessions; client to confirm dates):**
- Chronic endometritis: diagnosis, thresholds and what ESHRE says
- Repeated implantation failure: a structured work-up
- Endometrial receptivity testing: what the trials show
- Uterine immune testing: the evidence and its limits
- Endometrial biopsy: timing, handling and common pre-analytical errors

**CME credit:** {{CME_ACCREDITATION e.g. accredited by X State Medical Council, or "certificate of attendance"}}

**[Button]** Register for the next session → `{{CME_REGISTRATION_URL}}`
**[Link]** Watch past sessions → `{{YOUTUBE_PLAYLIST_URL}}`

---

## Section 7: Contact the scientific team (anchor `#contact`)

**[H2]** Contact the scientific team

**Copy:** For questions on test choice, sample collection, or a report, reach our scientific team directly.

- **Phone:** {{SCIENTIFIC_TEAM_PHONE}} ({{LAB_HOURS}})
- **WhatsApp (clinicians):** {{WHATSAPP}}. Please do not send patient-identifiable reports or images on WhatsApp.
- **Email:** {{SCIENTIFIC_TEAM_EMAIL}}

**Team (cards):**
- **Prof. (Dr.) Pulakes Purkait**, M.Sc., Ph.D., Postdoc. Founder & Director; reproductive geneticist.
- **Dr. Vidhu Wadhwa**, MBBS, MD (Pathology). Consultant Pathologist and Quality Manager. {{NMC_REG_NO_VIDHU_WADHWA}}
- **Dr. Meenu Bhanot**, Ph.D. (Clinical Embryology). Consultant Embryologist.

**Short form (optional, inline):**
Fields: Name (required) · Registration number (optional) · Clinic and city (required) · Email (required) · Phone (required) · Topic (select: Test choice / Sample collection / Report query / CME / Other) · Message, no patient details (required, max 500 characters).
Consent checkbox (required, unticked): "I agree to EmbryoGenesis using these details to respond to my query, as described in the [Privacy Policy](/privacy-policy/)."
Notice text above the checkbox: use the same notice as the partner enquiry form (see `02-partner-with-us.md`, Section 12), with "query" in place of "partnership enquiry".
Submit button: **Send to the scientific team**
Success message: "Thank you. A member of our scientific team will reply within {{RESPONSE_TIME}}."

---

## Section 8: Partner rate card CTA

**[H2]** Partner pricing

**Copy:** We do not publish test prices. Registered clinics and hospitals can request our partner rate card, which we share privately after a short verification call.

**[Button, primary]** Request the partner rate card → `/partner-with-us/#rate-card`
**[Link]** Become a Collection Partner → `/partner-with-us/`

---

## Section 9: FAQ

**[H2]** Questions from clinicians

**[H3]** Can I order without becoming a collection partner?
{{CONFIRM_NON_PARTNER_ORDERING. Suggested answer: "Yes. Any registered medical practitioner can order. Partners get training, scheduled pickups and a named scientific contact."}}

**[H3]** Can one biopsy be used for more than one test?
{{CONFIRM_COMBINED_SAMPLE}} The timing must suit every test requested.

**[H3]** Which test should I start with after repeated implantation failure?
That depends on the case. Of our tests, chronic endometritis assessment has the clearest guideline support [1]. ESHRE's RIF recommendations also cover other assessments, such as uterine anatomy and embryo factors, that should be considered alongside it.

**[H3]** Do your receptivity tests improve live-birth rates?
We do not make that claim. A 2022 randomised trial of 767 patients found no improvement in live birth when frozen embryo transfer was timed by a commercial receptivity test (58.5% vs 61.9%) [5]. ERFA is offered for selected cases where the clinician wants more information about endometrial function. Our own validation data: {{VALIDATION_STATUS}}.

**[H3]** Why offer the Endo-Immune Test if guidelines advise against routine immune testing?
Some clinicians want an endometrial immune profile in selected, well-counselled cases, or within research protocols. We state the guideline position clearly on the test page and on every report. {{CLIENT_TO_REVIEW_WORDING}}

**[H3]** Who signs the reports?
{{REPORTING_SIGNATORIES e.g. Dr. Vidhu Wadhwa, MD (Pathology), NMC/SMC Reg. No. ...}}

**[H3]** Is the lab accredited?
{{LAB_ACCREDITATION e.g. NABL certificate number and scope, or "We are preparing for NABL (ISO 15189) accreditation."}}

**[H3]** Do you send results to patients?
{{CONFIRM_REPORT_TO_PATIENT_POLICY}}

---

## Reviewer line

Scientifically reviewed by Prof. (Dr.) Pulakes Purkait, M.Sc., Ph.D., Founder & Director, EmbryoGenesis, on {{REVIEW_DATE}}. Clinical review by {{RMP_NAME}}, {{RMP_QUALIFICATION}}, {{NMC_REG_NO}}, on {{REVIEW_DATE}}.

**Disclaimer (small):** For healthcare professionals. Test selection and interpretation are the responsibility of the treating clinician. EmbryoGenesis does not guarantee pregnancy or IVF outcomes.

## References

1. Cimadomo D, de los Santos MJ, Griesinger G, et al.; ESHRE Working Group on Recurrent Implantation Failure. ESHRE good practice recommendations on recurrent implantation failure. *Hum Reprod Open.* 2023;2023(3):hoad023. doi:10.1093/hropen/hoad023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10270320/
2. ESHRE Guideline Group on RPL; Bender Atik R, et al. ESHRE guideline: recurrent pregnancy loss: an update in 2022. *Hum Reprod Open.* 2023;2023(1):hoad002. doi:10.1093/hropen/hoad002. Full guideline: https://www.eshre.eu/-/media/sitecore-files/Guidelines/Recurrent-pregnancy-loss/2022/ESHRE-RPL-Guideline-_-Update-2022_-Final-Version-January-2023_v2.pdf
3. ESHRE Add-ons Working Group; Lundin K, et al. Good practice recommendations on add-ons in reproductive medicine. *Hum Reprod.* 2023;38(11):2062–2104. doi:10.1093/humrep/dead184. https://pmc.ncbi.nlm.nih.gov/articles/PMC10628516/
4. Human Fertilisation and Embryology Authority. Treatment add-ons with limited evidence (endometrial receptivity testing: red). Last reviewed 28 Sep 2026. https://www.hfea.gov.uk/treatments/treatment-add-ons/ (accessed 15 Oct 2026)
5. Doyle N, Jahandideh S, Hill MJ, et al. Effect of timing by endometrial receptivity testing vs standard timing of frozen embryo transfer on live birth in patients undergoing in vitro fertilization: a randomized clinical trial. *JAMA.* 2022;328(21):2117–2125. doi:10.1001/jama.2022.20438

## Internal-link suggestions

| From | Anchor text | To |
|---|---|---|
| Test menu | test names | each `/diagnostics/...` page |
| Hero, Section 8 | Request the partner rate card | `/partner-with-us/#rate-card` |
| Section 8 | Become a Collection Partner | `/partner-with-us/` |
| Section 3 | patient leaflets | `/patients/` |
| Section 7 | team names | `/about/#team` |
| Home, test pages, partner page | clinician hub / test menu / sample collection | this page and its anchors |

## Image and alt-text notes

- **Hero:** real photo of the pathologist at a microscope in the Mohali lab. Alt: "Consultant pathologist reviewing endometrial biopsy slides at EmbryoGenesis".
- **Sample collection section:** photo of the actual kit and a labelled container. Alt: "Correctly labelled endometrial sample container with two patient identifiers".
- **Team cards:** real portraits only. Alt: "[Name], [role] at EmbryoGenesis".
- **CME:** screenshot of a real past webinar title slide, or a branded card. No AI-generated faces.

## Developer notes

1. **Evidence status column.** Render as coloured chips: Guideline-supported (Green `#218A6A`), Emerging (Teal Mid `#11858E` outline), Limited (grey outline). Keep the citation numbers.
2. **Mobile table.** The test menu becomes stacked cards on small screens, with each column as a labelled row. Do not hide the evidence status on mobile.
3. **Downloads.** Requisition, consent and sample report PDFs must be approved by the client before upload. The SOP PDF is for partners only: place it behind a simple partner login or send it by email. Do not put it in the public media library.
4. **Forms.** Same consent pattern as the partner form: unticked required checkbox, full notice, consent log, no field values sent to analytics or ad pixels.
5. **WhatsApp link.** Use `https://wa.me/{{WHATSAPP}}?text=Clinician%20query` and fire `whatsapp_click` with `page: for-clinicians`.
6. **Schema.** `ItemList` of four `MedicalTest` items (name, url, `usedToDiagnose` where applicable). No `offers`. `FAQPage` only for answered questions.
7. **No therapy content.** No links to therapy pages or therapy training courses from this hub.

---

Draft prepared by TechnoTaau Team — scientific review pending: Prof. (Dr.) Pulakes Purkait
