#!/usr/bin/env python3
"""
Surface Keyword and SERP Scan

Cheap first-pass sizing of a topic before any deep research: exact-match
metrics for the project's seed keywords, long-tail suggestions for the seeds
that come back empty, and top SERP domains for a short shortlist.

Reads from project.json:
  bofu_keywords / mofu_keywords / alternative_keywords - the seed list
  serp_keywords     - keywords to pull a SERP for (keep it short, SERP costs)
  suggestion_seeds  - phrases to expand into long-tail suggestions

Writes a JSON dump of everything fetched next to the project's reports so the
written analysis can cite real numbers.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add data_sources to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data_sources"))

from modules.dataforseo import DataForSEO
from modules.project_config import add_project_argument, load_project

SEED_BUCKETS = ["bofu_keywords", "mofu_keywords", "alternative_keywords"]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    add_project_argument(parser)
    parser.add_argument(
        "--serp-depth",
        type=int,
        default=20,
        help="How many organic results to keep per SERP (default: 20)",
    )
    parser.add_argument(
        "--suggestions",
        type=int,
        default=25,
        help="Suggestions per seed phrase (default: 25)",
    )
    parser.add_argument(
        "--no-serp",
        action="store_true",
        help="Skip the SERP pass (metrics only)",
    )
    parser.add_argument(
        "--worldwide",
        action="store_true",
        help="Ask Google Ads for global volume instead of the project market",
    )
    parser.add_argument(
        "--geo-scan",
        action="store_true",
        help=(
            "Also run the metrics pass per country from geo_scan_locations, "
            "using geo_scan_keywords (or key_queries) as the probe list"
        ),
    )
    return parser.parse_args()


def collect_seeds(project):
    """Seed keywords from every bucket, de-duplicated, order preserved"""
    seeds = []
    for bucket in SEED_BUCKETS:
        for keyword in project.keywords(bucket):
            if keyword not in seeds:
                seeds.append(keyword)
    return seeds


def fmt(value, width=None):
    text = "n/a" if value is None else str(value)
    return text.rjust(width) if width else text


def print_metrics(rows):
    print(f"\n{'keyword':<45} {'vol':>8} {'cpc':>7} {'comp':>6} {'KD':>5}  intent")
    print("-" * 92)
    for row in rows:
        print(
            f"{(row['keyword'] or '')[:45]:<45} "
            f"{fmt(row['search_volume'], 8)} "
            f"{fmt(row['cpc'], 7)} "
            f"{fmt(row['competition'], 6)} "
            f"{fmt(row['keyword_difficulty'], 5)}  "
            f"{fmt(row['main_intent'])}"
        )


def main():
    args = parse_args()
    project = load_project(args.project)

    print("=" * 80)
    print("SURFACE KEYWORD AND SERP SCAN")
    print("=" * 80)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Project: {project.name} ({project.slug})")
    print(f"Market: location {project.location_code}, language {project.language_code}")

    try:
        dfs = DataForSEO(**project.dataforseo_kwargs())
    except Exception as e:
        print(f"\n✗ DataForSEO error: {e}")
        return 1

    seeds = collect_seeds(project)
    if not seeds:
        print("\n✗ No seed keywords in project.json - nothing to scan")
        return 1

    payload = {
        "project": project.slug,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "location_code": project.location_code,
        "language_code": project.language_code,
        "seed_count": len(seeds),
    }

    # ---- 1. exact-match metrics for the seed list ----
    print(f"\n1. Keyword overview for {len(seeds)} seeds...")
    overview = dfs.get_keyword_overview(seeds)
    payload["overview"] = overview

    returned = {row["keyword"] for row in overview}
    missing = [kw for kw in seeds if kw not in returned]
    with_volume = [r for r in overview if r["search_volume"]]
    no_volume = [r for r in overview if not r["search_volume"]]

    print(f"   ✓ {len(overview)} keywords returned")
    print(f"   {len(with_volume)} with volume, {len(no_volume)} null volume, "
          f"{len(missing)} not in the database at all")
    print_metrics(overview)

    if no_volume:
        print("\n   Null volume (below provider threshold - not proof of zero demand):")
        for row in no_volume:
            print(f"   - {row['keyword']}")
    if missing:
        print("\n   Not returned by the API:")
        for keyword in missing:
            print(f"   - {keyword}")
    payload["missing_from_api"] = missing

    # ---- 1b. Google Ads volume, which answers for every keyword asked ----
    scope = "worldwide" if args.worldwide else "project market"
    print(f"\n1b. Google Ads search volume ({scope}) for {len(seeds)} seeds...")
    volumes = dfs.get_search_volume(seeds, worldwide=args.worldwide)
    payload["search_volume_scope"] = scope
    payload["search_volume"] = volumes

    print(f"   ✓ {len(volumes)} rows")
    print(f"\n{'keyword':<45} {'vol':>8} {'cpc':>7} {'comp':>10} {'idx':>5}")
    print("-" * 80)
    for row in volumes:
        print(
            f"{(row['keyword'] or '')[:45]:<45} "
            f"{fmt(row['search_volume'], 8)} "
            f"{fmt(row['cpc'], 7)} "
            f"{fmt(row['competition'], 10)} "
            f"{fmt(row['competition_index'], 5)}"
        )

    # ---- 2. long-tail suggestions for the configured seed phrases ----
    suggestion_seeds = project.get("suggestion_seeds", [])
    payload["suggestions"] = {}
    if suggestion_seeds:
        print(f"\n2. Long-tail suggestions for {len(suggestion_seeds)} phrases...")
        for seed in suggestion_seeds:
            try:
                items = dfs.get_keyword_suggestions(seed, limit=args.suggestions)
            except Exception as e:
                print(f"   ✗ {seed}: {e}")
                continue
            payload["suggestions"][seed] = items
            print(f"\n   '{seed}' -> {len(items)} suggestions")
            for row in items[:15]:
                print(
                    f"     {(row['keyword'] or '')[:52]:<52} "
                    f"vol {fmt(row['search_volume'], 7)}  "
                    f"KD {fmt(row['keyword_difficulty'], 4)}  "
                    f"cpc {fmt(row['cpc'])}"
                )
    else:
        print("\n2. No suggestion_seeds configured - skipping")

    # ---- 2b. same probe keywords across other countries ----
    payload["geo_scan"] = {}
    geo_locations = project.get("geo_scan_locations", [])
    if args.geo_scan and geo_locations:
        probe = project.get("geo_scan_keywords") or project.keywords("key_queries")
        print(f"\n2b. Geo scan: {len(probe)} keywords x {len(geo_locations)} countries...")
        for location in geo_locations:
            code = location.get("code")
            name = location.get("name", str(code))
            language = location.get("language", project.language_code)
            try:
                rows = dfs.get_keyword_overview(
                    probe, location_code=code, language_code=language
                )
            except Exception as e:
                print(f"   ✗ {name}: {e}")
                continue
            payload["geo_scan"][name] = {
                "location_code": code,
                "language_code": language,
                "keywords": rows,
            }
            found = [r for r in rows if r["search_volume"]]
            total = sum(r["search_volume"] for r in found)
            print(f"\n   {name} ({code}/{language}): {len(rows)} returned, "
                  f"{len(found)} with volume, {total} total volume")
            for row in rows:
                print(
                    f"     {(row['keyword'] or '')[:42]:<42} "
                    f"vol {fmt(row['search_volume'], 7)}  "
                    f"KD {fmt(row['keyword_difficulty'], 4)}"
                )
    elif args.geo_scan:
        print("\n2b. No geo_scan_locations configured - skipping")

    # ---- 3. SERP composition for the shortlist ----
    serp_keywords = project.get("serp_keywords", [])
    payload["serp"] = {}
    if serp_keywords and not args.no_serp:
        print(f"\n3. SERP scan for {len(serp_keywords)} keywords "
              f"(top {args.serp_depth})...")
        for keyword in serp_keywords:
            try:
                data = dfs.get_serp_data(keyword, limit=args.serp_depth)
            except Exception as e:
                print(f"   ✗ {keyword}: {e}")
                continue
            if data.get("error"):
                print(f"   ✗ {keyword}: {data['error']}")
                continue
            results = data.get("organic_results", [])[: args.serp_depth]
            payload["serp"][keyword] = {
                "search_volume": data.get("search_volume"),
                "features": data.get("features", []),
                "organic_results": results,
            }
            print(f"\n   '{keyword}' - vol {fmt(data.get('search_volume'))}, "
                  f"features: {', '.join(data.get('features', [])) or 'none'}")
            for item in results[:12]:
                print(f"     {item['position']:>3}. {item['domain']}  {item['url']}")
                print(f"          {(item['title'] or '')[:100]}")
    elif args.no_serp:
        print("\n3. SERP pass skipped (--no-serp)")
    else:
        print("\n3. No serp_keywords configured - skipping")

    # ---- 4. persist the raw pull ----
    stem = f"{datetime.now().strftime('%Y-%m-%d')}-keyword-surface-data"
    if args.worldwide:
        stem += "-worldwide"
    out_path = project.output_path(f"{stem}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print(f"Raw data: {project.rel(out_path)}")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())
