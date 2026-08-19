#!/usr/bin/env python3
"""
GSC query -> DataForSEO follow-up

Takes the queries a project already has GSC impressions for, plus normalized
variants, and pulls exact-match DataForSEO metrics for them in the project
market, worldwide, and in any extra market passed on the command line. Ends
with a SERP pull for a short shortlist so the intent behind the queries can be
read off real results rather than guessed.
"""

import argparse
import csv
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
    parser.add_argument("--queries-csv", action="append", default=[])
    parser.add_argument("--extra-keyword", action="append", default=[])
    parser.add_argument("--serp-keyword", action="append", default=[])
    parser.add_argument(
        "--extra-market",
        action="append",
        default=[],
        help="Additional market as location_code:language_code:label",
    )
    parser.add_argument("--serp-depth", type=int, default=20)
    return parser.parse_args()


def read_queries(paths):
    queries = []
    for path in paths:
        with open(path, newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                query = (row.get("query") or "").strip()
                if query and query not in queries:
                    queries.append(query)
    return queries


def parse_markets(specs):
    markets = []
    for spec in specs:
        parts = spec.split(":")
        markets.append(
            {
                "location_code": int(parts[0]),
                "language_code": parts[1],
                "label": parts[2] if len(parts) > 2 else parts[0],
            }
        )
    return markets


def index_by_keyword(rows):
    return {(row.get("keyword") or "").lower(): row for row in rows}


def main():
    args = parse_args()
    project = load_project(args.project)
    client = DataForSEO(**project.dataforseo_kwargs())

    gsc_queries = read_queries(args.queries_csv)
    keywords = list(dict.fromkeys(gsc_queries + args.extra_keyword))
    print(f"{len(gsc_queries)} GSC queries, {len(keywords)} keywords total")

    data = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "project": project.slug,
        "gsc_queries": gsc_queries,
        "keywords": keywords,
        "markets": {},
        "worldwide_ads": [],
        "serp": {},
    }

    print("home market: keyword_overview + google_ads volume")
    home_label = f"{project.location_code}/{project.language_code}"
    data["markets"][home_label] = {
        "location_code": project.location_code,
        "language_code": project.language_code,
        "overview": client.get_keyword_overview(keywords),
        "ads": client.get_search_volume(keywords),
    }

    print("worldwide: google_ads volume")
    data["worldwide_ads"] = client.get_search_volume(keywords, worldwide=True)

    for market in parse_markets(args.extra_market):
        print(f"market {market['label']}: keyword_overview + google_ads volume")
        data["markets"][market["label"]] = {
            "location_code": market["location_code"],
            "language_code": market["language_code"],
            "overview": client.get_keyword_overview(
                keywords,
                location_code=market["location_code"],
                language_code=market["language_code"],
            ),
            "ads": client.get_search_volume(
                keywords,
                location_code=market["location_code"],
                language_code=market["language_code"],
            ),
        }

    for spec in args.serp_keyword:
        parts = spec.split("::")
        keyword = parts[0]
        location = int(parts[1]) if len(parts) > 1 else project.location_code
        language = parts[2] if len(parts) > 2 else project.language_code
        print(f"SERP: {keyword} ({location}/{language})")
        data["serp"][f"{keyword} [{location}/{language}]"] = client.get_serp_data(
            keyword,
            location_code=location,
            language_code=language,
            limit=args.serp_depth,
        )

    json_path = project.report_path("gsc-query-dataforseo-data").with_suffix(".json")
    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
    print(f"wrote {json_path}")

    csv_path = project.report_path("gsc-query-dataforseo-metrics").with_suffix(".csv")
    market_labels = list(data["markets"].keys())
    worldwide = index_by_keyword(data["worldwide_ads"])
    with open(csv_path, "w", newline="", encoding="utf-8") as handle:
        header = ["keyword", "in_gsc"]
        for label in market_labels:
            header += [
                f"{label}_volume_labs",
                f"{label}_volume_ads",
                f"{label}_kd",
                f"{label}_cpc",
                f"{label}_competition",
                f"{label}_intent",
            ]
        header.append("worldwide_volume_ads")
        writer = csv.writer(handle)
        writer.writerow(header)

        for keyword in keywords:
            row = [keyword, "yes" if keyword in gsc_queries else "no"]
            for label in market_labels:
                overview = index_by_keyword(data["markets"][label]["overview"]).get(
                    keyword.lower(), {}
                )
                ads = index_by_keyword(data["markets"][label]["ads"]).get(
                    keyword.lower(), {}
                )
                row += [
                    overview.get("search_volume"),
                    ads.get("search_volume"),
                    overview.get("keyword_difficulty"),
                    overview.get("cpc") if overview.get("cpc") is not None else ads.get("cpc"),
                    overview.get("competition_level") or ads.get("competition"),
                    overview.get("main_intent"),
                ]
            row.append(worldwide.get(keyword.lower(), {}).get("search_volume"))
            writer.writerow(row)
    print(f"wrote {csv_path}")


if __name__ == "__main__":
    main()
