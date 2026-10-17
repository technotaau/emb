# EmbryoGenesis: Search, Answer-Engine and AI-Visibility Landscape 2026 (SEO, AEO, GEO)

**Prepared by:** TechnoTaau Team (search strategy research; project lead: Jakhar Singh)
**Client:** EmbryoGenesis, Mohali, Punjab (https://embryogenesis.in)
**Date:** 17 October 2026 | **Version:** 1.0
**Read with:**
- `docs/00-project-brief.md`. Section 0 applies: the old site content stays as it is, only the design changes, and the B2B copy is parked.
- `docs/research/01-industry-research.md` (compliance detail).
- `docs/strategy/02-seo-strategy.md` (technical specification).

**Method and limits**
- Web research on 17 Oct 2026. Every URL in the source list (section 7) was accessed on **17 Oct 2026** unless the entry says otherwise. In-text references such as (G2) or (I1) point to that list.
- Primary sources come first: Google Search Central and Help Center; OpenAI, Anthropic, Perplexity and Microsoft documentation; statutes. The NMC public notice of 6 Oct 2026 was read page by page from the scanned PDF published on nmc.org.in.
- Studies by SEO and analytics vendors (Ahrefs, SE Ranking, Seer, Profound, Whitespark, SparkToro/Gumshoe) are labelled **vendor study**. They show correlation, not cause.
- Labels used:
  - **[SECONDARY]**: taken from a news report, law-firm note or blog, not the primary text.
  - **[UNVERIFIED]**: could not be confirmed.
  - **[VERIFY with counsel]**: a legal reading that needs a lawyer.
- No keyword-volume tool and no AI-tracking tool was used. Every number is as published by the cited source.
- Some pages could not be read:
  - help.openai.com and one Search Engine Land article returned 403;
  - Bing help pages rendered empty;
  - two Google blog posts returned only navigation.
  In each case a mirror or secondary report is cited and labelled.
- **Scope note:** under brief section 0, the compliance points here are TechnoTaau Team recommendations. They do not change page content unless the client asks. Items outside page copy are within our remit: robots.txt, llms.txt, schema, Search Console, Bing, GA4 and the Google Business Profile.

---

## Contents

0. Executive summary: what this means for EmbryoGenesis
1. Google Search for YMYL health queries
2. Answer engines and generative engines
3. Measurement
4. India compliance for online medical and fertility marketing
5. Local SEO in India
6. Updates needed in existing TechnoTaau documents, and facts not verified
7. Sources

---

## 0. Executive summary: what this means for EmbryoGenesis

1. **AI search on Google is still Google SEO.** Google's guide of 15 May 2026 says AI Overviews and AI Mode use Google's core ranking and quality systems. It also says llms.txt, "chunking", AI-specific rewrites and extra structured data are not needed (G2). For EmbryoGenesis, the technical spec we already have, plus original and reviewed content, *is* the AI plan. A separate "GEO" budget for Google is not justified.

2. **Informational health queries give fewer clicks, so being cited is the new unit of visibility.** Pew tracked US users in March 2025:
   - visits to pages with an AI summary led to a click on a result 8% of the time, against 15% without a summary;
   - only 1% of those visits clicked a source cited inside the summary (R2).

   Report citations and branded demand alongside organic sessions.

3. **FAQ rich results have been gone for every site since 7 May 2026.** HowTo and Course info results are gone too (G5, G7). FAQ sections still help readers, but they earn no search feature. `02-seo-strategy.md` section 6 needs a small update (section 6.1 below).

4. **YouTube and third-party mentions matter more than on-page tweaks.**
   - YouTube is the most-cited domain in AI Overviews (R3). In German health queries it was the single most-cited domain (R8).
   - In Ahrefs' study of 75,000 brands, branded web mentions had the strongest correlation with brand visibility in AI Overviews: 0.664 (R4).

   EmbryoGenesis's gap is corroboration of the brand as an entity, not markup. Universities, partner hospitals, the IFS, press, ORCID and PubMed are where that corroboration comes from.

5. **The llms.txt on the built site is a compliance risk with no proven benefit.**
   - Google Search does not use llms.txt (G2).
   - In Ahrefs' log study, 97% of llms.txt files got no requests in May 2026 (R6).
   - `site/src/llms.txt` tells AI systems that "Stem Cell Therapy" and four other therapies are "given at the Mohali centre". The NMC advisory of 5 Sep 2026 says promoting stem cell therapy beyond approved indications is professional misconduct (I3).

   **Remove the therapy lines, or the whole file, before launch.**

6. **The NMC guidelines of 6 Oct 2026 limit the social plan.** We verified them from the primary notice (I1):
   - AI-generated promotional campaigns are prohibited, and any permitted AI content must state that it comes from AI;
   - synthetic patients, doctors and endorsements are banned;
   - testimonials are banned even with patient consent;
   - reviews must not be solicited, bought or manipulated for promotion;
   - electronic-media posts by clinical establishments "should" name the registered doctor (RMP) with qualifications, registration status and SMR/NMR registration number.

   The planned "informative AI-produced reels" need legal sign-off and a strictly educational, labelled format.

7. **The B2B collection-centre model has a new legal edge.** Clause 8.1(vii) bars any RMP from paying or receiving a commission, referral fee or lead-generation fee connected with the referral of patients **or specimens** for diagnosis (I1). Counsel must check partner terms and any future "Become a partner" copy. Never advertise per-sample incentives. **[VERIFY with counsel]**

8. **AI visibility can now be measured; set it up at launch.**
   - Search Console's Generative AI performance report gives AI Overviews and AI Mode impressions (G4).
   - Bing's AI Performance report gives citations, grounding queries and citation share (M1, M2).
   - GA4 added a native "AI Assistant" channel on 13 May 2026 (GA1) **[SECONDARY]**.

   AI answers rarely repeat (R11), so run each panel prompt 3 times per surface and report visibility %, not rank.

9. **The Google Business Profile is the main local asset, but common review tactics are banned for EmbryoGenesis.** Google bans incentivised reviews, selectively solicited reviews and reviews from people with a conflict of interest (G15). The NMC bans soliciting or manipulating reviews to promote medical services (I1). In practice:
   - set up the profile with the real-world name, an accurate category and the single phone number;
   - run no review campaigns aimed at patients or partner clinics;
   - never confirm in a reply that someone was a patient.

10. **DPDP's main obligations start in mid-May 2027 (13 or 14 May, depending on the source; check the Gazette).** MeitY proposed bringing this forward to November 2026, but we found no notification as of September 2026 (I12). Build forms and analytics to the consent standard now:
    - unticked consent box and an itemised notice;
    - parental consent for minors;
    - no health data in ad pixels;
    - no personalised ads to under-18s. Google already makes them ineligible (G18).

---

## 1. Google Search for YMYL health queries

### 1.1 AI Overviews and AI Mode: how sources are selected and cited

**What Google says (primary sources)**

| Topic | What Google states | Source |
|---|---|---|
| Underlying system | AI Overviews and AI Mode "rely on Google's core ranking and quality systems". They use grounding (retrieval-augmented generation) on the Search index plus "query fan-out": several related searches across subtopics while the answer is built. AI Mode and AI Overviews may use different models, so their links differ. | G1 (updated 10 Dec 2025), G2 (published 15 May 2026, updated 10 Jul 2026) |
| Eligibility | A page must be indexed and "eligible to be shown in Google Search with a snippet". There are "no additional requirements" and no "special optimizations". Indexing and serving are not guaranteed. | G1 |
| Site-level switch | A site must be "included in Search generative AI features in Search Console". The default is *Include*. The control reached all sites worldwide by 31 Aug 2026. Excluding a site removes its AI impressions and traffic. It is not a ranking signal for the rest of Search and does not affect AI training (Google-Extended controls training). | G2, G3 |
| Page-level controls | `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex` limit what appears. | G1 |
| What helps | Non-commodity content that adds a unique point of view or first-hand experience. Clear headings and sections. Relevant images and video. Crawlable, semantic HTML. Good page experience. Less duplication. A current Business Profile for local businesses. | G2 |
| What Google says is unnecessary ("mythbusting") | llms.txt, AI text files, special markup or Markdown copies ("Google Search itself doesn't use them"); "chunking" content ("There's no ideal page length"); rewriting content for AI; chasing inauthentic "mentions"; over-focusing on structured data ("Structured data isn't required for generative AI search"). | G2 |
| Spam | Mass-producing pages for query variations falls under the scaled content abuse policy. Since 15 May 2026, spam policies explicitly cover generative AI responses. | G2, G5 |
| Click quality (Google's claim) | Google says clicks from AI Overview pages "tend to be higher quality". This is Google's own statement, not independent data. | G1 |

**What independent and vendor studies show about who gets cited**

| Finding | Evidence type | Source |
|---|---|---|
| Ahrefs analysed 863K SERPs and 4M AI Overview URLs (2 Mar 2026). For the same query, only **37.9%** of cited URLs ranked in the top 10; **31.2%** ranked 11–100 and **31.0%** ranked below 100. A July 2025 study found 76%, but Ahrefs changed its parsing method, so the two figures are not a clean trend. AI Overviews have run on Gemini 3 since Jan 2026. Likely reading: pages are cited for the fan-out sub-questions, not only for the head query. | Vendor study | R3 |
| YouTube is the most-cited domain in AI Overviews. Of cited pages that rank outside the top 100, 18.2% are YouTube URLs. | Vendor study | R3 |
| SE Ranking, German-language health searches (Dec 2025 snapshot; 50,807 prompts; 465,823 citations): AI Overviews showed on **more than 82%** of health searches. YouTube was the top cited domain at **4.43%**. Government and academic sources together made about **1%**, and the authors' "more reliable" group about **34%**. Germany only; we found no equivalent India data. | Vendor study | R8 |
| Pew (US, browsing data from 900 adults, Mar 2025):<br>• clicks on a traditional result: **8%** of visits with an AI summary vs **15%** without;<br>• clicks on a link inside the summary: **1%**;<br>• browsing ended on the page: **26%** vs **16%**;<br>• .gov sites: **6%** of AI summary sources vs **2%** of standard results. | Independent research | R2 |
| Seer (3,119 informational queries, 42 organisations, published 4 Nov 2025):<br>• organic CTR on queries with an AI Overview: **0.70%** when the brand was cited vs **0.52%** when not;<br>• queries without an AI Overview: **1.45%**;<br>• all were down sharply year on year.<br>Seer says it "cannot definitively prove that citation causes higher CTRs". | Vendor study | R10 |
| Health accuracy: a Guardian investigation (11 Jan 2026) reported wrong liver-test reference ranges. Google removed AI Overviews for some of those queries, and said many flagged answers were supported by high-quality sites. | News **[SECONDARY]** | R12 |

**India availability**
- AI Overviews have been live in India since August 2024, in English and Hindi (G19).
- AI Mode in India **[SECONDARY]** (G20):
  - opened in Search Labs on 24 Jun 2025;
  - reached all users in English in early July 2025;
  - added Hindi in September 2025;
  - added seven more Indian languages in October 2025.

**Preferred sources**
- On 27 May 2026 Google added the "preferred sources" feature to AI Overviews and AI Mode (G5).
- It lets users favour sources they choose. It matters mostly for news publishers and is low relevance for a lab.

### 1.2 Rich results and structured data: 2025–26 changes

| Feature | Status in Oct 2026 | Key dates | Source |
|---|---|---|---|
| **FAQ rich result** | **Not shown for any site.** Documentation removed. | Aug 2023: limited to "well-known, authoritative government and health websites".<br>7 May 2026: stopped appearing.<br>15 Jun 2026: docs removed.<br>Search Console report and Rich Results Test support: removed Jun 2026.<br>Search Console API support: removed Aug 2026. | G5 (log entries 8 May and 15 Jun 2026), G8, R13a |
| HowTo rich result | Removed | Announced Aug 2023. We could not retrieve the post body. HowTo is absent from the current Search Gallery. | G8, G7, R13a |
| Course info | Removed (*Course list* remains) | Deprecation banner Jun 2025; docs removed 9 Sep 2025 | G5, G7 |
| Estimated salary, learning video, special announcement, vehicle listing | Removed | Docs removed 9 Sep 2025 | G5 |
| ClaimReview, book actions | Deprecation banners added Jun 2025 (later changes in the log are not relevant here) | 12 Jun 2025 | G5 |
| Practice problem | Removed | Docs removed 6 Jan 2026 | G5 |
| **Still supported and relevant to EmbryoGenesis** | Organization, Local business, Breadcrumb, Article, Event, Course list, Profile page, Video, Image metadata. Q&A and Discussion forum exist but do not fit our pages. | Search Gallery updated 16 Oct 2026 | G7 |
| MedicalWebPage, MedicalTest, DiagnosticLab, MedicalBusiness | Valid schema.org types. **No Google rich result** is attached to them. | n/a | G7 (not listed) |

**Two platforms, two views on markup**
- **Google:** structured data is not required for AI features. Keep it for rich-result eligibility, and keep it consistent with the visible text (G1, G2).
- **Microsoft Bing:** AI answers are assembled from page sections. Bing recommends:
  - schema markup (JSON-LD);
  - question-and-answer pairs and tables;
  - "self-contained" one- or two-sentence answers.

  It advises against hiding key answers in tabs, PDFs or images (M3).
- These views do not conflict for us. Clear sections and tables help readers, Bing and Google. The only things to avoid are fragmenting content into thin pages and adding markup that does not match the visible text.

### 1.3 Helpful content, E-E-A-T, quality raters and site reputation

- **People-first content** (G9; updated 5 Oct 2026):
  - "trust is most important" among the E-E-A-T aspects;
  - Google gives extra weight to strong E-E-A-T on "Your Money or Your Life" (YMYL) topics, including health;
  - authorship should be clear, with bylines where readers expect them;
  - automation should be disclosed where readers might ask "How was this created?";
  - fabricated creator profiles, such as made-up names or AI headshots, are treated as deception.
- **Generative AI content** (G10; updated 1 Oct 2026):
  - AI-assisted content must meet Search Essentials and the spam policies, especially scaled content abuse;
  - output must be fact-checked, including titles, meta descriptions, structured data and alt text;
  - the page points to rater guideline sections 4.6.5 (scaled content abuse) and 4.6.6 (low effort and originality).
- **Quality Rater Guidelines:**
  - last revised on 11 Sep 2025: YMYL clarifications and AI Overview examples. Google called it a minor update (R16).
  - We found no 2026 revision **[UNVERIFIED that none exists]**.
  - Raters do not directly change rankings.
- **Site reputation abuse:**
  - policy text clarified in Jan 2025;
  - updated on 28 Aug 2026 with "adjusted" enforcement in the European Economic Area (G5, G12; post body not retrieved).
  - Relevance to EmbryoGenesis is low. It would matter only if EmbryoGenesis content were hosted on another site to borrow its ranking strength, or the reverse. Paid "advertorials" on news or university sites are one example.
- **Helpful content updates:** none appears in the 2025–26 Search Status Dashboard or the documentation log (G5, G11). On 9 Dec 2025 Google added a section explaining that it also makes "smaller core updates" continuously (G5).

### 1.4 Core and spam updates, 2025–26

Source: Google Search Status Dashboard (G11). End dates are worked out from the duration the dashboard states.

| Update | Type | Start | Rollout complete (approx.) |
|---|---|---|---|
| March 2025 core update | Core | 13 Mar 2025 | 26–27 Mar 2025 |
| June 2025 core update | Core | 30 Jun 2025 | 16–17 Jul 2025 |
| August 2025 spam update | Spam | 26 Aug 2025 | 21–22 Sep 2025 |
| December 2025 core update | Core | 11 Dec 2025 | 29 Dec 2025 |
| February 2026 Discover update | Discover | 5 Feb 2026 | 26 Feb 2026 |
| March 2026 spam update | Spam | 24 Mar 2026 | 25 Mar 2026 |
| March 2026 core update | Core | 27 Mar 2026 | 8 Apr 2026 |
| May 2026 core update | Core | 21 May 2026 | 1–2 Jun 2026 |
| June 2026 spam update | Spam | 24 Jun 2026 | 26 Jun 2026 |
| August 2026 spam update | Spam | 18 Aug 2026 | 20 Aug 2026 |
| September 2026 spam update | Spam | 24 Sep 2026 | 7 Oct 2026 |

- Google has not said that any of these updates targeted health sites.
- Blog claims that the May 2026 core update hit health and other YMYL sites hardest are third-party analysis **[SECONDARY]**.
- The planned launch (17 Nov 2026 in `02-seo-strategy.md` section 9) falls after the last listed update. A new core update could start at any time.

### 1.5 Google Business Profile ranking factors for local medical and lab businesses

- **Google's own statement** (G13): local results depend on **relevance, distance and prominence**.
  - Prominence includes links and reviews: "More reviews and positive ratings can help your business's local ranking."
  - Replying to reviews is recommended.
  - "There's no way to request or pay for a better local ranking."
- **Guidelines that matter for a lab inside a university campus** (G14):
  - **Name:** use the real-world name on signage and stationery. "Including unnecessary information in your business name isn't permitted."
  - **Departments inside institutions:** "Publicly-facing departments that operate as distinct entities should have their own page", with a name distinct from the institution's.
  - **Locations:** one profile per location. No virtual offices.
  - **Practitioners:** doctors may have their own profiles only if they are public-facing and can be contacted at the verified location during stated hours.
  - **Categories:** "the fewest number of categories". Use the "This business IS a" test, not "HAS a".
  - **Phone:** the number must be under the business's direct control.
- **Expert survey: Whitespark Local Search Ranking Factors, 2026 edition** (R14; published 6 Nov 2025; 47 experts scored 187 factors).
  - Top local-pack factors:
    1. primary GBP category;
    2. proximity of the address to the searcher;
    3. keywords in the GBP business title;
    4. physical address in the city searched;
    5. business open at the time of search.
  - Review signals and behavioural signals rose in importance.
  - Citations lost about half a percentage point for local search. The author argues that mentions ("citations") matter more for AI search visibility. The top AI-visibility factor was "presence of business on expert curated best-of and similar lists".
  - Group weightings such as "GBP signals about 32%" appear only in secondary summaries **[SECONDARY]**.
  - This is a survey of expert opinion, not a measurement.
  - **Caution:** "keywords in the business title" is a strong factor in the survey, but it breaks Google's guidelines (G14). For a medical business it would also arguably breach NMC clause 8.1(xii) on manipulating visibility (section 4). Do not use it.
- **AI answers:** Google's AI guide tells local businesses to keep Business Profile data current so they appear in AI responses (G2). Bing gives the same advice for Bing Places (M1).
- **India-specific evidence:** we found no India-specific study of local ranking factors **[UNVERIFIED]**. Google tested its fake-review warning labels in the US, UK and India before a global rollout **[SECONDARY]** (G22).

### Implications for EmbryoGenesis

1. **No separate "AEO/GEO" work for Google.** The levers Google names are what `02-seo-strategy.md` sections 4–6 already cover:
   - indexable, server-rendered HTML;
   - bylines and reviewer credentials;
   - named and dated references;
   - "Reviewed on" dates;
   - real images and video;
   - a clean technical base.
2. **Original, non-commodity content is the only lever Google names.** EmbryoGenesis has original material that big chains do not:
   - biopsy timing and sample transport protocols;
   - report-interpretation guidance;
   - method descriptions for its own tests;
   - patent-application facts;
   - the founder's publications.

   Under brief section 0 these are future additions. For now, keep the kept pages indexable, accurate and free of the claims flagged in `01-industry-research.md`.
3. **Structured data, for the developer:**
   - Keep Organization (`DiagnosticLab` + `MedicalBusiness`), BreadcrumbList, Article/BlogPosting, Person/ProfilePage, Event (CME), Course/EducationalOccupationalProgram and VideoObject.
   - FAQPage is now optional. It earns no rich result. Keep it only where it is already templated and matches a visible FAQ.
   - Do not add review or rating markup. There are no compliant first-party reviews to mark up (NMC ban on testimonials, section 4).
4. **Leave the Search Console "Search generative AI features" control on *Include*.** Excluding the site would remove it from AI Overviews and AI Mode for no benefit (G3).
5. **Video is the format with the most evidence.** Short educational videos by named, qualified staff, with transcripts on the matching page, are the main new format worth considering. Examples: what a biopsy-based test can and cannot tell; timing of the biopsy. They must follow the NMC rules in section 4 and need client approval, since they are new content.
6. **Biggest YMYL risk in the kept content:** the therapies page (`/advanced-fertility-therapies/`) and the LIT blog post. Google's YMYL standard and the NMC rules (section 4) are strictest on unproven treatments. Our recommendation, pending the client's legal review:
   - noindex the page, or put it back to draft;
   - remove it from llms.txt and from any machine-readable summaries now.
7. **Rank changes around core-update dates** should be read against the dashboard (G11) before anyone reacts to them.

---

## 2. Answer engines and generative engines

### 2.1 How each engine finds and cites sources

| Engine | Where its sources come from | What is documented about selection | Source |
|---|---|---|---|
| **ChatGPT search** | OpenAI's own crawl by **OAI-SearchBot**, plus third-party search providers. OpenAI rewrites the user's prompt into one or more targeted queries and may send follow-up queries. It shares general location, inferred from IP, with providers. Bing and Shopify are the providers named in OpenAI's documentation, and OpenAI states that Bing is the only third-party provider for Enterprise and Edu workspaces (both as quoted by Semrush, O4) **[SECONDARY]**. Experiments in 2025 suggested some paid tiers also retrieve Google results **[SECONDARY]**. | Not disclosed beyond "any public website can appear". A site that blocks OAI-SearchBot will not be shown in ChatGPT search answers, though it can still appear as a navigational link. ChatGPT adds `utm_source=chatgpt.com` to referral links. | O1, O2, O3 (mirror; the help.openai.com page returned 403), O4 |
| **Perplexity** | Its own index built by **PerplexityBot**, which is "not used to crawl content for AI foundation models". **Perplexity-User** fetches pages live for a user and "generally ignores robots.txt rules". | Ranking method not published. Claims about rerankers and score thresholds on SEO blogs are unverified. | P1 |
| **Google Gemini app** | Grounding on Google Search when the model decides to search. **Google-Extended** controls both training of future Gemini models and supplying Search-index content to the Gemini apps and Vertex AI at prompt time. It "does not impact a site's inclusion in Google Search". | No first-party data on which domains Gemini cites. Vendor trackers disagree widely **[SECONDARY]**. | G16 |
| **Claude** | **Claude-SearchBot** indexes for search quality, **Claude-User** fetches for a user's question and **ClaudeBot** collects training data. Each obeys robots.txt and supports Crawl-delay. Claude's web search was reported in Mar 2025 to use Brave Search, which Anthropic lists as a subprocessor **[SECONDARY]**. | Not disclosed. | A1, A2 |
| **Microsoft Copilot / Bing** | The Bing index. Microsoft's AI Performance report covers citations in Copilot, Bing AI summaries and "select partner integrations". | Microsoft guidance favours sections that are clear, structured and self-contained, claims backed by data, fresh content (notify with IndexNow) and consistent entities (M1, M3). | M1, M2, M3 |

### 2.2 What is known about getting cited: studies, not hype

| Claim often made | What the evidence says | Strength | Source |
|---|---|---|---|
| Adding statistics, quotations and citations increases visibility | **GEO paper** (Aggarwal et al., KDD 2024). It tested 9 methods. The best (Quotation Addition, Statistics Addition, Cite Sources) improved a position-adjusted visibility measure by about **40%** in a GPT-3.5 pipeline built on top-5 Google results. Keyword stuffing performed below baseline. Sources ranked 5th gained most; top-ranked sources lost some visibility. A smaller check on Perplexity (200 queries) showed smaller but positive effects. Limitations: a lab pipeline, early-generation models, automatic labels. | Peer-reviewed, but experimental and dated | R1 |
| Brand mentions drive AI visibility | **Ahrefs, 75K brands (26 May 2025).** Spearman correlations with brand visibility in AI Overviews:<br>• branded web mentions **0.664**<br>• branded anchors **0.527**<br>• branded search volume **0.392**<br>• Domain Rating **0.326**<br>• backlinks **0.218**<br>• number of pages **0.17**<br>Only domains with DR above 40 were included, so the result may not hold for small brands. | Vendor study, correlation | R4 |
| Fresh content is cited more | **Ahrefs, about 17M citations (28 Jul 2025).** AI assistants cite newer pages than organic results do; ChatGPT citations average about **458 days newer**. Google AI Overviews cite slightly *older* pages than organic results. The average cited page is still about **2.9 years old**. Correlation only. | Vendor study | R5 |
| Wikipedia and Reddit dominate | **Profound, 680M citations (Aug 2024 – Jun 2025), all industries.**<br>• Wikipedia: **7.8%** of all ChatGPT citations (47.9% of ChatGPT's top-10-domain share).<br>• Reddit: **2.2%** of AI Overview citations and **6.6%** of Perplexity citations.<br>• YouTube: **1.9%** of AI Overview citations.<br>The widely quoted "47.9%" is a share of the top 10 domains, not of all citations. | Vendor study | R7 |
| Health answers favour institutions | **Jacques et al. (arXiv, 23 Jan 2026).** 100 consumer health questions in ChatGPT 5.2 Pro produced 615 citations. More than three-quarters came from established institutions such as Mayo Clinic, Cleveland Clinic, the NHS, PubMed and Wikipedia. The authors propose an "Authority Signals" framework: author credentials, institutional affiliation, quality assurance and digital authority. Preprint; one engine. | Academic preprint | R9 |
| AI rankings can be tracked like Google rankings | **SparkToro and Gumshoe (published 30 Jan 2026; 2,961 prompts).** ChatGPT and Google's AI had less than a 1-in-100 chance of returning the same brand list twice. The same list *in the same order* appeared less than 0.1% of the time. How often a brand appears across runs ("visibility %") was more stable, and tight, niche markets were more stable than broad ones. Not peer-reviewed; Gumshoe sells tracking tools. | Vendor-partnered study | R11 |
| Structure the page as Q&A "chunks" | **Microsoft** recommends question-style headings, Q&A pairs, tables and self-contained sentences (M3). **Google** says chunking is unnecessary (G2). Write clear sections for readers; do not split content into thin pages. | Official guidance (both) | M3, G2 |

**Wikipedia, Wikidata, Reddit, Quora and YouTube: practical position**
- **Wikipedia.** Editors with a conflict of interest are "strongly discouraged from editing affected articles directly". They may propose changes on talk pages. Paid editors "must disclose who is paying them" (R15).
  - In our judgement EmbryoGenesis does not yet meet Wikipedia's notability bar (a lab founded in Nov 2023, with limited independent coverage).
  - Do not create or commission an article.
- **Wikidata.** An item qualifies if it refers to "a clearly identifiable conceptual or material entity" that serious, publicly available references can support (R16a).
  - Items for the organisation and the founder look feasible. References could include the Times of India item of 3 Jul 2024, ORCID and IP India application records.
  - Keep them strictly factual and declare the conflict of interest.
  - We found no study showing that a Wikidata item increases AI citations for a small organisation **[UNVERIFIED benefit]**. Treat it as low-cost entity hygiene.
- **Reddit and Quora.**
  - Perplexity and AI Overviews cite them often (R7).
  - Google says chasing inauthentic mentions "isn't as helpful as it might seem" (G2).
  - The NMC bars using third parties to do indirectly what is prohibited directly, and bars causing any third party to manipulate engagement (I1, clauses 8.1(xi) and (xii)).
  - **No seeding, no paid posts, no staff posting without disclosure.** Named experts may answer clinical questions under their real names with their affiliation disclosed, without self-promotion.
- **YouTube.**
  - It is the most-cited domain in AI Overviews (R3, R8).
  - Since Dec 2024, registered doctors and other licensed health professionals in India can apply for YouTube's health source information panels and health shelves (G21). Eligibility includes a licence check, health-information principles and a watch-time threshold. India thresholds may differ from the global help page **[UNVERIFIED]**.
  - A channel with educational videos by an RMP is possible, but NMC clause 9.2 (RMP photos as self-advertisement) and clause 5.1 (education that does not promote personal practice) apply.

### 2.3 llms.txt: status of adoption

| Evidence | Finding | Source |
|---|---|---|
| Google | Google Search does not use llms.txt. Google clarified this on 15 Jun 2026: the file is not needed for Search; it may be crawled like any file; it neither helps nor hurts. | G2, G5 |
| Ahrefs log study (published 15 Jun 2026) | Of 137,210 domains with traffic in May 2026, **28%** published an llms.txt (likely an upper bound; the sample skews technical). **97%** of those files got **no requests** that month. AI retrieval bots such as OAI-SearchBot and PerplexityBot made only **1.1%** of requests. The main readers were SEO audit tools, unidentified bots and coding agents. | R6 |
| Other AI labs | We found **no statement from OpenAI, Anthropic, Perplexity or Microsoft** that their search or answer systems read llms.txt **[UNVERIFIED]**. | n/a |
| Lighthouse | Reported to check llms.txt in an *experimental* "agent readiness" audit **[SECONDARY]**. This relates to browser agents, not search ranking. | R17 |

**Verdict:** the evidence that llms.txt helps AI visibility is weak to nil. The file is harmless only if it is an exact, reviewed subset of facts already on the site. The current file is not: it lists held therapies (section 0, bullet 5).

### 2.4 Bot names and robots.txt controls

| User agent | Operator | Purpose | robots.txt | Effect of blocking | Source |
|---|---|---|---|---|---|
| Googlebot | Google | Search, including AI Overviews and AI Mode | Obeyed | Blocks Search *and* AI features | G1 |
| Google-Extended | Google | Gemini training, plus grounding in the Gemini apps and Vertex AI | Obeyed (token only, no separate crawler) | No effect on Google Search inclusion or ranking. Blocks Gemini training and app grounding. | G16 |
| Bingbot | Microsoft | Bing index, which feeds Copilot | Obeyed (Bing says it respects robots.txt) | Removes the site from Bing and Copilot answers | M1 |
| OAI-SearchBot | OpenAI | ChatGPT search index | Obeyed | Site not shown in ChatGPT search answers | O1 |
| GPTBot | OpenAI | Training data | Obeyed | Training opt-out only; no search effect | O1 |
| ChatGPT-User | OpenAI | User-initiated fetches | "robots.txt rules may not apply" | Not the search control | O1 |
| OAI-AdsBot | OpenAI | Checks landing pages of ChatGPT ads | Not stated | n/a (we run no ChatGPT ads) | O1 |
| ClaudeBot | Anthropic | Training data | Obeyed; Crawl-delay supported | Training opt-out | A1 |
| Claude-SearchBot | Anthropic | Search index | Obeyed | May reduce visibility in Claude search | A1 |
| Claude-User | Anthropic | User-initiated fetches | Obeyed | Stops user-directed retrieval | A1 |
| PerplexityBot | Perplexity | Search index (not training) | Obeyed; changes take up to 24 h | Removes the site from Perplexity results | P1 |
| Perplexity-User | Perplexity | User-initiated fetches | "Generally ignores robots.txt" | n/a | P1 |
| Applebot-Extended | Apple | Opt-out of Apple AI training | **[UNVERIFIED in this research]** | n/a | n/a |

**Built site check.** `site/dist/robots.txt` allows all of the above, plus `*`. That fits a visibility-first goal. One mismatch: it points to `/sitemap.xml`, while `02-seo-strategy.md` section 5.4 specifies `/sitemap_index.xml` (Rank Math). The developer must use whichever the WordPress build actually serves.

### 2.5 Bing Webmaster Tools and IndexNow: relevance for Copilot and ChatGPT

- **AI Performance report** (Bing Webmaster Tools; public preview since 10 Feb 2026; M1). It shows:
  - total citations;
  - average cited pages per day;
  - **grounding queries**, a sample of the phrases the AI used to retrieve your content;
  - page-level citation counts and trends.

  It does **not** show clicks or traffic. Later additions:
  - query-to-page mapping **[SECONDARY]** (M4);
  - on 16 Jun 2026, preview features **Intents**, **Topics**, **Citation Share** (your share of all citations for a grounding query) and **Compare** (M2).
- **Microsoft's guidance for being cited** (M1):
  - deepen topic coverage;
  - use clear headings, tables and FAQ sections;
  - support claims with data and sources;
  - keep content current and use **IndexNow** to notify changes;
  - keep entities consistent;
  - register with **Bing Places**.
- **IndexNow:**
  - It is a push protocol supported by Bing and some other engines. **Google does not participate** **[SECONDARY]** (M5).
  - No first-party source says IndexNow affects ChatGPT. OpenAI names Bing as *a* provider, not the only one (O4).
  - Treat IndexNow as a Bing and Copilot tool that may *indirectly* help ChatGPT. That benefit is unproven.
  - Rank Math reportedly offers IndexNow through its Instant Indexing module **[UNVERIFIED here; developer to confirm]**.

### Implications for EmbryoGenesis

1. **Keep every search and answer bot allowed.** Whether to opt out of AI training (GPTBot, ClaudeBot, Google-Extended) is a client decision (`{{AI_TRAINING_OPT_OUT}}` in 02-seo-strategy section 5.6). Note the trade-off: blocking **Google-Extended** also blocks grounding in the Gemini apps (G16). Our recommendation is to allow all.

   Before launch, check that the host's firewall or CDN bot protection is not blocking these agents. Some CDNs now block AI crawlers by default **[UNVERIFIED in this research; check the host settings]**.
2. **Set up Bing properly at launch:**
   - verify Bing Webmaster Tools;
   - submit the sitemap;
   - turn on IndexNow;
   - create a Bing Places listing;
   - read the AI Performance report monthly.

   This is the only first-party view of Copilot citations.
3. **Build entity corroboration, not markup.** Concrete targets, all factual and earned:
   - Rayat Bahra University and Bahra University programme pages that name EmbryoGenesis and its role;
   - partner hospital pages that name EmbryoGenesis as their sample-collection lab;
   - the Indian Fertility Society membership listing;
   - the founder's ORCID, Google Scholar and PubMed affiliations;
   - IP India records of the published applications;
   - the LinkedIn company page;
   - press coverage that uses the standard one-line description.

   Never buy mentions or "best lab" list placements. That would breach NMC clauses 8.1(ix), (xi) and (xii) (section 4) and Google's warning on inauthentic mentions (G2).
4. **Writing pattern for future content.** This matches `02-seo-strategy.md` section 8.1:
   - answer first, then detail;
   - tables for comparisons;
   - statistics only with a named, dated source (R1);
   - author and reviewer credentials visible (R9);
   - real "Reviewed on" dates.

   Do not change dates without changing content (R5).
5. **Wikipedia: no.** **Wikidata: optional,** as low-cost hygiene with the conflict of interest declared.
6. **llms.txt: before launch, remove the therapy statements from `site/src/llms.txt`, or delete the file.** Line numbers as of 17 Oct 2026:
   - line 3: "fertility therapies at the Mohali centre";
   - line 13: the therapy list, including Stem Cell Therapy;
   - line 28: the "Therapeutic services" link;
   - line 42: the LIT blog post;
   - line 24: soften "diagnostic and therapeutic services" to "diagnostic services".

   If the file stays, it must be regenerated from reviewed page facts whenever those change.
7. **No Reddit or Quora seeding.** Named, disclosed expert answers only.

---

## 3. Measurement

### 3.1 Tools that now exist

| Tool | What it measures | Limits | Source |
|---|---|---|---|
| **Search Console: Performance report (Web)** | AI Overview activity, and AI Mode activity since 16 Jun 2025, is counted inside the normal "Web" totals | Cannot be separated from classic results in this report | G1, G5 |
| **Search Console: Generative AI performance report** | **Impressions** of your links in AI Overviews and AI Mode, by page, country, date and device. Can be filtered to text-based or multimodal (Lens, Circle to Search) searches. Rolled out worldwide. | No clicks and no queries. Appears **only after enough AI impressions**. Discover has a separate report. 1,000-row table limit. | G4 |
| **Search Console: generative AI control** | Include or exclude the site from AI Overviews, AI Mode and Discover AI features | Default is Include. Changes take 1–2 days or longer. | G3 |
| **Bing Webmaster Tools: AI Performance** | Citations in Copilot, Bing AI summaries and partners; grounding queries; page-level counts; intents, topics, citation share (preview) | Sampled; no clicks or traffic; partner surfaces not named | M1, M2 |
| **GA4: "AI Assistant" default channel** (added 13 May 2026) | Sessions from recognised AI assistants get medium `ai-assistant`, channel "AI Assistant" and campaign `(ai-assistant)` | Google has not published the full referrer list; examples given are ChatGPT, Gemini and Claude **[SECONDARY]**. Visits from AI Overviews and AI Mode still count as Google organic. | GA1 |
| **ChatGPT UTM** | ChatGPT appends `utm_source=chatgpt.com` | Only when a link is clicked from ChatGPT | O3 |
| **Third-party AI visibility tools** (prompt-sampling trackers) | Mentions and citations across sampled prompts | Google: no third-party tool has access to its internal ranking or AI systems; judge their advice against official guidance (G2). Results vary run to run (R11). | G2, R11 |

**GA4 backstop.** Default channel groups cannot be edited, so keep a **custom channel group** with an "AI search" rule placed *above* Referral. Source regex:

```
(^|\.)(chatgpt\.com|openai\.com|perplexity\.ai|gemini\.google\.com|claude\.ai|copilot\.microsoft\.com)$
```

Review the referrer list quarterly in GA4 (Reports › Acquisition › Traffic acquisition, dimension "Session source"). Two limits apply:
- Some AI visits arrive with no referrer and land in Direct. Vendor estimates of how many vary widely **[UNVERIFIED]**.
- With Consent Mode set to "denied" by default (02-seo-strategy section 5.7), GA4 sees only consented sessions.

So every AI-referral figure is a floor, not a total.

### 3.2 Prompt panels: method fix

`02-seo-strategy.md` section 8.4 currently runs 20 prompts once a month on 5 surfaces. SparkToro's data shows that a single run is mostly noise (R11). Change the method to:

1. Run each prompt **3 times** per surface, each in a fresh logged-out session, from India.
2. Use 4 surfaces at minimum: ChatGPT (search on), Google AI Mode, Perplexity and Copilot. Add AI Overviews when it triggers and Gemini if time allows.
3. A prompt is **visible on a surface** if EmbryoGenesis is mentioned or cited in at least **2 of 3** runs.
4. The blueprint score stays: a prompt counts if it is visible on at least 2 surfaces. Targets are unchanged (0/20 → 3/20 at 3 months → 8/20 at 6 months).
5. Record for each run:
   - mentioned (Y/N);
   - URL cited;
   - facts correct, wrong or outdated;
   - compliance problems. For example, an AI calling a test "patented", calling the lab "best", or listing stem cell therapy.
6. Effort: 20 prompts × 4 surfaces × 3 runs = 240 checks a month, roughly half a day for one person (our estimate). A paid tracker is optional. Apply the same scepticism to it as to any sampled data.

### 3.3 Realistic KPIs (proposed; recalibrate after the first 30 days of data)

| KPI | Source | Realistic expectation for a small, new entity | Why |
|---|---|---|---|
| Branded demand: impressions and clicks for queries containing "embryogenesis" together with Mohali, ERFA, Purkait, test or lab | GSC | Upward trend from launch. Set a numeric target after a 30-day baseline. | The generic word "embryogenesis" pollutes the brand query (02 research, finding 1). Filter by modifier. |
| Brand prompts (#14–16 in the panel) visible with **correct facts** | Prompt panel | First wins. Aim for visible on at least 2 surfaces by month 3. | Navigational questions are where a small entity can win early. |
| Category and clinical prompts (#1–13, 17–20) | Prompt panel | Slow. Blueprint targets 3/20 at 3 months and 8/20 at 6 months overall. | These compete with chains, YouTube and Wikipedia (R3, R7, R8). |
| Pages with AI impressions | GSC Generative AI report | The report may not appear for months. That is not a failure. | It appears only after enough impressions (G4). |
| Copilot citations and cited pages | Bing AI Performance | At least 1 cited page by month 3 (our proposal). | First-party citation data |
| AI-referred sessions and key events (form submits, WhatsApp and call clicks) | GA4 AI Assistant + custom channel | Track only. Expect small numbers; report them as a floor. | Undercounting (section 3.1) |
| GBP actions: calls, direction requests, website clicks | GBP Performance | Track monthly from verification | Main local conversion signal |
| AI factual errors about EmbryoGenesis traced and fixed at source within 30 days | Prompt panel log | 100% (process KPI) | Accuracy matters more than volume for a YMYL brand |
| Compliance incidents (ASCI, NMC or platform complaints) | Log | Zero | Required |

**Not recommended as KPIs:** "rank position in ChatGPT" (unstable; R11); "share of traffic from AI" on its own (undercounted; section 3.1); raw totals of AI Overview impressions without page context.

### Implications for EmbryoGenesis

1. **Developer launch checklist:**
   - GSC verified as a domain property, with the generative AI control on Include;
   - Bing Webmaster Tools verified;
   - GA4 with the custom AI channel group added;
   - key events defined.
2. **The panel method changes** (3 runs, 2-of-3 rule). The blueprint KPI numbers stay the same.
3. **The monthly report** gets a short "AI visibility" block:
   - GSC Generative AI impressions by page;
   - Bing citations and top grounding queries;
   - GA4 AI sessions and key events;
   - the panel score;
   - the error log.
4. **Expectation setting with the client:**
   - brand and navigational prompts first;
   - category prompts later;
   - head health terms in AI Overviews unlikely within 6 months (our judgement from the competitive set in R3 and R8 and `02-competitor-keyword-social.md`).

---

## 4. India compliance for online medical and fertility marketing

This section updates and extends `01-industry-research.md` section 3. Where that document already covers a topic in depth (PCPNDT, CCPA, the patent wording, ASCI education guidelines), it is summarised here and referenced there.

### 4.1 NMC Guidelines on Ethical Advertising and Public Communication (6 Oct 2026)

**Status: verified from the primary notice (I1).**
- Public notice No. R-13014/01/2024-Ethics, dated 06/10/2026, issued by the NMC's Ethics & Medical Registration Board.
- Signed by Dr. Raghav Langer, Secretary, NMC.
- Framed in view of Supreme Court W.P.(C) No. 1160/2023 and the IMC (Professional Conduct, Etiquette and Ethics) Regulations 2002.
- In force "with immediate effect".
- Trade coverage agrees on the main points (I2).

**Does it apply to EmbryoGenesis?**
- **The guidelines bind every RMP.** EmbryoGenesis's registered medical practitioner, Dr. Vidhu Wadhwa (MBBS, MD Pathology), is bound personally.
- **"Hospital/Medical Institution"** (clause 3.4) means "a clinical establishment providing facilities and services for the diagnosis, treatment or care of illness…". It includes institutions under section 2(c)(i) of the Clinical Establishments Act 2010.
  - Diagnostic laboratories are covered by section **2(c)(ii)** of that Act (I6). Clause 3.4 does not cite 2(c)(ii) explicitly, but its main wording ("facilities and services for the diagnosis") arguably covers the lab.
  - For institutions, clause 4.3 says the guidelines are read with the applicable Clinical Establishment Act or State Act.
  - Punjab has its own Clinical Establishments Act 2020 (Act 17 of 2020; I7). A CAG audit reported that rules had not been framed and registration was limited, so its practical reach over a lab is unclear **[VERIFY with counsel]**.
- **Practical position:** treat the guidelines as binding on everything EmbryoGenesis publishes. The founder is not an RMP, but posts by the institution and by Dr. Wadhwa are covered.

**Provisions that change what EmbryoGenesis can publish** (clause numbers from the notice)

| Clause | Rule (paraphrased; short quotes in marks) | Effect on EmbryoGenesis |
|---|---|---|
| 3.2 | "Advertisement" includes digital, social-media, sponsored, targeted, influencer-led, **search-engine**, platform-based, **AI-generated or AI-assisted** promotional communication | SEO pages, GBP posts, reels and WhatsApp broadcasts with a promotional character are all "advertising" |
| 3.2 Explanation I | Non-promotional public information with no intent of commercial benefit is exempt | Educational articles are safest when they are clearly educational. Heavy booking CTAs make them promotional (our reading) |
| 3.2 Explanation II | Information on "diagnostic facilities or services" may be shared as factual information if it contains no "claims of superiority, guaranteed accuracy, guaranteed outcomes, comparative claims" | Test pages may describe what a test is, the sample, timing and turnaround. No accuracy percentages, "most accurate", "only test in India" or outcome promises |
| 3.2 Explanations III–IV | RMPs, and clinical establishments in electronic-media posts, should disclose the RMP's name, qualifications, registration status and SMR/NMR registration number | **Every social and GBP post with clinical content names Dr. Vidhu Wadhwa (or the relevant RMP) with qualifications and registration number.** The number is still a placeholder in our documents (brief section 2) |
| 3.2 Explanation V | No soliciting, buying, procuring or manipulating of fake, paid or misleading reviews, ratings, testimonials, endorsements or recommendations. An RMP shall not request or share patient testimonials or reviews for promotion on social media | No review drives aimed at patients; no "share your success story" posts |
| 6.1–6.4 | Patient information, photos, records and testimonials are not used for advertising except as the law permits. **"Patient consent shall not, by itself, make permissible any testimonial"** or before/after content. Identifying marks must be masked | Confirms the brief's ban on testimonials. Any case discussion must be anonymised and educational |
| 7.2 | **"AI Generated promotional campaign for furtherance of commercial interest is prohibited."** Permitted AI content must "compulsorily carry the source mark" stating its AI origin. AI must not create synthetic endorsements or representations of a patient, RMP or other person | The planned AI-produced reels: educational only, labelled as AI-generated, no synthetic doctors or patients, and legal sign-off before the first post. The wording of 7.2 is internally tense (a prohibition next to labelled permission) **[VERIFY with counsel]** |
| 7.4, 7.6 | No identifiable patient data published; advertising must comply with the IT Act and the DPDP Act and Rules | Links advertising compliance to DPDP (section 4.7) |
| 8.1(i) | No advertising intended to create unnecessary demand, **promote unnecessary diagnostics** or use **fear-based marketing** | Patient pages must not imply that every IVF patient needs endometrial testing. State the indications |
| 8.1(iii) | No success rates, patient numbers or phrases such as "Guaranteed cures", "Best doctors", "No.1 Specialist", "100% success", "Painless treatment", "Miracle treatment", "Exclusive cure" | Consistent with brief guardrail 1. "Thousands of tests done" style claims are also out |
| 8.1(iv) | An RMP may not endorse any diagnostic product, device or commercial product | Dr. Wadhwa should not appear as an endorser of EmbryoGenesis test kits or products |
| 8.1(v) | No case stories, before/after or success stories unless published strictly for scientific or educational purposes with anonymised consent | Only journal-style case reports |
| 8.1(vi) | No statements that create unrealistic expectations, conceal risks or **promote unproven therapies** | Reinforces the hold on the therapies page (and on the LIT blog post) |
| **8.1(vii)** | No RMP shall "offer, pay, solicit, receive or participate in any commission, rebate, bonus, gift, gratuity, referral fee, lead-generation fee" connected with the referral of patients, **"specimens or materials for diagnosis"** | **Directly relevant to the collection-centre model.** Counsel must review partner terms. Public copy must never mention per-sample payments, revenue share or incentives to referring doctors **[VERIFY with counsel]** |
| 8.1(viii) | Agencies, influencers and platforms must not be paid in a way linked to the procurement or referral of individual patients | No pay-per-lead patient campaigns through agencies (our reading for patient leads; B2B partner leads need counsel's view) |
| 8.1(ix) | No "best", "No.1", "leading", "most trusted", "top", "number one", "unmatched" claims unless objectively verifiable through a transparent, independent methodology. Rankings and awards relied on must be verifiable, with methodology, date and awarding body disclosed | Awards: use the exact name, issuer and date (e.g. NBHC 2024 at IIT Delhi). Do not buy "best lab" list placements |
| 8.1(x) | No discounts, limited-period offers, coupons, free procedures or referral benefits likely to encourage unnecessary tests. Disclosure of charges must be factual | No "free test camps" or ERFA discounts. Note: factual prices are *allowed* by the NMC. The client's no-price rule is a business decision |
| 8.1(xi) | No celebrity, influencer, patient, employee or third-party endorsement; material commercial relationships must be disclosed; no third party used to do indirectly what is prohibited | Influencer posts about tests are out. Partner hospitals' posts about EmbryoGenesis must be factual and disclose the relationship |
| 8.1(xii) | No procuring or manipulating fake followers, likes, reviews, ratings, comments or views, and no manipulating "search rankings, visibility or algorithms to create a misleading impression of professional standing" | No keyword-stuffed GBP names, review schemes, bought engagement or link schemes |
| 8.2 | Allowed: research communication published in reputed journals; public-health talks in the RMP's own name "without promoting their employer organization"; factual announcements | Webinars and CME are fine when educational |
| 8.3, 9.1 | Institutions may publish factual name, location, contact details, departments, facilities, equipment, services, **accreditation status** and charges. A website doctor directory with qualifications and **registration details** is patient information, not advertising | Supports an `/about/team/` page with registration numbers |
| 9.2 | Using an RMP's photograph as self-advertisement or promotional publicity is not permitted | Team photos belong in the directory, not in promotional creatives |
| 10 | Penalties for RMPs: warning and ethics training; censure and a monetary penalty; suspension for 3–6 months; for serious violations (misleading cure claims, inducements, "digital mass solicitation") suspension for 6–12 months; for repeat violations removal from the register for 1–3 years | The personal risk sits with the RMP named on the content |

### 4.2 Stem cell and unproven therapies

- **NMC EMRB advisory of 5 Sep 2026** (reviewed in `01-industry-research.md` section 3.3; I3): "Stem Cell Therapy may be offered as standard clinical care, ONLY for approved indications…". Any unauthorised administration, prescription, promotion or advertisement beyond those indications "shall constitute professional misconduct".
- **Google Ads** (G17):
  - prohibits "promotion of speculative and/or experimental medical treatments";
  - restricts cell and gene therapy promotion (the licensed-product exception refers to US FDA approval);
  - allows "exclusively educational or informational" ads about cell and gene therapies.
- **Practical rules:**
  - no therapy advertising on any channel;
  - no therapy facts in llms.txt or schema;
  - therapy pages held, per the brief.

### 4.3 ART (Regulation) Act 2021 and ART Rules

- **Section 32(1):** "The clinic, or bank or agent thereof, shall not issue, publish, distribute, communicate or cause to be issued … any advertisement in any manner including internet, regarding facilities of sex selective assisted reproductive technology." **Section 32(2)** sets the penalty: 5 to 10 years' imprisonment and a fine of ₹10 to 25 lakh, or both (I4).
- **ART (Regulation) Amendment Rules 2026** (G.S.R. 491(E), 17 Jun 2026): add rules on the registration-fee account (7A) and on renewal of registration (8A) **[SECONDARY: seen only in a republication of the Gazette text; I5]**. We found no new advertising provision.
- **Whether EmbryoGenesis needs ART clinic or bank registration:** diagnostics alone probably do not require it. See `01-industry-research.md` section 3.1 **[VERIFY with counsel]**.
- **Practical rules:**
  - no sex-selection terms anywhere, including Hindi and Punjabi phrasing;
  - comment moderation;
  - negative keywords in any paid search.

### 4.4 PCPNDT Act 1994

- Section 22 bans any advertisement of pre-natal or pre-conception sex determination, including on the internet (`01-industry-research.md` section 3.2).
- Google does not allow ads for pre-natal gender determination products in India (G17).

### 4.5 Drugs and Magic Remedies (Objectionable Advertisements) Act 1954

- **The Schedule covers "sterility in women" and "sexual impotence".** Section 3 also covers miscarriage and menstrual disorders (`01-industry-research.md` section 3.5).
- **The Act targets drugs and remedies.** Diagnostic services are not clearly covered. Any product or kit is covered, such as the founder's "LIT-H2 Antioxidant Kit" design registration.
- **Enforcement is tightening.** On 26 Mar 2025 the Supreme Court (*Indian Medical Association v. Union of India*) directed states to:
  - appoint gazetted officers to exercise search-and-seizure powers under section 8;
  - set up public grievance mechanisms within two months;
  - train police on enforcing the Act.

  Commentators read liability as extending to those who design, publish or disseminate such ads, including on social media **[SECONDARY]** (I8).
- **Practical rule:** no "treats", "cures" or "improves fertility" claims for any product, supplement, kit or "therapy" sold or promoted by EmbryoGenesis.

### 4.6 ASCI (self-regulation) and synthetic media

- **ASCI Code:** claims must be truthful and substantiated. Superlatives need objective evidence. Healthcare is the largest category of upheld complaints (`01-industry-research.md` section 3.6).
- **Influencer guidelines, Addendum II** (dated 7 Apr 2025; announced 28 Apr 2025; I9):
  - influencers making technical claims on prevention, treatment, cure or remedies must be qualified health professionals;
  - the qualification must be shown up front: superimposed or spoken at the start of a video, before the body of a text post;
  - unqualified creators may post only generic, non-technical awareness content.
- **Guidelines for Responsible Labelling of Synthetically Generated Content in Advertising** (released 29 Sep 2026; **in effect from 29 Dec 2026**; I10, read via a Khaitan & Co note). Three categories:
  1. **Prohibited even if labelled:** misleading or illegal ads, including fabricated endorsements or testimonials and synthetic depictions that exaggerate results.
  2. **Label required** where the synthetic content materially influences a decision, e.g. "Audio/Video created using AI" or "Audio/Video enhanced using AI".
  3. **No label** for minor edits, decorative elements, subtitles and captions.
- **IT Rules amendment** (notified 10 Feb 2026, G.S.R. 120(E), in force 20 Feb 2026) **[SECONDARY]** (I11):
  - platforms and tools must label synthetically generated audio-visual content and keep provenance metadata;
  - unlawful content flagged by courts or government must be taken down within 3 hours.

  Meta and YouTube will apply labels; EmbryoGenesis should self-label as well.
- **Education claims:** ASCI education guidelines (no "100% placement"; the awarding university named prominently). See `01-industry-research.md` section 3.6.

### 4.7 DPDP Act 2023 and DPDP Rules 2025: forms and analytics consent

| Item | Status | Source |
|---|---|---|
| Rules notified | 13 Nov 2025 (G.S.R. 846(E)) | I12 |
| Board provisions | In force on notification | I12 |
| Consent Manager registration (Rule 4) | About 14 Nov 2026 | I12 |
| **Substantive duties:** notice (Rule 3), security (Rule 6), breach notification (Rule 7), retention and erasure (Rule 8), **parental consent for children (Rule 10)** and the others | **About 13–14 May 2027.** Sources differ by a day; check the Gazette | I12 |
| Proposal to bring the 18-month timeline forward to 12 months (Nov 2026) | Floated Jan 2026; consultation closed 4 Feb 2026; **not notified** according to legal analyses up to Sep 2026 **[re-check before launch]** | I12 |

**What forms and analytics must do (design now, enforceable from May 2027):**
- **Notice:** itemised and plain, listing the data collected, the purpose and how to withdraw or exercise rights. Available in the Eighth Schedule languages on request (Rule 3).
- **Consent:** a clear affirmative action, with no pre-ticked boxes. A separate consent for marketing. Withdrawal as easy as giving consent.
- **Children (under 18):** verifiable parental consent, and no tracking, behavioural monitoring or targeted advertising directed at children (Act s.9; Rule 10). This matters for B.Sc. applicant forms.
  - Google already makes users under 18 ineligible for personalised ads (G18).
  - Do not build remarketing audiences from admission-form visitors.
- **Health data:**
  - no form contents or health information sent to Google or Meta tags;
  - in Google Ads, "Health" is a sensitive interest category, so advertisers cannot use their own uploaded audiences (Customer Match or remarketing lists) for health-related ads (G18).
- **Analytics:** Consent Mode v2 with default "denied" (`02-seo-strategy.md` section 5.7) remains the right setup. It also makes AI-referral counts a floor (section 3.1).
- **Reviews and replies:** never confirm in a public reply that a reviewer was a patient or tested at the lab (NMC clauses 6 and 7.4; DPDP purpose limitation).

### 4.8 Ad platform policies (if paid media is ever used)

- **Google Ads:**
  - experimental treatments are prohibited, and pre-natal gender determination ads are banned in India (G17);
  - "birth control, fertility and STI" products and services, including **fertility testing**, are restricted "in certain locations". The policy page does not list the locations, so check India status in the Ads policy manager before any campaign **[UNVERIFIED for India]** (G17);
  - personalised-advertising limits apply (G18).
- **Meta:** since January 2025, vendor and agency sources report that health and wellness advertisers face restrictions on optimisation events and custom audiences **[SECONDARY; applicability to India not verified]**. Plan on awareness-objective campaigns only, with no health events passed to the pixel.

### "Must / must not publish": checklist for EmbryoGenesis

| Topic | Must | Must not | Basis |
|---|---|---|---|
| Test pages | Factual: what the test is, who orders it, sample, timing, typical turnaround, limits, references, "ordered and interpreted by your doctor" | Superiority claims, "guaranteed accuracy", accuracy %, outcome or pregnancy promises, "only in India" | NMC 3.2 Expl. II, 8.1(iii), 8.1(ix); ASCI |
| Superlatives | n/a | best, No.1, leading, top, most trusted, unmatched, revolutionary, miracle, cure, 100%, painless | NMC 8.1(iii), (ix); brief guardrail 1 |
| Awards | Exact name, issuer, date; methodology if relied on | Implying the award covers test accuracy or the whole lab | NMC 8.1(ix) proviso; ASCI awards guideline |
| Patents | "Patent application published (No. …)" | "Patented" | Brief guardrail 2; `01-industry-research.md` section 3.7 |
| Patient stories | Anonymised, journal-style case reports only | Testimonials, success stories, before/after, patient videos, **even with consent** | NMC 6.2, 8.1(v) |
| Reviews | Let reviews arrive organically; reply politely without confirming patient status | Incentives, gating (asking only happy patients), staff or partner-clinic reviews, bought followers, likes or views | Google G15; NMC Expl. V, 8.1(xii) |
| RMP identity | Name, qualifications, registration status and SMR/NMR number on clinical electronic posts; team directory with registration details | RMP photos used as self-promotion; RMP endorsing products | NMC Expl. III–IV, 8.1(iv), 9.1, 9.2 |
| AI media | Educational, labelled "created using AI", legal sign-off | AI promotional campaigns; synthetic doctors, patients or testimonials; AI depictions of outcomes | NMC 7.2; ASCI SGC (from 29 Dec 2026); IT Rules 2026 |
| Therapies | Held (brief). Research framing only with ethics approval and CTRI registration | Any promotion of stem cell therapy beyond approved indications; promotion of unproven therapies; ads; llms.txt or schema mentions | NMC 5 Sep 2026 advisory; NMC 8.1(vi); Google Ads |
| Necessity and fear | Evidence-graded indications ("may be discussed with your doctor if…") | Fear-based copy; implying every IVF patient needs testing; discounts, free tests, camps | NMC 8.1(i), (x) |
| Referral economics | Counsel-approved partner terms | Commission, referral or lead-generation fees for patients **or specimens**; paying agencies per patient | NMC 8.1(vii), (viii) |
| Sex selection | n/a | Any reference, in any language; any ad | ART Act s.32; PCPNDT s.22; Google Ads |
| Products and kits | n/a | Claims that a product treats or cures infertility, impotence or miscarriage | DMR Act; SC order of 26 Mar 2025 |
| Education | Degree-awarding university named prominently; placement or salary claims only with latest-year evidence and the disclaimer | "100% placement", unsubstantiated salary claims | ASCI education guidelines |
| Influencers | Qualified professionals for technical health content, qualification shown up front, relationship disclosed | Unqualified creators making health claims; payment linked to patients | ASCI Addendum II; NMC 8.1(viii), (xi) |
| Data | Itemised notice, unticked consent, withdrawal, parental consent for minors | Health data in ad pixels; retargeting or personalised ads to under-18s; publishing identifiable patient data | DPDP; NMC 6, 7.4, 7.6; Google G18 |

### Implications for EmbryoGenesis

1. **Update brief section 5** (client approval needed) with four NMC-driven additions:
   - (a) RMP name, qualifications and registration number on clinical posts;
   - (b) no AI promotional campaigns; AI content labelled; no synthetic people;
   - (c) no fear-based or "unnecessary diagnostics" framing and no discounts;
   - (d) counsel review of partner economics under clause 8.1(vii).
2. **Before launch, outside page copy:** remove the therapy facts from `site/src/llms.txt` and from any therapy schema. This is within TechnoTaau Team's remit and does not rewrite page content.
3. **Within page copy (client decision under brief section 0):** the kept therapies page and the LIT post carry the highest risk under NMC clause 8.1(vi) and the stem cell advisory. Recommend noindex or draft pending legal review.
4. **Social plan:** move the "AI-produced informative reels" to a legal-review gate. Use a fixed AI label and a fixed RMP credential line on every clinical post.
5. **Register Dr. Vidhu Wadhwa's SMR/NMR number** in the placeholder list. Without it, clinical social posts cannot comply with Explanation IV.
6. **DPDP:** forms and analytics are built to the consent standard now. Confirm the May 2027 date (or any earlier notified date) at launch.

---

## 5. Local SEO in India

### 5.1 Google Business Profile setup for a lab inside a university campus

| Decision | Recommendation | Basis |
|---|---|---|
| Profile name | The real-world name on the lab's signage, e.g. "EmbryoGenesis" (or the full signage form "EmbryoGenesis – Infertility Diagnostic & Research" if that is what the sign shows). **No keywords** such as "ERA test lab Mohali" or "IVF test" | G14; NMC 8.1(xii); Whitespark lists title keywords as a factor, but they break the guidelines (R14) |
| Eligibility inside the RBU campus | The lab is a distinct, named entity on the top floor of Rayat Bahra Dental College & Hospital. It qualifies for its own profile **if it is public-facing during stated hours with its own signage** (department rule) | G14; **[check on site: signage and staffed hours]** |
| Address | The brochure address with PIN 140302, including "Top Floor, Rayat Bahra Dental College & Hospital". The map pin is the client's own place (02-seo-strategy) | G14; brief section 2 |
| Primary category | The most precise "IS a" category for a diagnostic lab, likely **"Medical laboratory"** **[check the exact category list in the GBP interface]**. Do **not** use "Fertility clinic" or "IVF clinic": EmbryoGenesis does not provide IVF | G14 "IS a" test; brief section 4 |
| Academy | A separate profile **only** if the academy is a distinct public-facing entity with its own signage and staffed hours at an address. Otherwise list courses on the website and leave the academy to the universities' own profiles | G14 (one profile per location; departments rule) |
| Collection centres | **Never** create profiles at partner hospital addresses. They are not EmbryoGenesis locations | G14 (precise address; one page per location) |
| Practitioner profiles | Not needed. If Dr. Wadhwa ever has one, it must be under her name only and must not be used promotionally | G14; NMC 9.2 |
| Phone | The single confirmed public number, under EmbryoGenesis's direct control, with the same number on the site, schema and directories | G14; brief section 2 (to confirm) |
| Hours | Accurate hours, including holiday hours. "Open at time of search" is a top factor. Hours are not yet in any source document (`{{HOURS}}`) | R14; 02-seo-strategy placeholders |
| GBP posts | Treat as advertising under NMC clause 3.2: factual updates (CME, new partner centre, publication) with the RMP credential line where clinical | I1 |
| Bing Places (Apple Business Connect optional) | Same data as the GBP profile. Bing explicitly recommends Bing Places (M1). Apple was not researched **[UNVERIFIED]** | M1 |

### 5.2 NAP consistency and citations

**Name, address and phone (NAP):** one string set used everywhere: the website footer, schema, GBP, Bing Places, LinkedIn, directories and partner pages:
- **Name:** "EmbryoGenesis" (alternate: "EmbryoGenesis – Infertility Diagnostic & Research");
- **Address:** the brochure address with PIN;
- **Phone:** the single public number.

The old site shows four numbers (02 research, finding 11). Fixing that is the first local task.

**Directory priorities**

| Priority | Listing | Fit for EmbryoGenesis | Notes |
|---|---|---|---|
| 1 | Google Business Profile | Essential | Section 5.1 |
| 2 | Bing Places | High | Feeds Bing and Copilot local answers (M1) |
| 3 | Institutional pages: Rayat Bahra University, Bahra University, partner hospitals, Indian Fertility Society (IFS-2900), NABL directory *if* accredited | High; strongest corroboration | Ask each body to use the standard name and one-line description. Earned, not bought |
| 4 | LinkedIn company page | High (B2B) | Exists (brief section 2); align the description and address |
| 5 | Justdial | Medium (consistency) | A large Indian business directory whose business model centres on paid visibility packages **[SECONDARY]**. Whether free basic listings and verification are still offered was **not verified**. Claim or correct an existing listing; avoid paid "top placement" packages (NMC 8.1(ix) and (xii), our reading) |
| 6 | Practo | Low to medium | A healthcare platform. NMC clause 9.4 requires platforms hosting RMPs to comply with NMC norms and bars paid ranking of doctors. How labs are listed today was **not verified** |
| 7 | Sulekha | Low | A services lead marketplace aimed at consumers; poor fit for a B2B-first lab **[process not verified]** |
| 8 | IndiaMART | Low | A B2B product marketplace. Relevant only for kits or equipment, and any product claim is sensitive under the DMR Act |

**How much citations matter:** Whitespark's 2026 survey says citations lost about half a point for local-pack ranking but matter more for AI visibility, as "mentions" (R14). This is expert opinion. Treat directories as **consistency hygiene**: correct the wrong ones, claim the big ones, and do not chase volume.

### 5.3 Reviews policy

- **Google** (G15) prohibits:
  - content posted because of an incentive ("payment, discounts, free goods and/or services");
  - discouraging negative reviews or "selectively solicit[ing] positive reviews";
  - reviews from people with a conflict of interest, including "current or former employment, a contractual or consultory relationship".

  **Partner clinics are in a contractual relationship and must not review EmbryoGenesis.**
- **Enforcement:** Google shows a "suspected fake reviews were recently removed" warning on profiles and can pause new reviews. The labels were tested in the US, UK and India before a global rollout **[SECONDARY]** (G22).
- **NMC** (I1): no soliciting, buying or manipulating reviews, ratings or testimonials to promote medical services. An RMP may not request patient reviews for promotion on social media (Explanation V; clause 8.1(xii)).
- **India consumer law:** IS 19000:2022 (BIS) on online consumer reviews is a **voluntary** standard aimed mainly at platforms. We found no notice making it mandatory (I13). The CCPA misleading-advertisement rules still apply to fake endorsements (`01-industry-research.md` section 3.6).
- **Practical rules:**
  - no review QR-code drives aimed at patients;
  - no "rate us 5 stars" messages;
  - no reviews from staff, students on placement or partner clinics;
  - reply to every review factually, without confirming any patient relationship or any detail;
  - report suspicious reviews through GBP tools rather than arguing in public.

### 5.4 Course listings (Shiksha, Collegedunia, Careers360 and similar)

- These portals list **programmes under the degree-awarding university**. Careers360 already lists the Rayat Bahra Mohali B.Sc./M.Sc. ART & Clinical Embryology (02 research, section 1).
- How institutions claim or correct listings, and what paid packages cost, was **not verified** for any of the three portals.
- **Practical rules:**
  - ask the universities' admission offices to correct listings and to name ITHS/EmbryoGenesis's role accurately;
  - do not create an EmbryoGenesis "college" profile that implies it awards degrees (ASCI education guidelines: the awarding institution must be named prominently; see `01-industry-research.md` sections 3.6 and 5 on the franchise risk);
  - no planted Q&A answers or reviews on these portals;
  - placement or salary claims only with latest-year evidence.

### 5.5 Local landing pages

`02-seo-strategy.md` section 1.1 already says: city pages only where a real collection point exists, with at least 400 words unique to that city. Google's scaled content guidance (G2) and doorway risks support that rule. Under brief section 0 these pages are parked anyway.

### Implications for EmbryoGenesis

1. **Before go-live** (client inputs needed):
   - confirm the single public phone number;
   - confirm opening hours;
   - confirm that signage and staffed hours at the RBU top-floor lab support a GBP profile.

   Then create or claim the GBP profile with the real-world name and the precise category, with no keywords. Verification in India is often by video **[UNVERIFIED]**; plan for a short video of the signage, the entrance and the lab.
2. **Bing Places** in the same week, with identical data.
3. **NAP clean-up list:** the old site's four numbers; social bios; LinkedIn; Justdial if a listing exists; partner hospital pages.
4. **No review campaigns.** Write a one-page reply policy for staff: polite, factual, no patient confirmation, no medical detail.
5. **Academy listings** are corrected through the universities, not through EmbryoGenesis profiles.

---

## 6. Updates needed in existing TechnoTaau documents, and facts not verified

### 6.1 Updates to existing documents (proposed; no files changed by this research)

| Document | Current text | Proposed update | Basis |
|---|---|---|---|
| `docs/strategy/02-seo-strategy.md` section 5 (schema notes, line ~871) | "FAQ rich results show only for well-known government and health authority sites … The markup still helps AI systems parse Q&A" | FAQ rich results were deprecated for **all** sites on 7 May 2026. Google says structured data is not required for its AI features; Bing says schema helps its systems. Keep FAQPage only where cheap and matching a visible FAQ | G2, G5, M3 |
| `02-seo-strategy.md` section 8 intro | "AI Overviews appear on a large share of health queries (estimates range from 44% to 88%)" | The only figure verified here is SE Ranking's German data (more than 82% of health searches). No India data was found. Reword as "a large share in available studies (e.g. >82% of German health searches; no India data)" | R8 |
| `02-seo-strategy.md` section 8.3 (llms.txt) | "no major engine is confirmed to use it" | Add: Google says Search does not use it (Jun 2026); Ahrefs found 97% of files never requested. Keep it optional and limited to reviewed facts. **Remove the therapy lines in `site/src/llms.txt`** | G2, R6 |
| `02-seo-strategy.md` section 8.4 (prompt panel) | One run per prompt per surface | 3 runs per surface; visible = mentioned in at least 2 of 3 runs; same blueprint score | R11 |
| `02-seo-strategy.md` section 5.6 (robots.txt) | Lists GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended | Add Claude-SearchBot, Claude-User, ChatGPT-User and Perplexity-User (as in the built site). Note that Google-Extended also controls grounding in the Gemini apps. Keep the Search Console generative AI control on Include | A1, O1, P1, G3, G16 |
| `02-seo-strategy.md` section 5.7 (GA4) | Custom AI channel only | Add a note on GA4's native "AI Assistant" channel (13 May 2026); keep the custom group as a backstop | GA1 |
| `02-seo-strategy.md` sections 5.4/5.6 vs `site/dist/robots.txt` | `sitemap_index.xml` vs `/sitemap.xml` | The developer aligns them with what WordPress serves | Built site |
| `docs/00-project-brief.md` section 5 | Guardrails 1–10 | Add the NMC 6 Oct 2026 items (section 4, implication 1); extend guardrail 9 with NMC 7.2 and the ASCI SGC guidelines (from 29 Dec 2026) | I1, I10 |
| `docs/research/01-industry-research.md` section 3 | Mentions the "NMC framework of Oct 2026" | Cite the primary notice R-13014/01/2024-Ethics and the clause references in section 4.1 above | I1 |

### 6.2 Facts we could not verify

1. The official help.openai.com text of OpenAI's Publishers and Developers FAQ returned 403. We used the mirror (O3), including the `utm_source=chatgpt.com` detail.
2. Whether consumer ChatGPT search draws on Google results. Only third-party experiments exist (O4).
3. Claude's web-search provider (Brave). Reported, and listed by Anthropic as a subprocessor, but not described in Anthropic's search documentation (A2).
4. How Perplexity, Gemini and Copilot rank sources. Not published.
5. Whether IndexNow affects ChatGPT. No first-party evidence (M5).
6. The full referrer list behind GA4's "AI Assistant" channel. The Google support page was not reached (GA1 is secondary).
7. Bing's AI Performance help page rendered empty. Features are taken from Bing's blog posts (M1, M2) and Search Engine Land (M4).
8. The details of Google's 28 Aug 2026 site reputation update (post body not retrieved) and the body of the Aug 2023 HowTo/FAQ post. HowTo's removal is corroborated by its absence from the current Search Gallery (G7).
9. Whether the NMC guidelines formally cover a standalone diagnostic lab (clause 3.4 cites CEA s.2(c)(i); labs fall under s.2(c)(ii)). Also the implementation status of the Punjab Clinical Establishments Act 2020 for labs.
10. ART (Regulation) Amendment Rules 2026 (G.S.R. 491(E)). Seen only in a republication.
11. ASCI's synthetic-content labelling guidelines. Read through Khaitan & Co's summary, not ASCI's own PDF.
12. DPDP: whether the date is 13 or 14 May 2027, and whether MeitY has notified the acceleration after September 2026.
13. The countries where Google Ads restricts "fertility testing" ads, and whether India is one of them.
14. Whether Meta's health and wellness data restrictions apply in India.
15. Whitespark's factor-group percentages (only factor ranks were read on the primary page).
16. Any India-specific data on how often AI Overviews appear for fertility or IVF queries, and any India-specific GBP ranking study.
17. Listing processes and costs for Justdial, Practo, Sulekha, IndiaMART, Shiksha, Collegedunia and Careers360.
18. The exact GBP category name for a diagnostic lab, and the verification method in India.
19. Whether YouTube's India health-feature eligibility thresholds match the global help page.
20. Applebot-Extended behaviour, and whether the host's CDN blocks AI crawlers by default.

---

## 7. Sources

All accessed **17 Oct 2026** unless noted. "Updated" is the date shown on the page.

### Google (official)

| ID | Source | URL |
|---|---|---|
| G1 | Google Search Central: "AI features and your website" (updated 10 Dec 2025) | https://developers.google.com/search/docs/appearance/ai-features |
| G2 | Google Search Central: "Optimizing your website for generative AI features on Google Search" (published 15 May 2026; updated 10 Jul 2026; mythbusting section clarified 15 Jun 2026) | https://developers.google.com/search/docs/fundamentals/ai-optimization-guide |
| G3 | Search Console Help: Search generative AI features control (rolled out worldwide by 31 Aug 2026) | https://support.google.com/webmasters/answer/16908024 |
| G4 | Search Console Help: Generative AI performance report | https://support.google.com/webmasters/answer/16984139 |
| G5 | Google Search Central: documentation updates log (2025–26 entries cited by date) | https://developers.google.com/search/updates |
| G6 | Google Search Central: FAQ structured data page (deprecation and removal notices) | https://developers.google.com/search/docs/appearance/structured-data/faqpage |
| G7 | Google Search Central: Search Gallery (updated 16 Oct 2026) | https://developers.google.com/search/docs/appearance/structured-data/search-gallery |
| G8 | Google Search Central Blog: "Changes to HowTo and FAQ rich results" (Aug 2023; body not retrieved) | https://developers.google.com/search/blog/2023/08/howto-faq-changes |
| G9 | Google Search Central: "Creating helpful, reliable, people-first content" (updated 5 Oct 2026) | https://developers.google.com/search/docs/fundamentals/creating-helpful-content |
| G10 | Google Search Central: "Using generative AI content" (updated 1 Oct 2026) | https://developers.google.com/search/docs/fundamentals/using-gen-ai-content |
| G11 | Google Search Status Dashboard: ranking update history | https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history |
| G12 | Google Search Central Blog: "Update to the Site Reputation Policy" (Aug 2026; body not retrieved) | https://developers.google.com/search/blog/2026/08/update-site-reputation-policy |
| G13 | Google Business Profile Help: "How Google determines local ranking" | https://support.google.com/business/answer/7091 |
| G14 | Google Business Profile Help: guidelines for representing your business | https://support.google.com/business/answer/3038177 |
| G15 | Google Maps user-contributed content policy: fake engagement | https://support.google.com/contributionpolicy/answer/7400114 |
| G16 | Google crawling infrastructure: common crawlers (Google-Extended) | https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers |
| G17 | Google Ads policy: Healthcare and medicines | https://support.google.com/adspolicy/answer/176031 |
| G18 | Google Ads policy: Personalized advertising | https://support.google.com/adspolicy/answer/143465 |
| G19 | Google India Blog: "Expanding the helpfulness of AI Overviews" (Aug 2024) | https://blog.google/intl/en-in/products/explore-communicate/expanding-the-helpfulness-of-ai-overviews/ |
| G20 | TechCrunch: AI Mode adds Indian languages; Search Live in India (8 Oct 2025) **[SECONDARY]**; Search Engine Land: AI Mode expands beyond English (Sep 2025) **[SECONDARY]** | https://techcrunch.com/2025/10/08/googles-search-live-comes-to-india-ai-mode-gets-more-languages/ ; https://searchengineland.com/google-expands-ai-mode-beyond-english-461680 |
| G21 | YouTube Help: health features eligibility; Google India Blog: registered healthcare professionals in India (Dec 2024) | https://support.google.com/youtube/answer/12796915 ; https://blog.google/intl/en-in/products/platforms/new-ways-for-registered-healthcare-professionals-in-india-to-reach-people-on-youtube/ |
| G22 | 9to5Google: fake-review warnings on Maps (25 Sep 2024; 7 Apr 2025) **[SECONDARY]** | https://9to5google.com/2024/09/25/google-maps-warning-shows-which-business-profiles-might-have-fake-reviews/ ; https://9to5google.com/2025/04/07/google-maps-fake-reviews/ |
| GA1 | Search Engine Journal: "Google Analytics adds AI Assistant as default channel group" (May 2026) **[SECONDARY]** | https://www.searchenginejournal.com/google-analytics-adds-ai-assistant-as-default-channel-group/574974/ |

### AI platforms (official, unless marked)

| ID | Source | URL |
|---|---|---|
| O1 | OpenAI: "Overview of OpenAI crawlers" | https://developers.openai.com/api/docs/bots |
| O2 | OpenAI Help: ChatGPT search (content seen through search excerpts) | https://help.openai.com/en/articles/9237897-chatgpt-search |
| O3 | OpenAI Help: Publishers and developers FAQ (mirror; the help.openai.com version returned 403) | https://help-lb.openai.com/en/articles/12627856-publishers-and-developers-faq |
| O4 | Semrush: "ChatGPT definitely uses Google" (6 Aug 2025) **[SECONDARY]** | https://www.semrush.com/blog/chatgpt-definitely-uses-google |
| A1 | Anthropic: "Does Anthropic crawl data from the web, and how can site owners block the crawler?" | https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler |
| A2 | TechCrunch: Anthropic appears to use Brave for Claude web search (21 Mar 2025) **[SECONDARY]**; Simon Willison (21 Mar 2025) | https://techcrunch.com/2025/03/21/anthropic-appears-to-be-using-brave-to-power-web-searches-for-its-claude-chatbot/ ; https://simonwillison.net/2025/Mar/21/anthropic-use-brave/ |
| P1 | Perplexity: "Perplexity Crawlers" | https://docs.perplexity.ai/guides/bots |
| M1 | Bing Webmaster Blog: "Introducing AI Performance in Bing Webmaster Tools Public Preview" (10 Feb 2026) | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview |
| M2 | Bing Search Blog: "New AI Visibility Insights in Bing Webmaster Tools: Intents, Topics, Citation Share, Compare" (16 Jun 2026) | https://blogs.bing.com/search/June-2026/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare |
| M3 | Microsoft Advertising Blog: "Optimizing Your Content for Inclusion in AI Search Answers" (K. Madhavan, 8 Oct 2025) | https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers |
| M4 | Search Engine Land: Bing Webmaster Tools query-to-page mapping **[SECONDARY; not opened]** | https://searchengineland.com/bing-webmaster-tools-query-page-mapping-472320 |
| M5 | eSEOspace: Bing Webmaster Tools and IndexNow for AI search, confirmed vs unconfirmed **[SECONDARY]** | https://eseospace.com/blog/bing-webmaster-tools-indexnow-ai-search/ |

### Studies

| ID | Source | URL |
|---|---|---|
| R1 | Aggarwal et al., "GEO: Generative Engine Optimization", KDD 2024 (arXiv 2311.09735 v3) | https://arxiv.org/abs/2311.09735 ; https://arxiv.org/html/2311.09735v3 |
| R2 | Pew Research Center: "Google users are less likely to click on links when an AI summary appears in the results" (22 Jul 2025) | https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ |
| R3 | Ahrefs: AI Overview citations and the top 10 (updated study, 2 Mar 2026) | https://ahrefs.com/blog/ai-overview-citations-top-10/ |
| R4 | Ahrefs: "An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied)" (26 May 2025) | https://ahrefs.com/blog/ai-overview-brand-correlation/ |
| R5 | Ahrefs: "Do AI Assistants Prefer to Cite Fresh Content?" (28 Jul 2025) | https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/ |
| R6 | Ahrefs: "We Analyzed 137K Sites: 97% of llms.txt Files Never Get Read" (15 Jun 2026) | https://ahrefs.com/blog/llmstxt-study/ |
| R7 | Profound: AI platform citation patterns (data Aug 2024 – Jun 2025) | https://www.tryprofound.com/blog/ai-platform-citation-patterns |
| R8 | SE Ranking: Health AI Overviews, YouTube vs medical sites (14 Jan 2026; Germany) | https://seranking.com/blog/health-ai-overviews-youtube-vs-medical-sites/ |
| R9 | Jacques et al., "Authority Signals in AI Cited Health Sources" (arXiv 2601.17109, 23 Jan 2026) | https://arxiv.org/abs/2601.17109 |
| R10 | Seer Interactive: AIO impact on Google CTR, September 2025 update (published 4 Nov 2025) | https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update |
| R11 | Search Engine Journal on the SparkToro/Gumshoe study of AI recommendation consistency (30 Jan 2026) | https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242/ |
| R12 | Storyboard18: Google pulls AI Overviews from some medical searches after the Guardian investigation (Jan 2026) **[SECONDARY]** | https://www.storyboard18.com/digital/google-pulls-ai-overviews-from-select-medical-searches-after-guardian-investigation-87401.htm |
| R13a | Search Engine Journal: "Google Drops FAQ Rich Results From Search" (10 May 2026) | https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/ |
| R14 | Whitespark: Local Search Ranking Factors, 2026 edition (6 Nov 2025) | https://whitespark.ca/local-search-ranking-factors/ |
| R15 | Wikipedia: Conflict of interest guideline | https://en.wikipedia.org/wiki/Wikipedia:Conflict_of_interest |
| R16 | Search Engine Land: Quality Rater Guidelines update (Sep 2025) | https://searchengineland.com/google-updates-search-quality-raters-guidelines-adding-ai-overview-examples-ymyl-definitions-461908 |
| R16a | Wikidata: Notability | https://www.wikidata.org/wiki/Wikidata:Notability |
| R17 | TechWyse: Google AI search optimization guide and Lighthouse llms.txt audit **[SECONDARY]** | https://www.techwyse.com/news/ai-search/google-ai-search-optimization-guide-llms-txt-lighthouse-audit |

### India: law, regulators and self-regulation

| ID | Source | URL |
|---|---|---|
| I1 | **NMC public notice R-13014/01/2024-Ethics (6 Oct 2026):** Guidelines on Ethical Advertising and Public Communication by Hospitals/Medical Institutions and RMPs (13-page scanned PDF, read page by page) | https://www.nmc.org.in/whats-new/download/1874 |
| I2 | Medical Dialogues: NMC issues ethical advertising guidelines (7 Oct 2026); Storyboard18 coverage **[SECONDARY]** | https://medicaldialogues.in/health-news/nmc/nmc-issues-ethical-advertising-public-communication-guidelines-for-doctors-hospitals-details-180731 ; https://www.storyboard18.com/brand-marketing/nmc-tightens-medical-advertising-rules-to-curb-digital-marketing-ws-l-112193.htm |
| I3 | NMC EMRB advisory on stem cell therapy (5 Sep 2026), as reviewed in `01-industry-research.md` section 3.3 (not re-fetched on 17 Oct 2026) | https://medicaldialogues.in/pdf_upload/2026/09/07/nmc-advisory-05092026-474464.pdf |
| I4 | ART (Regulation) Act 2021, section 32 (bare act); India Code record | https://www.advocatekhoj.com/library/bareacts/assistedreproductive2021/32.php ; https://www.indiacode.nic.in/handle/123456789/17031 |
| I5 | ART (Regulation) Amendment Rules 2026, G.S.R. 491(E), 17 Jun 2026 (republication) **[SECONDARY]** | https://www.taxheal.com/?p=134081 |
| I6 | Clinical Establishments (Registration and Regulation) Act 2010, India Code PDF (s.2(c) definitions seen through search excerpts) | https://www.indiacode.nic.in/bitstream/123456789/15271/1/clinical_establishment_act_2010.pdf |
| I7 | Punjab Clinical Establishments (Registration and Regulation) Act 2020 (Act 17 of 2020); CAG audit report, Chapter VIII (2024) | https://prsindia.org/files/bills_acts/acts_states/punjab/2020/Act%2017%20of%202020.pdf ; https://cag.gov.in/uploads/download_audit_report/2024/Chapter-VIII-Adequacy-and-effectiveness-of-the-regulatory-mechanisms-067e28e8de297d3.08469546.pdf |
| I8 | LiveLaw: Supreme Court directs states to enforce the DMR Act (26 Mar 2025); KS&K analysis **[SECONDARY]** | https://www.livelaw.in/top-stories/misleading-medical-ads-supreme-court-directs-states-to-appoint-officers-to-enforce-drugs-magic-remedies-objectionable-advertisements-act-287581 ; https://ksandk.com/regulatory/supreme-court-drugs-magic-remedies-act/ |
| I9 | LexOrbis: ASCI updates influencer guidelines for health and finance (Addendum II, 7 Apr 2025) **[SECONDARY]**; ASCI Code page | https://www.lexorbis.com/asci-updates-influencer-guidelines-for-health-and-finance-sectors-strikes-balance-between-expertise-and-expression/ ; https://www.ascionline.in/the-asci-code-guidelines/ |
| I10 | Khaitan & Co ERGO note on ASCI Guidelines for Responsible Labelling of Synthetically Generated Content in Advertising (12 Oct 2026) **[SECONDARY]** | https://www.khaitanco.com/sites/default/files/2026-10/Ergo_ASCI%20Guidelines%20on%20SGC%20Labelling_12%2010%202026.pdf |
| I11 | Hogan Lovells: India introduces mandatory labelling for AI and 3-hour takedown (IT Rules amendment, Feb 2026) **[SECONDARY]** | https://www.hoganlovells.com/en/publications/india-introduces-mandatory-labelling-for-ai-and-3hour-takedown-for-illegal-content |
| I12 | DPDP Rules 2025 effective-date reference (dcomply); MirvoLegal compliance timeline (as at Sep 2026); Chambers on MeitY's proposal; PIB release (via `01-industry-research.md`) | https://dpdpa.dcomply.in/rules/ ; https://www.mirvolegal.com/insights/dpdp-rules-2025-compliance-timeline/ ; https://chambers.com/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs ; https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 |
| I13 | Centre for Advocacy and Research: India's legal response to fake online reviews (IS 19000:2022 status) **[SECONDARY]** | https://www.cag.org.in/blogs/regulating-trust-indias-legal-response-fake-online-reviews |

---

*Prepared and signed by **TechnoTaau Team** (project lead: Jakhar Singh), 17 October 2026. This is research for planning. It is not legal advice; items marked [VERIFY with counsel] need review by the client's lawyer or medical-council adviser before anyone acts on them.*
