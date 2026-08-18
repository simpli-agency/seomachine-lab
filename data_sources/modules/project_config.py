"""
Project Configuration

Resolves which project a research run belongs to, where its artifacts go, and
which market/domain/competitor settings apply.

A project is a directory under ``projects/`` holding a ``project.json`` file and
the research artifacts produced for it. Runs that belong to no particular
project fall back to ``projects/_general/``.

Credentials are NOT part of a project config - DataForSEO and Google service
account credentials are shared and live in the environment.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECTS_DIR = REPO_ROOT / "projects"
GENERAL_SLUG = "_general"
CONFIG_FILENAME = "project.json"
RESEARCH_SUBDIR = "research"


class ProjectConfig:
    """Settings and output paths for one research project"""

    def __init__(self, slug: str, data: Optional[Dict[str, Any]] = None):
        self.slug = slug
        self.data = data or {}

    # ---- identity ----

    @property
    def name(self) -> str:
        return self.data.get("name") or self.slug

    @property
    def domain(self) -> Optional[str]:
        return self.data.get("domain")

    @property
    def is_general(self) -> bool:
        return self.slug == GENERAL_SLUG

    # ---- market ----

    @property
    def location_code(self) -> Optional[int]:
        value = self.data.get("location_code")
        return int(value) if value else None

    @property
    def language_code(self) -> Optional[str]:
        return self.data.get("language_code")

    # ---- data sources ----

    @property
    def gsc_site_url(self) -> Optional[str]:
        """GSC property URL, falling back to the shared env var"""
        return self.data.get("gsc_site_url") or os.getenv("GSC_SITE_URL")

    @property
    def ga4_property_id(self) -> Optional[str]:
        return self.data.get("ga4_property_id") or os.getenv("GA4_PROPERTY_ID")

    @property
    def blog_path(self) -> str:
        return self.data.get("blog_path") or os.getenv("BLOG_PATH", "/blog/")

    # ---- competitors and keywords ----

    @property
    def direct_competitors(self) -> List[str]:
        return list(self.data.get("direct_competitors", []))

    @property
    def content_competitors(self) -> List[str]:
        return list(self.data.get("content_competitors", []))

    def keywords(self, bucket: str) -> List[str]:
        """Get a keyword list by bucket name, e.g. 'bofu_keywords'"""
        return list(self.data.get(bucket, []))

    def get(self, key: str, default: Any = None) -> Any:
        """Raw access to any config key"""
        return self.data.get(key, default)

    # ---- clients ----

    def dataforseo_kwargs(self) -> Dict[str, Any]:
        """Constructor kwargs carrying this project's market to DataForSEO"""
        kwargs: Dict[str, Any] = {}
        if self.location_code:
            kwargs["location_code"] = self.location_code
        if self.language_code:
            kwargs["language_code"] = self.language_code
        return kwargs

    # ---- output ----

    @property
    def dir(self) -> Path:
        return PROJECTS_DIR / self.slug

    @property
    def research_dir(self) -> Path:
        return self.dir / RESEARCH_SUBDIR

    def output_path(self, filename: str) -> Path:
        """Absolute path for an artifact, creating the directory if needed"""
        self.research_dir.mkdir(parents=True, exist_ok=True)
        return self.research_dir / filename

    def report_path(self, kind: str, suffix: str = "", date: Optional[str] = None) -> Path:
        """Path for a dated report, e.g. 'quick-wins' -> 2026-08-18-quick-wins.md"""
        date_str = date or datetime.now().strftime("%Y-%m-%d")
        stem = f"{date_str}-{kind}"
        if suffix:
            stem = f"{stem}-{suffix}"
        return self.output_path(f"{stem}.md")

    def rel(self, path: Path) -> str:
        """Repo-relative form of a path, for printing"""
        try:
            return str(path.relative_to(REPO_ROOT))
        except ValueError:
            return str(path)

    def __repr__(self) -> str:
        return f"ProjectConfig(slug={self.slug!r}, domain={self.domain!r})"


def list_projects() -> List[str]:
    """Slugs of every project directory that exists"""
    if not PROJECTS_DIR.is_dir():
        return []
    return sorted(
        p.name for p in PROJECTS_DIR.iterdir() if p.is_dir() and not p.name.startswith(".")
    )


def load_project(slug: Optional[str] = None) -> ProjectConfig:
    """
    Load a project config.

    Resolution order for the slug: explicit argument, SEO_PROJECT env var,
    then the shared '_general' bucket. A missing project.json is not an error -
    the project still resolves, it just carries no settings.
    """
    slug = slug or os.getenv("SEO_PROJECT") or GENERAL_SLUG
    config_path = PROJECTS_DIR / slug / CONFIG_FILENAME

    data: Dict[str, Any] = {}
    if config_path.is_file():
        with open(config_path, encoding="utf-8") as f:
            data = json.load(f)
    elif slug != GENERAL_SLUG:
        known = list_projects()
        hint = f" Known projects: {', '.join(known)}." if known else ""
        print(f"WARNING: {config_path} not found - running without project settings.{hint}")

    return ProjectConfig(slug, data)


def add_project_argument(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    """Add the standard --project flag to a script's arg parser"""
    parser.add_argument(
        "--project",
        "-p",
        default=None,
        help=(
            "Project slug under projects/ (defaults to $SEO_PROJECT, "
            f"then '{GENERAL_SLUG}')"
        ),
    )
    return parser


def project_from_args(description: str = "", add_help: bool = True) -> ProjectConfig:
    """
    Parse --project off the command line and load that project.

    Scripts that define their own parser pass add_help=False so that -h is
    handled by their full parser instead of this partial one.
    """
    parser = argparse.ArgumentParser(description=description, add_help=add_help)
    add_project_argument(parser)
    args, _ = parser.parse_known_args()
    return load_project(args.project)
