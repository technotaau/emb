# EmbryoGenesis Digital Rebuild: Knowledge Base

This repository holds the strategy, design direction, content and SEO specification that TechnoTaau Team is preparing for EmbryoGenesis (https://embryogenesis.in).

## Working preferences
- Address the client and sign all documents and proposals as **TechnoTaau Team** or **Jakhar Singh**.
- Read `docs/00-project-brief.md` before any task. It records the client's decisions, brand palette and compliance guardrails.
- Current direction (client decision, Oct 2026): keep the OLD website's content and URLs, redesign in the Indira IVF style with the new logo; the B2B partner pages are dropped. English only, pan-India, WordPress-based. TechnoTaau Team delivers design, content and SEO specs; the client's developer builds.
- Never publish test prices, superlatives ("best", "No. 1", "leading"), "patented" (use "patent application published"), testimonials (banned even with consent under the NMC guidelines of 6 Oct 2026), or therapy promotion. The therapy pages are held pending legal review, and therapy facts stay out of llms.txt and schema.
- AI-generated media only with legal sign-off and labelling (NMC clause 7.2); no synthetic doctors or patients. No partner-facing copy until counsel reviews NMC clause 8.1(vii).
- All medical content is reviewed by Prof. (Dr.) Pulakes Purkait (and Dr. Vidhu Wadhwa for clinical claims) and carries references and a disclaimer.

## Layout
- `brand/`: logo and palette reference.
- `docs/00-project-brief.md`: decisions and guardrails (source of truth).
- `docs/research/`: industry research, competitor/keyword/social landscape, current-site audit (15 Oct 2026); 07 search/AI/compliance landscape 2026; 08 keywords, competitors and AI-visibility baseline.
- `docs/strategy/`: business model, blueprint, SEO strategy (02, partly superseded), social strategy (03, AI reels and partner posts paused), brand voice, and **05 the 12-month SEO/AEO/GEO plan** (plus its client page `05-seo-aeo-geo-plan.html`).
- `docs/qc/`: QC reports (content fidelity, SEO/AEO/GEO, front-end, design, plan).
- `site/`: the multi-page reference build (`python3 site/build.py`, then `python3 site/qc.py`); `prototype/`: the single-page prototype.
- `content/`: page copy drafts and source extracts.
