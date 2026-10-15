# EmbryoGenesis Digital Rebuild: Project Blueprint & Workflow

**Prepared by:** TechnoTaau Team (project lead: Jakhar Singh)
**For:** EmbryoGenesis, Mohali ("Redefining Fertility Evaluation")
**Date:** 15 October 2026 | **Version:** 1.0

---

## 1. Executive summary

EmbryoGenesis has real assets that most competitors lack:
- proprietary endometrial tests developed in India;
- a stated 7–10 day turnaround, against the 3–4 weeks reported for imported receptivity panels;
- a published scientist-founder;
- an IIT Delhi innovation award;
- a working collection-centre network;
- a university-affiliated embryology academy.

None of this comes through online today.

**Where we stand (research of 15 Oct 2026):**
- **The website scores 38/100 on our SEO audit.** The flagship ERFA article tells Google to index a dead URL. The homepage loads about 21 MB of images. The privacy policy is empty although forms collect health data. There is no analytics. Many images are missing, and four different phone numbers appear.
- **The brand is nearly invisible in search,** because "embryogenesis" is also a common biology term.
- **The current claims carry legal risk:**
  - "best fertility centre";
  - "patented", while the numbers shown are published applications;
  - stem cell and immunotherapy promotion. The NMC advisory of 5 Sep 2026 treats stem cell promotion outside approved uses as professional misconduct.
- **There is a large B2B gap.** Punjab alone has about 200 registered ART clinics, 21 of them in Mohali. No lab in this niche publishes clinician-facing ordering protocols, report guides or CME.

**Our strategy in one line:** reposition EmbryoGenesis as **India's evidence-led endometrial diagnostics partner for IVF clinics**. That means three things:
1. Grow the collection-centre network through a clinician-first website and LinkedIn.
2. Use honest, cited content to win search and AI-answer visibility.
3. Use the academy as a second, lower-risk traffic engine.

---

## 2. Confirmed decisions

| Area | Decision |
|---|---|
| Primary audience | IVF clinics & doctors (B2B) |
| B2B model | Collection-centre partner network |
| Platform | WordPress (existing hosting) |
| Our delivery | Design + content + SEO spec. The client's developer builds; TechnoTaau Team QAs. |
| Language / reach | English / pan-India |
| Therapies | Drafted, held unpublished until legal sign-off |
| Test prices | Not published anywhere |
| Brand | Client logo + palette (Teal #25A2AA, Teal Mid #11858E, Deep Teal #0E6970, Green #218A6A, Gold #C39F4E) |
| Reviewer | Prof. (Dr.) Pulakes Purkait |
| Social | LinkedIn, Instagram + Facebook, AI-produced informative reels |
| Timeline | ASAP |

---

## 3. How TechnoTaau Team works on this project

### 3.1 Roles

| Role | Owns | Output in this repo |
|---|---|---|
| **Project Lead / QC (Claude for TechnoTaau Team, reporting to Jakhar Singh)** | Plan, briefs, final review of every deliverable, client communication | `docs/00-project-brief.md`, this blueprint |
| **Research Analyst** | Market, regulation, evidence status | `docs/research/01-industry-research.md` |
| **SEO Strategist** | Sitemap, keywords, redirects, schema, technical spec, editorial calendar | `docs/strategy/02-seo-strategy.md` |
| **Social Media Strategist** | Channel plan, AI reels system, scripts, LinkedIn playbook, calendar | `docs/strategy/03-social-media-strategy.md` |
| **Brand & Design Lead** | Messaging, claims dictionary, design system, wireframes | `docs/strategy/04-brand-voice-and-design-system.md` |
| **Medical Content Writer** | Page copy, articles, FAQs | `content/*.md` |
| **QA & Technical SEO Auditor** | Site audit, pre-launch and post-launch QA | `docs/research/03-current-site-audit.md`, QA checklists |
| **Client: Prof. (Dr.) Pulakes Purkait** | Scientific accuracy sign-off | Approval on each page |
| **Client: Legal adviser** | Therapy pages, patent wording, testimonials, privacy policy | Written opinion |
| **Client: WordPress developer** | Build, hosting, redirects, tracking install | Staging site |

### 3.2 Production pipeline (every page, post and reel)

```
Brief ─▶ Draft ─▶ Gate 1: Compliance check ─▶ Gate 2: SEO check ─▶ Gate 3: Lead QC
       ─▶ Gate 4: Scientific review (Prof. Purkait) ─▶ Build / Produce ─▶ Gate 5: Pre-publish QA ─▶ Publish ─▶ Measure
```

| Gate | Who | Pass criteria |
|---|---|---|
| 1. Compliance | Content writer + Lead | No superlatives, no "patented", no prices, no testimonials, no therapy promotion, disclaimer present, AI label on synthetic media |
| 2. SEO | SEO Strategist | Title/meta/H1 per template, primary keyword mapped, internal links, schema block, alt text |
| 3. Lead QC | Project Lead | Facts match the brief; tone; placeholders listed; nothing invented |
| 4. Scientific review | Prof. (Dr.) Pulakes Purkait | Accuracy, references, reviewer line dated |
| 5. Pre-publish QA | QA Auditor | Renders on mobile, under the Core Web Vitals budget, links resolve, tracking fires, forms carry consent |

**Turnaround target:** a draft-to-approved cycle of 3 working days per page. The scientific review slot is the bottleneck, so we batch pages for Prof. Purkait twice a week.

---

## 4. Do these on the live site now (before the rebuild)

These fixes take hours, not weeks. They reduce legal risk and stop SEO damage while the new site is built. Your developer can do all of them in the current WordPress admin.

| # | Action | Why | Effort |
|---|---|---|---|
| 1 | **Unpublish or noindex the therapies page (`/advanced-fertility-therapies/`) and remove the therapy cards from the homepage**, pending legal review | Live stem-cell promotion conflicts with the NMC advisory (5 Sep 2026) and ICMR guidelines | 15 min |
| 2 | Replace "best fertility centre", "India's most accurate" and "India's trusted" in titles, meta and footer | ASCI / CCPA / NMC advertising norms | 30 min |
| 3 | Change "patented" to "patent application published" on all pages and image captions | Patents Act s.120 risk | 30 min |
| 4 | Fix the ERFA post canonical in Rank Math (it points to a 404) and delete `/cache/` | The flagship article is currently de-indexed | 15 min |
| 5 | Publish a real privacy policy and add a consent checkbox to all three forms | DPDP Act 2023; data trust | 2 h (text from TechnoTaau Team) |
| 6 | Remove the broken `[grw id=1198]` testimonials block; update the footer to © 2026 | Credibility | 10 min |
| 7 | Choose **one** primary phone number + WhatsApp and use it everywhere | Consistent NAP for local SEO and AI entity matching | 30 min |
| 8 | Compress the 12 PNGs of about 2 MB each (homepage patents carousel and others) to WebP under 150 KB | The homepage is about 21 MB; mobile users bounce | 1 h |
| 9 | Install GTM + GA4 (Consent Mode) and verify Google Search Console | Today nothing is measured | 1 h |
| 10 | Claim/verify the Google Business Profile for the Mohali lab | Brand disambiguation, local visibility | 30 min |

---

## 5. Website plan (summary)

Full detail: `docs/strategy/02-seo-strategy.md`, `docs/strategy/04-brand-voice-and-design-system.md`, `content/`.

**Primary navigation:** For Clinicians · Diagnostics · Collection Network · Academy · Research · About · Contact
**Header call to action:** **Become a Collection Partner**

**Homepage "doors":**
- **Clinicians:** order tests, protocols, reports, CME
- **Partner hospitals:** become a collection centre
- **Couples:** "Your doctor can order these tests"
- **Students:** B.Sc./M.Sc. Clinical Embryology and lab training

**Content principles:**
- answer-first paragraphs;
- "what this test can and cannot tell you" boxes;
- citations to ESHRE and primary studies;
- a dated reviewer line;
- no prices;
- partner rate card on request only.

**Build approach on WordPress:**
- Replace the Elementor + heavy slider stack with a lightweight block theme (or Astra with native blocks).
- Keep Rank Math and LiteSpeed Cache.
- Add Forminator consent fields.
- Set a performance budget of a 1.5 MB maximum homepage weight and LCP under 2.5 s on 4G.

---

## 6. SEO strategy (summary)

1. **Entity first:**
   - Use "EmbryoGenesis Diagnostics, Mohali" naming in schema and listings.
   - Add Organization + DiagnosticLab schema with `sameAs` links.
   - Set up the Google Business Profile, ORCID, Google Scholar and a LinkedIn page.
   - Keep NAP consistent everywhere.
2. **B2B clinician cluster:**
   - chronic endometritis testing;
   - endometrial receptivity testing (ERFA vs imported panels);
   - uNK/immune profiling evidence;
   - biopsy timing protocols;
   - report interpretation;
   - "diagnostic lab partnership / collection centre" terms.
3. **Patient education cluster (English):** repeated IVF failure "what next", recurrent miscarriage and thin endometrium. Each points to "ask your doctor about testing", never to self-ordering.
4. **Academy cluster:**
   - clinical embryology course in Punjab;
   - B.Sc./M.Sc. clinical embryology;
   - embryologist salary and career;
   - "how to become an embryologist after 12th".

   Competing pages (LPU, Chitkara) are weak.
5. **GEO / AI answers:** structured, cited, answer-first pages, plus a 20-prompt monitoring panel checked monthly across ChatGPT, Gemini, Perplexity and Google AI Overviews.
6. **Cadence:** 2 articles per week, split as 50% clinician, 25% patient and 25% academy.

---

## 7. Social media strategy (summary)

Full detail: `docs/strategy/03-social-media-strategy.md`.

| Channel | Role | Cadence |
|---|---|---|
| LinkedIn company page + Prof. Purkait's profile | B2B authority, partner acquisition, CME promotion | 3–4 posts/week |
| Instagram + Facebook | Academy recruitment, science education, lab culture | 3 reels + 2 carousels/week |
| AI informative reels (cross-posted to IG/FB/YouTube Shorts/LinkedIn) | Explain the science simply and consistently at low cost | 3/week |

**Rules for the AI reels:**
- Every AI reel is scripted from approved website content and scientifically reviewed.
- Each one carries a visible "AI-generated visuals" label.
- AI avatars never impersonate doctors or patients.

---

## 8. Timeline (ASAP track)

| Week | Dates (2026) | TechnoTaau Team | Client |
|---|---|---|---|
| 1 | 15–21 Oct | Research ✅, brief ✅, blueprint ✅, SEO strategy, social strategy, design system, 5 priority pages of copy | Live-site fixes (section 4); send vector logo; pick primary phone/WhatsApp; book legal review |
| 2 | 22–28 Oct | Remaining copy: 3 test pages, patients hub, academy pages, research, contact, legal pages. High-fidelity homepage + 2 templates in Figma. LinkedIn page live and first 2 weeks of posts/reels. | Prof. Purkait reviews batch 1; developer sets up staging |
| 3–4 | 29 Oct–11 Nov | Developer support, QA on staging (SEO, performance, accessibility, compliance), redirects tested, schema validated | Developer builds; half-day lab photo shoot; review batch 2 |
| 5 | 12–18 Nov | **Launch.** 301 redirects, GSC/Bing submission, tracking verification, partner outreach begins | Approve go-live |
| 6–26 | Nov 2026–Apr 2027 | Content engine (2 articles/week), monthly CME webinar, monthly performance report, AI-visibility tracking | Monthly review call |

---

## 9. KPIs

| KPI | Baseline (Oct 2026) | 3 months | 6 months |
|---|---|---|---|
| New collection-centre partners signed | 3 centres today | +5 | +15 |
| Qualified partner/clinician enquiries per month | not tracked | 10 | 30 |
| Organic sessions per month | not tracked (estimated very low) | 1,500 | 5,000 |
| Indexed pages with impressions | ~20 | 45 | 80 |
| Academy enquiries per month | not tracked | 40 | 100 |
| LinkedIn followers | 0 (no page) | 500 | 1,500 |
| Brand appears in AI answers (20-prompt panel) | 0/20 (assumed) | 3/20 | 8/20 |
| Core Web Vitals (mobile) | failing | pass | pass |

These targets assume the client signs off copy on time and runs partner outreach. We will re-baseline them once GA4 and Search Console have 30 days of data.

---

## 10. What we need from you (open items)

1. **Vector logo files** (SVG/AI/EPS) plus the white/reversed version.
2. **One primary phone number and a WhatsApp Business number.**
3. **Legal adviser contact** for: the therapy pages, patent wording, testimonials policy and the privacy policy.
4. **Patent status:** grant certificates, if any have been granted since publication.
5. **Test details for clinicians:** methodology per test (e.g. CD138 IHC / PCR / culture), sample type, biopsy timing, transport conditions, report format sample.
6. **NABL accreditation / ART bank or lab registration numbers,** if held. These are strong trust signals.
7. **A registered medical practitioner** (NMC/state registration number) to co-review clinical pages. Prof. Purkait reviews the science; a registered clinician strengthens YMYL trust.
8. **Partner programme details:** what partners receive (kits, training, logistics, revenue model) and onboarding steps.
9. **Social media admin access,** a decision on the unified handle, and creation of the LinkedIn company page.
10. **WordPress staging site + developer contact.**

---

## 11. Deliverables index

| File | Status |
|---|---|
| `docs/00-project-brief.md` | ✅ Done |
| `docs/research/01-industry-research.md` | ✅ Done |
| `docs/research/02-competitor-keyword-social.md` | ✅ Done |
| `docs/research/03-current-site-audit.md` | ✅ Done |
| `docs/research/04-existing-website-and-social-review.md` | ✅ Done |
| `docs/strategy/01-project-blueprint.md` (this file) | ✅ Done |
| `docs/strategy/02-seo-strategy.md` | ✅ Done, in client review |
| `docs/strategy/03-social-media-strategy.md` | ✅ Done, in client review |
| `docs/strategy/04-brand-voice-and-design-system.md` | ✅ Done, in client review |
| `content/00–05` priority page copy + copy notes | ✅ Done, pending scientific review |
| `prototype/index.html` page-wise HTML prototype | ✅ Done, in client review |

*TechnoTaau Team, Jakhar Singh*
