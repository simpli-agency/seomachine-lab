# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SEO Machine Lab is a research workspace for SEO and search-visibility analysis across **many unrelated projects**. It is not tied to a single site or brand: DataForSEO is the primary data source, Google Search Console and GA4 are optional per project. There is no content production here - no writing, no publishing.

Most runs happen headlessly on a VPS agent, so scripts must work non-interactively and read credentials from the environment.

## Projects

Every research run belongs to a project directory:

```
projects/
  _general/          # research not tied to any project (default target)
  _example/          # template - copy it to start a new project
  <slug>/
    project.json     # domain, GSC property, market, competitors, keywords
    context.md       # optional free-form notes about the project
    research/        # artifacts: YYYY-MM-DD-<kind>.md (committed to git)
```

`project.json` fields (all optional): `name`, `description`, `domain`, `gsc_site_url`, `ga4_property_id`, `blog_path`, `location_code`, `language_code`, `direct_competitors`, `content_competitors`, `bofu_keywords`, `mofu_keywords`, `alternative_keywords`, `key_queries`, `relevant_terms`, `skip_terms`, `topic_patterns`.

**Credentials never go into `project.json`** - they are shared and live in `.env` / `credentials/`.

### Working rules

- Always establish which project a task belongs to before running anything. If none fits, use `_general`.
- Pass `--project <slug>` to every script; without it the run falls back to `$SEO_PROJECT`, then `_general`.
- Write artifacts to `projects/<slug>/research/` as `YYYY-MM-DD-<kind>.md`.
- **Reports are written in Russian.** Keywords, metrics, URLs, domains and code identifiers stay in their original form. Code comments stay in English.
- Starting a new project = copy `projects/_example/`, rename, fill in `project.json`.

## Setup

```bash
pip install -r data_sources/requirements.txt
cp .env.example .env   # fill in DataForSEO + Google credentials
python3 test_dataforseo.py --project _general   # verify API connectivity
```

`.env` holds shared credentials (DataForSEO login/password, paths to Google service account JSON). `credentials/` and `.env` are gitignored - on the VPS they are provisioned out of band.

## Commands

Slash commands in `.claude/commands/`:

- `/research [topic]` - keyword and competitor research, produces a brief
- `/research-serp [keyword]` - SERP composition, intent, content length benchmarks
- `/research-gaps` - keywords competitors rank for and the project does not
- `/research-trending` - rising queries and trend signals
- `/research-topics` - topic clusters and topical authority gaps
- `/research-performance` - content performance matrix (needs GSC/GA4)
- `/research-ai-citations [topic]` - which sources AI assistants cite for a topic
- `/priorities` - prioritization matrix across research outputs
- `/performance-review` - analytics-driven review (needs GSC/GA4)

Agents in `.claude/agents/`: `content-analyzer`, `keyword-mapper`, `cluster-strategist`, `performance`.

## Python

```bash
# every script takes --project
python3 research_quick_wins.py --project acme
python3 research_competitor_gaps.py --project acme
python3 research_serp_analysis.py "keyword phrase" --project acme
python3 research_topic_clusters.py --project acme
python3 research_trending.py --project acme
python3 research_performance_matrix.py --project acme
python3 research_priorities_comprehensive.py --project acme
python3 seo_baseline_analysis.py --project acme
python3 seo_bofu_rankings.py --project acme
python3 seo_competitor_analysis.py --project acme

python3 -m unittest discover -s tests
```

`data_sources/modules/project_config.py` resolves the active project and hands each client its settings:

- `PROJECT.gsc_site_url` → `GoogleSearchConsole(site_url=...)`
- `PROJECT.ga4_property_id` → `GoogleAnalytics(property_id=...)`
- `PROJECT.dataforseo_kwargs()` → `DataForSEO(location_code=..., language_code=...)`
- `PROJECT.report_path("kind")` → dated path inside the project's research directory

### Modules

- `dataforseo.py` - SERP data, rankings, keyword ideas, questions, domain metrics. Market defaults come from the project (class defaults: 2840/USA, `en`).
- `google_search_console.py` - rankings, impressions, CTR
- `google_analytics.py` - GA4 traffic and engagement
- `data_aggregator.py` - combines sources
- `opportunity_scorer.py` - 8 weighted factors: Volume 25%, Position 20%, Intent 20%, Competition 15%, Cluster 10%, CTR 5%, Freshness 5%, Trend 5%
- `search_intent_analyzer.py`, `keyword_analyzer.py`, `content_length_comparator.py`, `readability_scorer.py`, `seo_quality_rater.py`, `competitor_gap_analyzer.py`, `engagement_analyzer.py`

## Conventions

- Code and comments in English; research reports in Russian.
- Do not hardcode a domain, market or keyword set into a script - it belongs in `project.json`.
- New scripts follow the same pattern: import `project_from_args`, resolve `PROJECT` at module level, write output through `PROJECT.report_path()`.
