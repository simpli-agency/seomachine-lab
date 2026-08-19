#!/usr/bin/env python3
"""
Research GSC Search Footprint

Dumps the raw Google Search Console footprint for a project: totals, query rows,
page rows and query+page rows over two windows (default 90d and 30d), plus a
position-bucket breakdown. Writes JSON + CSV artifacts into the project's
research directory.

Also records which property shapes are actually reachable by the service
account, so a report can state the property shape as fact rather than guess.
"""

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timedelta

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "data_sources"))

from modules.project_config import add_project_argument, load_project  # noqa: E402

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
ROW_LIMIT = 25000

POSITION_BUCKETS = [
    ("1-3", 3.0),
    ("4-10", 10.0),
    ("10-30", 30.0),
    ("30+", float("inf")),
]


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    add_project_argument(parser)
    parser.add_argument("--property", default=None, help="Override the GSC property URL")
    parser.add_argument("--long-window", type=int, default=90)
    parser.add_argument("--short-window", type=int, default=30)
    parser.add_argument(
        "--lag-days",
        type=int,
        default=1,
        help="Days to shift the end date back; GSC finalises data with a delay",
    )
    return parser.parse_args()


def build_service(credentials_path):
    if not credentials_path or not os.path.exists(credentials_path):
        raise SystemExit(f"GSC credentials file not found: {credentials_path}")
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path, scopes=SCOPES
    )
    return build("searchconsole", "v1", credentials=credentials), credentials.service_account_email


def window(end_date, days):
    start = end_date - timedelta(days=days - 1)
    return start.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")


def query_rows(service, site_url, start, end, dimensions):
    body = {
        "startDate": start,
        "endDate": end,
        "dimensions": dimensions,
        "rowLimit": ROW_LIMIT,
    }
    if not dimensions:
        body.pop("dimensions")
    response = service.searchanalytics().query(siteUrl=site_url, body=body).execute()

    rows = []
    for row in response.get("rows", []):
        entry = {dim: value for dim, value in zip(dimensions, row.get("keys", []))}
        entry.update(
            {
                "clicks": row["clicks"],
                "impressions": row["impressions"],
                "ctr": round(row["ctr"], 6),
                "position": round(row["position"], 2),
            }
        )
        rows.append(entry)
    rows.sort(key=lambda r: (-r["impressions"], -r["clicks"]))
    return rows


def totals(service, site_url, start, end):
    response = (
        service.searchanalytics()
        .query(siteUrl=site_url, body={"startDate": start, "endDate": end})
        .execute()
    )
    rows = response.get("rows", [])
    if not rows:
        return {"clicks": 0, "impressions": 0, "ctr": 0.0, "position": None}
    row = rows[0]
    return {
        "clicks": row["clicks"],
        "impressions": row["impressions"],
        "ctr": round(row["ctr"], 6),
        "position": round(row["position"], 2),
    }


def bucket_rows(rows):
    """Group rows by average position, upper bound inclusive"""
    buckets = {label: {"rows": 0, "clicks": 0, "impressions": 0} for label, _ in POSITION_BUCKETS}
    for row in rows:
        for label, upper in POSITION_BUCKETS:
            if row["position"] <= upper:
                buckets[label]["rows"] += 1
                buckets[label]["clicks"] += row["clicks"]
                buckets[label]["impressions"] += row["impressions"]
                break
    return buckets


def probe_properties(service, candidates):
    """Which property shapes the service account can actually query.

    The service account is shared across unrelated projects, so only properties
    matching this project's candidates are recorded - other clients' domains
    must not leak into a committed artifact.
    """
    listed = {}
    listed_total = None
    try:
        entries = service.sites().list().execute().get("siteEntry", [])
        listed_total = len(entries)
        listed = {
            entry["siteUrl"]: entry.get("permissionLevel")
            for entry in entries
            if entry["siteUrl"] in candidates
        }
    except HttpError as exc:
        listed = {"error": str(exc.status_code)}

    probes = {}
    for candidate in candidates:
        try:
            service.searchanalytics().query(
                siteUrl=candidate,
                body={"startDate": "2026-01-01", "endDate": "2026-01-02", "rowLimit": 1},
            ).execute()
            probes[candidate] = {"reachable": True, "status": 200}
        except HttpError as exc:
            probes[candidate] = {"reachable": False, "status": exc.status_code}
    return {"listed": listed, "listed_total": listed_total, "probes": probes}


def write_csv(path, rows, columns):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main():
    args = parse_args()
    project = load_project(args.project)
    site_url = args.property or project.gsc_site_url
    if not site_url:
        raise SystemExit("No GSC property: set gsc_site_url in project.json or pass --property")

    service, service_account_email = build_service(os.getenv("GSC_CREDENTIALS_PATH"))

    end_date = datetime.now() - timedelta(days=args.lag_days)
    long_start, long_end = window(end_date, args.long_window)
    short_start, short_end = window(end_date, args.short_window)

    print(f"Project: {project.slug}")
    print(f"Property: {site_url}")
    print(f"Service account: {service_account_email}")
    print(f"Long window:  {long_start} .. {long_end} ({args.long_window}d)")
    print(f"Short window: {short_start} .. {short_end} ({args.short_window}d)")

    domain = project.domain or ""
    access = probe_properties(
        service,
        [site_url, f"https://{domain}/" if domain else None, f"sc-domain:{domain}" if domain else None],
    )
    access["probes"] = {k: v for k, v in access["probes"].items() if k}
    print(f"Properties visible to the service account: {list(access['listed'])}")
    print(f"Probe results: {json.dumps(access['probes'])}")

    data = {}
    for label, (start, end) in {
        "long": (long_start, long_end),
        "short": (short_start, short_end),
    }.items():
        data[label] = {
            "start_date": start,
            "end_date": end,
            "totals": totals(service, site_url, start, end),
            "queries": query_rows(service, site_url, start, end, ["query"]),
            "pages": query_rows(service, site_url, start, end, ["page"]),
        }

    data["long"]["query_page"] = query_rows(service, site_url, long_start, long_end, ["query", "page"])
    data["long"]["by_date"] = query_rows(service, site_url, long_start, long_end, ["date"])
    data["long"]["by_country"] = query_rows(service, site_url, long_start, long_end, ["country"])
    data["long"]["by_device"] = query_rows(service, site_url, long_start, long_end, ["device"])

    for label in ("long", "short"):
        data[label]["query_buckets"] = bucket_rows(data[label]["queries"])
        data[label]["page_buckets"] = bucket_rows(data[label]["pages"])

    date_str = datetime.now().strftime("%Y-%m-%d")
    out = lambda name: project.output_path(f"{date_str}-{name}")

    kw_cols = ["query", "clicks", "impressions", "ctr", "position"]
    page_cols = ["page", "clicks", "impressions", "ctr", "position"]

    write_csv(out(f"gsc-queries-{args.long_window}d.csv"), data["long"]["queries"], kw_cols)
    write_csv(out(f"gsc-queries-{args.short_window}d.csv"), data["short"]["queries"], kw_cols)
    write_csv(out(f"gsc-pages-{args.long_window}d.csv"), data["long"]["pages"], page_cols)
    write_csv(out(f"gsc-pages-{args.short_window}d.csv"), data["short"]["pages"], page_cols)
    write_csv(
        out(f"gsc-query-page-{args.long_window}d.csv"),
        data["long"]["query_page"],
        ["query", "page", "clicks", "impressions", "ctr", "position"],
    )

    summary = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "project": project.slug,
        "domain": project.domain,
        "property": site_url,
        "service_account_email": service_account_email,
        "access": access,
        "windows": {
            f"{args.long_window}d": {
                "start_date": long_start,
                "end_date": long_end,
                "totals": data["long"]["totals"],
                "query_rows": len(data["long"]["queries"]),
                "page_rows": len(data["long"]["pages"]),
                "query_page_rows": len(data["long"]["query_page"]),
                "query_buckets": data["long"]["query_buckets"],
                "page_buckets": data["long"]["page_buckets"],
                "top_queries": data["long"]["queries"][:50],
                "top_pages": data["long"]["pages"][:50],
                "query_page": data["long"]["query_page"][:100],
                "by_date": data["long"]["by_date"],
                "by_country": data["long"]["by_country"],
                "by_device": data["long"]["by_device"],
            },
            f"{args.short_window}d": {
                "start_date": short_start,
                "end_date": short_end,
                "totals": data["short"]["totals"],
                "query_rows": len(data["short"]["queries"]),
                "page_rows": len(data["short"]["pages"]),
                "query_buckets": data["short"]["query_buckets"],
                "page_buckets": data["short"]["page_buckets"],
                "top_queries": data["short"]["queries"][:50],
                "top_pages": data["short"]["pages"][:50],
            },
        },
    }

    summary_path = out("gsc-summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    for label, days in (("long", args.long_window), ("short", args.short_window)):
        t = data[label]["totals"]
        print(
            f"\n{days}d totals: clicks={t['clicks']} impressions={t['impressions']} "
            f"ctr={t['ctr']:.4f} avg_position={t['position']}"
        )
        print(f"  query rows: {len(data[label]['queries'])}, page rows: {len(data[label]['pages'])}")
        print(f"  query buckets: {json.dumps(data[label]['query_buckets'])}")

    print(f"\nSaved: {project.rel(summary_path)}")


if __name__ == "__main__":
    main()
