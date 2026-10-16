# EmbryoGenesis website: front-end QC report (responsive, accessibility, performance, engagement)

**Prepared by:** TechnoTaau Team (Front-end Quality Controller), for Jakhar Singh
**Date:** 16 October 2026
**Scope:** all 19 built pages in `site/dist/`, tested at 360, 390, 768, 1024, 1366 and 1920 px (plus 320 px and a 740x360 landscape check).
**Files changed (front-end ownership only):** `site/assets/css/style.css`, `site/assets/css/add-qc.css` (new, loaded last), `site/assets/js/main.js`, `site/src/partials/header.html`, `site/src/partials/footer.html`, and six PNGs in `site/assets/img/`. No page bodies, page JSON or `build.py` were edited.
**Final state:** `python3 site/build.py` builds 19 pages; `python3 site/qc.py` reports 0 errors, 0 warnings. Nothing committed by this agent.

---

## 1. Scores before and after

Lighthouse 12 (mobile preset, simulated throttling), all 19 pages, served locally with `python3 -m http.server` (no compression, no cache headers).

| Category | Before (avg, range) | After (avg, range) |
|---|---|---|
| Performance | 88.4 (85 to 98) | 89.2 (86 to 91) |
| Accessibility | 91.9 (90 to 94) | **100 (100 on every page)** |
| Best practices | 100 | 100 |
| SEO | 96.7 (100; 69 on `/404.html` and `/privacy-policy/` because they are `noindex` on purpose) | 96.7 (same) |

axe-core 4 (WCAG 2.0/2.1/2.2 A and AA plus best practice), every page at 1366 and 390 px:

| Rule | Impact | Before | After |
|---|---|---|---|
| color-contrast | serious | 38 of 38 page views | 0 |
| link-in-text-block | serious | 38 of 38 | 0 |
| region (content outside landmarks) | moderate | 38 of 38 | 0 |

Playwright layout audit (6 widths x 19 pages = 114 views):

| Check | Before | After |
|---|---|---|
| Horizontal scroll (incl. 320 px) | none | none |
| Elements overflowing the viewport | none | none |
| Distorted images | none | none |
| Text under 14 px | 30+ distinct elements (labels, tags, eyebrows, key-fact terms, breadcrumbs, form labels, footer legal line, menu button, mobile bar) | **none** |
| Interactive targets under 44 px tall | 40+ patterns (utility bar, socials 36 px, nav 43 px, link buttons 37 px, breadcrumbs 17 px, TOC 20 px, checkboxes 13 px, sidebar and contact links 37 to 40 px) | only short one-word links whose **width** is under 44 px (Home, Blog, INNR) while their height is 44 px, plus one page-body link (section 4) |
| Sticky header height on a phone (390x780) | 202 px (26 % of the screen) | 72 px (9 %) |
| Mobile action bar hiding the end of the page | yes (bar 69 px, page padding 64 px) | no |

Measured with Playwright at 390 px (no throttling): CLS 0.000 on every page; LCP element is the hero photo on Home, the post image on blog posts and the hero paragraph elsewhere. Transfer per page (first view, including Google Fonts): 175 KB (privacy) to 362 KB (home); full scroll 175 KB to 594 KB (home).

Keyboard and touch tests (scripted, 34 checks): before 16 pass / 18 fail (one of them a test artefact); after 33 pass / 1 expected exception (see section 3).

---

## 2. Issues fixed

### Responsive and header
1. **Sticky header too tall.** The whole block (utility bar + logo row + admissions strip) was sticky: 202 px on phones, 226 px at 1024 px. Now only the white logo/nav row sticks; the utility bar and admissions strip scroll away (Indira IVF pattern). `.headwrap` uses `display:contents`; `.site-head` is sticky.
2. **"Book Now" wrapped to a second header row at 901 to 1180 px** (header 226 px at 1024). Two tighter breakpoints keep logo, menu and button on one row.
3. **Utility bar duplicated on phones.** Hidden at 760 px and below, where the bottom action bar already offers Call and WhatsApp.
4. **Mobile action bar covered the footer.** Bar is now a fixed 60 px plus safe area; body padding and `scroll-padding-bottom` reserve the space. The WhatsApp float stays hidden while the bar is shown.
5. **Mobile menu could not be scrolled on short screens** (landscape 740x360 menu ran 250 px off screen). The open menu now scrolls within the viewport.
6. **Jump-bar targets landed under the sticky bars** (Diagnostic and Therapeutic pages: headings hidden 104 px under header + jump bar). Replaced the hard-coded `scroll-margin-top:130px` with `html{scroll-padding-top}` driven by `--header-h` and `--jump-h`, measured by `main.js` (also on font load and resize). This also fixes blog TOC anchors and keeps keyboard focus clear of the sticky header (WCAG 2.4.11).
7. **Home slider control drew a fourth "dot".** The pause button inherited the dot style; it is now a separate round 44 px control.

### Accessibility
8. **Colour contrast (serious):** admissions strip on `#11858E` (4.4:1) now on `--teal-ink #0F7C84` (5.0:1); eyebrows, key-fact terms, tags and the blog sub-title moved from `#11858E` to deep teal `#0E6970` (5.9 to 6.4:1); footer legal line `#BFDCDC` (4.4:1) now `#D8ECEC` (5.2:1).
9. **Contrast on gradient heroes** (not detectable by axe, found by pixel sampling): pale lead and intro text fell to 2.7 to 3.7:1 where the `.ihero` gradient reached `#25A2AA`. The gradient now runs `#0B5C62 → #0E6970 → #0E7178`; lead text `#FAF1DA`, intro text `#EAF6F7`, breadcrumbs `#E6F4F5`; translucent pills and the award card use a dark tint instead of a white one. All hero text now meets 4.5:1.
10. **Link only distinguishable by colour** (footer Privacy Policy): underlined.
11. **Landmarks:** utility bar and admissions strip are now `<aside>` with labels ("Quick contact", "Admissions"); the WhatsApp float moved inside `<footer>`.
12. **Focus ring contrast:** the gold ring was 2.5:1 on white. Rings are now dark teal `#0B5C62` on light surfaces and cream `#F3E7C8` on teal surfaces (via a `--focus` token), 3 px with 2 px offset, on every link, button, summary, field and focusable panel.
13. **Services dropdown** stayed open after a second click/tap or Escape (`:focus-within` and sticky hover on touch kept it visible). Now a proper disclosure: click, Enter or Space toggles; ArrowDown opens and moves in; ArrowUp/Down move between items; Escape closes and returns focus; leaving the group closes it. Hover-to-open only on hover-capable desktops.
14. **Tabs:** added Home and End keys (Arrow keys already worked).
15. **Slider:** `aria-live` is "off" while rotating and "polite" when paused; rotation skips while the tab is hidden; first slide no longer animates (protects LCP).
16. **Jump buttons** now move keyboard focus to the target section and mark the section in view (`aria-current`).
17. **Menu button glyph** "☰" hidden from screen readers; button text now 16 px.
18. **FAQ** `<summary>` marker hidden in Safari as well (`::-webkit-details-marker`).
19. **Readable sizes:** every text style below 14 px raised to 0.875 rem (labels, eyebrows, tags, chips, breadcrumbs, consent text, table headers, meta lines, legal line, mobile bar).
20. **Touch targets:** nav items, link buttons, chips, jump buttons, socials (44x44), sidebar and contact links, call pills and dropdown items are 44 px; breadcrumbs, card-title links, key-fact links and table links get a 44 px hit area without changing layout (padding plus negative margin); blog TOC links get 44 px inline hit areas; consent checkboxes are 20 px with the whole label clickable; footer links are spaced for thumbs on phones.

### Performance
21. Header `logo.png` 31 KB → 7.7 KB and `favicon.png` 41 KB → 7.8 KB (lossless-looking 256-colour quantisation, same dimensions, checked side by side). This saves about 56 KB on **every** page view. Partner-logo PNG fallbacks also reduced (69 → 15, 64 → 17, 45 → 8, 15 → 5 KB); the WebP versions actually served were kept unchanged.
22. Hero LCP image `hero-couple.webp` is 145 KB (under the 250 KB target); slides 2 and 3 are not downloaded until shown. No layout shift anywhere (CLS 0).
23. JPEGs were already at about quality 82 to 85; recompressing saved under 5 %, so they were left as they are.

### Engagement polish (CSS/JS only, palette unchanged)
24. Buttons: smooth colour/shadow transitions, 1 px lift on hover (hover devices only), ghost buttons fill white on hover, link-style buttons use an offset underline that turns gold on hover.
25. Cards (blog, media, programme, location, related links, quick links): lift and soft teal shadow on hover, gentle 3 % image zoom, focus-within halo for keyboard users.
26. Reveal on scroll: cards inside a revealed block now fade up in a short stagger (70 ms steps). The stagger is removed after it plays so hover effects are not delayed. Everything is skipped under `prefers-reduced-motion`.
27. Slider: soft cross-fade between slides (motion-safe only).
28. Spacing: section padding 44 px on phones (60 px on larger screens), active jump-bar pill highlighted, menu button fills teal when open, branded text selection colour, red border on invalid fields after the user has interacted.

---

## 3. Remaining issues and why

| Item | Status |
|---|---|
| **Performance capped near 90 by render-blocking Google Fonts CSS** (FCP about 2.9 s on simulated mobile). | Needs a `build.py` head change (not in my files). Measured fix in section 5: 98 to 100 with the same pages. |
| Phones download desktop-size images (hero 1800 px / 145 KB; Lighthouse estimates about 100 KB waste on Home). | Needs `srcset` in `build.py` (section 5). An 800 px WebP of the hero is about 41 KB. |
| No gzip/brotli or cache headers in the local test server. | Hosting/WordPress setting (section 5). |
| Last jump target on the Therapeutic page (Molecular Hydrogen) stops 6 px under the jump bar. | Expected: the page cannot scroll further because it ends soon after. Not a defect. |
| One-word links (Home, Blog, INNR, ITHS) are 29 to 40 px **wide** (44 px tall). | Meets WCAG 2.2 AA target size (24 px with spacing). Left as is to keep the nav rhythm. |
| Favicon artwork includes a cropped "E" from the wordmark at the right edge. | Needs a clean square icon (32 px and 180 px) from the designer. |
| Images in `assets/img/` that no page uses: `app-02`, `app-06`, `app-07`, `app-08`, `app-12`, `app-giostar2`, `app-team-iths`, `consult`, `eit` (`.jpg` + `.webp`). | Not served, so no speed cost; leave them out of the WordPress upload or use them later. |
| About 4 KB of prototype CSS in `style.css` is unused (`.ph`, `.timeline`, `.sideform`, `.office`, `.pagehead`, `.page`, ...). | Left in place in case the WordPress developer reuses it; gzip makes it about 1 KB. |

---

## 4. Page-body changes recommended (for the page owners)

The CSS and JS for both changes are already in place, so they are drop-in.

1. **Jump bars as real links** (work without JavaScript, announced as navigation).
   - `site/src/pages/diagnostic.html`, line 21
     - Current: `<div class="jump med-jump"><div class="wrap"><span>OUR ADVANCED DIAGNOSTIC TESTS</span><button type="button" data-jump="t-erfa">ERFA – The Soil Test</button><button type="button" data-jump="t-ei">Endo-Immune Test</button><button type="button" data-jump="t-eit">Endometrial Infection Test (EIT)</button></div></div>`
     - New: `<nav class="jump med-jump" aria-label="Diagnostic tests on this page"><div class="wrap"><span>OUR ADVANCED DIAGNOSTIC TESTS</span><a href="#t-erfa" data-jump="t-erfa">ERFA – The Soil Test</a><a href="#t-ei" data-jump="t-ei">Endo-Immune Test</a><a href="#t-eit" data-jump="t-eit">Endometrial Infection Test (EIT)</a></div></nav>`
   - `site/src/pages/advanced-fertility-therapies.html`, line 21: same pattern. Change the wrapper `<div class="jump med-jump">…</div>` to `<nav class="jump med-jump" aria-label="Therapies on this page">…</nav>` and each `<button type="button" data-jump="th-xxx">Label</button>` to `<a href="#th-xxx" data-jump="th-xxx">Label</a>` (th-lit, th-pbmc, th-prp, th-stem, th-h2).
2. **Home FAQ link tap target.** `site/src/pages/home.html`, line 147
   - Current: `<p><a href="/diagnostic/#faqs">Read our diagnostic test FAQs</a></p>`
   - New: `<p><a class="core-more" href="/diagnostic/#faqs">Read our diagnostic test FAQs</a></p>`

---

## 5. Changes recommended outside my files (`build.py`, hosting)

Measured on copies of `dist/` in the scratchpad (Lighthouse mobile, Home / About / Diagnostic):

| Variant | Performance | FCP | LCP |
|---|---|---|---|
| Current | 86 / 90 / 88 | 2.9 s | 2.9 to 3.2 s |
| gzip only | 88 / 91 / 89 | 2.8 s | 2.8 to 2.9 s |
| Non-blocking Google Fonts | **99 / 100 / 100** | 1.1 s | 1.5 to 2.3 s |
| Non-blocking fonts + gzip | **98 / 100 / 100** | 0.8 s | 1.0 to 2.0 s |

1. **Load Google Fonts without blocking render** (`page_html()` in `build.py`, line 163). Replace
   `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@500;600;700&family=Lato:wght@400;700&display=swap">`
   with
   `<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@500;600;700&family=Lato:wght@400;700&display=swap" onload="this.onload=null;this.rel='stylesheet'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@500;600;700&family=Lato:wght@400;700&display=swap"></noscript>`
   Better still for WordPress: self-host the two families as WOFF2 (for example with the OMGF plugin) and preload the Work Sans 500 file.
2. **Responsive images** (`enhance_imgs()`): also write 800 px and 1200 px WebP copies and emit `srcset="x-800.webp 800w, x-1200.webp 1200w, x.webp 1400w" sizes="(max-width:760px) 100vw, 50vw"` on the `<source>`; for the home hero use `sizes="100vw"`. WordPress does this natively when images are uploaded through the media library.
3. **Hosting:** enable gzip or brotli for HTML/CSS/JS/SVG and `Cache-Control: max-age=31536000, immutable` for `/assets/` (add a `mod_deflate` / `mod_expires` block to `.htaccess`, or the host's cache plugin).
4. **Optional:** minifying CSS saves only about 3 % here (the source is already compact); not worth a build step on its own.

---

## 6. How this was tested
- Layout: Playwright (Chromium) at 360, 390, 768, 1024, 1366 and 1920 px, every page, full-page screenshots; checks for horizontal scroll, overflowing or clipped elements, computed font size, target size and image aspect ratio. Extra checks at 320 px and 740x360.
- Accessibility: axe-core injected on every page at 1366 and 390 px; pixel-sampling contrast check for text on gradients and photos; scripted keyboard tests (skip link, focus ring on every tab stop, dropdown, tabs, slider pause, FAQ, jump bar) and touch tests (menu, Services, landscape menu, action bar overlap, sticky header height).
- Performance: Lighthouse 12 on all pages before and after; Playwright LCP/CLS observers and per-page transfer totals.
- Tools and screenshots are in the session scratchpad (`qc-fe/`), not in the repository.

TechnoTaau Team
