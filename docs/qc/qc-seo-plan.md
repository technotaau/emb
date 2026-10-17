# QC report: SEO, AEO and GEO plan (`docs/strategy/05-seo-aeo-geo-plan.md`, v1.0)

**Prepared by:** TechnoTaau Team (QC, independent reviewer), for Jakhar Singh
**Date:** 17 October 2026
**Document reviewed:** `docs/strategy/05-seo-aeo-geo-plan.md` (v1.0 of 17 Oct 2026, about 24,000 words)
**Evidence base and context:** `docs/research/07-seo-aeo-geo-landscape-2026.md` (R07), `docs/research/08-keyword-competitor-ai-baseline.md` (R08), `CLAUDE.md`, `docs/00-project-brief.md`, `docs/strategy/00-business-model.md`, `docs/strategy/04-brand-voice-and-design-system.md`, `docs/strategy/02` and `03` (for cross-references), `docs/research/03-current-site-audit.md`, the four reports in `docs/qc/`, `site/src/pages/*.json` and `*.html`, `site/src/llms.txt`, `site/build.py`, `site/dist/robots.txt`.
**Method:** full read of the plan, R07 and R08; scripted checks (URLs against page JSON paths, weekday and date pairs, title and meta lengths, em dashes, RACI, section 0 word count, prompt text against R08); primary-source checks on the web for items 2a to 2l, including a page-by-page reading of the scanned NMC notice and the NMC stem cell advisory.
**Files changed:** the plan (20 logged edits, section 6) and this report. Nothing else was edited. Nothing is committed.

---

## Verdict: READY AFTER FIXES

The plan is well built and well sourced. Every load-bearing external fact holds: 12 of 12 confirmed (11 from primary sources, 1 from legal reporters), none contradicted. Section numbering, D1 to D8, URLs, dates, weekdays, title lengths and the prompt panel are consistent.

We fixed 3 Major and 13 Minor problems that were inside our remit. The worst were in the client summary: it told the client that nobody owns topics that research 08 shows others own, and it gave one deadline (9 November) for decisions that are due from 23 October.

Four Major problems remain. Each changes dates, owners, workload or KPI numbers, which we may not change. The lead should resolve them before the plan goes to the client on 19 October:
1. Prof. Purkait's and Dr. Wadhwa's pre-launch review load is about three times the review time the plan asks for (J1).
2. The live 30-day social calendar in `03` publishes AI reels and starts partner outreach from 22 and 26 October, which this plan forbids until D8 and counsel (J2).
3. Two next-30-days tasks depend on decisions or inputs that arrive later (J3).
4. The enquiry targets imply that 44 to 57% of non-branded search clicks become enquiries at months 3 and 6, while the summary says the enquiries come "from search" (J4).

**Counts:** Blocker 0 · Major 7 (3 fixed, 4 open) · Minor 26 (13 fixed, 13 open).

---

## 1. Checks 1 to 7

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Traceability to R07 and R08 | **FAIL before fixes; PASS after** | 79 tagged claims sampled across §0 to Appendix C (table in section 4). 10 mismatches, 3 of them in §0. All 10 fixed. The labels [SECONDARY], [UNVERIFIED] and [VERIFY with counsel] were carried over correctly in all 14 places checked. |
| 2 | Primary-source verification (2a to 2l) | **PASS** | 12 of 12 confirmed; none contradicted (table in section 3). 2h is confirmed at legal-reporter level because the Gazette PDF could not be retrieved; the plan already says "about 13–14 May 2027; check the Gazette". 2e is now confirmed by Google's own release notes, so its [SECONDARY] label can go (J12). Two paraphrases of the NMC text were tightened (C17, C18). |
| 3 | Guardrails in what the plan proposes | **FAIL before fixes; PASS after** | No prices, superlatives, "patented", testimonials or outcome claims in the 13 N titles and slugs, the 5 W topics, the Hindi slug, 4 proposed titles for existing pages, the Dr. Wadhwa title, 3 proposed metas, 7 proposed H1s, the no-figure cost FAQ, the review lines or the boilerplate. One breach: §3.3 proposed adding an About answer box that names therapies while D1 is open (M2, fixed by C13). Open: the N3, N4 and N5 working titles and the N5 slug ("the CD138 test") pre-empt the reviewers' decisions flagged in R08 §8 (J11). |
| 4 | Consistency with the site and the brief | **PASS after fixes** | 47 distinct paths checked against `site/src/pages/*.json`: 19 exist, 21 are new pages and every one is labelled NEW or sits in a "NEW slug" column, 7 are technical paths (`/robots.txt`, `/wp-admin/`, `/cache/`, permalink patterns and similar). D1 to D8 are numbered and described the same way in §0, §1.6, §3, §4.1, §4.2, §6 and §8.1. Names, qualifications, address, PIN conflict, lab phone, programme names, durations and patent numbers match the brief and the site. Departures from brief §0 (D1 to D3, title and H1 changes) are presented as client decisions. Fixed: the §0 deadline (C6) and a stale llms.txt note (C20). Open: D1 scope list incomplete (J9), role of 98156 92195 (J13), a live-site change scheduled before the decision call (J14). |
| 5 | Dates and arithmetic | **FAIL (review capacity)** | 23 of 23 weekday and date pairs correct. M1 = Dec 2026 to M12 = Nov 2027, admission season M5 to M9 and the checkpoints (about 8 Mar, 8 Jun, 8 Dec 2027) are correct. 19 of 19 stated title and meta lengths are correct; the 13 new N titles are 46 to 58 characters. Fixed: "about 2 new posts a month" is 1.6 (19 posts in 12 months) (C15). Open: review capacity fails in Phase 0 and in M11 (section 5.3; J1, J6). |
| 6 | Feasibility and logic | **FAIL** | Every owner exists; every KPI has a definition (Appendix A), baseline, source and owner; missing (E) labels added (C10 to C12). Open: dependency ordering in §4.2 (J3); conflict with the `03` social calendar (J2); KPI ratios a client would challenge (J4); three deadlines on regional holidays (J8); WordPress build timeline unconfirmed (J16). |
| 7 | Client readability of §0 | **FAIL (minor)** | No em dashes anywhere in the plan. §0 is about 790 words, so roughly 3 minutes (736 before our accuracy fixes). PP and VW do not appear in §0. Problems: internal tags in client text (R07/R08 five times, "QC-SEO, QC-FE, QC-DES", "G0 to G6"); terms not explained ("structured data", "proxy", "QC", "LIT", and "AEO and GEO" in the title). Readability edits are outside our fix remit (J10). |

---

## 2. Findings by severity

### Blockers (0)

None.

### Major (7)

| ID | Location | Finding and evidence | Status |
|---|---|---|---|
| M1 | §0, goal bullet 2 and move 5 | Said "These are topics no one owns today (R08 §1)" about endometrial testing, IVF failure, RIF, RPL and embryology careers, and "gaps nobody owns: … chronic endometritis, RIF and RPL tests, and embryology careers". R08 §1 item 2 names who owns them (Shree IVF/ImmuRepro, Apollo, Birla, Indira, Nova, ESHRE and PMC, Careers360, Shiksha, Zollege); only the five gaps in item 3 are unowned. The plan's own §1.2 says this correctly. Client-facing and expectation-setting. | **Fixed** (C3, C5) |
| M2 | §3.3, `/about/` row | Proposed "Add the 51-word entity answer (QC-SEO §4.1 item 4)". That answer is already in the build (`site/src/pages/about.html` line 16, builder-added, QC-CF §6.2) and says the lab "offers … therapeutic services" (QC-SEO's version says "fertility therapies"). Answer boxes are written to be quoted by AI systems; the lead removed the same therapy facts from `llms.txt` and `ORG.description` on 17 Oct (R07 §4.2; brief guardrail 4; D1). | **Fixed** (C13) |
| M3 | §0, "What we need from you" | "Eight decisions (D1 to D8) by 9 November 2026". §8.1 and §4.2 need D4 by 23 Oct, D6 and D7 by 30 Oct, D1 to D3 by 9 Nov, and D5 and D8 by 13 Nov. A client reading only §0 would miss the first two deadlines. | **Fixed** (C6) |
| M4 | §0, §3.4.2, §4.1 (Phase 0), §4.2 item 13, §8.1 #12 | Pre-launch review load is about three times the review time requested. Using the plan's own slot rule, Prof. Purkait has about 8.5 slot-equivalents (R1 to R5, T1, N4, N9) between drafts on 6 Nov and the freeze on 27 Nov, when 3 weekly slots exist. Dr. Wadhwa has 5 items (R1, R3, R4, T2, N4) for 1 or 2 fortnightly slots. The `03` social calendar adds PP review batches. Detail in section 5.3. | Open, **J1** |
| M5 | §3.9 item 9; §4.2 | `03-social-media-strategy.md` §7 runs a 30-day calendar from 20 Oct to 18 Nov: AI-visual reels from Thu 22 Oct, LinkedIn outreach to clinics from Mon 26 Oct ("15–20 requests/day"), a "What does it mean to be a collection centre?" post on Wed 28 Oct, and PP review batches on 20 Oct, 27 Oct and 5 Nov. This plan allows no AI reels before D8 (13 Nov) and legal sign-off (§3.7.6, §3.9 item 7) and no partner-facing outreach before counsel reviews clause 8.1(vii) (§3.8). The re-alignment of `03` is listed as "Separate update" with no date. Brief §0 parks the B2B parts of the strategy documents, which covers the outreach, but `03` §7 has not been re-issued and its AI reels are not B2B content. | Open, **J2** |
| M6 | §4.2 items 8 and 13 | Tasks scheduled before the decisions or inputs they need. Item 8 (handover pack, Fri 30 Oct) includes the URL, redirect and noindex rules that depend on D1 (Mon 9 Nov) and robots rules that depend on D7 (due the same day, item 11). Item 13 (drafts "through G0 to G2" by Fri 6 Nov) needs, before G1, each university's eligibility for N9 and the academy data for R5, which §8.2 #15 asks for by 13 Nov; T2 needs Dr. Wadhwa's consent and registration number, due the same day (§8.1 #11). | Open, **J3** |
| M7 | §0 goal and table; §2.3 B1, B2, S1, S2 | §0 says the goal is enquiries "from search", but B1 and B2 count all website-sourced enquiries. Against the S1 click targets, (B1 + B2) is 56% of non-branded clicks at month 3, 44% at month 6 and 15% at month 12 (floors 57%, 46%, 15%). Implied non-branded CTR is 1.3 to 1.7%, against Seer's 0.52 to 0.70% on queries with an AI Overview and 1.45% without (R07 §1.1). The numbers can work only if most enquiries come from branded, direct, GBP and referral visits, which the plan does not state. | Open, **J4** |

### Minor (26)

| ID | Location | Finding | Status |
|---|---|---|---|
| m1 | §0, "Where we are" | "Google still shows the old site … its listing carries the title". R08 §7 saw this in a proxy search with a US-based index; Google results could not be observed (R08 §0). | Fixed (C2) |
| m2 | §1.3 Aggregators; §1.6 item 14 | "one listing spells the founder 'Pulakesh'". R08 §7: seen in a search summary, "could not render to confirm". | Fixed (C8, C9) |
| m3 | §1.1 | The `/cache/` post is audit finding H6, not C1 or C7. | Fixed (C7) |
| m4 | §9, row 02 §8.3 | "residual lines 23 and 34 to fix" is stale: commit fda8576 removed that wording, and §1.1, §1.6 item 7 and §3.6.2 item 9 say the fix is done. Verified in `site/src/llms.txt` and `site/dist/llms.txt`. | Fixed (C20) |
| m5 | §2.3 S4, A2, A3 | TechnoTaau numbers without (E). For A2 the numbers were attributed to R07 §3.3, which gives no number. | Fixed (C10 to C12) |
| m6 | §3.4.4, N11 | Listed as answering Q35. R08 §5 maps Q35 to N9 and `/courses/`, and §3.5 agrees. N11 is a K15 hub topic with no R08 question. | Fixed (C14) |
| m7 | §3.5 | "Each … question has one target URL. A question is answered on that page only", while the same table gives two pages for questions 10, 20, 35 to 38 and 40 (as R08 §5 does). | Fixed (C16) |
| m8 | §9, rows 02 §3.1–3.2 and 02 §9 | The "50% clinician and B2B mix" is in 02 §9 (the calendar), not in 02 §3. | Fixed (C19) |
| m9 | §3.7, Objective | "treat search-engine and AI-assisted communication as advertising" dropped the qualifier in clause 3.2: only where the content "has a promotional character" (primary text; R07 §4.1). | Fixed (C17) |
| m10 | §3.7.4 | "the photo is a directory image, not self-promotion (NMC 9.2)" presented TechnoTaau's reading as the clause. Clause 9.2 bars RMP photos used as self-advertisement and contains no directory exemption. | Fixed (C18) |
| m11 | §0, move 3 | "two unsourced statistics"; §3.7.2 item 6 lists three figures in two posts. | Fixed (C4) |
| m12 | §3.4.5, Totals | "about 2 new posts a month on average": 19 posts (18 without the conditional Hindi post) over 12 months is 1.6 (1.5). | Fixed (C15) |
| m13 | Reading key | About 30 citations use "R08 §1.1" to "§1.10", but R08 §1 is a numbered list, not subsections. | Fixed (C1) |
| m14 | §0 move 5; §3.4.2 | "About two new reviewed articles a month" and "Steady cadence (M5 to M12): about 2 new posts a month", while the calendar gives 1.4 a month in M5 to M12 (1 in M6, M9 and M11; none in M12). | Open, J5 |
| m15 | §3.4.5 | Re-reviews due around M12 are missing: the second 6-month review of `/diagnostic/` and the 12-month reviews of R2 to R4 (refreshed Nov 2026). "At least one refresh or re-review a month" in M1 to M4 is not in the calendar. M11 (W4 plus R8, eight academy items) needs about 5 PP slots against about 4.3. | Open, J6 |
| m16 | §2.3 C2; §3.4.2 step-up rule | Median G3 turnaround of 5 working days or less is hard for any item that needs Dr. Wadhwa, whose slot is fortnightly: expect 5 to 10 working days. | Open, J7 |
| m17 | §4.2 | Tue 20 Oct is Dussehra (item 2); Mon 9 Nov, the D1 to D3 deadline (item 14), is the day after Diwali and appears as Vishwakarma Day on a Punjab holiday list; Tue 24 Nov (Guru Nanak Gurpurab) falls in the QA pass 2 and freeze week. | Open, J8 |
| m18 | §3.7.1 "In scope" | The D1 scope list omits builder-added therapy mentions and links: the About answer box and its "Explore our … therapeutic services" line, the Contact line "ask about therapies" and its link, the LIT and Hindi cards on the blog index, and the 404 page link (`grep` of `site/src/pages`). The go-live crawl would catch the links, but the client is approving the list. | Open, J9 |
| m19 | §0 | Readability: see check 7. | Open, J10 |
| m20 | §3.4.4, §3.4.5 | N5 is titled and slugged around "the CD138 test", and N3 and N4 around timing wording, before the reviewers decide on CD138 framing and biopsy timing (R08 §8.1, §8.3; Odendaal 2026). | Open, J11 |
| m21 | §2.4, §3.1 item 17, §9 | GA4's AI Assistant channel is still labelled [SECONDARY]; Google's release notes (13 May 2026) and Help Center now confirm it. | Open, J12 |
| m22 | §3.2 Phone row; §8.1 #4 | Brief §2 lists 98156 92195 as the Delhi regional centre number; the old site, schema `contactPoint`, `llms.txt` and the course pages label it "Admissions". D4 asks for "admissions labels" but does not name this conflict. | Open, J13 |
| m23 | §4.2 item 5; §1.6 items 1 and 5 | Live-site title and meta changes on Fri 23 Oct come before the decision call (week of 26 Oct). They are SEO metadata, but they are the client's current wording. | Open, J14 |
| m24 | §6 RACI vs §5.5 | RACI makes JS accountable for "Incident response"; §5.5 makes the client accountable for I3 to I5. "TechnoTaau builder" (§4.2 item 10) is not a defined role. | Open, J15 |
| m25 | §1.1, §4.2, §3.1 QC check | WordPress port "not yet started as far as we know", yet staging is due 13 Nov and the code freeze is 27 Nov. QA pass 2 falls on the freeze day, which leaves no time to fix what it finds before the freeze. | Open, J16 |
| m26 | §2.3 T1 | Baseline gives Lighthouse performance scores (20/100, about 89) for a KPI defined as Core Web Vitals pass or fail. Suggest "Lab pass/fail to be measured on staging; reference build Lighthouse about 89". | Open (note) |

---

## 3. Primary-source verification (2a to 2l)

| Item | What the plan relies on | Result | Primary or most authoritative source | Notes |
|---|---|---|---|---|
| 2a | FAQ rich results not shown for any site since 7 May 2026; HowTo and Course info gone (§3.5, §2.4, §9) | **Confirmed** | Google Search Central documentation updates, entries of 8 May 2026 ("This feature will no longer appear in Google Search starting May 7, 2026") and 15 Jun 2026 (docs removed): https://developers.google.com/search/updates · Google's notice as quoted by SEJ, 10 May 2026 (FAQ report and Rich Results Test support dropped June 2026; API August 2026): https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/ · HowTo deprecated 13 Sep 2023: https://developers.google.com/search/blog/2023/08/howto-faq-changes · Course info docs removed 9 Sep 2025 (updates log) | No site-level exception remains. |
| 2b | Google guidance of 15 May 2026: AI Overviews and AI Mode use core ranking systems; llms.txt, chunking and extra structured data not needed (§3.6, §3.1) | **Confirmed** | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (added 15 May 2026 per the updates log; last updated 10 Jul 2026): "rooted in our core Search ranking and quality systems"; "You don't need to create new machine readable files, AI text files, markup, or Markdown"; "There's no requirement to break your content into tiny pieces"; "Structured data isn't required for generative AI search". llms.txt clarification, 15 Jun 2026 (updates log). | The guide says "rooted in"; "rely on" is the wording of the older AI features page (R07 G1). Same meaning. |
| 2c | Search Console Generative AI report (impressions only) and the "Include" control (§2.4, §3.1 item 15) | **Confirmed** | https://support.google.com/webmasters/answer/16984139 (impressions only; pages, countries, dates, devices; missing until enough AI impressions) · https://support.google.com/webmasters/answer/16908024 (default Include; "As of August 31, 2026, we've rolled out this control to all websites worldwide"; excluding affects neither ranking nor training) · launch post (June 2026): https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports | |
| 2d | Bing Webmaster Tools AI Performance report: citations, grounding queries (§2.4, §3.6.2) | **Confirmed** | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview (10 Feb 2026: total citations, average cited pages, grounding queries as a sample, page-level citations; Copilot, Bing AI summaries, select partners) · https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare (16 Jun 2026: Intents, Topics, Citation Share, Compare, in preview) | The launch post does not itself say "no clicks or traffic" (R07's wording). The plan does not repeat that point. |
| 2e | GA4 native "AI Assistant" channel, 13 May 2026 (§2.4, §3.1 item 17) | **Confirmed (primary)** | https://support.google.com/analytics/answer/9164320 ("What's new", 13 May 2026: "New AI Assistant traffic measurement"; medium `ai-assistant`, campaign `(ai-assistant)`) · https://support.google.com/analytics/answer/9756891 (channel excludes AI Overviews and AI Mode, which count as Organic Search) | R07 and the plan label it [SECONDARY]; the label can be lifted (J12). |
| 2f | NMC Guidelines on Ethical Advertising and Public Communication, notice of 6 Oct 2026, R-13014/01/2024-Ethics; clauses 3.2, 6.2, 7.2, 8.1(i), (iii), (v), (vi), (vii), (ix), 9.1, 9.2, Explanations III to V | **Confirmed** | Primary notice, 13-page scanned PDF, read page by page: https://www.nmc.org.in/whats-new/download/1874 . Page 1: No. R-13014/01/2024-Ethics, dated 06/10/2026, Ethics & Medical Registration Board, signed Dr. Raghav Langer, "in force with immediate effect". Clause 3.2 lists "search-engine … AI-generated or AI-assisted promotional communications" as advertising "where their content or manner of dissemination has a promotional character"; Explanations I to V, 6.2, 7.2, 8.1(i), (iii), (v), (vi), (vii) ("specimens or materials for diagnosis"), (ix) with its award proviso, 9.1 and 9.2 match the plan and R07 §4.1. Trade coverage agrees: https://medicaldialogues.in/health-news/nmc/nmc-issues-ethical-advertising-public-communication-guidelines-for-doctors-hospitals-details-180731 | Two plan paraphrases were tightened (C17, C18). Note for counsel: 8.1(i) to (viii) are framed as duties of RMPs, while (ix) to (xii) name "RMP or hospital/medical institution". The plan treats all of them as binding, with [VERIFY with counsel], which is the right posture. |
| 2g | NMC stem cell advisory of 5 Sep 2026 (§3.7.1) | **Confirmed** | NMC EMRB advisory No. R-13014/28/2022-Ethics, dated 05.09.2026 (copy of the signed document): https://medicaldialogues.in/pdf_upload/2026/09/07/nmc-advisory-05092026-474464.pdf : "Stem Cell Therapy may be offered as standard clinical care, ONLY for approved indications as listed in ICMR/DHR/MoHFW guidelines. Any unauthorized administration, prescription, promotion or advertisement thereof, beyond such approved indications, shall constitute professional misconduct." | Issued under the Supreme Court order of 30 Jan 2026 (autism case). |
| 2h | DPDP Rules 2025: main obligations from about 13 or 14 May 2027 (§3.1 item 18, §5.3, §7 risk 11) | **Confirmed (legal-reporter level)** | SCC Online, 14 Nov 2025: Rules notified 13 Nov 2025; Rules 3, 5–16, 22–23 after eighteen months: https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/ · DPDP rules reference (G.S.R. 846(E); Rules 3 and 5–16 from 14 May 2027; the proposal to shorten the timeline "has not been notified"): https://dpdpa.dcomply.in/rules/ | The Gazette and PIB pages could not be retrieved (PIB returned 403). Sources differ between 13 and 14 May 2027, as the plan says. |
| 2i | ESHRE 2023 RIF good practice recommendations: uNK testing "not recommended"; chronic endometritis assessment "can be considered" (§3.4.3 R1, R3; §3.5) | **Confirmed** | ESHRE Working Group on RIF, Hum Reprod Open 2023, hoad023: https://pmc.ncbi.nlm.nih.gov/articles/PMC10270320/ : "Uterine NK cell testing is not recommended."; "Assessment for chronic endometritis (CE) can be considered."; also "insufficient data to recommend the routine use of any commercially available test of endometrial receptivity". | |
| 2j | Odendaal et al. 2026, Human Reproduction: CD138 testing "should not be performed outside of a research context" (§3.4.2, §7 risk 7) | **Confirmed** | Human Reproduction 2026;41(5):699–711, doi 10.1093/humrep/deag032; eprint: https://eprints.whiterose.ac.uk/id/eprint/239619 : "CD138-based CE testing and treatment should not be performed outside of a research context." | The cohort is 103 samples from women with recurrent pregnancy loss (CERM trial). The reviewers should weigh that population when framing EIT for IVF patients. |
| 2k | ESHRE 2022 RPL guideline recommends against LIT (§3.7.1) | **Confirmed** | ESHRE RPL guideline, update 2022 (final version January 2023), recommendation 68, strength "Strong": "Lymphocyte immunization therapy should not be used as treatment for unexplained RPL as it has no significant effect and there may be serious adverse effects." https://www.eshre.eu/-/media/sitecore-files/Guidelines/Recurrent-pregnancy-loss/2022/ESHRE-RPL-Guideline-_-Update-2022_-Final-Version-January-2023_v2.pdf | The journal summary (Hum Reprod Open hoad002, PMC9982362) lists only changed recommendations and does not repeat it. Cite the full guideline. |
| 2l | Pew 2025: 8% vs 15% clicks, 1% on cited sources; Ahrefs 75,000 brands, 0.664 for branded web mentions (§2.1, §3.6.1) | **Confirmed** | Pew Research Center, 22 Jul 2025 (900 US adults, March 2025; 8% vs 15%; 1%; 26% vs 16% ended browsing): https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ · Ahrefs, 26 May 2025 (75,000 brands; Spearman 0.664; domains with DR above 40 only): https://ahrefs.com/blog/ai-overview-brand-correlation/ | |

Also checked (not required): the ASCI synthetic-content labelling guidelines were released on 29 Sep 2026 and take effect on 29 Dec 2026 (Khaitan & Co note, R07 I10). The plan's [SECONDARY] label is still right, because ASCI's own final PDF was not opened.

---

## 4. Traceability sample (79 claims)

✓ = the cited section says it, with numbers, dates and labels intact. ✗ = mismatch (all fixed; see section 6).

| # | Plan location | Claim (short) | Cited | Verdict |
|---|---|---|---|---|
| 1 | §0 | AI search cited EmbryoGenesis 0 times in 25 prompts | R08 §6 | ✓ |
| 2 | §0 | PIN shown three ways; the only university page naming the lab is gone | R08 §7 | ✓ |
| 3 | §0 | "These are topics no one owns today" | R08 §1 | ✗ contradicts item 2 (C3) |
| 4 | §0 | "Google still shows" the old title | R08 §7 | ✗ proxy index, not Google (C2) |
| 5 | §0 | Advertising rules stricter from 6 Oct 2026 | R07 §4.1 | ✓ |
| 6 | §0 | "gaps nobody owns: … CE, RIF, RPL, careers" | R08 §1 | ✗ (C5) |
| 7 | §1.1 | Old titles still indexed for `/diagnostic/` and `/unexplained-infertility/` | R08 §7 | ✓ |
| 8 | §1.1 | llms.txt therapy facts removed | R07 §2 impl. 6 | ✓ (file checked) |
| 9 | §1.1 | `ORG.description` without therapies | R07 §4.2 | ✓ (`build.py` checked) |
| 10 | §1.2 | No appearance in non-branded results | R08 §1.1 | ✓ |
| 11 | §1.2 | Brand searches return Mohali directories and West Bengal politicians | R08 §1.1 | ✓ |
| 12 | §1.2 | Who owns the answers | R08 §1.2, §4 | ✓ |
| 13 | §1.2 | Five open gaps | R08 §1.3 | ✓ |
| 14 | §1.3 | Maps place, KG ID `/g/11y4zwq7dd` | R08 §7 | ✓ |
| 15 | §1.3 | 140302 / 140103 / 140104 and their sources | R08 §7 | ✓ |
| 16 | §1.3 | Wikidata Q28962 = biological process; no items | R08 §7 | ✓ |
| 17 | §1.3 | Latrexa PIN 140103, phone 081462 17196 | R08 §7 | ✓ |
| 18 | §1.3 | ORCID, 40 works incl. ERFA, ReceptivityPX, LIT-H2 | R08 §7 | ✓ |
| 19 | §1.3 | ITHS "15+ patents", no link | R08 §7, §8.5 | ✓ |
| 20 | §1.3 | Bahra page 301 to bushimla.in | R08 §7 | ✓ |
| 21 | §1.3 | News items and dates (TOI, Himachal Tonite, NewsNation "brand story") | R08 §7 | ✓ |
| 22 | §1.3 | "Pulakesh" spelling on ivf.net | R08 §7 | ✗ caveat dropped (C8, C9) |
| 23 | §1.4 | P6, P24, P19 appearances | R08 §6.1 | ✓ |
| 24 | §1.4 | Proxy with a US-based index | R08 §0 | ✓ |
| 25 | §1.4 | Hindi post: LIT "increases the chance of successful conception" | R08 §1.5 | ✓ |
| 26 | §1.5 | Generative AI report appears only after enough impressions | R07 §3.1 | ✓ |
| 27 | §2.1 | Being cited is the new unit of visibility | R07 §0 item 2 | ✓ |
| 28 | §2.2 | GA4 figures are floors under consent mode | R07 §3.1 | ✓ |
| 29 | §2.3 A2 | "1 / 2 of 3" | R07 §3.3 | ✗ R07 gives no number (C11) |
| 30 | §2.3 A3 | At least 1 cited page by month 3 | R07 §3.3 | ✓ |
| 31 | §2.3 A5 | 100% of AI errors fixed at source in 30 days | R07 §3.3 | ✓ |
| 32 | §2.3 | "Not used as KPIs" list | R07 §3.3 | ✓ |
| 33 | §2.4 | AI report: impressions only, no clicks or queries | R07 §3.1 | ✓ |
| 34 | §2.4 | GA4 AI Assistant channel 13 May 2026 [SECONDARY] | R07 §3.1 | ✓ label carried |
| 35 | §2.4 | Rich Results Test no longer supports FAQ | R07 §1.2 | ✓ |
| 36 | §3.1 item 7 | Bot list; Applebot-Extended [UNVERIFIED] | R07 §2.4 | ✓ (matches `dist/robots.txt`) |
| 37 | §3.1 item 8 | CDN default blocking [UNVERIFIED] | R07 §2 impl. 1 | ✓ |
| 38 | §3.1 item 10 | Rank Math IndexNow [UNVERIFIED]; Google not participating [SECONDARY] | R07 §2.5 | ✓ |
| 39 | §3.1 item 18 | DPDP duties about 13–14 May 2027; earlier date not notified | R07 §4.7 | ✓ |
| 40 | §3.2 item 2 | Category likely "Medical laboratory" [check]; never "IVF clinic" | R07 §5.1 | ✓ |
| 41 | §3.2 item 3 | Video verification [UNVERIFIED] | R07 §5 impl. 1 | ✓ |
| 42 | §3.2 item 9 | Justdial free listings not verified | R07 §5.2 | ✓ |
| 43 | §3.2 item 11 | Wikidata benefit [UNVERIFIED]; no Wikipedia | R07 §2.2 | ✓ |
| 44 | §3.3 | Keyword traps: ICSI, RIF test, ERA cost, soil test, PBMC | R08 §1.6 | ✓ |
| 45 | §3.3 | Birla's 39 city cost pages | R08 §4 | ✓ |
| 46 | §3.3 | Sex-selection terms: ART Act s.32, PCPNDT s.22 | R07 §4.3, §4.4 | ✓ |
| 47 | §3.4.2 | Three of five priority-1 posts wait on reviewer decisions | R08 §8.1, §8.3 | ✓ |
| 48 | §3.4.3 R1 | ESHRE wordings ("can be considered", "insufficient data …", "not recommended") | R08 §8 | ✓ (also primary, 2i) |
| 49 | §3.4.3 R3 | "uterine NK cell testing is not recommended" | R08 §8.2 | ✓ |
| 50 | §3.4.4 | Questions and priorities for N1 to N10, N12, N13 | R08 §5, §1.10 | ✓ |
| 51 | §3.4.4 | N11 answers Q35 | R08 §5 | ✗ (C14) |
| 52 | §3.4.4 W1 | "is an embryologist a doctor": 7 autocomplete variants | R08 K19, Q36 | ✓ |
| 53 | §3.5 | FAQ gone 7 May 2026; HowTo and Course info gone | R07 §1.2 | ✓ (also primary, 2a) |
| 54 | §3.5 | "one target URL" per question | R08 §5 | ✗ two-page mappings (C16) |
| 55 | §3.5 | YouTube is the most-cited domain in AI Overviews | R07 §1.1 (R3) | ✓ |
| 56 | §3.5 | Hindi and Hinglish queries return English foreign pages | R08 §2.1 | ✓ |
| 57 | §3.6 | Core ranking systems; llms.txt and chunking not needed | R07 §0 item 1, §1.1 | ✓ (also primary, 2b) |
| 58 | §3.6.1 | 0.664; DR above 40 only | R07 §2.2 (R4) | ✓ |
| 59 | §3.6.1 | About 40% in a lab pipeline | R07 §2.2 (R1) | ✓ |
| 60 | §3.6.1 | 37.9% of cited URLs in the top 10 | R07 §1.1 (R3) | ✓ |
| 61 | §3.6.2 item 9 | 97% of llms.txt files got no requests | R07 §2.3 | ✓ |
| 62 | §3.6.3 | 3 runs, 2-of-3 rule, 2 surfaces | R07 §3.2 | ✓ |
| 63 | §3.6.3 | 300 runs about 6 hours (E), scaled from 240 = half a day | R07 §3.2 | ✓ plausible |
| 64 | §3.7 | Search-engine and AI-assisted communication treated as advertising | R07 §4.1, cl. 3.2 | ✗ "promotional" dropped (C17) |
| 65 | §3.7.1 | Stem cell advisory of 5 Sep 2026 | R07 §4.2 | ✓ (also primary, 2g) |
| 66 | §3.7.1 | DMR Act covers "sterility in women" | R07 §4.5 | ✓ |
| 67 | §3.7.1 | ESHRE 2022 RPL against LIT | R08 §8.4 | ✓ (also primary, 2k) |
| 68 | §3.7.2 | Testimonials: NMC 6.2, 8.1(v), Explanation V | R07 §4.1 | ✓ |
| 69 | §3.7.4 | Directory photo "not self-promotion (NMC 9.2)" | R07 §4.1 | ✗ reading shown as rule (C18) |
| 70 | §3.7.6 | NMC 7.2 quotation [VERIFY with counsel] | R07 §4.1 | ✓ |
| 71 | §3.7.6 | ASCI from 29 Dec 2026 [SECONDARY]; IT Rules from 20 Feb 2026 [SECONDARY] | R07 §4.6 | ✓ labels carried |
| 72 | §3.7.8 | Four proposed brief additions | R07 §4 impl. 1, §6.1 | ✓ |
| 73 | §3.8 | Paid advertorials and site reputation abuse | R07 §1.3 | ✓ |
| 74 | §3.9 item 6 | YouTube health features; India thresholds [UNVERIFIED] | R07 §2.2 (G21) | ✓ |
| 75 | §7 risk 5 | Core update 11–29 Dec 2025 | R07 §1.4 | ✓ |
| 76 | §7 risk 13 | "Origin LIFE" programme on the RBU campus | R08 §1.9, §4 | ✓ |
| 77 | §9 | Only verified figure: more than 82% of German health searches | R07 §1.1, §6.1 | ✓ |
| 78 | §9 | llms.txt "residual lines 23 and 34 to fix" | R07 §6.1 | ✗ stale (C20) |
| 79 | Appendix C | 25 prompts "paste exactly" | R08 §6.1 | ✓ 25 of 25 identical (P2's note reads "also in" instead of "also run in") |

---

## 5. Dates, arithmetic and capacity: detail

### 5.1 Weekdays, months and lengths
- All 23 weekday and date pairs (§0 to §4.2) are correct for 2026, checked with Python `datetime`.
- M1 = Dec 2026 to M12 = Nov 2027; the admission season April to August is M5 to M9. Checkpoints 3, 6 and 12 months after 8 Dec 2026 are 8 Mar, 8 Jun and 8 Dec 2027. All correct.
- Character counts: all 19 lengths stated in §3.3 and §3.7.4 (15 kept or proposed titles, the Dr. Wadhwa title and 3 metas) match. The 13 N titles run from 46 to 58 characters (limit 60).
- Regional holidays in the next 30 days: Dussehra Tue 20 Oct 2026, Diwali Sun 8 Nov, Vishwakarma Day Mon 9 Nov (Punjab list), Guru Nanak Gurpurab Tue 24 Nov. Sources: AG Punjab holiday list (https://cag.gov.in/ag2/punjab/en/page-ag2-punjab-holiday-list) and a Punjab bank-holiday list citing punjab.gov.in for 9 Nov (confirm).

### 5.2 Posts per month (calendar §3.4.5)

| M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 (incl. Hindi H1, conditional) | 1 | 0 | 19 (18 without H1) |

So the year averages 1.6 new posts a month (1.5 without H1). M5 to M12 average 1.4, against the "about 2" stated in §0 and §3.4.2.

### 5.3 Review capacity (the plan's own slot rule, §3.4.2: a medical post or a medical refresh = 1 slot; two academy posts or small updates = 1 slot)

**Phase 0, drafts on Fri 6 Nov to freeze on Fri 27 Nov.** Prof. Purkait's slots fall in the weeks of 9, 16 and 23 Nov, so 3 slots.

| Item | Reviewers | PP slot-equivalents |
|---|---|---|
| R1 diagnostic page | PP + VW | 1 |
| R2 ERFA post | PP | 1 |
| R3 EIP post | PP + VW | 1 |
| R4 unexplained post | PP + VW | 1 |
| R5 four course and training pages | PP + admissions | 2 |
| T1 editorial policy | PP (+ counsel) | 1 (our assumption) |
| N4 biopsy post | PP + VW | 1 |
| N9 embryologist post | PP + admissions | 0.5 |
| **Total** | | **8.5 against 3 (about 2.8 times); 7 against 3 without N4 and N9** |

Dr. Wadhwa has 5 items (R1, R3, R4, T2, N4) and one or two fortnightly 60-minute slots in the same window. Both reviewers also sit the 90-minute decision session on 28 Oct. In addition, `03` §7 books Prof. Purkait for social review batches on 20 Oct, 27 Oct and 5 Nov, plus LinkedIn posts and outreach.

**Steady state.** Prof. Purkait has about 4.3 slots a month. The calendar needs about 1.5 to 2.5 in M1 to M10, about 5 in M11 (W4 plus R8's eight academy items) and 1.5 in M12. M12 rises to about 5.5 if the missing re-reviews are added (m15). If "one new medical post (two review rounds)" means two separate slots, M7 reaches 4 and M11 reaches 6. Dr. Wadhwa's load (1 or 2 items a month) fits a fortnightly slot. The plan's C2 target of 5 working days does not fit it (m16).

### 5.4 KPI ratios (§2.3)

| Checkpoint | Implied non-branded CTR (S1 ÷ S2), floor / target | (B1 + B2) ÷ S1, floor / target |
|---|---|---|
| 3 months | 1.33% / 1.33% | 57% / 56% |
| 6 months | 1.50% / 1.67% | 46% / 44% |
| 12 months | 1.50% / 1.71% | 15% / 15% |

For comparison, R07 §1.1 (Seer) gives an organic CTR of 0.52 to 0.70% on queries with an AI Overview and 1.45% without one.

---

## 6. Change log (fixes applied to the plan)

| # | Section | Old → new | Reason |
|---|---|---|---|
| C1 | Reading key (line 16) | "(R08 §x) = research 08." → "(R08 §x) = research 08; (R08 §1.6) means research 08, section 1, finding 6." | R08 §1 is a numbered list, not subsections; about 30 citations use §1.1 to §1.10. |
| C2 | §0, "Where we are", bullet 2 | "Google still shows the old site. Its listing for the Diagnostic page still carries the title …" → "Search results still show the old site. In our search checks, the Diagnostic page was still listed with the title …" | R08 §7 evidence is a proxy search; Google results could not be observed (R08 §0). |
| C3 | §0, goal bullet 2 | "These are topics no one owns today (R08 §1)." → "Clinic chains, journals and education portals answer most of these questions today. Our research found five open gaps that no one owns yet, such as ERA versus ERFA, the endometrial biopsy explained for patients and north-India embryology admissions (R08 §1)." | Contradicted R08 §1 item 2; only the five gaps in item 3 are unowned. |
| C4 | §0, move 3 | "two unsourced statistics" → "unsourced statistics" | §3.7.2 item 6 lists three figures in two posts. |
| C5 | §0, move 5 | "on gaps nobody owns: endometrial biopsy, receptivity tests, chronic endometritis, RIF and RPL tests, and embryology careers" → "first on the open gaps (the endometrial biopsy, receptivity tests including ERA versus ERFA), then on topics others answer today: chronic endometritis, RIF and RPL tests, and embryology careers" | As C3 (R08 §1 items 2 and 3). The cadence words were not changed. |
| C6 | §0, "What we need from you" | "Eight decisions (D1 to D8) by **9 November 2026**" → "Eight decisions (D1 to D8) between **23 October and 13 November 2026** (each date in §8.1)" | §8.1 and §4.2: D4 23 Oct; D6 and D7 30 Oct; D1 to D3 9 Nov; D5 and D8 13 Nov. |
| C7 | §1.1, "Old site defects" | "R03 (C1, C7)" → "R03 (C1, H6, C7)" | The `/cache/` post is audit finding H6. |
| C8 | §1.3, Aggregators | "one listing spells the founder 'Pulakesh'" → "one listing reportedly spells the founder 'Pulakesh' (seen in a search summary; not confirmed)" | R08 §7: "could not render to confirm". |
| C9 | §1.6, item 14 | "'Pulakesh' spelling on ivf.net … ask ivf.net to correct the spelling" → "'Pulakesh' spelling reported on ivf.net, not confirmed … check the ivf.net listing and ask for a correction if the spelling is confirmed" | As C8. |
| C10 | §2.3, S4 | "85% / 95%", "90% / 100%", "90% / 100%" → each followed by "(E)" | TechnoTaau estimates; the Phase 1 exit criterion for the same metric already carries (E). |
| C11 | §2.3, A2 | "1 / 2 of 3 (R07 §3.3)" → "1 / 2 of 3 (E; R07 §3.3 aims for brand prompts visible by month 3)"; 6- and 12-month cells + "(E)" | R07 §3.3 gives no numeric floor or target. |
| C12 | §2.3, A3 | "1 / 2 (R07 §3.3 proposes at least 1)" → "1 / 2 (E; R07 §3.3 proposes at least 1)" | The target of 2 is TechnoTaau's. |
| C13 | §3.3, `/about/` notes | "Add the 51-word entity answer and the disambiguation line (QC-SEO §4.1 item 4; client approval)." → "The entity answer box (QC-SEO §4.1 item 4) is already in the build: take 'therapeutic services' out of it while D1 is open, because answer boxes are written to be quoted and therapy facts stay out of machine-readable summaries (R07 §4.2). Add the disambiguation line (client approval)." | Guardrail 4 and D1; consistency with the lead's 17 Oct fix. The answer exists in `about.html` (builder-added, QC-CF §6.2). |
| C14 | §3.4.4, N11 | Questions answered "35" → "– (K15 hub topic, R08 §3)" | R08 §5 and §3.5 map Q35 to N9 and `/courses/`. |
| C15 | §3.4.5, Totals | "That is about 2 new posts a month on average." → "That is about 1.6 new posts a month on average (19 in 12 months, or 18 without the conditional Hindi post): 2 a month from M1 to M5, then 0 to 2 a month." | Arithmetic: 19 ÷ 12 = 1.58. |
| C16 | §3.5, Question bank usage | "has one target URL. A question is answered on that page only; other pages link to it." → "has one main target URL. Where the table names a second page (questions 10, 20, 35 to 38 and 40), that page gives only a short answer and links to the main one; all other pages link to it." | The section's own table and R08 §5 give two pages for these questions. |
| C17 | §3.7, Objective | "which treat search-engine and AI-assisted communication as advertising" → "which treat promotional search-engine and AI-assisted communication as advertising" | NMC clause 3.2 (primary text) and R07 §4.1. |
| C18 | §3.7.4, Dr. Wadhwa profile row | "the photo is a directory image, not self-promotion (NMC 9.2)" → "NMC 9.2 bars RMP photos used as self-advertisement; in our reading a plain directory photo is not self-promotion" | Clause 9.2 has no directory exemption; this is TechnoTaau's reading (R07 §4.1). |
| C19 | §9, rows 02 §3.1–3.2 and 02 §9 | "including its 50% clinician and B2B mix" moved from the keyword-map row ("including its B2B keyword focus") to the calendar row ("By §3.4.5, including its 50% clinician and B2B mix") | The 50% mix is in 02 §9, not in 02 §3. |
| C20 | §9, row 02 §8.3 | "residual lines 23 and 34 to fix" → "the residual therapy wording in lines 23 and 34 was removed on 17 Oct 2026" | Commit fda8576; matches §1.1, §1.6 item 7 and §3.6.2 item 9. |

After these edits the plan still has no em dashes, all weekday and date pairs still check out, and §0 is about 790 words.

---

## 7. Judgement calls for the lead

These are strategic or scheduling choices we did not change. Each has our reasoning and a suggested resolution.

| ID | Issue | Reasoning | Suggested resolution |
|---|---|---|---|
| **J1** (M4) | Pre-launch review capacity | The plan asks for 90 minutes a week from Prof. Purkait and 60 minutes a fortnight from Dr. Wadhwa. Phase 0 needs about 8.5 and 5 slot-equivalents in three weeks (section 5.3). A client who agrees to the stated time will be surprised in November, or the refresh pack will slip past the freeze. | Ask for a pre-launch surge (Prof. Purkait 3 × 90 minutes a week and Dr. Wadhwa weekly, 9 to 27 Nov) and say so in §0 and §8.1 #12. Or move N4 and N9 review to 1 to 11 Dec (they publish after the freeze, from week 2 of M1), and let admissions check R5 facts with Prof. Purkait approving wording only. |
| **J2** (M5) | `03` social calendar conflicts with this plan | AI-visual reels from 22 Oct, clinic outreach from 26 Oct and a collection-centre post on 28 Oct run before D8 and counsel. The plan says no AI reels until legal sign-off and no partner-facing outreach until counsel reviews clause 8.1(vii). Its own fix ("Separate update") has no date. | Add a §4.2 item for Mon 19 Oct: "pause the AI reels and the partner-facing posts and outreach in 03 §7 until D8 and counsel; non-AI educational posts continue through G4". Re-issue the `03` calendar after 13 Nov. |
| **J3** (M6) | Dependency ordering in §4.2 | Item 8 needs D1 (9 Nov) and D7 (same day); item 13 needs academy facts due 13 Nov and Dr. Wadhwa's consent due the same day. | Issue the handover pack as v1 on 30 Oct with the D1-dependent rules written for both options, and v2 on Tue 10 Nov. Move §8.2 #15 (academy facts) to 30 Oct, or move the N9 and R5 drafts to 16 Nov. Make T2 conditional on §8.1 #11. |
| **J4** (M7) | KPI framing and plausibility | (B1 + B2) is 44 to 57% of non-branded clicks at months 3 and 6, and implied CTR is above published benchmarks. §0 says enquiries come "from search". The A2 target (2 of 3 brand prompts by month 3) is also below R07 §3.3's aim of all brand prompts visible by month 3. | State the assumption in §2.2: most website enquiries come from branded, direct, GBP and referral visits, and non-branded search adds an estimated share. Re-word §0 to "from your website, including search". Keep or revise the numbers at L+30 as the plan already provides. Decide whether A2 stays deliberately conservative. |
| J5 | Cadence wording | §0 and §3.4.2 say about 2 posts a month; the calendar gives 1.6 a year and 1.4 in M5 to M12. | Either add reserve or data-led posts in M6, M9, M11 and M12, or restate the cadence as "2 a month until April, then 1 to 2". |
| J6 | Calendar gaps and M11 load | Re-reviews due around M12 are missing; the M1 to M4 refresh promise is not scheduled; M11 is over capacity. | Add the R2 to R4 12-month reviews and the second `/diagnostic/` review to M12 or M13. Split R8 across M10 and M11, or move W4 to M12. |
| J7 | C2 target vs Dr. Wadhwa's fortnightly slot | Items needing a clinical review will usually wait 5 to 10 working days. | Report C2 for each reviewer, or set 10 working days for items that need Dr. Wadhwa, or ask for a weekly slot. |
| J8 | Holidays | 20 Oct (Dussehra), 9 Nov (D1 to D3 deadline, day after Diwali, likely a Punjab holiday) and 24 Nov (Gurpurab, freeze week). | Move the D1 to D3 deadline to Tue 10 Nov (or Fri 6 Nov) and allow for 24 Nov in the freeze week. |
| J9 | D1 scope list | Builder-added therapy mentions and links on About, Contact, the blog index and the 404 page are missing from the list the client approves. | Add them to §3.7.1 "In scope" and to §4.2 item 10, which already removes builder-added therapy names from the Related boxes. |
| J10 | §0 readability | Internal tags and unexplained terms in client text. | Replace the in-line tags with one closing "Sources" line. Add one line on AEO and GEO ("answer engines: being the direct answer; generative engines: being cited by AI assistants"). Expand LIT and QC, and say "search labels (structured data)". Trim back toward 700 words. |
| J11 | N3, N4, N5 titles and slugs | They pre-empt the reviewers' CD138 and timing decisions. | Mark the titles and slugs provisional until the 28 Oct session. Consider a neutral slug such as `/chronic-endometritis-testing/` for N5. |
| J12 | GA4 label | Google's own release notes now confirm the channel. | Lift [SECONDARY] in §2.4, §3.1 item 17 and §9 and cite https://support.google.com/analytics/answer/9164320 . |
| J13 | 98156 92195 | The brief and the site disagree on whether it is the Delhi centre or admissions. | Name it in D4 (§4.2 item 4; §8.1 #4). |
| J14 | Live-site changes on 23 Oct | These change the client's current metadata before the decision call. | Add "with the client's go-ahead by email" to §4.2 item 5 and §1.6 items 1 and 5. |
| J15 | RACI | Incident accountability differs between §6 and §5.5; "builder" is not a defined role. | Make the RACI row read "per §5.5", and add the builder to the roles or name CW or QA. |
| J16 | Launch realism | Port not started; staging 13 Nov; freeze 27 Nov; QA pass 2 on the freeze day. | Get the developer's own estimate before D6 is confirmed, and hold QA pass 2 two working days before the freeze. |

---

## 8. Limits of this review
- We did not run the AI panel or the manual SERP checks (they are Phase 0 tasks in the plan).
- The DPDP Gazette PDF and PIB release could not be retrieved; 2h rests on legal reporters.
- The Bing help pages were not reached; 2d rests on Bing's own blog posts.
- Capacity figures use the plan's own slot rule, which is itself an estimate (E). The T1 slot cost is our assumption.
- The Vishwakarma Day date comes from one secondary list; please confirm against punjab.gov.in.

TechnoTaau Team (QC)
