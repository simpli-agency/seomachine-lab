#!/usr/bin/env python3
"""
Domain Visibility Snapshot

Answers "does this domain rank for anything, and how does it compare to the
players already on its SERPs" without a GSC connection: DataForSEO Labs domain
metrics plus the domain's ranked keywords, for the project domain and for every
competitor listed in project.json.

Reads from project.json:
  domain                                 - the project's own domain
  direct_competitors / content_competitors - domains to benchmark against
  visibility_domains                     - extra domains to include

Writes a JSON dump next to the project's reports.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data_sources"))

from modules.dataforseo import DataForSEO
from modules.project_config import add_project_argument, load_project


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    add_project_argument(parser)
    parser.add_argument(
        "--ranked-limit",
        type=int,
        default=50,
        help="Ranked keywords to pull per domain (default: 50)",
    )
    parser.add_argument(
        "--own-only",
        action="store_true",
        help="Only look at the project domain, skip competitors",
    )
    return parser.parse_args()


def collect_domains(project, own_only):
    domains = []
    for domain in [project.domain] if project.domain else []:
        domains.append(domain)
    if own_only:
        return domains
    for bucket in (
        project.direct_competitors,
        project.content_competitors,
        project.get("visibility_domains", []),
    ):
        for domain in bucket:
            if domain not in domains:
                domains.append(domain)
    return domains


def fetch_ranked_keywords(dfs, domain, limit, location_code, language_code):
    """DataForSEO Labs ranked_keywords - the keywords a domain already ranks for"""
    data = [
        {
            "target": domain,
            "location_code": location_code,
            "language_code": language_code,
            "limit": limit,
            "order_by": ["ranked_serp_element.serp_item.etv,desc"],
        }
    ]
    response = dfs._post("/v3/dataforseo_labs/google/ranked_keywords/live", data)
    if response.get("status_code") != 20000:
        return {"error": response.get("status_message"), "items": []}

    task = dfs._first_task(response)
    if not task or task.get("status_code") != 20000:
        return {"error": (task or {}).get("status_message", "no task"), "items": []}

    result = dfs._first_result(task)
    if result is None:
        return {"error": "no result", "items": []}

    rows = []
    for item in result.get("items") or []:
        kw_data = item.get("keyword_data", {}) or {}
        kw_info = kw_data.get("keyword_info", {}) or {}
        kw_props = kw_data.get("keyword_properties", {}) or {}
        serp_item = (item.get("ranked_serp_element", {}) or {}).get("serp_item", {}) or {}
        rows.append(
            {
                "keyword": kw_data.get("keyword"),
                "search_volume": kw_info.get("search_volume"),
                "cpc": kw_info.get("cpc"),
                "keyword_difficulty": kw_props.get("keyword_difficulty"),
                "position": serp_item.get("rank_absolute"),
                "url": serp_item.get("url"),
                "etv": serp_item.get("etv"),
            }
        )
    return {
        "total_count": result.get("total_count"),
        "items": rows,
    }


def fmt(value, width=None):
    text = "n/a" if value is None else str(value)
    return text.rjust(width) if width else text


def main():
    args = parse_args()
    project = load_project(args.project)

    print("=" * 80)
    print("DOMAIN VISIBILITY SNAPSHOT")
    print("=" * 80)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Project: {project.name} ({project.slug})")
    print(f"Market: location {project.location_code}, language {project.language_code}")

    try:
        dfs = DataForSEO(**project.dataforseo_kwargs())
    except Exception as e:
        print(f"\n✗ DataForSEO error: {e}")
        return 1

    domains = collect_domains(project, args.own_only)
    if not domains:
        print("\n✗ No domain in project.json - nothing to check")
        return 1

    payload = {
        "project": project.slug,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "location_code": project.location_code,
        "language_code": project.language_code,
        "domains": {},
    }

    for domain in domains:
        print(f"\n{'-' * 80}\n{domain}")
        try:
            metrics = dfs.get_domain_metrics(domain)
        except Exception as e:
            print(f"   ✗ metrics: {e}")
            metrics = {}

        print(
            f"   organic keywords: {fmt(metrics.get('organic_keywords'))}   "
            f"est. traffic: {fmt(metrics.get('organic_traffic'))}   "
            f"domain rank: {fmt(metrics.get('domain_rank'))}"
        )

        try:
            ranked = fetch_ranked_keywords(
                dfs,
                domain,
                args.ranked_limit,
                project.location_code,
                project.language_code,
            )
        except Exception as e:
            print(f"   ✗ ranked keywords: {e}")
            ranked = {"error": str(e), "items": []}

        if ranked.get("error"):
            print(f"   ✗ ranked keywords: {ranked['error']}")
        else:
            print(f"   ranked keywords returned: {len(ranked['items'])} "
                  f"(total {fmt(ranked.get('total_count'))})")
            for row in ranked["items"][:20]:
                print(
                    f"     {fmt(row['position'], 4)}. {(row['keyword'] or '')[:45]:<45} "
                    f"vol {fmt(row['search_volume'], 7)}  "
                    f"KD {fmt(row['keyword_difficulty'], 4)}  "
                    f"etv {fmt(row['etv'])}"
                )
                print(f"           {row['url']}")

        payload["domains"][domain] = {"metrics": metrics, "ranked_keywords": ranked}

    stem = f"{datetime.now().strftime('%Y-%m-%d')}-domain-visibility-data"
    out_path = project.output_path(f"{stem}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print(f"Raw data: {project.rel(out_path)}")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())
