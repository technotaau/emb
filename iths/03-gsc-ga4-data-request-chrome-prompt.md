# ITHS: Search Console and GA4 Data Export (prompt for Claude in Chrome)

**Prepared by:** TechnoTaau Team (lead: Jakhar Singh)
**Date:** 27 November 2026
**Purpose:** collect the baseline the master plan needs (`02-iths-master-plan.md` sections 3, 4.3 and 9): which URLs carry the traffic, which queries they rank for, which pages compete with each other, and the technical health of translationalhealthscience.in.

## How to use

1. Open Chrome, signed in to the Google account that has access to Search Console (and GA4) for translationalhealthscience.in.
2. Open Claude in Chrome and paste the prompt below (everything inside the box).
3. When it finishes, put all the downloaded files in one folder named `ITHS-GSC-export-<date>`, zip it, and upload the zip to this Claude Code session together with the summary Claude in Chrome gives you at the end.
4. TechnoTaau Team stores the raw files in `iths/data/raw/` (kept out of git) and commits only the baseline report.

Time needed: about 30–45 minutes of browser work. It is read-only: nothing in Search Console or GA4 is changed.

---

```text
You are helping TechnoTaau Team collect read-only data from Google Search Console (GSC) and Google Analytics 4 (GA4) for the website https://www.translationalhealthscience.in (and https://ithsedu.in if a property exists).

SAFETY RULES (follow strictly)
- READ and EXPORT only. Never change any setting, never add/remove users or owners, never click "Request indexing", "Validate fix", "Remove URL", "Submit" on sitemaps, never accept invitations, never link or unlink products, never delete anything.
- If a login, account choice, 2-step verification or permission prompt appears, STOP and ask me.
- Do not send data anywhere. Only download files to this computer and summarise in this chat.
- If a step is not available (no access, no data, report missing), write "not available" in the summary and continue.

FILE NAMING
Rename every downloaded file as: <NN>_<short-name>_<date-range>.<ext>
Example: 01_perf_all_last16m.zip . Keep a list of every file you downloaded.

PART A: SEARCH CONSOLE (https://search.google.com/search-console)

A0. Properties
- Open the property selector. List every property shown that contains "translationalhealthscience" or "ithsedu" (write the exact name: Domain property or URL-prefix, http/https, www/non-www).
- For the main property, open Settings and write down: my permission level (do not change it), whether ownership is verified (yes/no), the "Associations" section (which GA4 or other products are associated). Do not change anything.
- Use the Domain property for translationalhealthscience.in if it exists; otherwise use https://www.translationalhealthscience.in/ .

A1. Performance > Search results (Search type: Web). Turn on all four metrics (Clicks, Impressions, CTR, Position). For each export use the Export button (top right) > Download CSV (it downloads a zip with Queries, Pages, Countries, Devices, Search appearance, Dates and Filters).
- 01 Date: Last 16 months. Export -> 01_perf_all_last16m
- 02 Date: Last 3 months. Export -> 02_perf_all_last3m
- 03 Date > Compare > "Compare last 3 months year over year". Export -> 03_perf_compare_3m_yoy
- 04 Date > Custom: 1 May 2026 to 31 August 2026 (last admission season). Export -> 04_perf_season2026
- 05 Date: Last 16 months. Add filter Query > Custom (regex) > Matches regex: iths|translational|ithsset|ithsedu . Export -> 05_perf_brand_last16m
- 06 Same, but "Doesn't match regex" with the same pattern. Export -> 06_perf_nonbrand_last16m
- Remove the query filter before the next steps.

A2. Topic clusters (Date: Last 16 months). For each line, add filter Query > Custom (regex) > Matches regex, export, then remove the filter:
- 07 embryolog          -> 07_cluster_embryology
- 08 nutrigen|nutrition|dietetic -> 08_cluster_nutrigenetics
- 09 stem cell|tissue engineering|regenerative -> 09_cluster_stemcell
- 10 cancer            -> 10_cluster_cancer
- 11 shimla|bahra|solan|waknaghat|himachal -> 11_cluster_shimla
- 12 bhopal|sgsu|scope|madhya -> 12_cluster_bhopal
- 13 hoshiarpur|rbpu|phagwara -> 13_cluster_hoshiarpur
- 14 chandigarh|mohali|rayat|rbu|kharar|punjab -> 14_cluster_chandigarh_mohali
- 15 neet|after 12th|12th pcb|without neet -> 15_cluster_after12th
- 16 fee|scholarship|iths set|ithsset|admission -> 16_cluster_admission_fees

A3. Top pages (Date: Last 3 months). Open the Pages tab and sort by Clicks. For the top 10 pages, one at a time: click the page (it becomes a Page filter), open the Queries tab, export, then remove the filter.
- Name them 17_page01_<slug> ... 26_page10_<slug>.
- If time is short, do at least the top 5.

A4. Indexing > Pages
- Write down: number of Indexed and Not indexed pages, and the date of the last update.
- Under "Why pages aren't indexed", list every reason with its page count and whether the source is "Website" or "Google systems".
- Click each reason and use Export (top right) > Download CSV -> 27_index_<reason-short-name>.
- Also open "View data about indexed pages" and export -> 28_index_indexed_pages.

A5. Indexing > Sitemaps
- Write down every submitted sitemap: URL, type, submitted date, last read date, status, discovered pages. Do not submit or remove anything.

A6. Indexing > Removals: write down whether any removal requests exist (do not create any).

A7. Experience
- Core Web Vitals: for Mobile and Desktop, write down Poor / Need improvement / Good URL counts and the issue names. Open each report and export if an export button exists -> 29_cwv_mobile, 30_cwv_desktop.
- HTTPS: write down HTTPS vs non-HTTPS URL counts and any issue.

A8. Enhancements / Shopping / other report sections in the left menu: list every report that appears (e.g. Breadcrumbs, Videos, Review snippets) with Valid / Invalid counts.

A9. Security & Manual Actions: write down the status of Manual actions and Security issues (expected "No issues detected").

A10. Links
- Export external links: use "Export external links" > "Top linking sites" -> 31_links_top_linking_sites ; "More sample links" -> 32_links_sample ; "Latest links" -> 33_links_latest
- Export internal links -> 34_links_internal
- Write down the top 10 linking sites and the top 10 externally linked pages.

A11. Settings > Crawl stats > Open report
- Write down for the last 90 days: total crawl requests, total download size, average response time, Host status (any problems with robots.txt fetch, DNS or server connectivity), and the split "By response" (OK 200, 301, 302, 404, 5xx etc. with percentages), "By file type", "By purpose" and "By Googlebot type".
- Click "Server error (5xx)" if present and write down example URLs and dates.

A12. If a property exists for ithsedu.in, repeat A0, A1 (01 only), A4 and A5 for it with prefix "ITHSEDU_".

PART B: GOOGLE ANALYTICS 4 (https://analytics.google.com) — only if I have access
B0. Write down: account name, property name, property ID, and in Admin (read only): Data streams (each stream name, URL, Measurement ID), Key events list, Data retention setting, Google signals on/off, Product links (Google Ads, Search Console, BigQuery) present yes/no. Change nothing.
B1. Reports > Acquisition > Traffic acquisition. Dimension: Session default channel group. Date: last 12 months. Use Share this report > Download File > CSV -> 40_ga4_traffic_acq_last12m
B2. Same report, date 1 May 2026 to 31 Aug 2026 -> 41_ga4_traffic_acq_season2026
B3. Reports > Engagement > Landing page, last 12 months -> 42_ga4_landing_pages_last12m (if this report is missing, use Pages and screens -> 42_ga4_pages_last12m)
B4. Reports > Engagement > Events, last 12 months -> 43_ga4_events_last12m
B5. If a "Key events" or "Conversions" report exists, export it for last 12 months -> 44_ga4_key_events_last12m
B6. Traffic acquisition with secondary dimension "Session source / medium", last 12 months -> 45_ga4_source_medium_last12m

PART C: BING WEBMASTER TOOLS (https://www.bing.com/webmasters) — only if I already have access; skip otherwise
C1. Search Performance, last 6 months: export pages and keywords -> 50_bing_pages, 51_bing_keywords
C2. Write down indexed page count and any site scan or crawl errors.

FINAL SUMMARY (write it in this chat in exactly this structure)
1. Properties found (GSC, GA4, Bing) and my permission level on each.
2. GSC totals: Last 16 months clicks / impressions / avg CTR / avg position; Last 3 months the same; YoY change for the last 3 months (%).
3. Brand vs non-brand clicks, last 16 months.
4. Top 20 queries (last 3 months): query, clicks, impressions, position.
5. Top 20 pages (last 3 months): URL, clicks, impressions, position.
6. For each cluster 07–16: the top 3 pages by clicks and the top 5 queries; flag any cluster where 2 or more pages each get more than 10% of the clicks.
7. Indexing: indexed / not indexed counts and every reason with counts.
8. Sitemaps table.
9. Core Web Vitals and HTTPS status.
10. Enhancements, manual actions, security issues.
11. Links: top 10 linking sites, top 10 linked pages.
12. Crawl stats: totals, host status, response-code split, any 5xx examples.
13. GA4: streams and Measurement IDs, key events, channel totals last 12 months, top 10 landing pages, season 2026 channel totals.
14. Anything that was "not available", and why.
15. The full list of files downloaded.
```

---

## After the upload: what TechnoTaau Team does

1. Baseline report `iths/04-baseline-report.md`: traffic by page and cluster, protected URLs, brand vs non-brand, indexing and crawl issues, GA4 lead events.
2. Final decisions for the [DATA] items in the master plan (landing pages, cluster merges, `/news-events/`, category archives, URL moves).
3. KPI targets (master plan section 9) set from the baseline.
