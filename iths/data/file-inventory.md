# ITHS data files: inventory (identified by contents, not by name)

**Prepared by:** TechnoTaau Team (lead: Jakhar Singh) | **Date:** 27 November 2026

## How each file was identified

Chrome saved every export under Google's default name. So the numbers in the names (`_1`, `_2` …) do not match the numbers in the Chrome prompt (01–45), and some names don't make the property obvious. Each file was therefore identified from its contents:

- **Property:**
  - the file-name prefix: `translationalhealthscience.in-` means the Domain property; `https___www.translationalhealthscience.in_-` means the URL-prefix property;
  - checked against the contents: only the Domain-property indexing files contain URLs on the `bu.` and `rbu.` subdomains (redirect 6, 404 5, duplicate 8, crawled 1), which a `https://www.` property cannot contain;
  - checked against the date range: URL-prefix charts start on **26 Jul 2025**, while the Domain property's data starts on **29 Apr 2026** (Chrome summary).
- **Report:** `Filters.csv` (date range, query or page filter) for Performance exports; `Metadata.csv` (issue name, device) for indexing and Core Web Vitals; CSV headers for the link reports; the `#` header lines for GA4.
- **Consistency:** for the same page and dates, both properties give the same numbers (PhD 90, ART guide 83, cancer post 75, stem cell 65, last 3 months 1,759).

## Search Console: Performance

| Prompt no. | Export | URL-prefix file | Domain file | Key figure |
|---|---|---|---|---|
| 01 | All, last 16 months | `…Performance-on-Search-2026-11-27.zip` (uploaded twice; the second copy, `f1a482ef`, is byte-identical) | – | 7,196 clicks (chart); 201 pages |
| 02 | All, last 3 months | `_1` | – | 1,759 clicks |
| 03 | Compare 3 months, year on year | `_2` | – | Pages: 1,797 vs 941 clicks |
| 04 | Season, 1 May – 31 Aug 2026 | `_3` | – | 2,570 clicks |
| 05 | Brand, 16 months | `_4` | – | 904 clicks |
| 06 | Non-brand, 16 months | `_5` | – | 1,084 clicks |
| 07 | Cluster: embryology | `_6` | – | 368 |
| 08 | Cluster: nutrigenetics | `_7` | – | 110 |
| 09 | Cluster: stem cell | **missing** (Chrome reported the page froze) | – | Domain figure 45 (Chrome summary) |
| 10 | Cluster: cancer | `_8` | – | 202 |
| 11 | Cluster: Shimla | `_9` | – | 25 |
| 12 | Cluster: Bhopal | **missing** | – | Domain figure 10 (Chrome summary) |
| 13 | Cluster: Hoshiarpur | `_10` | – | 0 |
| 14 | Cluster: Chandigarh/Mohali | **missing** | – | Domain figure 13 (Chrome summary) |
| 15 | Cluster: after 12th / NEET | `_11` | – | 140 |
| 16 | Cluster: admission/fees | `_12` | – | 9 |
| 17 | Page 01: homepage (3 months) | `_13` | – | 398 |
| 18 | Page 02: embryologist post | **missing** | **missing** | Its queries appear in clusters 07 and 15 |
| 19 | Page 03: BSc embryology colleges guide | – | `_17` | 168 |
| 20 | Page 04: Bhopal campus | – | `_18` | 110 |
| 21 | Page 05: PhD | `_14` | `_19` | 90 (identical) |
| 22 | Page 06: ART guide | `_15` | `_20` | 83 (identical) |
| 23 | Page 07: food and nutrition guide | – | `_21` | 76 |
| 24 | Page 08: cancer scientist post | `_16` | `_22` | 75 (identical) |
| 25 | Page 09: stem cell programme | `_17` | `_23` | 65 (identical) |
| 26 | Page 10: MSc Neuroscience | `_18` | – | 58 |

## Search Console: indexing, experience and links

| Prompt no. | Report | URL-prefix file (rows) | Domain file (rows) | Difference |
|---|---|---|---|---|
| 27 | Page with redirect | `Coverage-Drilldown` (15) | `Coverage-Drilldown` (29) | Domain adds subdomain and http/non-www URLs |
| 27 | Not found (404) | `_1` (12) | `_1` (17) | 5 subdomain URLs |
| 27 | Duplicate without user-selected canonical | not uploaded | `_2` (8) | All 8 are bu./rbu. `?xx` URLs, so the www property has none |
| 27 | Alternate page with proper canonical | `_2` (6) | `_3` (6) | Same |
| 27 | Excluded by noindex | `_3` (2) | `_4` (2) | Same |
| 27 | Blocked due to other 4xx | `_4` (1) | `_5` (1) | Same |
| 27 | Crawled, currently not indexed | `_5` (38) | `_6` (39) | 1 subdomain URL |
| 27 | Discovered, currently not indexed | `_6` (7) | `_7` (7) | Same |
| 28 | Indexed pages | `Coverage-Valid` (123) | `Coverage-Valid` (123) | Same |
| 29 | Core Web Vitals, mobile | `core-web-vitals` | `core-web-vitals` | Same (0 failing URLs) |
| 31 | Top linking sites | yes (15) | yes (15) | Identical |
| 32 | More sample links | yes (61) | yes (61) | Identical |
| 33 | Latest links | yes (61) | yes (61) | Identical |
| 34 | Internal links (top target pages) | yes (53) | yes (53) | Identical |

## GA4 (property ITHS, 443162610)

| Prompt no. | Report | File | Range |
|---|---|---|---|
| 40 | Traffic acquisition by channel | `Traffic_acquisition_…Default_Channel_Group.csv` | 27 Nov 2025 – 26 Nov 2026 |
| 41 | Same, season | `…_1.csv` | 1 May – 31 Aug 2026 |
| 42 | Landing pages | `Landing_page_Landing_page.csv` | 12 months |
| 43 | Events | `Events_Event_name.csv` | 12 months |
| 45 | Channel plus source / medium | `…_2.csv` | 12 months |

## What this changes

- **Baseline source:** the URL-prefix property, because it has the longer history (26 Jul 2025 onwards) and supplied all the Performance totals. Domain figures (since 29 Apr 2026, from the Chrome summary) are kept for reference only, and the baseline report labels them.
- **Subdomain problems** (bu./rbu.) are visible only in the Domain property, so keep both properties in Search Console.
- **Still missing** (low impact): clusters 09 (stem cell), 12 (Bhopal) and 14 (Chandigarh/Mohali), and the embryologist post's page export. Re-export them from the URL-prefix property if 16-month figures are needed for those rows.
