# Review of Client Source Materials against the Old Website

**Prepared by:** TechnoTaau Team (Jakhar Singh)
**For:** EmbryoGenesis, Mohali
**Date:** 15 October 2026
**Materials reviewed:**
1. `Content_of_Embryogenesis.docx`: the content document behind the current website (About, Leadership, Therapeutic, Courses, Media & Events).
2. `Embrogentics_Broucher_2024.pdf`: 16-page company brochure (old black/green logo).
3. `ERFA_EMBRYOGENESIS_brochure.pdf`: 8-page ERFA product brochure.

Text extracts are saved in `content/source/`; the company brochure PDF is in `brand/`. Read with `04-existing-website-and-social-review.md`, which covers the live site itself.

---

## 1. Summary

The brochures contain **more, and better, information than the website**. The website is a thinned-down copy of the brochure text with the same marketing phrases and fewer facts. Several things we had to leave as placeholders are answered here, and several things the website says are contradicted by the brochures. Specifically:

- **New facts we can now use:** full address with PIN code, the complete diagnostic test menu (10 tests, not 3), ERFA sample requirements and biopsy timing, what ERFA reports, a registered medical doctor on the team (Dr. Vidhu Wadhwa, MBBS, MD Pathology), MoUs with four IVF groups, Times of India coverage, ISO / MSME / Indian Fertility Society credentials, the founder's LinkedIn and ResearchGate, and a brand metaphor ("soil and seed") worth keeping.
- **Conflicts to resolve:** the collection-centre network (website: 3 centres; brochure: a Delhi regional centre plus 5 centres in different cities), course fees (website: ₹39,875 / ₹1,00,000 per semester; brochure: ₹50,000 / ₹1,45,000), the Udaipur partner hospital (two different names), the programme list (website: 2 programmes; brochure: 6 plus Ph.D.), and four phone numbers with no stated primary.
- **Compliance problems carried from brochure to website:** "best infertility diagnostic centre in India", "patented" and "the only India-based patented test" for published applications, "greatly improve the chances of successful pregnancy", "diagnosis and treatment option for mothers-to-be", therapy promotion including stem cell, an ISO logo without a certificate number, and the patient-facing framing of a lab.

---

## 2. What the materials add (use in the rebuild)

### 2.1 Organisation facts

| Fact | Source | Status |
|---|---|---|
| Central laboratory address: EmbryoGenesis – Infertility Diagnostic & Research, Rayat Bahra University Campus, VPO Sahauran, Tehsil Kharar, Dist. Mohali, Punjab **140302** | Both brochures | Use. The website's "Top Floor, Rayat Bahra Dental College & Hospital" is the floor; the brochure gives the postal address and PIN |
| Lab phone **+91 81462 17196**; director **+91 95998 77196** (Dr. Purkait); admissions 96917 36435; Delhi regional centre 98156 92195 | Brochures, docx | Four numbers now have roles. **Recommendation:** +91 81462 17196 as the single public number and WhatsApp; the others become internal |
| Emails: director@embryogenesis.in, info.embryogenesis@gmail.com, embryogenesis.laboratory@gmail.com, iths.rbu@gmail.com | Brochures, site | Use **director@** and **info@embryogenesis.in** (create a domain mailbox); retire the Gmail addresses from public pages |
| Credentials shown as logos: ISO, MSME (Ministry of MSME, Govt. of India), Life Member Indian Fertility Society (IFS-2900) | Brochure covers; docx | Use with numbers: ISO standard and certificate number, Udyam registration number, IFS membership number |
| Taglines in use: "Hope for Mother's-to-Be", "Explain the Unexplained Sub-fertility & Implantation Failure", "Discover Your Answer – Hope – Future", "The unknown causes are not unknown anymore", plus the new "Redefining Fertility Evaluation" | Brochures | Keep **one**: "Redefining Fertility Evaluation" (on the new logo). "Explain the Unexplained" can survive as the ERFA product line if softened (see 4.3) |
| Founder's "soil and seed" view: the endometrium is the soil, the embryo the seed; the endometrium is the rate-limiting factor | Both brochures | **Keep.** It is the one memorable, ownable idea in all the material, and it explains the test name. Use it as the patient-education metaphor and the ERFA story |

### 2.2 Diagnostic menu (the website shows 3 of these 10)

| # | Test | Notes from brochure |
|---|---|---|
| 1 | ERFA – The Soil Test (Endometrial Receptivity & Function Assay) | Patent application 202431001616 A, published 09/02/2024. Multi-biomarker; "post-translational protein expression, epigenetic level" (i.e. tissue-based protein markers, consistent with immunohistochemistry: client to confirm) |
| 2 | ERMA (Endometrial Receptivity & Maturation Analysis) | Patent application 202211073981 A, published 30/12/2022. Adhesion vs anti-adhesion molecules at the window of implantation. **Not on the website at all.** The YouTube Short titled "ERMA Test" was therefore not a typo |
| 3 | Endo-Immune Test | TNF-α (Th1), PDM (Th17), uNK cells, plasma cells |
| 4 | Endometrial Infection Test (EIT) | Infection and inflammation of the endometrium |
| 5 | Endometrial Cytokine Test (ECT) | Component of Endo-Immune |
| 6 | Chronic Endometritis Factor (CEF) | Plasma-cell marker (CD138-type) for chronic endometritis |
| 7 | TNF-α | Component |
| 8 | Pregnancy Destroying Molecules (PDM) | Component (Th17). The name is marketing language; keep the scientific description alongside |
| 9 | uNK cells | Component |
| 10 | Female genital TB / TB-PCR / PAMP | Add-on at physician request |

**ERFA reports seven factors:** glandular development arrest, maturation, receptivity, anti-adhesion molecules, cytokine abnormalities, immune tolerance, inflammation/infection (chronic endometritis); optional gynaecological evaluation and genital TB PCR.

**Sample requirements (ERFA brochure):** endometrial tissue by D&C or needle (pipelle) biopsy. Timing: menstrual cycle day 21–23 (preferred day 21); natural cycle LH+7 to LH+9; HRT/mock cycle P+6 to P+8. This fills the `{{TIMING}}` placeholders in the copy and prototype.

**Implication for the site:** one page per headline test (ERFA, ERMA, Endo-Immune, EIT) with the component markers (ECT, CEF, TNF-α, PDM, uNK) explained inside Endo-Immune and EIT rather than as ten separate products. Clinicians think in panels; ten SKUs confuse.

### 2.3 Team

- **Dr. Vidhu Wadhwa, MBBS, MD (Pathology), Consultant Pathologist** (ERFA brochure, with photo). The website calls her "Consultant Pathologist & Quality Manager" with no degree. This matters: she is a **registered medical practitioner** and can be the clinical reviewer for every medical page, which the NMC norms and Google's medical-content standards expect. We need her NMC/State Medical Council registration number.
- Founder profile adds: LinkedIn (`in.linkedin.com/in/pulakes-purkait-aa634094`), ResearchGate, Global Andrology Forum membership, IFS life membership, five renin-gene variants accepted by NCBI, and departmental headships at both universities. All usable on the About page and in Person schema.
- The founder's patent list has **14 entries**, of which **4 relate to this business** (ERFA, ERMA, LIT-H2, a method of improving implantation); the rest cover a biothesiometer, waste management, water filtration, cardiology, student stress and nutrigenetics. The website's "14 patent" claim should become "four published patent applications in reproductive diagnostics" on EmbryoGenesis pages, with the full list on the founder's profile only.

### 2.4 Network and partnerships

| Website (2026) | Company brochure (2024) |
|---|---|
| Navi Mumbai: Nirmal Multi Speciality Hospital | Regional centre, New Delhi: CD Imaging & Path Lab, Najafgarh |
| Udaipur: Shree B.L. Jain Memorial Hospital | Udaipur: Narayani Women's Hospital & Fertility Center |
| Jalandhar: Advance Fertility Services & IVF Centre | Jalandhar: Advanced Fertility Services & IVF Centre |
| — | Ahmedabad: Parul Women's Hospital & Fertility Centre |
| — | Bikaner: Vatsalya IVF Centre |
| — | Panchkula: IRCC Hospital & IVF Centre |

The 2024 network looks larger than today's. **Client to confirm which centres are active**; only active ones go on the site, each with written consent to be named.

**MoUs listed:** GIOSTAR USA, Indira IVF Udaipur, Vatsalya IVF Bikaner, Parul IVF Ahmedabad, plus Guru Ghasidas Vishwavidyalaya (website). The appreciation photos name 14 people including Dr. Ritesh Agarwal (Indira IVF, Udaipur), Dr. Parul Sharda (Parul IVF), Dr. Krishan Poonia (Vatsalya IVF), Dr. Kamla Singh (ex-DGHS Haryana; IRCC Hospital). **This is the best B2B proof the brand has**, and none of it is on the website. With consent, a "Clinicians who work with us" strip is far stronger than patient testimonials, and it is compliant (professional endorsement of a lab, not patient outcome claims). GIOSTAR is a stem-cell company; the legal adviser should decide whether to show it.

### 2.5 Media coverage (website Media page is empty)

- Times of India, 3 Jul 2024: "Therapy kit to check IVF failure launched at RBU" (ERFA and LIT-H2 kit).
- Himachal Tonite, 6 Jul 2024: Bahra University launches HP's first clinical embryology programme with ITHS and EmbryoGenesis.
- News Nation, 27 Jul 2024: digital biothesiometer design patent (founder; not reproductive).

The first two go on the News page and in a "Featured in" strip (Baby Joy pattern), with the Times of India item framed around the ERFA launch, not the LIT kit.

### 2.6 Academy

The brochure shows ITHS as a multi-programme institute (Nutrigenetics, Cancer Biology, Stem Cell & Regenerative Medicine, Anthropology, ART & Clinical Embryology) with a fee table:

| Programme | Duration | Total fee | Per semester |
|---|---|---|---|
| B.Sc. ART & Clinical Embryology | 4 years | ₹4,00,000 | ₹50,000 |
| M.Sc. ART & Clinical Embryology | 2 years | ₹5,80,000 | ₹1,45,000 |
| PG Diploma ART & Clinical Embryology | 1 year | ₹2,00,000 | ₹1,00,000 |
| PG Diploma Genetic Counselling | 1 year | ₹80,000 | ₹40,000 |
| Certificate in Infertility Counselling | 6 months | ₹48,000 | ₹48,000 |
| Ph.D. Clinical Embryology | 3 years | ₹4,50,000 | ₹75,000 |

The website shows B.Sc. ₹39,875 and M.Sc. ₹1,00,000 per semester. **Which is current?** Also: is EmbryoGenesis Academy the embryology track only, or the whole ITHS catalogue? Our recommendation is embryology only on embryogenesis.in, with a link to ITHS for the rest, so the lab's brand stays focused.

Admission office: Room No. 8, Research & Incubation Centre, Rayat Bahra University (brochure) vs "Shimla Hills" on the B.Sc. page (website).

---

## 3. Where the website fell short of its own source material

1. **It copied the slogans and dropped the facts.** The brochure's sample requirements, biopsy timing, seven-factor report, full test list, network, MoUs, media and credentials never reached the site. The site kept "cutting-edge", "beacon of hope" and "best in India".
2. **It lost ERMA.** A test with its own published patent application is missing from the site, while its YouTube Short exists.
3. **It hid the registered doctor.** Dr. Wadhwa's MBBS, MD is the single most useful trust fact for a medical site and the site omits it.
4. **It shows a smaller network than the brochure** and a different Udaipur partner, without explanation.
5. **It uses AI-generated images** where the brochure has real photographs of the founder, Dr. Wadhwa at the microscope, and 14 partner handover photos.
6. **Fees disagree** between the two.

---

## 4. Compliance findings in the source materials (fix before any reuse)

### 4.1 Claims to remove everywhere
- "the best Infertility diagnostic centre in India" (brochure p.0 and Vision; website About and footer).
- "Patented", "a patented groundbreaking … tool", "the only, India based Patented and multi-biomarker test" (ERFA brochure). All numbers are published applications ("A"). Say "Indian patent application published (No. 202431001616 A, 9 Feb 2024)". "The only" is also an unverifiable superlative.
- "we can greatly improve the chances of successful pregnancy and implantation"; "ultimately increasing the chances of successful conception"; "The unknown causes are not unknown anymore". Outcome promises.
- "We provide personalized, diagnosis and **treatment** option for mothers-to-be" and "Mother needs intense care and **cure**". A lab with no registered clinician treating patients should not say it treats or cures.
- "unparalleled efficiency", "revolutionary", "groundbreaking", "cutting-edge" throughout.

### 4.2 Therapies
The brochure markets LIT-H2 ("Patented"), PBMC, PRP, stem cell and molecular hydrogen with the same outcome language. This content stays on legal hold, as decided. The ISO/IFS logos must not appear next to therapy pages in a way that implies endorsement.

### 4.3 What can be kept, reworded
- "Explain the Unexplained" → "Looking deeper at unexplained implantation failure" (a question, not a promise).
- Soil metaphor → keep as education: "If the embryo is the seed, the endometrium is the soil. ERFA looks at the soil."
- "Hope for Mother's-to-Be" → retire; it positions a lab as a clinic.

### 4.4 Credentials
- ISO logo: state the standard (e.g. ISO 9001:2015 or ISO 15189) and certificate number, or remove.
- MSME: show the Udyam registration number.
- IFS life membership: fine, with the number.

---

## 5. Decisions needed from the client

1. **Primary phone and WhatsApp:** confirm +91 81462 17196 as the single public number.
2. **Active collection centres today**, with address, contact and written consent to be named. Is the Delhi regional centre still running?
3. **Dr. Vidhu Wadhwa's registration number** and her agreement to be named as clinical reviewer.
4. **ERFA method** (confirm immunohistochemistry / which markers) so we can state it in clinician terms.
5. **Current fee table** and whether tuition fees may be shown (the brief bans only test prices; both the site and the brochure show fees today).
6. **Scope of the Academy on embryogenesis.in:** embryology programmes only (our recommendation) or the full ITHS catalogue.
7. **Consent to use the 14 appreciation photos** and the MoU partner names, and the legal adviser's view on showing GIOSTAR.
8. **ISO standard and certificate number; Udyam number.**
9. **Which patent applications to show on EmbryoGenesis pages** (we propose the four reproductive ones) and whether any has since been granted.

---

## 6. Changes made to our deliverables as a result

- Project brief updated: postal address with PIN, Dr. Wadhwa's qualifications, the ten-test menu, ERFA timing, MoUs, media coverage, proposed primary phone.
- Prototype updated: PIN code and address, ERFA biopsy timing, ERMA added to the test tabs and clinician table, Dr. Wadhwa's MBBS, MD, a "Featured in" line, and "Clinicians who work with us" marked as a consent-pending block.
- Copy files: `content/00-copy-notes.md` placeholders for timing and address can now be resolved; test pages for ERMA to be added to the content plan.

*TechnoTaau Team, Jakhar Singh*
