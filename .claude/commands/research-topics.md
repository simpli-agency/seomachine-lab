# Research Topics Command

Analyze topical authority by clustering keywords into related topics.

## Usage
`/research-topics`

## Project Context

This repo runs research for many unrelated projects. Before doing anything:

1. Determine the target project. The user names it, or the last-used project applies. If no project fits, use `_general`.
2. Read `projects/<slug>/project.json` for domain, GSC property, market (`location_code`/`language_code`), competitors and keyword lists. Read `projects/<slug>/context.md` if it exists.
3. Pass `--project <slug>` to every Python script you run.
4. Write every artifact to `projects/<slug>/research/`, named `YYYY-MM-DD-<kind>.md`.
5. Write the report in Russian. Keep keywords, metrics, URLs and code identifiers in their original form.

## What This Command Does

Groups all your ranking keywords into topic clusters and identifies:
- **Strong Authority Topics**: Where you dominate (maintain & expand)
- **Moderate Authority Topics**: Partial coverage (strengthen)
- **Weak Authority Topics**: BIGGEST OPPORTUNITY (build comprehensive clusters)
- **Coverage Gaps**: Related keywords within each topic you don't rank for

For each topic:
- Authority score (0-100) based on coverage, position, demand
- Number of keywords ranking
- Average position
- Total impressions and clicks
- Coverage gaps to fill

## Process

Execute topic cluster analysis:
```bash
python3 research_topic_clusters.py
```

This will:
1. Fetch all ranking keywords from GSC (90 days)
2. Cluster keywords into topics using:
   - ML clustering (TF-IDF + K-means) if sklearn available
   - Pattern-based clustering as fallback
3. Calculate authority score for each cluster
4. Identify coverage gaps using DataForSEO
5. Prioritize weak clusters with high demand
6. Generate report: `projects/<slug>/research/YYYY-MM-DD-topic-clusters.md`

## Output

The report includes:

### Authority Distribution
- Strong Authority: Topics you dominate
- Moderate Authority: Partial coverage
- Weak Authority: **OPPORTUNITIES**
- Minimal Authority: Major gaps

### Weak Authority Topics (FOCUS HERE!)
For each weak cluster:
- Authority score and level
- Current keyword count
- Average position
- Total impressions
- Top 5 current keywords
- 8-10 coverage gaps with search volume
- Recommended action (build 8-12 article cluster)

### Strong Authority Topics (MAINTAIN)
For each strong cluster:
- Performance metrics
- Top performing keywords
- Expansion opportunities
- Maintenance recommendations

## Key Insight

**Weak clusters with high demand = Your biggest opportunity**

Example: "Content Marketing"
- Only 3 keywords ranking
- Average position 28
- 5,000 impressions/month (HIGH DEMAND!)
- 15+ related keywords you don't rank for
- **Action**: Build comprehensive 10-article cluster

## Strategy

### Priority 1: Build Weak Clusters
- Select top 2-3 weak clusters with highest demand
- Create comprehensive pillar page (3000+ words)
- Create 8-12 supporting cluster articles
- Target all identified coverage gaps
- Internal link everything to pillar

### Priority 2: Maintain Strong Clusters
- Keep content fresh
- Expand with advanced topics
- Fill any remaining gaps

### Priority 3: Strengthen Moderate Clusters
- Add 3-5 articles to reach strong authority
- Improve rankings for existing content

## Integration

After running `/research-topics`:
- Select weak cluster to build
- Use `/research-serp [gap keyword]` for each gap
- Create pillar page first, then cluster content

## Example Output

```
Weak Authority: Content Marketing (Score: 32/100)
- Keywords: 3
- Avg Position: 28.4
- Impressions: 5,240/mo

Coverage Gaps:
- "content marketing strategy" (1,200 vol)
- "content marketing ROI" (980 vol)
- "content calendar template" (580 vol)
...

Action: Create 10-article cluster to build authority
```

## Time & Cost

**Time:** 2-3 minutes
**API Cost:** ~$0.50 (if fetching coverage gaps)
**Cost:** Free for clustering only

## When to Run

- **Monthly**: Monitor topical authority growth
- **Before content planning**: Identify cluster opportunities
- **When entering new niche**: Find what topics to own
