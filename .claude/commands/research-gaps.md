# Research Gaps Command

Identify content gaps where competitors rank but you don't.

## Usage
`/research-gaps`

## Project Context

This repo runs research for many unrelated projects. Before doing anything:

1. Determine the target project. The user names it, or the last-used project applies. If no project fits, use `_general`.
2. Read `projects/<slug>/project.json` for domain, GSC property, market (`location_code`/`language_code`), competitors and keyword lists. Read `projects/<slug>/context.md` if it exists.
3. Pass `--project <slug>` to every Python script you run.
4. Write every artifact to `projects/<slug>/research/`, named `YYYY-MM-DD-<kind>.md`.
5. Write the report in Russian. Keep keywords, metrics, URLs and code identifiers in their original form.

## What This Command Does

Analyzes 7 competitors to find keywords they rank for (top 20) that you don't rank for at all:
- **Direct Competitors**: Configured in `projects/<slug>/project.json` or passed as arguments
- **Content Competitors**: Industry blogs and media sites in your niche

For each gap:
- Filters out branded/irrelevant keywords
- Scores opportunity based on volume, difficulty, and intent
- Determines content type needed (listicle, how-to, guide)
- Prioritizes by potential impact

## Process

Execute the competitor gap analysis:
```bash
python3 research_competitor_gaps.py
```

This will:
1. Fetch your current ranking keywords from GSC
2. Analyze each competitor's top 20 ranking keywords
3. Identify gaps (they rank, you don't)
4. Enrich with search volume, difficulty, SERP features
5. Score and prioritize opportunities
6. Generate report: `projects/<slug>/research/YYYY-MM-DD-competitor-gaps.md`

## Output

The report includes:
- Top 20 content gap opportunities
- Priority level (CRITICAL/HIGH/MEDIUM)
- Competitor intel (who ranks, at what position)
- Keyword metrics (volume, difficulty, CPC)
- Search intent and content type needed
- Specific action steps for each gap

## Integration

After running `/research-gaps`:
- Use `/research-serp [keyword]` to analyze what ranks
- Focus on CRITICAL/HIGH priority gaps first

## Time & Cost

**Time:** 3-5 minutes
**API Cost:** ~$1-3 (DataForSEO) - analyzes ~300-500 competitor keywords

## When to Run

- **Monthly**: Full competitive landscape review
- **When entering new topic**: Find what's missing
- **Before content planning**: Identify proven opportunities
