# EmbryoGenesis Digital Rebuild: Project Brief

**Prepared by:** TechnoTaau Team (project lead: Jakhar Singh)
**Client:** EmbryoGenesis, Mohali, Punjab (https://embryogenesis.in)
**Date:** 15 October 2026
**Status:** Phase 1 (strategy, design direction and content) in progress

This brief is the single source of truth for every TechnoTaau Team contributor. If something here conflicts with an older note, this file wins.

---

## 0. Decision update (Jakhar Singh, 15 Oct 2026, evening)

The client has changed the scope of the website work:

- **Keep the old website's content as it is.** No rewriting of pages. The new pages we proposed ("For Clinicians", "Become a Collection Partner", clinician hub) are **dropped**. The site keeps the old structure: Home, About Us, Services (Diagnostic, Therapeutic), Courses, Lab Training, Blog, Media & Event, Contact Us.
- **Change only the design**, in the style of Indira IVF (https://www.indiraivf.com/), with the new logo and palette. Photos and icons may be used.
- Prototype v3 (`prototype/index.html`) implements this. The B2B copy in `content/` and the B2B parts of the strategy documents are **parked**, not deleted, in case the client returns to them.
- The compliance findings in `docs/research/` remain TechnoTaau Team's recommendations. They do not change the content unless the client asks.

## 1. Client decisions (confirmed by Jakhar Singh, 15 Oct 2026, morning; see section 0 for later changes)

| Topic | Decision |
|---|---|
| Primary audience | **IVF clinics and doctors (B2B) first.** Patients and students are secondary audiences served by the same site. |
| B2B model | **Collection-centre network.** Partner hospitals/IVF clinics become official sample collection points (current: Navi Mumbai, Udaipur, Jalandhar). Growth goal = more partner centres pan-India. |
| Platform | **Stay on WordPress.** |
| Delivery mode | **Design + content first, build later.** TechnoTaau Team delivers strategy, sitemap, wireframes, page copy and SEO spec; the client's developer implements in WordPress. |
| Languages | **English only** (for now). |
| Geography | **Pan-India**, with local pages only where a real collection centre exists. |
| Therapies (Stem Cell, LIT, PBMC, PRP, Molecular Hydrogen) | **Keep, pending legal review.** Pages are drafted but stay unpublished until a lawyer / medical-council adviser approves the wording. No ads, no social promotion of therapies until then. |
| Test prices | **Do not publish prices** anywhere (site, social, ads). Use "enquire / partner rate card on request". |
| Brand | **New logo and palette supplied** (see section 3). |
| Content reviewer | **Prof. (Dr.) Pulakes Purkait** (Founder & Director) signs off all content. |
| Social channels | **LinkedIn (primary B2B), Instagram + Facebook, and informative AI-produced reels.** |
| Timeline | **ASAP.** |

## 2. Business facts

- **Entity:** EmbryoGenesis, an infertility diagnostic and research centre. Established Nov 2023.
- **Address (brochure, with PIN):** EmbryoGenesis – Infertility Diagnostic & Research, Top Floor, Rayat Bahra Dental College & Hospital, Rayat Bahra University Campus, VPO Sahauran, Tehsil Kharar, Dist. Mohali, Punjab 140302.
- **Email:** director@embryogenesis.in, info.embryogenesis@gmail.com (also embryogenesis.laboratory@gmail.com, iths.rbu@gmail.com for admissions).
- **Phones by role (from brochures):** lab +91 81462 17196 (**proposed single public number and WhatsApp, to confirm**); director +91 95998 77196; admissions 96917 36435; Delhi regional centre 98156 92195.
- **Collection centres (conflicting; client to confirm which are active):**
  - Website 2026: Navi Mumbai (Nirmal Multi Speciality Hospital), Udaipur (Shree B.L. Jain Memorial Hospital), Jalandhar (Advance Fertility Services & IVF Centre).
  - Brochure 2024: Regional centre New Delhi (CD Imaging & Path Lab, Najafgarh); Ahmedabad (Parul Women's Hospital & Fertility Centre); Udaipur (Narayani Women's Hospital); Bikaner (Vatsalya IVF); Panchkula (IRCC Hospital & IVF); Jalandhar.
- **MoUs (brochure/docx):** GIOSTAR USA (stem-cell company: legal view needed before showing), Indira IVF Udaipur, Vatsalya IVF Bikaner, Parul IVF Ahmedabad, Guru Ghasidas Vishwavidyalaya.
- **Credentials shown in brochures (numbers needed):** ISO (standard and certificate no.), MSME/Udyam registration, Indian Fertility Society life membership IFS-2900.
- **Media:** Times of India, 3 Jul 2024 (ERFA launch at RBU); Himachal Tonite, 6 Jul 2024 (HP's first clinical embryology programme).
- **Source materials:** text extracts in `content/source/`; review in `docs/research/06-source-materials-review.md`.
- **Founder:**
  - Prof. (Dr.) Pulakes Purkait, M.Sc., Ph.D., Postdoc. Scientist; **not MBBS**.
  - ORCID 0000-0002-8814-9939.
  - Best Innovator Award, NBHC 2024 (IIT Delhi), and Best Innovator Award for Human Infertility Treatment, Research & Innovation Park, New Delhi, Nov 2024.
- **Team on site:** Dr. Vidhu Wadhwa, **MBBS, MD (Pathology)**, Consultant Pathologist & Quality Manager (registered medical practitioner: proposed clinical reviewer; registration number needed); Dr. Meenu Bhanot (Consultant Embryologist).
- **Diagnostics (full menu from brochures; website shows only three):**
  - ERFA, "The Soil Test" (Endometrial Receptivity & Function Assay): patent application 202431001616 A, published 9 Feb 2024. Reports seven factors: glandular development arrest, maturation, receptivity, anti-adhesion molecules, cytokine abnormalities, immune tolerance, inflammation/infection.
  - ERMA (Endometrial Receptivity & Maturation Analysis): patent application 202211073981 A, published 30 Dec 2022. Adhesion vs anti-adhesion molecules.
  - Endo-Immune Test: TNF-α (Th1), PDM (Th17), uNK cells, plasma cells. Components also offered singly: ECT (cytokines), CEF (chronic endometritis factor), TNF-α, PDM, uNK.
  - Endometrial Infection Test (EIT, chronic endometritis).
  - Receptivity PX (patent application 202411059621 A).
  - Add-on: female genital TB / TB-PCR / PAMP.
  - **Sample:** endometrial biopsy (D&C or pipelle). **Timing:** cycle day 21–23 (preferred 21); natural cycle LH+7 to LH+9; HRT cycle P+6 to P+8.
  - Stated turnaround is 7 to 10 days.
  - **Brand metaphor to keep:** "the embryo is the seed, the endometrium is the soil."
- **Therapies (on hold, see section 1):** LIT, PBMC, PRP, Stem Cell, Molecular Hydrogen.
- **Academy:**
  - B.Sc./M.Sc. Clinical Embryology with ITHS + Bahra University (Shimla Hills, HP).
  - B.Sc./M.Sc. ART & Clinical Embryology with ITHS + Rayat Bahra University (Mohali).
  - Short hands-on lab-training courses.
- **Milestones:**
  - Nov 2024: MoU with Guru Ghasidas Vishwavidyalaya, Bilaspur.
  - PJ Embryogenesis Health & Education Foundation, Kolkata.
  - Patent applications published in 2024 (e.g. ERFA 202431001616 A).
- **Social handles (inconsistent, to be unified):**
  - instagram.com/embryo_genesis
  - facebook.com/EmbryoGenesis
  - youtube.com/@Embryo-Genesis
  - twitter.com/EmbryoGenesiss
  - No LinkedIn page yet.

## 3. Brand identity (client-supplied)

- **Logo:** mother-and-child silhouette with DNA helix and leaves, gold arc; wordmark **EMBRYOGENESIS™**. Reference image: `brand/logo-and-palette.png`.
- **Tagline:** **"Redefining Fertility Evaluation"**.
- **Palette:**

| Token | Hex | Suggested use |
|---|---|---|
| Teal | `#25A2AA` | Icons, borders, large text only (3.08:1 on white) |
| Teal Mid | `#11858E` | Focus rings, active states, large numerals (4.40:1 on white: white button labels fail AA) |
| Deep Teal | `#0E6970` | Primary buttons, headings, links, header/footer background (6.42:1 on white; hover `#0B5C62`) |
| Green | `#218A6A` | Evidence highlights, success states, large text/icons (4.28:1) |
| Gold | `#C39F4E` | Decorative accents only: awards, dividers (2.50:1 on white; never as text on white) |

Contrast ratios were computed for `docs/strategy/04-brand-voice-and-design-system.md` (section 7.2).

## 4. Positioning (TechnoTaau Team recommendation)

EmbryoGenesis is **a specialised endometrial and reproductive diagnostics lab and academy that partners with IVF clinics across India**. It is not a "fertility centre". The tagline "Redefining Fertility Evaluation" carries this.

Proof points:
- proprietary in-house tests developed in India;
- 7 to 10 day turnaround;
- a scientist-founder with published research;
- a growing collection-centre network;
- a university-affiliated academy that trains embryologists.

## 5. Compliance guardrails (apply to every word we publish)

1. **No superlatives or unverifiable claims.** Avoid "best", "No. 1", "India's most accurate", "trusted by all", "guaranteed", "100% success", "revolutionary", "miracle" and "cure". (ASCI, CCPA 2022, IMC Regulations 2002, NMC advertising framework of Oct 2026.)
2. **Patents:** say **"patent application published (No. …)"** or **"patent-pending"**. Never say "patented" unless a grant certificate is verified on IP India.
3. **Evidence honesty:** state the indication, who the test is for, what the result can and cannot tell, and cite guidelines (ESHRE, etc.). Lead with the Endometrial Infection Test (chronic endometritis), the test with the strongest guideline support. Present ERFA / Endo-Immune as specialised tools for clinician-directed use. Do not promise pregnancy or improved IVF success rates.
4. **Therapies stay unpublished** until legal sign-off. Stem cell therapy must not be promoted at all: NMC advisory of 5 Sep 2026 and ICMR guidelines.
5. **No sex-selection related terms** (PCPNDT, ART Act s.32).
6. **No patient testimonials, before/after or outcome stories** until legal review under the NMC framework.
7. **Every medical page carries:**
   - "Scientifically reviewed by Prof. (Dr.) Pulakes Purkait" with the review date;
   - references;
   - a medical disclaimer ("Information only; testing is ordered and interpreted by your treating doctor").
   - Clinical claims must also have a registered medical practitioner (with NMC/state registration number) named when available.
8. **Data protection (DPDP Act 2023):**
   - consent checkbox and privacy-policy link on every form;
   - no health data passed to ad pixels;
   - no ad targeting of minors (B.Sc. applicants).
9. **AI-generated media** must be labelled as AI-generated / synthetic (Meta "AI info" label; India IT Rules on synthetically generated information). No AI faces posing as real doctors or patients.
10. **No prices** for tests in any public channel.
