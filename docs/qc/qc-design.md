# EmbryoGenesis website: design QC report (colour, contrast, alignment)

**Prepared by:** TechnoTaau Team (visual design), for Jakhar Singh
**Date:** 17 October 2026
**Trigger:** client feedback "color combination is not visible proper and alignment also not correct". The screenshots came from the old dark-mode prototype, which has since been removed. We still treated the feedback as valid for the real site and fixed the same areas there.
**Scope:** all 19 pages in `site/preview/`. Each page was tested at 320, 360, 768, 1024, 1366 and 1920 px, then once with `prefers-color-scheme: dark` emulation and once with Chrome forced dark (`--force-dark-mode --enable-features=WebContentsForceDark`).
**Files changed:** `site/assets/css/style.css` (root rules) and `site/assets/css/add-qc.css` (new section 7, "Design pass"). We made no changes to page HTML, partials, JSON, `build.py` or `main.js`, and no JS change is needed. Nothing is committed.
**Final state:** `build.py` builds 19 pages. `qc.py` gives 0 errors and 0 warnings. axe-core 4.10 (WCAG 2.0/2.1/2.2 A and AA plus best practice) finds 0 violations on all 38 page views (1366 and 390 px). No horizontal scroll and no text closer than 12 px to the screen edge on any page at 320 or 360 px. The earlier QC work is unchanged: 44 px targets, focus rings, reduced motion, 14 px minimum text.

## 1. How contrast was measured
Each page was rendered twice: once normally, and once with every text colour set to transparent. For every text node, the background was read from the real pixels behind it (5th percentile, so the worst part of a gradient, photo or ring counts). That background was compared with the computed text colour. Pass mark: 4.5:1, or 3:1 for large text. For forced dark, the browser repaints the colours, so the text colour was also read from the pixels.

| Run | Text blocks checked | Failures before | Failures after |
|---|---|---|---|
| Light, 5 widths x 19 pages | about 11,000 | 7 (5 elements) | **0** |
| `prefers-color-scheme: dark` emulation | 4,439 | 0 | **0** (page stays in the light palette) |
| Chrome forced dark | 4,439 | 68 (every gold button and badge, 2.48:1) | **0** |

## 2. Issues found and fixes

### The five areas the client pointed at
| # | Page / area | Problem | Fix |
|---|---|---|---|
| 1 | Home, "Leaders in Fertility Diagnostics and Research" | Heading centred in its column. Paragraph next to it justified (rivers), behind a thin dark divider. Heading broke into 3 lines with "Diagnostics" alone on the middle line. On phones the heading was centred while the text below was left-aligned. | Heading left-aligned and vertically centred on the paragraph. Wider heading column, so it now reads "Leaders in Fertility / Diagnostics and Research". Paragraph left-aligned (62ch max) with a 3 px teal rule. The same left alignment and rule are used on phones. |
| 2 | Home, "Explore Our Advanced Fertility Services" | Cards 459 px different in height. The description under each card title started 80 px to the right of the items below it. Icon top-aligned instead of centred on the title. "Book Now→" was a small 14 px text link with the arrow touching the words. | Both cards now have equal height. Icon and title are vertically centred, and the description and all items share one left edge. "Book Now →" is now a 44 px outlined pill (deep teal #0E6970 on white, 6.42:1; fills teal on hover). The diagnostic card fills its spare height with a decorative lab photo (`microscope`, CSS background, 800 px WebP, desktop only), so both "View all" buttons sit on one line. |
| 3 | About, "Road Map of Embryogenesis" | The line ran from the screen-side edge past the first and last dots. Dot, date and text were offset from each other. On phones the line ran on below the last dot, 1 px off the dot centre. | Rebuilt. Each step draws its own connector from its dot to the next dot, so the line starts and ends exactly on the first and last dots. Desktop: dot, date and text share one left edge. Phones and tablets (860 px and below): a clean vertical timeline in which the dot centre lines up with the first line of the date (24 px line box). |
| 4 | Footer | Columns had equal widths, so the address wrapped tightly and the five social icons wrapped to a second row (one lonely LinkedIn icon). The phone number broke inside "+91 / 9599877196". At 768 px the columns fell into 3 + 1. | Columns sized to their content: 1.3 / 0.8 / 1 / 1.45 on desktop and 2 x 2 on tablets. On phones: About, then Quick Links and Useful Links side by side, then Contact. Social icons stay on one row. Phone numbers never break. Contrast was already fine and was checked: links #FFF on #0E6970 6.42:1, text #D8ECEC 5.23:1, legal line 5.23:1. |
| 5 | Hero panel and coloured bands | Inner heroes: the gold ring crossed pale text at 768 to 1366 px (profile credentials 3.85:1, leads 4.20 to 4.45:1). Pause button on the home slider was 3.34:1. Paragraphs in the "Academic Programs" band were justified, with buttons at three different heights. | Inner-hero gradient now ends on deep teal #0E6970 instead of the lighter #0E7178. Ring opacity cut from 35 % to 20 %. Credentials line now #FAF1DA. Slider control is solid deep teal. Programme band: left-aligned text, icons centred, buttons on one baseline, 3 columns at 1000 px and up, 1 column below. |

### Other issues found in the audit
| Page | Area | Problem | Fix |
|---|---|---|---|
| All | Justified text (`.just`, `.vcard p`, `.svc p`, `.feature p`, `.split .para`) on About, Therapies, Diagnostic, both programme pages and Home | Rivers of white space | `text-align:left` everywhere. The audit finds no justified text left on the site. |
| Home | Care pathway numbers 1 to 4 | Gold text on light teal, 2.30:1 | Gold badge with gold-ink number, 6.94:1 |
| Home | "Why choose" tiles | 2 + 1 (lonely third tile) | 3 across from 761 px, with matching card style |
| Home | Patents and Recognition | Photos at three different sizes. Captions wrapped unevenly ("Scientific Team MBBS MD / Pathology") | Photos fill equal columns. Title and subtitle each on their own line |
| Home | Key facts (6), About key facts (7) | 4 + 2 and 3 + 3 + 1 | 3 x 2 on home and 4 + 3 on About. On tablets, 2 across with the last fact spanning the row |
| Home | Book Now band | Heading centred above a left-aligned form. Map column vertically centred against it | Heading left-aligned, both columns top-aligned |
| Home, Blog, Media | Photo cards | Images stretched when a neighbour card was taller. "Read more" links at different heights | Image row keeps its size. Links sit on the bottom edge of every card in a row |
| Home, About, Contact, Diagnostic, Courses | 3-card rows at 768 px | 2 + 1 lonely card | Photo cards stay 3 across. Text cards go 2 across with the third spanning the row |
| B.Sc. page | "Why choose" 4 cards at 768 px | 3 + 1 | 2 x 2 |
| Media | 10 cards | 3 + 3 + 3 + 1 at 1024 px | 4 / 2 / 1 columns |
| Blog posts (ERFA, Unexplained) | Related reading, 4 links | 3 + 1 | 2 x 2 |
| Courses | "Why choose" cards | Read-more links at different heights | Aligned to the bottom |
| Diagnostic, Therapies, Courses | `.cross` card placed on `.wrap` | Card 16 px wider than the content on desktop and touching the screen edges on phones | Kept to the content width with the page gutter |
| Skill training | "Who can apply" column | Eyebrow, heading and box spread over the full column height | `.stack` packs to the top (`align-content:start`) |
| Home hero | H1 | "Mohali" alone on the last line on desktop. Third button alone on a row on phones | Panel 580 px and H1 2.6 rem max (now "EmbryoGenesis, Mohali" on one line). Phone buttons: Book Now full width, Diagnostic and Therapeutic side by side |
| About | Appreciation gallery | 5 + 3 | 4 + 4 (2 across on phones) |
| Home | Lone FAQ link band | 120 px of padding around one link | Compact band |
| All | Buttons | Heights 46 to 49 px depending on font metrics. Gold buttons and call pills differed in one row | One height for all buttons and call pills (46 px) |

### Forced dark (Chrome flag, Android "darken websites")
Chromium 141 forced dark ignores every page-side opt-out. We tested six combinations of `<meta name="color-scheme">` (`only light`, `light dark`, `dark`, none) and `:root{color-scheme}` on a test page, and all of them were darkened. In that mode Chrome keeps the gold fill but lightens the dark gold-ink text to 2.48:1. Users in that mode always match `prefers-color-scheme: dark`, so for them gold surfaces (primary buttons, the "Admissions open" tag, care badges, the phone action bar) switch to the palette's Gold Dark #7A5C1B with white text. That is 6.22:1 with or without forced darkening. Users with a normal light or dark OS setting and no forcing see the light brand page. The only difference for OS-dark users is this deeper gold on primary buttons.

## 3. Contrast numbers (worst case measured on the rendered page)
| Element | Before | After |
|---|---|---|
| Profile hero credentials line | 3.85 | 4.86 |
| Profile hero lead | 4.20 | 4.86 |
| Profile hero intro | 4.34 | 4.96 |
| 404 hero lead | 4.31 | 4.93 |
| Blog hero intro | 4.45 | 5.09 |
| Home care step numbers | 2.30 | 6.86 |
| Home slider pause button | 3.34 | 6.57 |
| Gold buttons and tags under forced dark | 2.48 | 6.22 |
| Services card headings, items and "Book Now" (unchanged colour, now larger) | 6.42 | 6.42 |
| Footer links / text / legal | 6.42 / 5.23 / 5.23 | same |
| Hero panel text on deep teal | 5.36 | 5.36 |
| Road map dates on light teal | 5.89 | 5.89 |

## 4. Screenshots (session scratchpad, not in the repository)
`/tmp/claude-0/-home-user-emb/b14c7f6e-a696-51d0-a38b-d172266186db/scratchpad/design/`: `before-*` and `after-*` for each area at 1366 and 390 px. Areas are 1 home Leaders band, 2 home services, 3 about road map, 4 footer, 5a home hero, 5b diagnostic hero, 5c academic band, 5d CTA band and 5e header strip. There are also `after-dark-home-*.png` and `after-force-home-*.png`.

## 5. Remaining items
1. **Forced dark cannot be switched off by the page** (Chrome limitation). It is now readable everywhere, but the page shows in dark colours in that mode.
2. **One-word last lines that cannot be avoided without changing wording:** home H1 "Mohali" on phones under 400 px; two long media-card titles (8+ lines, beyond the browser's `text-wrap:balance` limit); and "receptivity?" or "Infertility?" alone on a second line in two post headings at 360 px.
3. **Decorative photo in the diagnostic services card** is the stock `microscope` image already on the site. Swap it for a photo of the Mohali lab when the client supplies one.
4. Lighthouse was not re-run. axe-core (the engine behind the Lighthouse accessibility score) reports 0 violations on every page view.
5. **Content concerns for the client (not changed, wording is the client's call):** home services "Patented diagnostic test" and About road map "(Patented)" conflict with the project guardrail ("patent application published"). The footer "As the best fertility centre" and About "best fertility diagnostic centre in India" conflict with the no-superlatives guardrail.

TechnoTaau Team
