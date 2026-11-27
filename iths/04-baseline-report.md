# ITHS: Search and Analytics Baseline (translationalhealthscience.in)

**Prepared by:** TechnoTaau Team (lead: Jakhar Singh)
**Date:** 27 November 2026 | **Version:** 1.1 (all uploaded files reviewed, including the 16-month all-pages export from the URL-prefix property; 5 GA4 reports, 7 top-page Performance exports, 8 not-indexed drilldowns, the indexed-pages list, Core Web Vitals, and 4 link reports; §8 lists the files still missing)
**Sources:** Claude in Chrome read-only exports of Search Console (Domain property `translationalhealthscience.in` and URL-prefix property `https://www.translationalhealthscience.in/`; each file identified by its contents in `iths/data/file-inventory.md`) and GA4 (property ITHS, 443162610) on 27 Nov 2026; GA4 CSV files 40, 41, 42, 43 and 45 in `iths/data/raw/`; our `curl` checks of live URLs on 27 Nov 2026.
**Data range:** the Domain property has data only from **29 April 2026**. The **URL-prefix property** (`https://www.translationalhealthscience.in/`) has data from **26 July 2025**, so year-on-year comparison is possible there (§2.0). GA4 covers 27 Nov 2025 to 26 Nov 2026.

---

## 1. Headline findings

1. **Search clicks nearly doubled year on year** (+91% for Aug–Nov, URL-prefix property, §2.0). **Organic search is the main source of visits and leads.** It brings 44% of GA4 sessions (5,366 of 12,196) and 46% of key events (665 of 1,448) over 12 months. Search Console (URL-prefix property) shows 7,196 clicks in 16 months (26 Jul 2025 – 25 Nov 2026).
2. **Paid search ran only in the 2026 season and converted best among large channels.** 985 of its 992 yearly sessions came between 1 May and 31 August, with a 17.7% key-event rate. Its landing page `/art-and-clinical-embryology-program/` (correctly `noindex`) is the **top lead page on the site**: 1,085 sessions and 339 key events.
3. **AI assistants already send leads.** 195 sessions (mostly ChatGPT) with a 23.6% key-event rate, the highest of any channel. GEO work (master plan §6.8) moves up in priority.
4. **The brand is searched, and the homepage takes those searches.** Brand queries got 904 clicks in 16 months (URL-prefix). The top query is "institute of translational health science (iths) kurali" (162 clicks in 3 months, position 1), which looks like the name of a Google Business Profile. The homepage gets 398 clicks in 3 months and 278 GA4 key events in 12 months.
5. **Guides and programme pages bring the non-brand traffic**, and they mostly answer different questions. "Want to become an embryologist" (220 clicks, 25,221 impressions in 3 months) and "BSc embryology colleges in India" (168 clicks) are the strongest non-brand pages.
6. **Bhopal leads the campuses; Shimla and Hoshiarpur barely appear in search.** `/campuses/bhopal/`: 110 clicks in 3 months, 471 sessions and 194 key events in 12 months. `/campuses/shimla/`: 0 clicks from 335 impressions. `/campuses/hoshiarpur/`: 0 clicks from 42 impressions.
7. **Measurement has gaps that will distort the 2027 season** unless they are fixed now:
   - GA4 keeps event data for only **2 months**.
   - "Form Submit" fires about twice per user (814 events from 438 users).
   - Phone and WhatsApp clicks are tracked as key events only for RBU.
   - Developer and test traffic (localhost, Tag Assistant) is mixed in with real visits.
8. **There are more copies and leftovers of the site than we knew of:**
   - **iths.rbuchd.in** serves an ITHS "Apply Now in Bahra University" page with no `noindex` and no canonical tag.
   - **demo.ithsedu.in** (the new site's staging) is `noindex` but publicly open, and its title says "Top Private Institute in India".
   - The bu. and rbu. subdomains still exist in Search Console, and Google cannot fetch their robots.txt.
   - Several old URLs that still get visits return 404.

## 2. Search Console

### 2.0 Year on year (URL-prefix property, last 3 months vs the same period in 2025)

| | 26 Aug – 25 Nov 2026 | Same period 2025 | Change |
|---|---|---|---|
| Clicks (pages report) | 1,797 | 941 | **+91%** |
| Impressions | 125,448 | 95,780 | +31% |
| Clicks from visible queries | 624 | 210 | +197% |

Gains came from:
- the homepage (398 vs 173 clicks; position 4.7 vs 6.3);
- the embryologist post (220 vs 109; position 6.1 vs 9.1);
- the cancer scientist post (75 vs 37; position 5.7 vs 12.7);
- the ART guide (83 vs 7);
- pages that did not exist a year ago: the colleges guide (168), Bhopal (110), PhD (90), stem cell (65), MSc Neuroscience (58), the cancer programme pages (103).

Losses are mostly old URLs that now redirect (the 2025 site structure):
- `/ba-bsc-and-ma-msc-anthropology-admission-2025/` (101 → 0);
- `/rayat-bahra-university/bsc-in-cancer-biology/` (89 → 0);
- the genetic counselling, stem cell and anthropology URLs under `/rayat-bahra-university/`;
- `/apply-now-in-bahra-university/`;
- the "leading" nutrigenetics post (35 → 4).

**Monthly clicks, all pages (URL-prefix, 16 months; 7,331 clicks, 708,107 impressions in total):**

| Month | 2025 | 2026 | Change |
|---|---|---|---|
| August | 354 | 662 | +87% |
| September | 359 | 593 | +65% |
| October | 261 | 509 | +95% |
| November | 294 | 547 (to the 25th) | about +100% |

2026 season: May 519, June 582, **July 807 (the peak)**, August 662. No 2025 season data exists, because the property starts on 26 July 2025.

**The 2026 restructure worked.** The site nearly doubled its search clicks year on year.

**Brand trend (URL-prefix, brand regex):** 904 clicks and 6,376 impressions since July 2025. Monthly clicks rose from 15–42 in late 2025 to 58–101 in the 2026 season, and **222 in November 2026 so far** (a jump, mostly the "…(iths) kurali" query, so probably the Google Business Profile). Top brand queries:
- "iths": 439 clicks, position 3.5;
- "institute of translational health sciences": 186;
- "institute of translational health science (iths) kurali": 162;
- "…kurali reviews": 147 impressions, which shows people look for reviews.


### 2.0a 16-month trends by topic (URL-prefix property, July 2025 – November 2026)

| Segment | Clicks (visible queries) | Monthly clicks, late 2025 | Monthly clicks, 2026 | Reading |
|---|---|---|---|---|
| Non-brand (all) | 1,084 | 29–53 | 83–128 (May–Oct) | Non-brand demand grew about 2.5 times after the 2026 restructure |
| Embryology | 368 | 3–18 | 37–56 (Jul–Oct) | The strongest topic. The embryologist post takes 240 of 370 page clicks. "bsc embryology" (5,107 impressions, position 11.3) and "embryologist" (6,640, position 7.5) are the biggest gaps |
| Cancer | 202 | 5–11 | 14–36 (Apr–Aug) | Seasonal. The old `/rayat-bahra-university/bsc-in-cancer-biology/` (56 clicks) now 301s to the BSc page, so its value carried over. "bsc cancer biology" and "bsc in cancer biology" rank at position 3.6–3.9 |
| Nutrigenetics and nutrition | 110 | 0–8 | 2–15 | The dietetics salary guide takes 70 clicks. The "India's leading" nutrigenetics post (23 clicks) out-earned the programme page (17, position 14.8): **merge the post into the programme page with a 301**, and rewrite the page for "nutrigenetics course" and "nutrigenomics course in India" |
| Shimla and Bahra University | 25 | 1–7 | **0 since April 2026** | `/apply-now-in-bahra-university/` ranked at position 4.2 for "bahra university" (10,202 impressions, 7 clicks) until it was 301'd to `/campuses/shimla/`. The campus page has not taken over: Shimla visibility was lost in the restructure. Mostly navigational searches for the university itself, so few clicks are at stake, but "bahra university shimla" (787 impressions) and "bu shimla" (157) are winnable with a stronger campus page |

| Hoshiarpur and RBPU | **0** (48 impressions in 16 months) | 0 | 0 | Never visible. Searches are mostly "rbpu hoshiarpur" (36 impressions, position 7.4). The campus needs a Google Business Profile, an RBPU link and a fuller page before it can show in search. An old URL `/rayat-bahra-professional-university-hoshiarpur/` also appears; check that it 301s to the campus page |
| After 12th and NEET | 140 | 0–6 | 5–26 (strong May–Sep) | Ranks at positions 1.7–2.6: "ivf courses after 12th" 56 clicks, "how to become an embryologist after 12th" 29. Two posts carry it (embryologist post 74, ART guide 47). **Refresh both before April 2027**; they are season engines |
| Fees, scholarship, admission | 9 | 0 | 0–3 | "embryology course fees" (99 impressions, position 11), "ivf course fees", "bsc embryology course fees": there is demand, but the site has no fee page. Supports D8 (publish fees) |

The homepage drew 232 clicks in November to the 25th, against 91 in September and 65 in October. 152 of them came from "…(iths) kurali", which confirms a new or more prominent Google Business Profile in November.

Other demand seen in non-brand queries:
- "bsc anthropology": 4,179 impressions. Is anthropology still offered? (audit B7).
- "india first undergraduate engineering biology": 2,850 impressions, the B.Tech.
- "embryologist course": 3,154 impressions at position 3.6.

### 2.1 Totals (Web search)

**Two Search Console properties are in play.** File names alone don't say which property each file came from, so each file was identified by its contents (`iths/data/file-inventory.md`):
- the **URL-prefix property** `https://www.translationalhealthscience.in/` has data from **26 July 2025**, and all the uploaded Performance totals come from it;
- the **Domain property** `translationalhealthscience.in` has data only from **29 April 2026**, and the Chrome summary's 16-month figures come from it.

For www pages, the two agree exactly over the same dates. **This report uses the URL-prefix figures as the baseline.** The Domain figures are shown for reference only.

| Period | Clicks | Impressions | CTR | Avg position | Source |
|---|---|---|---|---|---|
| Last 16 months (26 Jul 2025 – 25 Nov 2026) | **7,196** (by page: 7,331) | 708,107 (by page) | – | – | URL-prefix file (no number) |
| Last 3 months (26 Aug – 25 Nov 2026) | 1,759 | 107,465 | 1.64% | 6.4 | URL-prefix `_1`; the Domain property gives the same figures |
| Season 2026 (1 May – 31 Aug) | 2,570 (by page: 2,628) | 212,706 (by page) | – | – | URL-prefix `_3`. The Domain property gave 2,583 / 187,764 in the Chrome summary |
| Since 29 Apr 2026 (Domain, reference only) | 4,271 | 291,324 | 1.47% | 6.6 | Chrome summary |

"By page" totals are a little higher than property totals because Search Console counts a click on each page that appears for a search.

The season produced 60% of all clicks in under 60% of the days. Interest peaks with results and counselling, as the plan assumed.

### 2.2 Brand and non-brand

| Segment | URL-prefix, 16 months (baseline) | Domain, since 29 Apr 2026 (reference) |
|---|---|---|
| Brand (iths, translational, ithsset, ithsedu) | **904 clicks**, 6,376 impressions (`_4`) | 609 clicks, 2,831 impressions, CTR 21.5%, position 3.9 |
| Non-brand (visible queries) | **1,084 clicks**, 148,046 impressions (`_5`) | 706 clicks, 81,487 impressions, CTR 0.87%, position 8.3 |
| Anonymised queries (Google hides them) | about 5,200 clicks (7,196 − 904 − 1,084) | about 2,956 |

About 70% of clicks come from queries Google does not show, so query-level conclusions rest on the visible 30%. Page-level data (§2.4, §4.2) is complete.

### 2.3 Top queries (last 3 months)

| Query | Clicks | Impressions | Position | Reading |
|---|---|---|---|---|
| institute of translational health science (iths) kurali | 162 | 342 | 1.0 | Brand plus "Kurali": probably a Google Business Profile name. A fifth place label (Chandigarh, Mohali, Kharar, Sahauran, Kurali) |
| iths | 99 | 573 | 3.2 | Brand; ithsedu.in will compete for this after launch (§4) |
| institute of translational health sciences | 33 | 95 | 2.0 | Brand |
| msc neuroscience india | 20 | 111 | 8.3 | `/msc-neuroscience/` (58 clicks): protect |
| phd in clinical embryology | 14 | 312 | 6.9 | PhD page (90 clicks): protect |
| ivf courses after 12th | 13 | 304 | 1.2 | Guides |
| bsc embryology colleges | 12 | 503 | 2.5 | Colleges guide |
| embryology course after 12 | 12 | 240 | 1.8 | Guides |
| how to become an embryologist after 12th | 12 | 208 | 1.8 | Embryologist post |
| iths chandigarh | 11 | 41 | 1.3 | Brand plus Chandigarh: supports "near Chandigarh" in copy (D4) |
| embryologist | 7 | **5,531** | 8.2 | Large opportunity: page 1, bottom half |
| bsc oncology / bsc cancer biology / bsc in cancer biology | 12 | 721 | 4.3–5.1 | Cancer programme pages |
| nutrigenomics course | 5 | 128 | 18.8 | Weak; nutrigenetics pages rank on page 2 |
| regenerative medicine courses in india | 4 | 157 | 18.6 | Weak; stem cell page on page 2 |
| how to become ivf doctor after 12th without neet | 4 | 142 | 1.6 | Guides; wording needs care ("IVF doctor" needs MBBS) |

### 2.4 Top pages (last 3 months) and their status

| Page | Clicks | Impressions | Position | Status in the plan |
|---|---|---|---|---|
| / | 398 | 3,622 | 4.6 | Protected |
| /want-to-become-an-embryologist-admissions-open… | 220 | 25,221 | 6.1 | **Protected** (was a merge candidate in plan v1.0; now kept) |
| /bsc-embryology-colleges-in-india-clinical-embryology-course-guide/ | 168 | 14,516 | 5.4 | Protected |
| /campuses/bhopal/ | 110 | 2,046 | 3.6 | Protected |
| /programs/clinical-embryology/phd/ | 90 | 3,426 | 5.1 | Protected |
| /assisted-reproductive-technology-course-in-india-complete-guide-2026/ | 83 | 6,473 | 4.7 | Protected |
| /food-nutrition-and-dietetics-complete-career-guide/ | 76 | 16,135 | 7.2 | Protected |
| /want-to-become-a-cancer-research-scientist… | 75 | 7,883 | 5.7 | Protected |
| /programs/stem-cell-regenerative-medicine/ | 65 | 2,561 | 7.7 | Protected |
| /msc-neuroscience/ | 58 | 3,285 | 6.8 | Protected (stays outside `/programs/`) |
| /bsc-clinical-embryology-scope-career-jobs-eligibility-india/ | 53 | 6,904 | 5.5 | Protected |
| /programs/cancer-biology/ | 53 | 3,883 | 5.5 | Protected |
| /programs/cancer-biology/bsc/ | 50 | 2,692 | 4.5 | Protected |
| /programs/clinical-embryology/bsc/ | 31 | 3,590 | 6.0 | Protected |
| /admission/ | 23 | 1,350 | 2.8 | Protected |
| /programs/nutrigenetics-personalized-nutrition/ | 22 | 838 | 10.4 | Protected; improve |
| /programs/stem-cell-regenerative-medicine/bsc/ | 16 | 680 | 8.6 | Protected |
| /programs/clinical-embryology/ | 15 | 1,455 | 9.6 | Protected; improve |
| /campuses/ | 15 | 1,340 | 4.1 | Protected |
| /bsc-cancer-biology-colleges-in-india-course-guide-iths/ | 14 | 1,507 | 7.0 | Protected |

### 2.5 Clusters: is there real cannibalisation?

Flag ⚑ = two or more pages each with more than 10% of a cluster's clicks.

Source: URL-prefix, 16 months, for every row. The stem cell, Bhopal, Chandigarh and Mohali rows come from the later re-exports, which use a simple "query contains" filter rather than the prompt's regex, so they are narrower than the other rows.

| Cluster | Clicks | Pages sharing clicks | Verdict |
|---|---|---|---|
| Embryology ⚑ (URL-prefix) | 368 | Embryologist post 65%, colleges guide 13%, PhD page 11% | **Healthy.** Each answers a different question (become one / which college / PhD). Keep all three; link them to each other and to the BSc and MSc pages |
| Nutrigenetics ⚑ (URL-prefix) | 110 | Nutrition and dietetics guide 64%, "India's leading" post 21%, programme 15% | The programme ranks at position 14.8. Merge the "leading" post and the 2025 admission post into it (§4.2) |
| Stem cell (URL-prefix, contains "stem cell") | 28 | Programme 32%, BSc 29%, old RBU URL 21% (redirected) | Small. "stem cell and regenerative medicine course in india" gets 236 impressions at position 4.6 and **0 clicks**: rewrite the programme title and meta. "bsc molecular medicine stem cell subjects per semester" (214 impressions) shows demand for a semester-wise syllabus. Merge the two older B.Tech posts into the B.Tech page (§4.2). Answer "stem cell therapy courses" searches as academic courses only (guardrail 11) |
| Cancer ⚑ (URL-prefix) | 202 | Old RBU URL 28% (now 301 to the BSc page), programme 25%, BSc 25%, scientist post 21% | Healthy. Watch "bsc cancer biology", where the programme and BSc pages may swap; make the BSc page the target for "bsc" queries |
| After 12th ⚑ (URL-prefix) | 140 | Embryologist post 52%, ART guide 33% | Healthy. Different angles (embryologist vs ART course) |
| Shimla (URL-prefix) | 25 (0 since April 2026) | Old `/apply-now-in-bahra-university/` page | **Visibility lost in the restructure** (§2.0a) |
| Hoshiarpur (URL-prefix) | 0 | – | **Never ranked** |
| Bhopal (URL-prefix, contains "bhopal") | 5 | Campus page 100% | The campus page's 249 clicks come mostly from hidden or SGSU searches ("sgsu college bhopal" position 9.2, "sgsu bhopal" 7.0), not from "bhopal" searches. Put "SCOPE Global Skills University (SGSU), Bhopal" in the title and H1 (§2.10) |
| Chandigarh and Mohali (URL-prefix, "chandigarh" plus "mohali") | 12 + 1 | Homepage 92% ("iths chandigarh" 11) | **The RBU campus page is invisible for location searches.** `/campuses/mohali/` ranks at **position 30.6** for "chandigarh" searches and gets no Mohali clicks ("rbu mohali" 40 impressions). Only brand searches reach the homepage. The main campus needs the same local work as Shimla and Hoshiarpur: a title with "Rayat Bahra University, Mohali (near Chandigarh)", full address and PIN, a Google Business Profile check (the "Kurali" listing) and an RBU link. The Punjab guide (December) supports this |
| Admission/fees (URL-prefix) | 9 | – | Too small to judge. People search fees ("ivf course fees", "embryology course fees"); supports publishing fees (D8) |

**Conclusion:** the overlaps are mostly healthy. Merge only posts with almost no clicks (§5, item 3). Keep every page listed in §2.4.

### 2.6 Indexing (Search Console, updated 23 Nov 2026)

123 indexed, 109 not indexed.

| Reason | Pages | Action |
|---|---|---|
| Page with redirect | 29 | Expected: old `/rayat-bahra-university/…`, `/bahra-university/…`, `/courses/` and profile URLs 301 correctly (we checked five) |
| Not found (404) | 17 (12 on the www property, down from 16 in September) | 301 those that still get visits (§3.4) to the closest page; leave the rest. **Template bug:** five 404s end in `/Admission.iths@gmail.com` (for example `/category/higher-education-admissions/feed/Admission.iths@gmail.com`). A link somewhere uses the email address as a relative `href` without `mailto:`. Fix the link to `mailto:admission.iths@gmail.com` |
| Duplicate without user-selected canonical | 8 | Check the list when the files arrive |
| Alternate page with proper canonical | 6 | Expected |
| Excluded by noindex | 2 | Includes `/art-and-clinical-embryology-program/`, the ads page. Correct |
| Blocked due to other 4xx | 1 | Check |
| **Crawled, currently not indexed** | 39 | Includes **`/programs/clinical-embryology/msc/`**, a main programme page. Add unique MSc content (curriculum, eligibility, research project, campuses) so it differs from the BSc page, link to it from the embryology hub and the PhD page, then request indexing |
| Discovered, currently not indexed | 7 | Check the list |

### 2.7 Technical health

| Item | Status | Action |
|---|---|---|
| Sitemaps | Index plus post and page sitemaps read on 20–22 Nov; 97 URLs | Remove thank-you pages; add `noindex` to form pages (audit B2–B3) |
| Core Web Vitals (mobile) | 53 good, 0 poor | Keep |
| HTTPS | 58 HTTPS, 0 issues | Keep |
| Crawl response time | **1.63 s average** (slow) | Hosting or caching review; target under 600 ms server response |
| Crawl responses | 200: 89%, 301: 5%, 304: 4%, 404: 2%, no 5xx | Fine |
| robots.txt | Fails on `bu.` and `rbu.` subdomains ("4 critical errors") | Remove the subdomains' DNS records, or redirect each host to the main site with a working robots.txt |
| Structured data | Breadcrumbs 12 valid; **Events 0 valid** (missing url, offers, image, description); Job Postings 4 valid with warnings | Fix the Event markup or remove it; complete JobPosting fields (and move them to ithsedu.in with the careers page) |
| Manual actions and security | None | – |
| External links | 63 links; mostly embryogenesis.in (17) and nutrigenetics.in (17); rbuchd.in 3 | Very thin. University and press links (plan §6.6) are the main off-page task |

### 2.8 Indexed pages that should not be (from the indexed-pages list, 122 URLs)

| Group | Count | Action |
|---|---|---|
| Workshop certificates with participants' names (`ITHSINNRRBU2025104.pdf` … `130.pdf`) | 17 | **P0.** Send `X-Robots-Tag: noindex` for these PDFs (server or plugin rule) and use the Removals tool for quick removal. Rebuild `/certificate/` as a verification page: enter the certificate number to get name, event and date. Then the QR codes work again, and the PDFs need not be public. Check consent wording for future certificates (DPDP) |
| Category archives | 25 | `noindex, follow` for all categories except about 5 topic hubs that will get written introductions (Clinical Embryology, Nutrigenetics, Stem Cell, Cancer Biology, Campus Life) |
| Date archives (`/2025/04/24/` and 14 others) and author archives | 15 + 2 | `noindex` (Rank Math: disable date archives; noindex author archives) |
| Thank-you pages | 3 (`/thank-you/` and the Shimla and nutrigenetics thank-you pages) | `noindex` (audit B2) |
| Old brochure `Brochure-of-translational-health-science-2024.pdf` and two prospectus PDFs (RBPU; MSc/BSc Clinical Embryology 2025) | 3 | Keep the current prospectuses; replace or remove the 2024 brochure if its facts or claims are out of date |

### 2.9 Internal links (Search Console "Top target pages")

- **Menu pages** (home, programme hubs, campuses, apply, about, admission, blog, contact): about 100 internal links each.
- **Under-linked money pages:**

| Page | Internal links |
|---|---|
| `/programs/clinical-embryology/phd/` | 2 (yet 90 organic clicks in 3 months) |
| `/programs/clinical-embryology/msc/` | not listed (0 or 1); "crawled, not indexed" |
| `/programs/clinical-embryology/bsc/` | 10 |
| `/programs/cancer-biology/bsc/` | 3 |
| `/programs/stem-cell-regenerative-medicine/bsc/`, `/msc/` | 1, 2 |
| `/programs/clinical-embryology/pgd-clinical-embryology/`, `/programs/cancer-biology/msc/`, `/programs/nutrigenetics-personalized-nutrition/bsc/` | not listed |

**Fix:**
- Add the level pages (BSc, MSc, PhD, PG Diploma) to the Courses menu under each programme.
- Add a "Choose your level" block on each programme hub.
- Link from every related guide to the right level page with descriptive anchors ("PhD in Clinical Embryology", "MSc Clinical Embryology eligibility").

### 2.10 What the top pages rank for (last 3 months, from the page exports)

| Page | Biggest queries (impressions, position) | Opportunity |
|---|---|---|
| BSc embryology colleges guide | bsc embryology (591, 9.8), bsc embryology colleges (498, 2.5), government colleges (310, 2.6), bsc in embryology (198, 10.1), b voc in embryology (179, 3.3) | "bsc embryology" belongs to the BSc programme page: give it that phrase in the title and H1 and link to it from the guide |
| Campus Bhopal | sgsu logo (66), sgsu college bhopal (43, 9.3), sgsu bhopal (30, 7.0), SGSU PIN code (18) | People search the university name: put "SCOPE Global Skills University (SGSU), Bhopal" in the title, and the full address with PIN on the page |
| PhD clinical embryology | phd in clinical embryology (292, 5.6), phd in embryology (183, 3.8), phd embryology (160, 17.7) | Already converts; add internal links (2.9) and an eligibility and admission-cycle section |
| ART course guide | ivf courses after 12th (304, 1.2), how to become ivf doctor after 12th without neet (124, 2.2), ivf technician course (76, 6.9) | State plainly that "IVF doctor" needs MBBS plus specialisation and that the course leads to embryologist or lab roles. This honest answer is what AI answers quote |
| Food, nutrition and dietetics guide | diet salary (227), bsc nutrition and dietetics salary (197), nutritionist salary in india (184) | Salary searches, 12 clicks: add a sourced salary table and a link to the nutrigenetics programme; low priority for admissions |
| Cancer research scientist post | bsc oncology (158, 8.8), bsc in oncology (140, 8.8), oncology courses after 12th (100, 7.5) | "bsc oncology" should go to the cancer biology BSc page; explain that cancer biology is the research route, not clinical oncology |
| Stem cell programme | regenerative medicine courses in india (119, 6.1), regenerative medicine courses (117, 6.9) | Strengthen the title and intro for "regenerative medicine course in India" |

Devices: 80–95% of clicks are on mobile for the guides (the PhD page is about half desktop). Country: India for almost all clicks.

**Whole site, 16 months (URL-prefix):**

| Measure | Result |
|---|---|
| Mobile | 5,498 clicks (76%), position 4.9 |
| Desktop | 1,524 clicks (21%), position 10.2 |
| Tablet | 174 clicks |
| India | 6,816 clicks (95%) |
| Next countries | UAE 48, US 26, Nepal 23, UK 21 |
| **"Translated results"** | **174 clicks, 14,879 impressions** |

"Translated results" are visits where Google translated the English page for a user searching in another language, most likely Hindi. This is a sign of Hindi-language demand. It is not a reason to change the English-only decision now, but Hindi summaries of key pages are worth revisiting after the season.

Desktop ranks about 5 positions lower than mobile, so check the desktop layout of the programme pages (heavy sliders, content lower on the page).

## 3. GA4

### 3.1 Channels (27 Nov 2025 – 26 Nov 2026; sum of channel rows)

| Channel | Sessions | Share | Key events | Key-event rate | Season 2026 sessions |
|---|---|---|---|---|---|
| Organic Search | 5,366 | 44.0% | 665 | 6.0% | 2,442 |
| Direct | 4,432 | 36.3% | 219 | 1.9% | 1,401 |
| Paid Search | 992 | 8.1% | 301 | 17.5% | 985 |
| Paid Social | 411 | 3.4% | 82 | 10.9% | 351 |
| Organic Social | 366 | 3.0% | 19 | 2.2% | 199 |
| Referral | 234 | 1.9% | 32 | 6.4% | 99 |
| AI Assistant | 195 | 1.6% | 97 | 23.6% | 131 |
| Unassigned | 141 | 1.2% | 7 | 1.4% | 47 |
| Cross-network | 57 | 0.5% | 26 | 17.5% | 57 |
| **Total** | **12,196** | | **1,448** | | **5,712** |

Readings:
- **Direct is large and low quality** (19.5% engagement). It probably includes untagged links from WhatsApp, Instagram bios and PDFs, plus some bots. UTM tags on every link we control (plan §7.3) will move this traffic into the right channels.
- **Organic social sends little** (366 sessions, 19 key events). The social plan's job is reach and trust; leads come through search, ads and AI.
- **Referrals include test traffic:** localhost:3000, 127.0.0.1:5500 and tagassistant.google.com. Exclude these with GA4's internal and developer traffic filters. Spam referrals (gipkd.com, x-find.pro, kaegtcr.online) are noise.

### 3.2 Landing pages by key events (12 months)

| Landing page | Sessions | Key events |
|---|---|---|
| /art-and-clinical-embryology-program (ads page, noindex) | 1,085 | 339 |
| / | 3,479 | 278 |
| /campuses/bhopal | 471 | 194 |
| /programs/clinical-embryology/phd | 198 | 65 |
| /campuses/mohali | 409 | 62 |
| /apply-now | 233 | 53 |
| /molecular-medicine | 20 | 45 (more key events than sessions: double-counting) |
| /programs/stem-cell-regenerative-medicine | 175 | 41 |
| /programs/clinical-embryology | 179 | 40 |
| ART course guide 2026 | 358 | 34 |
| Embryologist post | 794 | 30 |
| BSc embryology colleges guide | 220 | 30 |

Guides bring many visits but few leads (1–4%). Campus, programme and ads pages convert at 8–31%. Each guide needs a clearer next step: a campus-and-programme chooser and a short enquiry form.

### 3.3 Events and key events

| Event | Count | Users | Note |
|---|---|---|---|
| Form Submit | 814 | 438 | Key event. About 1.9 per user: probably fires on more than one trigger. Fix in GTM before counting leads |
| form_submit (GA4 automatic) | 3 | 3 | The enhanced-measurement version barely fires; keep one source of truth |
| form_start | 165 | 139 | – |
| RBU Chandigarh WhatsApp Click | 354 | 270 | Key event |
| Phone_Call_Click | 250 | 167 | Key event (generic) |
| RBU Chandigarh Phone Click | 220 | 148 | Key event |
| BU Shimla WhatsApp Click | 29 | 19 | Marked key event but shows no key-event data |
| file_download | 85 | 69 | Prospectus downloads; not a key event |
| purchase | – | – | Marked as key event with no data; remove |

**Lead events by campus are not comparable today.** Only RBU has phone and WhatsApp events of its own. Use one event set with a `campus` parameter instead: `generate_lead`, `tel_click`, `whatsapp_click` and `brochure_download`, each tagged rbu, rbpu, bu or sgsu.

### 3.4 Old URLs with visits that now return 404 (checked 27 Nov 2026)

| URL | GA4 sessions (12 months) | Suggested 301 target |
|---|---|---|
| /art-clinical-embryology-chandigarh/ | 50 | `/art-and-clinical-embryology-program/` if the ads page stays live; else `/programs/clinical-embryology/` |
| /document-library/ | 38 | Ask the client what it held; else `/` |
| /media/, /event-media/ | 14 each | `/campus-life/` (later ithsedu.in `/media/`) |
| /research-and-development/ | 6 | `/about/` now; ithsedu.in `/research/` after launch |
| /art-clinical-embryology-mohali/, /bsc-msc-clinical-embryology/, /iths-embryology-landing/ | 5, 4, 1 | `/programs/clinical-embryology/` (also check that no live ad points here) |
| /certificate/ | 4 | Ask the client |

Also: `/anthropology/` 301s to the B.Tech stem cell page, and the two anthropology posts 301 to the homepage. Both are the wrong targets (redirects to the homepage are treated as soft 404s), and the two posts are **still listed in `post-sitemap.xml`**. If anthropology is not offered: remove them from the sitemap and return 410 (gone), or point them to `/programs/`.

### 3.5 Settings

| Setting | Found | Change |
|---|---|---|
| Event data retention | **2 months** | Set to **14 months** now. Otherwise explorations cannot compare the 2027 season with earlier months |
| Google signals | Off | Keep off (privacy; DPDP) |
| Google Ads link | Linked (Institute of Translational Health Science) | Keep; import "applied" and "enrolled" as offline conversions (plan §8.2) |
| Search Console link | Linked | Keep |
| Stream URL | `https://translationalhealthscience.in` (non-www) | Fine; add ithsedu.in for cross-domain at launch |
| Internal traffic | Not filtered (localhost, Tag Assistant visible) | Define and activate internal and developer traffic filters |

## 4. Other hosts found

| Host | What it is | Risk | Action |
|---|---|---|---|
| iths.rbuchd.in | An ITHS "Apply Now in Bahra University" page on Rayat Bahra University's domain; indexable; no canonical; 49 + 21 sessions referred | A second public copy of ITHS admissions content; confusing (Bahra University page on an RBU domain) | Ask who controls it. Either `noindex` it and link to `/campuses/shimla/`, or 301 it to that page |
| demo.ithsedu.in | Staging of the new site (home page only); `noindex, nofollow`; open to the public | Can be found and shared; title "Top Private Institute in India" breaks guardrail 1 | Password-protect it; change the title wording before any copy reaches the live site |
| bu.translationalhealthscience.in, rbu.translationalhealthscience.in | Old campus subdomains; GSC properties; robots.txt not fetchable; old URLs 404 | Crawl errors; lost link value | Retire (remove DNS) or 301 to the matching campus pages |
| iths.technotaau.com | Staging linked from the live Mohali campus page (audit A2) | As in the audit | Fix the link; password-protect |
| embryogenesis.34gaon.com | **A full, indexable copy of the EmbryoGenesis site** (`index, follow`, self-canonical); links to ITHS 11 times | Duplicate content for embryogenesis.in; outside ITHS, but it affects the group | EmbryoGenesis team: take it down or password-protect and `noindex` it |

### 4.1 External links (Search Console, 63 links from about 15 sites)

- **Sister sites:** embryogenesis.in 17, nutrigenetics.in 17 (many from tag feeds), embryogenesis.34gaon.com 11 (the copy above).
- **Directories:** weboworld, khojbiz, bharatibiz (shows phone 96917 36435, the old EmbryoGenesis admissions number), magicpin (a Shimla listing "Institute of Translational Health Science, Bahra University"), tracxn, aeroleads.
- **Education and university sites:** rbuchd.in 3, ivf.net 1, careerplanb.co 1.
- **Social:** YouTube 1 — channel **@InstituteofTranslationalHealth**, a different handle from the site footer's @TranslationalHealthScience (confirm which is real); Facebook 1.
- **Reading:** almost no independent links. Off-page priorities: links from the four universities, education portals (via the universities), and regional press (plan §6.6). Correct the directory listings' phone and name to the fact sheet.

### 4.2 Page-level decisions from the 16-month all-pages export

| Page (16-month clicks, URL-prefix) | Decision |
|---|---|
| `/ba-bsc-and-ma-msc-anthropology-admission-2025/` (**206 clicks, 49,115 impressions**, now 301 to the homepage) and `/rayat-bahra-university/msc-and-bsc-anthropology/` (54) | The biggest lost asset. "bsc anthropology" still gets 4,179 impressions. **If anthropology is still offered**, publish `/programs/anthropology/` and 301 both old URLs to it. If not, 410 them and remove them from the sitemap (B7). Client decision |
| `/join-indias-leading-program-in-nutrigenetics…` (127) and `/bsc-and-msc-nutrigenetics-admission-2025/` (41) | Merge into `/programs/nutrigenetics-personalized-nutrition/` (83, position 10.9). Move their useful content (careers, eligibility, FAQs) into the programme page first, then 301. The combined signals should lift the programme page |
| `/study-stem-cell-tissue-engineering…` (71, position 12.1) and `/indias-1st-b-tech…` (21) | Merge into `/programs/b-tech-stem-cell-tissue-engineering/` (74) the same way |
| `/exploring-the-possibilities-of-an-msc-and-bsc-in-clinical-embryology/` (48, 17,945 impressions) | Merge into `/programs/clinical-embryology/bsc/` (36). This also gives the BSc page the "bsc embryology" signals |
| `/transform-your-career-with-advanced-health-science-courses-at-iths/` (29) | Merge into `/programs/` |
| `/what-is-translational-health-science-courses-careers-india/` (0) | Keep only if rewritten for ithsedu.in's About page; otherwise move it to ithsedu.in with a 301 after launch (it is an institute topic) |
| `/clinical-embryology-shimla/` (2), `/nutrigenetics-admissions/` (0) | Confirmed ads-only: `noindex`, out of the sitemap |
| `/news-events/` (0 clicks, 208 impressions), `/careers/` (2) | Confirmed: move to ithsedu.in with 301s after launch |
| `/Brochure-of-translational-health-science-2024.pdf` (**84 clicks**) and the 2025 prospectus PDFs (47 and 34) | PDFs get real search traffic. Replace the content at the **same URL** with the current, compliant brochure (don't delete it), and link from each PDF's first page to the admission page |
| `/campuses/shimla/` (46), `/campuses/mohali/` (50), `/campuses/hoshiarpur/` (10) | Campus pages are under-performing compared with Bhopal (249). This confirms the campus-visibility priority |
| `/iths-set/` (3 clicks, position 28) | Weak. Add real content (test dates, syllabus, scholarship slabs, past results) before the March campaign |

102 of 201 pages with impressions got 0 clicks in 16 months; most are categories, tags, PDFs and old redirected URLs.

## 5. What changes in the plan (applied in `02-iths-master-plan.md` v1.1)

1. **Brand searches and ithsedu.in.** The homepage takes the brand searches and many leads. When ithsedu.in launches, Google may rank it first for "ITHS". That is the goal (§6.1), but it must not cost admissions leads. So:
   - ithsedu.in's home page carries an "Admissions 2027–28" band above the fold, linking to the admissions site;
   - K1 measures **non-brand** organic clicks plus **total leads**, not brand clicks;
   - the launch date stays before the season (target 9 Feb 2027), so the brand results settle before May.
2. **Protected pages.** Every page in §2.4, `/msc-neuroscience/` and the ads page `/art-and-clinical-embryology-program/` are protected.
3. **Cluster merges only for posts with almost no clicks:**
   - `bsc-and-msc-nutrigenetics-admission-2025` and `join-indias-leading-program-in-nutrigenetics…` → nutrigenetics programme page;
   - `study-stem-cell-tissue-engineering…` and `indias-1st-b-tech…` → B.Tech page;
   - `exploring-the-possibilities-of-an-msc-and-bsc…` → BSc embryology page;
   - `transform-your-career…` → `/programs/`;
   - anthropology posts: after B7.

   File 01 (16 months, §4.2) confirms the list and the click numbers. Content first, then the 301.
4. **Campus visibility for Shimla, Hoshiarpur and the RBU Mohali page becomes a priority** (the Mohali page ranks at position 30 for Chandigarh searches; only Bhopal's page performs):
   - Google Business Profiles (if signage exists);
   - deeper campus pages (programmes, labs, hostel, travel, fees, FAQs, real photos);
   - links from Bahra University and RBPU;
   - the planned Punjab guide moves to December.
5. **Snippet work on high-impression pages:** the embryologist post (25,221 impressions), the food and nutrition guide (16,135), the colleges guide (14,516) and "embryologist" (5,531 impressions at position 8.2). Rewrite the titles and meta descriptions, and add direct 40–60-word answers at the top.
6. **GEO moves up.** AI assistants convert at 23.6%. llms.txt, fact consistency and the monthly AI panel start in December, not after launch.
7. **Measurement fixes before 1 March 2027:**
   - GA4 retention set to 14 months;
   - de-duplicate Form Submit;
   - per-campus lead events;
   - internal-traffic filter;
   - UTM tags on all social, WhatsApp and PDF links;
   - remove the `purchase` key event.
8. **New P0 items:** certificate PDFs (§2.8), iths.rbuchd.in, demo.ithsedu.in, the bu./rbu. subdomains (§4) and the EmbryoGenesis copy on 34gaon.com.
9. **Internal links to level pages** (§2.9) before the season.
10. **Paid search worked:** 17.7% key-event rate in season. Plan the 2027 budget from the CRM's cost per admission (D7), and start brand and PG/PhD search earlier (February).

## 6. KPI baselines (for master plan §9)

| KPI | Baseline | Period |
|---|---|---|
| Organic clicks, year on year (URL-prefix) | 1,797 vs 941 (+91%) | 26 Aug – 25 Nov 2026 vs 2025 |
| Organic clicks (GSC) | 1,759 a quarter (about 586 a month) off-season; 2,583 in the 4-month season (about 646 a month) | Aug–Nov 2026; May–Aug 2026 |
| Brand / non-brand clicks (visible queries, URL-prefix) | 904 / 1,084 | 16 months to 25 Nov 2026 |
| All clicks (URL-prefix) | 7,196 | 16 months to 25 Nov 2026 |
| Brand CTR and position | 21.5%, 3.9 | Since 29 Apr 2026 |
| GA4 sessions | 12,196 a year; 5,712 in season | Nov 2025 – Nov 2026 |
| GA4 key events | 1,448 a year; 1,022 in season (inflated by double-counting; reset after the fix) | Same |
| Paid search key-event rate | 17.7% | Season 2026 |
| AI Assistant sessions | 195 a year; 23.6% key-event rate | Same |
| Campus organic clicks (3 months) | Bhopal 110; Mohali (in homepage and brand); Shimla 0; Hoshiarpur 0 | Aug–Nov 2026 |
| Indexed pages | 123 indexed, 109 not indexed | 23 Nov 2026 |
| Referring domains | about 10 (63 links) | Nov 2026 |

Targets (E) are set after the files arrive and after the client shares 2025–26 and 2026–27 admission numbers (D7).

## 7. Questions for the client

1. Is there a **Google Business Profile** named "Institute of Translational Health Science (ITHS) Kurali" (or similar)? Who manages it? Which address does it use?
2. Who controls **iths.rbuchd.in** and the **bu./rbu.** subdomains?
3. What was on `/document-library/` and `/certificate/`?
4. Are ads still pointing to any of the 404 URLs in §3.4?
5. Which CRM or sheet holds the leads? Can we see lead, application and admission counts by campus for 2025–26 and 2026–27?

## 8. Files reviewed and files still missing

**Reviewed (27 Nov 2026):**
- GA4 40, 41, 42, 43, 45.
- Top-page Performance exports for pages 03–09: colleges guide, Bhopal, PhD, ART guide, nutrition guide, cancer post, stem cell programme.
- Indexing drilldowns:
  - page with redirect (29);
  - 404 (17);
  - duplicate without canonical (8, all `?xx` parameter URLs on the bu./rbu. subdomains);
  - alternate with canonical (6, `/?xx` parameters, fine);
  - noindex (2, both ads pages);
  - other 4xx (admin-ajax, fine);
  - crawled not indexed (39: mostly RSS feeds and old redirected URLs, which is harmless, plus the MSc page and three PDFs);
  - discovered not indexed (7: thin categories and the two admission forms).
- The indexed-pages list (122); Core Web Vitals (mobile, no failing URLs); top linking sites, latest links, sample links, top target pages (internal).

- URL-prefix Performance exports: last 3 months, last 3 months vs last year, season 2026, brand and non-brand (16 months), the clusters embryology, nutrigenetics, cancer, Shimla, Hoshiarpur, after-12th and fees (16 months), and the page exports for the homepage and the PhD page. Sample links (the same 61).
- URL-prefix property `https://www.translationalhealthscience.in/` (uploaded separately): Core Web Vitals; all eight indexing drilldowns; the indexed-pages list (122 URLs, the same as the Domain property); latest links (the same 61 links). They match the Domain property, minus the subdomain URLs. Mobile Core Web Vitals "good" URLs rose from 40 (29 Aug) to 53 (26 Nov), with none poor.

**Received later (URL-prefix property):** the 16-month all-pages export (file 01); page exports for the ART guide, the cancer scientist post, the stem cell programme and MSc Neuroscience. File 01 settles the merge list (§4.2).

**No longer needed / still missing:**
- The Performance exports 01–16: all-pages, 3-month, season, brand and non-brand, and the ten clusters. The cluster numbers in §2.5 come from the Chrome summary.
- The top-page exports for the home page, the embryologist post and `/msc-neuroscience/`.

The Domain-property versions of 01–16 are not needed: the URL-prefix exports cover the same pages with a longer history. Still missing, with low impact: the page export for the embryologist post (its queries appear in the embryology and after-12th clusters).
