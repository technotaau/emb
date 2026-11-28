# ithsedu.in: How the Website Works, Pages and Workflow

**Prepared by:** TechnoTaau Team (lead: Jakhar Singh) | **Date:** 28 November 2026 | **Version:** 1.0
**Read with:** `02-iths-master-plan.md` §5 (the ithsedu.in specification) and `05-action-plan-by-issue.md` (Issue 3).

---

## 1. In one line

**ithsedu.in is the official website of ITHS.** It tells people who ITHS is, what it has achieved and what is new. **Admissions stay on translationalhealthscience.in.** Every "Programmes & Admissions" button on ithsedu.in leads there.

| | ithsedu.in (official site) | translationalhealthscience.in (admissions site) |
|---|---|---|
| Job | Trust and credibility | Admissions and enquiries |
| Who it's for | Parents checking ITHS, partners, faculty candidates, media, researchers | Students and parents choosing a course |
| What it has | About, leadership, partner universities, research, achievements, news, careers | Programmes, campuses, fees, eligibility, ITHS-SET, apply forms |
| Main button | "Programmes & Admissions" (goes to the admissions site) | "Enquire" / "Apply" |
| Social accounts | @ithsedu | Campus accounts |

## 2. How it works: four visitor journeys

1. **A parent checks ITHS before admission.** Google "ITHS" → ithsedu.in home → About, Leadership, Partners → "Programmes & Admissions" → campus page on the admissions site → enquiry form → the campus counsellor calls within 24 hours.
2. **A student looks for a course.** Google "bsc clinical embryology" → the admissions site directly (ithsedu.in does not compete for course searches) → programme page → enquiry.
3. **Media, a hospital or a university wants to partner or report.** ithsedu.in → News, Research or Media kit → Contact form ("Partnership" or "Media") → the ITHS office replies.
4. **Someone wants to work at ITHS.** ithsedu.in → Careers → application form → HR.

## 3. How many pages

**Launch: 18 pages, plus 4 templates, plus at least 6 news stories.** No programme, campus or fee pages; those live on the admissions site.

### 3.1 Main pages (15)

| # | Page | Web address | What goes on it |
|---|---|---|---|
| 1 | Home | `/` | One-line mission; "Admissions 2027–28" band linking to the admissions site; **"Our Programmes" cards that open the admissions site (§3a)**; latest 3 news items; the 4 partner universities; research highlights; leadership; one fact strip (numbers from the fact sheet only) |
| 2 | About ITHS | `/about/` | Story, founding year, mission and vision, how the university collaboration works (wording approved by counsel), values |
| 3 | Leadership | `/leadership/` | Founder, Director and programme heads, with short bios |
| 4 | Founder profile | `/leadership/jyoti-garhewal/` | Qualifications, research, awards (exact name, issuer, year) |
| 5 | Director profile | `/leadership/pulakes-purkait/` | Qualifications, ORCID, publications, patent applications with numbers, awards |
| 6 | Faculty | `/faculty/` | Faculty by campus and subject, with qualifications and photos |
| 7 | Partner universities | `/partners/` | RBU Mohali, RBPU Hoshiarpur, BU Shimla, SGSU Bhopal: what each awards, the campus, approvals, and a link to each campus page on the admissions site |
| 8 | Research | `/research/` | Research areas, labs, patent applications (numbers and dates) |
| 9 | Publications | `/research/publications/` | Full list with DOIs (from ORCID) |
| 10 | Achievements | `/achievements/` | Awards, student achievements (with consent), milestones by year |
| 11 | News | `/news/` | All announcements, newest first, filterable by category and campus |
| 12 | Events | `/events/` | Conferences, workshops, guest lectures; upcoming and past |
| 13 | Media kit | `/media/` | Logos, fact sheet, approved short description, leadership photos, press contact, press coverage |
| 14 | Careers | `/careers/` | Open roles and the application form (moved from the old site) |
| 15 | Contact | `/contact-us/` | Institute office, partnerships, media; admission numbers point to the admissions site |

### 3.2 Policy pages (3)

| # | Page | Web address |
|---|---|---|
| 16 | Privacy policy | `/privacy-policy/` |
| 17 | Terms of use | `/terms/` |
| 18 | Grievance redressal | `/grievance-redressal/` (grievance officer; links to each university's grievance and anti-ragging pages) |

### 3.3 Templates (designed once, reused)

| Template | Used for |
|---|---|
| News story | Every announcement (headline, date, place, 150–400 words, 2–6 real photos) |
| Event | Every event (date, venue, speakers, registration link, photos after the event) |
| Thank-you | After a contact or careers form (hidden from Google) |
| 404 | Page not found, with links to Home, News and Admissions |

### 3.4 News at launch (at least 6 stories)

- The 5 existing news posts move from the old site, each with a 301 from its old address: Aashakiran IVF Centre visit, Teachers' Day 2026, Orientation 2026, Talent Hunt prize, Nutrition Week 2026.
- At least 1 new story, for example "ITHS launches its official website" or a 2027–28 session announcement.

### 3.5 Later (after the season, optional)

About 4–8 more pages, only if there is real content for them:
- a page for each research area;
- an annual report;
- alumni;
- a page for each partner university;
- a page for each convocation or conference.

## 3a. The "Our Programmes" section on the home page: where each click goes

The home page shows one card per programme. **Every card opens the matching page on the admissions website**, in the same tab. There is no course page on ithsedu.in, so there is nothing to duplicate, and every enquiry still lands in one place.

**Example:** a visitor on ithsedu.in clicks **Clinical Embryology** → `https://www.translationalhealthscience.in/programs/clinical-embryology/` → chooses a level (BSc, MSc, PhD, PG Diploma) and a campus → enquiry form → the campus counsellor calls within 24 hours.

**What each card shows:**
- programme name;
- a 1–2 line description;
- the levels, as small links;
- the campuses where it runs, and the awarding universities;
- a button "View course & apply →", with the small note "opens our admissions website".

| Card on ithsedu.in | Main button goes to | Level links |
|---|---|---|
| Clinical Embryology (ART) | `/programs/clinical-embryology/` | BSc `/programs/clinical-embryology/bsc/` · MSc `/msc/` · PhD `/phd/` · PG Diploma `/pgd-clinical-embryology/` |
| Nutrigenetics & Personalised Nutrition | `/programs/nutrigenetics-personalized-nutrition/` | BSc `/bsc/` · MSc `/msc/` |
| Stem Cell & Regenerative Medicine | `/programs/stem-cell-regenerative-medicine/` | BSc `/bsc/` · MSc `/msc/` |
| Cancer Biology | `/programs/cancer-biology/` | BSc `/bsc/` · MSc `/msc/` |
| B.Tech Stem Cell & Tissue Engineering | `/programs/b-tech-stem-cell-tissue-engineering/` | – |
| Molecular Medicine | `/molecular-medicine/` | BSc `/molecular-medicine/bsc-molecular-medicine/` · MSc `/molecular-medicine/msc-molecular-medicine/` |
| Neuroscience | `/msc-neuroscience/` | – |
| Anthropology | Only if D13 confirms it is offered | – |
| "View all programmes" | `/programs/` | – |

All addresses are on `https://www.translationalhealthscience.in` (all checked live on 28 Nov 2026).

**Rules for these links:**
1. **Same tab, not a new tab.** On phones (76% of visitors), new tabs confuse people. The admissions site has the same logo and colours and a slim line "Official website: ithsedu.in" at the top, so the visitor knows they are still with ITHS and can go back.
2. **No UTM tags on these links.** Both sites share one GA4 setup with cross-domain measurement, so the visit counts as one journey from ithsedu.in to the enquiry. UTM tags between our own sites would break that.
3. **Track the click.** A GA4 event `programme_click` with the programme name, so we can see which cards send applicants.
4. **Normal links** (no `nofollow`), with descriptive text ("Clinical Embryology: BSc, MSc, PhD, PG Diploma"). This passes trust from the official site to the course pages.
5. **One source of truth for facts.** Card text (levels, campuses) comes from the fact sheet and must match the admissions site.

The header button **"Programmes & Admissions"** goes to `/programs/`. The **Partner universities** page links each university to its campus page (`/campuses/mohali/`, `/campuses/hoshiarpur/`, `/campuses/shimla/`, `/campuses/bhopal/`).

## 4. Menu

- **Header:**
  - About ▾ (About ITHS, Leadership, Faculty)
  - Partners
  - Research ▾ (Research, Publications)
  - News & Events ▾ (News, Events, Achievements)
  - Careers
  - Contact
  - **[Programmes & Admissions]** button, which goes to the admissions site
- **Footer:**
  - quick links;
  - Media kit;
  - the three policy pages;
  - @ithsedu social links;
  - the address of the institute office;
  - the line "Admissions: translationalhealthscience.in".

## 5. How news gets published (the weekly routine)

1. **Something happens** at a campus (event, award, visit, result).
2. **The campus coordinator** posts it the same day on the campus social account. That is daily activity, and it stays there.
3. **Is it important for the whole institute?** For example, an award, a new collaboration, a result, a published paper, a patent application published, or a programme launch. If yes, the coordinator sends the central team, the same day:
   - 3–6 real photos;
   - who, what, where and when;
   - names, with photo consent.
4. **The central team** writes the news story (150–400 words) and checks it against the fact sheet and the claims checklist (no unproven "first", no placement percentages, the partner university named).
5. **Approval** by the Director's office within 24 hours.
6. **Publish** on ithsedu.in `/news/`.
7. **Share** on @ithsedu as an Instagram Collab post with the campus account, and on LinkedIn. Link to the news story, and to the admissions site only if the story is about admissions.

Target: **2–4 news stories a month**, and a short monthly roundup.

## 6. Building the website: the 10 steps

| Step | What happens | Who | By |
|---|---|---|---|
| 1 | Approve this page list and menu | ITHS leadership | 11 Dec 2026 |
| 2 | Send the content: fact sheet, leadership bios, faculty list, partner agreements wording, research list, patent application numbers, photos, logo files | ITHS team | 18 Dec 2026 |
| 3 | Wireframes (page layouts) for Home, About, Leadership profile, Partners, Research, News list and News story | TechnoTaau Team | 20 Dec 2026 |
| 4 | Visual design, matched to the ITHS logo and colours | TechnoTaau Team | 31 Dec 2026 |
| 5 | Write the copy for all 18 pages; SEO titles and descriptions | TechnoTaau Team; reviewed by Prof. Purkait | 10 Jan 2027 |
| 6 | Build in WordPress on a password-protected test site (demo.ithsedu.in) | Developer | 24 Jan 2027 |
| 7 | Review and corrections | ITHS team and TechnoTaau Team | 31 Jan 2027 |
| 8 | Pre-launch checks: speed, mobile, forms, structured data, Search Console, analytics across both sites, links to the admissions site | TechnoTaau Team and developer | 6 Feb 2027 |
| 9 | Launch: remove the temporary redirect; move Careers and News with 301s; update social bios | Developer | **Tue 9 Feb 2027** (to be confirmed) |
| 10 | After launch: weekly checks for 8 weeks; 2–4 news stories a month | TechnoTaau Team and central team | From 10 Feb 2027 |

## 7. Content checklist from the ITHS team

- [ ] Fact sheet (official name, founding year, campus count, addresses with PIN, phones, emails)
- [ ] Mission and vision text, and the history in 5–8 milestones with years
- [ ] Bios and photos: Founder, Director, programme heads
- [ ] Faculty list per campus (name, qualification, subject, photo)
- [ ] For each university: the approved description of the collaboration, which degrees it awards, logo use permission
- [ ] Research areas; publications (ORCID links); patent application numbers and dates
- [ ] Awards with exact name, issuer and year
- [ ] Real photos: labs, campuses, events (with consent)
- [ ] Open job roles
- [ ] Grievance officer name and contact
- [ ] Logo files (SVG or high-resolution PNG)

## 8. Rules for ithsedu.in

1. Never copy programme, campus, fee or admission pages. Link to the admissions site.
2. No claims without proof: no "No. 1", no unproven "first" or "only", and no placement or salary figures on this site.
3. "Patent applications" with numbers, never "patents" unless they are granted.
4. Name the degree-awarding university whenever a programme is mentioned.
5. Do not call ITHS a university until it has that status.
6. Real photos only, with consent (a parent's consent for anyone under 18). Label any AI-made image, and never show AI-made people.
7. Keep the test site password-protected and hidden from Google.

*Prepared by TechnoTaau Team. Sign-off: Jakhar Singh.*
