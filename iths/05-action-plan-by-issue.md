# ITHS: Action Plan by Issue

**Prepared by:** TechnoTaau Team. Team lead and sign-off: Jakhar Singh.
**Date:** 27 November 2026 | **Version:** 1.0
**What this is:** the answer to each point the client raised on 27 Nov 2026, using the Search Console and GA4 data (`04-baseline-report.md`). The full detail is in `02-iths-master-plan.md`; this document is the short version to act on.

---

## At a glance

| # | Client's point | Our answer | First action |
|---|---|---|---|
| 1 | translationalhealthscience.in ranks well and gets good traffic; use it for admissions and ads | **Yes.** The data shows it is growing fast. Keep every page that earns clicks, and fix the risks | P0 fixes this week; protect the ranking pages |
| 2 | Four campuses: ITHS at RBU, and the Department of Clinical Embryology by ITHS at RBPU Hoshiarpur, BU Shimla and SGSU Bhopal | **Yes, with one naming pattern**, and with the old site serving **all four** campuses. Three of the four campus pages can't be found in search, so each needs local work | Confirm programmes per campus and the names (D3) |
| 3 | ithsedu.in is the new website, and the future university site | **Yes.** An official institute site for achievements and announcements that never copies admission pages. Built so it can absorb the old site later | Wireframes and copy in December; launch 9 Feb 2027 |
| 4 | Social media: old accounts for ITHS at RBU, new accounts for the other campuses and for ithsedu; daily posts on campus accounts, important ones on ithsedu | **Yes to the split.** We recommend one change: the old accounts become the official @ithsedu (they hold all the followers), and RBU gets a new account | Decision D1; reserve handles |
| 5 | Will this cause duplication? | **No**, if every topic has one home. The duplication found today comes from site copies and leftovers, not from the two-domain plan | Remove the copies (C1–C4) |
| 6 | How should we proceed? | Week-by-week roadmap below: data and fixes in December, ithsedu.in in January–February, campaign ready by 1 March, peak May–August | Decisions D1–D4 and D13 by 11 December |

---

## Issue 1: the old domain ranks well, so use it for admissions and ads

### What the data says

| Measure | Result |
|---|---|
| Search clicks, 16 months | 7,196 (URL-prefix property, 26 Jul 2025 – 25 Nov 2026) |
| Year on year (Aug–Nov) | **+91%** (1,797 vs 941 clicks) |
| Best month | July 2026, 807 clicks |
| Share of visits and leads | Organic search 44% of GA4 sessions, 46% of key events |
| Paid search (May–Aug 2026 only) | 17.7% key-event rate; the ads page `/art-and-clinical-embryology-program/` is the top lead page (339 key events) |
| AI assistants | 195 visits, 23.6% key-event rate, the best of any channel |
| Mobile | 76% of clicks |

The client is right: this domain is the admissions asset. The plan keeps it and makes it safer and stronger.

### Plan

1. **Protect.** Keep every URL with clicks: the homepage, the embryologist post, the colleges guide, Bhopal, PhD, the ART guide, the nutrition guide, the cancer pages, the stem cell pages, MSc Neuroscience and the ads page. No slug changes; any move needs a 301 approved by Jakhar Singh.
2. **Fix the P0 risks this week:**
   - the bank account on the admission form (A1);
   - the staging link (A2);
   - the public build note (A3);
   - the wrong NAAC badge (A4);
   - the indexed certificate PDFs with participants' names, and the broken QR verification (C1).
3. **Correct the claims** before any 2027 ad runs: placement percentages, "first" and "only" claims, "15+ patents" (A5–A7).
4. **Consolidate.** Merge six low-value posts into their programme pages (content first, then 301):
   - two nutrigenetics posts (127 + 41 clicks in 16 months);
   - two B.Tech posts (71 + 21);
   - `exploring-the-possibilities…` (48);
   - `transform-your-career…` (29).
5. **Win the near misses.** Rewrite titles and meta descriptions where impressions are high and clicks are low:
   - "embryologist" (6,640 impressions, position 7.5);
   - "bsc embryology" (5,107 impressions, position 11.3; target the BSc page);
   - "stem cell and regenerative medicine course in india" (position 4.6, 0 clicks);
   - "bsc oncology" (target the cancer BSc page).
6. **Link the level pages.** Add BSc, MSc, PhD and PG Diploma under each programme in the Courses menu (the PhD page has only 2 internal links; MSc Embryology isn't indexed).
7. **Refresh the season pages before April 2027.** The embryologist post and the ART guide rank at positions 1.7–2.6 for "after 12th" searches.
8. **Ads.** Use the same ads page, which converted best in 2026. Start brand and PG/PhD search in February, then peak May–August. Ads target 18+ and parents only. Fix GA4 first: retention to 14 months, de-duplicate Form Submit, campus-tagged events.
9. **Tidy the index:**
   - `noindex` the thank-you pages, form pages, categories, date archives and author archives;
   - replace the 2024 brochure PDF at the same URL (84 clicks);
   - fix the `Admission.iths@gmail.com` link bug.

## Issue 2: the four campuses and their names

### What the data says (16 months, URL-prefix)

| Campus | Campus page clicks | Location searches | Leads (GA4 landing, 12 months) | Status |
|---|---|---|---|---|
| SGSU Bhopal | **249** | Mostly SGSU and hidden queries | **194 key events** | The only campus page that performs |
| RBU Mohali | 50 | Ranks at **position 30.6** for "chandigarh"; "rbu mohali" 0 clicks | 62 | Brand searches go to the homepage; the campus page is invisible for location searches |
| BU Shimla | 46 (0 since April 2026) | Lost "bahra university" (position 4.2) when the old page was redirected | 9 | Visibility lost in the 2026 restructure |
| RBPU Hoshiarpur | 10 | "rbpu hoshiarpur" position 7.4, 0 clicks | 1 | Never visible |

### Plan

1. **One website for all four campuses: translationalhealthscience.in.** The client's note links the old site to "ITHS at RBU". We recommend it keeps serving all four campuses, because:
   - Bhopal's best-performing page lives there;
   - moving campuses out would split rankings across sites.
2. **One naming pattern everywhere** (website, Google Business Profile, social, ads), confirmed by D3 after the programme table per campus is checked:

| Campus | Name on the website and Google | Social display name (client's wording) |
|---|---|---|
| RBU | ITHS at Rayat Bahra University, Mohali (near Chandigarh) | ITHS at RBU |
| RBPU | ITHS at Rayat Bahra Professional University, Hoshiarpur | Department of Clinical Embryology by ITHS at RBPU, Hoshiarpur |
| BU | ITHS at Bahra University, Shimla Hills (Waknaghat, Solan) | Department of Clinical Embryology by ITHS at BU, Shimla. If Stem Cell also runs there (the site says it does), use "ITHS at BU, Shimla" |
| SGSU | ITHS at SCOPE Global Skills University (SGSU), Bhopal | Department of Clinical Embryology by ITHS at SGSU, Bhopal |

   - The university's full name and the city go first in page titles, because that is what people search ("sgsu bhopal", "bahra university shimla", "rbu mohali", "rbpu hoshiarpur").
   - The department wording goes in the H1 subtitle and the social bios.
   - Google Business Profile names must match the signage at the campus.
3. **Local work for RBU, Shimla and Hoshiarpur** (Bhopal gets the same, lighter):
   - title and H1 as above;
   - full address with PIN (the RBU PIN conflict, 140104 vs 140302, to be settled);
   - campus phone and WhatsApp, map, travel and hostel information;
   - real photos;
   - programmes with the degree-awarding university named;
   - a fee table (D8);
   - an FAQ (NEET, eligibility, hostel, scholarship).
   - **Google Business Profiles:** one per campus where ITHS has its own signage. Find out who manages the "Kurali" listing that drives most brand clicks.
   - **University links:** ask each university to link its programme page to the matching campus page.
   - **Shimla:** give the campus page the "Bahra University Shimla" wording the old apply-now page ranked for.
   - **Punjab guide (December):** "Clinical embryology course in Punjab: Mohali and Hoshiarpur".
4. **One fact sheet** (master plan §5.3) settles campus count, founding year, distances, programmes per campus, phones and the RBU locality (Chandigarh, Mohali, Kharar, Sahauran and Kurali are all in use today).

## Issue 3: ithsedu.in as the new site and the future university site

### Plan

1. **Role:** the official institute website, covering:
   - About, Leadership, Faculty and Partners (the four universities);
   - Research (patent applications with numbers, publications);
   - Achievements, News & Events, Media kit, Careers, Contact and Policies.
2. **No copies.** ithsedu.in never repeats programme, campus, fee or admission content. Its "Programmes & Admissions" button goes to translationalhealthscience.in.
3. **Brand searches will move.** Today the old homepage takes the brand searches ("iths", "institute of translational health science…", 904 clicks in 16 months), and they bring leads. Once ithsedu.in is live, Google will likely show it first for "ITHS". So:
   - ithsedu.in's home page carries an **"Admissions 2027–28" band above the fold**;
   - our protection KPI counts non-brand clicks and total leads, not brand clicks.
4. **Moves at launch:** `/careers/` (keeping its JobPosting markup) and `/news-events/` (0 clicks in 16 months) move to ithsedu.in with 301s. From launch, all institutional news goes to ithsedu.in only.
5. **Staging:** demo.ithsedu.in is public. Password-protect it, and remove "Top Private Institute in India" from its title (guardrail 1).
6. **Built for the future university:**
   - ithsedu.in reuses the old site's paths for shared pages (`/about/`, `/contact-us/`, `/careers/`);
   - it never uses `/programs/`, `/campuses/`, `/admission/`, `/apply-now/`, `/iths-set/` or `/blog/`;
   - if ITHS becomes a university, the admissions pages then move across one-to-one with 301s, outside the admission season (master plan §14);
   - until that status is official, neither site calls ITHS a university.
7. **Timeline:** wireframes and copy by 20 December → staging approved by 31 January → **launch Tuesday 9 February 2027** (to be confirmed).

## Issue 4: social media

### What the data says

- Organic social brought 366 sessions and 19 key events in 12 months.
- Paid social brought 411 sessions and 82 key events.
- Social builds trust and reach; search and ads bring the leads.
- So the follower base matters more for credibility than for direct leads.

### Plan

| Account set | Platforms | Posts | Content |
|---|---|---|---|
| **@ithsedu** (official) | Instagram, Facebook, LinkedIn company page, YouTube (one channel), X | Instagram 3–4 a week; LinkedIn 1–2 a week | Achievements, announcements, collaborations, research, results, the session launch, ITHS-SET |
| **ITHS at RBU** (`@iths.rbu`) | Instagram, Facebook, LinkedIn showcase page | 5–7 a week plus stories | Daily campus life, labs, visits, events, admission reminders in season |
| **RBPU, BU, SGSU** (`@iths.rbpu`, `@iths.bushimla`, `@iths.sgsu`) | Instagram, Facebook, LinkedIn showcase pages | 4–6 a week | The same, per campus |

1. **Decision D1 (our recommendation):** rename the existing accounts (Instagram @translationalhealthscience, Facebook /TranslationalHealthScience, X @ITHScience) to the official **@ithsedu** and keep all followers. Create **@iths.rbu** new.
   - The client's version (old accounts become RBU) is workable, but the official account would then start from zero.
   - Followers from Shimla, Hoshiarpur and Bhopal would stay on an RBU account.
2. **YouTube:** keep **one** channel. Search Console shows a channel **@InstituteofTranslationalHealth**, while the website links to **@TranslationalHealthScience**. Confirm which is real, merge to one, and put campus videos in playlists.
3. **No duplication on social:**
   - Use **Instagram Collab posts** (one post on both the campus account and @ithsedu) instead of reposting.
   - Use LinkedIn showcase pages under one ITHS company page.
   - Put UTM tags on every bio and post link. Today much of this traffic lands in GA4's "Direct" channel (36% of sessions).
4. **Rules:**
   - no claims without evidence;
   - the awarding university named on admission posts;
   - written consent for student photos (parental consent under 18);
   - no AI-made students or faculty;
   - stem cell content is academic only.
5. **Setup:** reserve all handles by 6 December; playbook, Canva templates and the January calendar by 22 December; one coordinator per campus and one central lead for @ithsedu.

## Issue 5: will this cause duplication?

**The two-domain plan does not cause duplication if every topic has one home.** The rules are in master plan §1:
- admission content lives only on the old site;
- institute content and news live only on ithsedu.in;
- both sites point to one organisation in structured data;
- campaign copies are `noindex`.

**The duplication that exists today** comes from copies and leftovers. Fix these now:

| Problem found | Action |
|---|---|
| iths.rbuchd.in: an indexable ITHS "Apply Now in Bahra University" page | Find the owner; `noindex` it or 301 it to `/campuses/shimla/` |
| demo.ithsedu.in: public staging | Password-protect it |
| iths.technotaau.com: linked from the live Mohali page | Fix the link; password-protect it |
| bu. and rbu.translationalhealthscience.in: old subdomains with errors and duplicate URLs | Remove the DNS records or 301 them to the campus pages |
| Overlapping posts (nutrigenetics, B.Tech, embryology) | The six merges in Issue 1 |
| Two ads pages with copy similar to the programme pages | Already `noindex`; keep them out of the sitemap |
| **embryogenesis.34gaon.com**: a full indexable copy of the EmbryoGenesis site (sister project) | Take it down or `noindex` it (EmbryoGenesis team) |

## Issue 6: how to proceed

### Roadmap

| When | ITHS team (client) | Developer | TechnoTaau Team |
|---|---|---|---|
| **Week of 30 Nov** | Confirm the bank account, staging owners, the Kurali profile and the YouTube channel; reserve handles | P0 fixes A1–A4, C1–C3; GA4 retention, Form Submit de-duplication, internal-traffic filter | Claims rewrite text (A5–A7); titles and meta for the 6 high-impression pages |
| **Week of 7 Dec** | Decisions D1–D4, D13; fact sheet; programme table per campus; 2025–27 lead and admission numbers | Thank-you, form and archive `noindex`; sitemap clean-up; `mailto` fix; 404 redirects | KPI targets; ithsedu.in sitemap sign-off; Punjab guide |
| **14 – 31 Dec** | Approve claims and copy; counsel review (collaboration wording, admission form data) | Level-page links in the menu; campus-page templates | ithsedu.in wireframes and copy (Home, About, Leadership, Partners); campus-page copy for RBU, Shimla, Hoshiarpur; social playbook and templates |
| **January 2027** | Google Business Profiles; university link requests; real photos | ithsedu.in build on staging; post merges with 301s | Remaining ithsedu.in copy; merge content; UGC-check and after-12th guides; social accounts live |
| **1 – 9 Feb 2027** | Approve staging | Launch ithsedu.in; 301 `/careers/` and `/news-events/`; cross-domain GA4 | Launch checklist; brand-search monitoring |
| **By 1 Mar 2027** | 2027–28 dates, fees and ITHS-SET details | 2027–28 updates; evergreen admission-form URL | Season posts refreshed; ITHS-SET page; ads plan with budget |
| **Apr – Aug 2027** | Lead handling within 24 hours; campus posting | Support | Ads peak May–Aug; weekly lead review; monthly SEO, social and AI-answer report |
| **Sep – Nov 2027** | Season review | – | Next-year plan; university-path review |

### Decisions needed by 11 December 2026

| # | Decision | Our recommendation |
|---|---|---|
| D1 | Old social accounts: official @ithsedu, or ITHS at RBU | Official @ithsedu |
| D2 | Old website: all four campuses, or RBU only | All four |
| D3 | Names and programmes per campus | The table in Issue 2 |
| D4 | RBU locality wording | "Mohali (near Chandigarh)" |
| D13 | Is anthropology still offered? (The 2025 post had 206 clicks; "bsc anthropology" gets 4,179 impressions) | If yes, restore a programme page; if no, 410 |

Also needed: the fact sheet, lead and admission numbers per campus (D7), the ads budget, and who builds ithsedu.in (D9). The other decisions (D5–D12) are in master plan §12.

### How we will measure it

- Non-brand clicks no more than 10% below the same month last year (current trend +91%).
- Leads per campus at or above the 2026 season, at a known cost per admission.
- ithsedu.in and the old site both in the top 3 for "ITHS" within 3 months of launch.
- Shimla, Hoshiarpur and Mohali campus pages ranking in the top 10 for their university and city searches before July 2027.
- ITHS named correctly in the monthly AI-answer check.
- Zero unsupported claims in the monthly compliance check.

*Prepared by TechnoTaau Team. Sign-off: Jakhar Singh.*
