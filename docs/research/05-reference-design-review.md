# Reference Design Review: Indira IVF, Nova IVF, Baby Joy IVF

**Prepared by:** TechnoTaau Team (Jakhar Singh)
**For:** EmbryoGenesis, Mohali
**Date:** 15 October 2026
**Method:** Each homepage was loaded in a real browser at 1366 px and 390 px, screenshotted in full, and its fonts, colours, navigation, headings and calls to action were extracted. Screenshots are in the project scratchpad; the extracted data is summarised below.

---

## 1. What the three sites have in common (the "IVF-chain" pattern)

| Element | Indira IVF | Nova IVF | Baby Joy IVF | Verdict for EmbryoGenesis |
|---|---|---|---|---|
| Utility bar above the logo | Phone + WhatsApp icons | Phone, "Exclusive Rs.999 package", Book | "We strictly follow ART Act 2021" | **Adopt.** Use it for a trust line and the clinician desk number |
| Logo + wide navigation + one strong CTA button | "Book Appointment" (blue pill) | "BOOK AN APPOINTMENT" (maroon) | "MAKE AN APPOINTMENT" (pink block) | **Adopt** with "Become a Collection Partner" |
| Mega-menu with 30–40 links | Yes (treatments, testing, problems, centres) | Yes (dropdowns) | Yes | **Adopt a lighter version.** Four groups: Clinicians, Diagnostics, Network, Academy |
| Full-width photo hero (real people) | Couple, warm tones, brand-colour swoosh | Pregnant woman / family | Mother and newborn + award banner | **Adopt** with real lab and clinician photography; no AI images |
| Lead form in or beside the hero | Pop-up on load, then form band | Pop-up on load, then form band | Pink form card beside hero | **Adopt the in-page form card; drop the pop-up** (see section 3) |
| Big-number stat circles / tiles | "2.00 lakh+ IVF pregnancies, 200+ centres, 340+ doctors" | Three circles: 120 centres, 75 cities, 1,00,000 pregnancies | Four circles: 31,000+ babies, 18 babies/week, 2 of 3 positive, 12 countries | **Adopt the format, change the numbers.** We show turnaround, panels per biopsy, cities, year established. No outcome statistics |
| "Which stage are you in?" segmentation | Checkbox self-assessment → "Get recommendations" | Four hexagon photo cards | — | **Adopt** as our four doors (Clinicians, Partners, Couples, Students) |
| Service list with icons, tabbed | Tabs: Testing, Treatments, Advanced, Preservation, Donor | Text list on yellow block | Mega-menu only | **Adopt** tabs: Diagnostics, Clinician services, Academy |
| Centres list / map | Google map with 200 pins | "Find clinic" | Nine centres with addresses in a grid | **Adopt the address grid** for the four real locations |
| FAQ accordion | Open answer in a filled brand-colour box | — | Numbered accordion | **Adopt** Indira's filled-answer style |
| Testimonials / success stories | Video stories carousel | "Success Story" menu | Quote slider with photos | **Do not adopt.** NMC's Oct 2026 framework restricts patient testimonials; our brief bans them |
| Press / certification logo strip | — | — | "Featured in" newspaper logos; "Certifications & Affiliations" | **Adopt** for universities, MoUs, award issuer, ORCID |
| Calculators / tools | Five pregnancy calculators | Calculators menu | — | **Adapt** later: a "Which test should my doctor consider?" checker (planned in the SEO strategy) |
| Floating phone + WhatsApp buttons | Chat avatar | WhatsApp + chat | Phone left, WhatsApp right | **Adopt** phone + WhatsApp |
| Sticky mobile bottom bar | "Book Appointment \| 18003092323" | — | "Make An Appointment" sticky band | **Adopt** ("Partner with us \| Call") |
| Blog cards | — | "Fertility blogs" | "Latest blog" | **Adopt** |

**Typography:** all three use clean sans-serif families (Lato + Work Sans; Montserrat + Proxima Nova; Montserrat). Headings are medium weight, large, often centred. Nothing is serif.

**Colour:** each uses one strong brand colour on white (Indira crimson #B61E42 with blue buttons; Nova maroon with cyan buttons and a yellow block; Baby Joy cyan #00B7CD with pink #E97195). Section backgrounds alternate white / pale tint / brand colour band.

**Layout rhythm:** hero → proof numbers → segmentation → services → form band → stories → FAQ → blog → footer. Pages are long (Indira's is about 7,000 px on desktop).

---

## 2. Site-by-site notes

### Indira IVF
- **Strengths:** the cleanest of the three. One primary colour, one accent, generous white space, consistent icon style, a clear hero with the brand swoosh, FAQ with a filled active answer, a well-structured mega-menu by intent (treatment / testing / problems / centres).
- **Weaknesses:** a pop-up form blocks the hero on first load on desktop and mobile; "Join the 2,00,000+ couples" is an outcome claim; title tag "Best IVF Center/Hospital in India" is a superlative; the page is very long.

### Nova IVF Fertility
- **Strengths:** strong photography; a yellow services block that breaks the rhythm; "Which stage of fertility journey are you in?" is a good segmentation idea; stat circles.
- **Weaknesses:** eleven font families load (Montserrat, Proxima Nova, Ubuntu, Poppins, Open Sans, Arial…); the page has no H1; a pop-up and a "Rs.999 package" promo dominate; a "franchise scam" warning banner interrupts; inconsistent button colours (maroon, cyan, white). Visually the busiest of the three.

### Baby Joy IVF
- **Strengths:** the utility bar ("We strictly follow ART Act 2021") is a smart trust line; "featured in" press strip; a centre grid with real addresses; a form card next to the hero that needs no pop-up; a sticky mobile CTA.
- **Weaknesses:** the hero is a banner image with baked-in text ("Best IVF Chain of Northern India", "Treatment pehle, payment baad mein", "IVF @ 1 Lac"), which is unreadable to Google and risky under advertising norms; four stat circles include "2 out of 3 couples positive"; H1 "Best IVF Centre in Delhi NCR"; cyan + pink + grey testimonial band is visually noisy.

---

## 3. What we deliberately will not copy, and why

1. **Pop-up form on page load.** Google treats intrusive interstitials on mobile as a ranking negative, and for a B2B audience it is irritating. The in-page form card (Baby Joy style) gets the same lead without the penalty.
2. **Outcome and success statistics** ("2,00,000+ couples", "2 out of 3 positive", "18 babies every week"). We are a lab, and our brief and the NMC/ASCI rules exclude outcome claims. Our proof numbers are operational: turnaround, panels per biopsy, cities, year established.
3. **"Best" in titles and H1s.** All three do it; all three are large enough to absorb the regulatory risk. We are not.
4. **Testimonials and success-story carousels.** Replaced with a clinician-resources block and a recognition strip.
5. **Promotional offers** ("Rs.999 package", "IVF @ 1 Lac", EMI). We do not publish prices.
6. **Text baked into hero images.** Our hero text is live HTML.
7. **Nova's font and colour sprawl.** Two font families, one primary colour, one accent.

---

## 4. Design direction for EmbryoGenesis (applied in the prototype)

- **Fonts:** Montserrat for headings and buttons, Lato for body. This replaces the serif heading proposed in the design-system document, to match the client's chosen references. The design-system document will be updated once the client confirms.
- **Colour:** Deep Teal `#0E6970` as the primary (header CTA, form band, footer), Teal `#25A2AA` for icons and highlights, Gold `#C39F4E` as the accent for the phone pill and stat numbers, pale teal tint `#E8F4F5` for alternating sections. White on Deep Teal is 6.42:1 (passes); gold is used only on large numerals and as a fill behind dark text.
- **Homepage rhythm:** utility bar → header with CTA → photo hero with lead form card → four proof circles → "How can we help you?" four doors → tabbed services → sample journey → collection-centre grid → form band (deep teal) → affiliations strip → FAQ (filled answer) → blog cards → footer. Floating phone + WhatsApp; sticky mobile bar.
- **Inner pages:** same header/footer; a shorter hero with the form card; content in the two-column pattern (text left, form or facts right) that all three references use.

*TechnoTaau Team, Jakhar Singh*
