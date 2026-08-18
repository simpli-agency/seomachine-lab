"""
DataForSEO API Integration

Fetches SERP data, competitor rankings, keyword research, and more.
"""

import os
import base64
import requests
from typing import Dict, List, Optional, Any
from datetime import datetime


class DataForSEO:
    """DataForSEO API client"""

    # Class-level defaults for the target market. Instances override them from
    # the constructor args or the environment; a project config can set both.
    location_code = 2840  # USA
    language_code = "en"

    def __init__(
        self,
        login: Optional[str] = None,
        password: Optional[str] = None,
        location_code: Optional[int] = None,
        language_code: Optional[str] = None,
    ):
        """
        Initialize DataForSEO client

        Args:
            login: API login (defaults to env var)
            password: API password (defaults to env var)
            location_code: Default DataForSEO location code for every call
                (defaults to env var DATAFORSEO_LOCATION_CODE, then 2840/USA)
            language_code: Default language code for every call
                (defaults to env var DATAFORSEO_LANGUAGE_CODE, then "en")
        """
        self.login = login or os.getenv("DATAFORSEO_LOGIN")
        self.password = password or os.getenv("DATAFORSEO_PASSWORD")
        self.base_url = os.getenv("DATAFORSEO_BASE_URL", "https://api.dataforseo.com")
        resolved_location = location_code or os.getenv("DATAFORSEO_LOCATION_CODE")
        if resolved_location:
            self.location_code = int(resolved_location)
        resolved_language = language_code or os.getenv("DATAFORSEO_LANGUAGE_CODE")
        if resolved_language:
            self.language_code = resolved_language

        if not self.login or not self.password:
            raise ValueError("DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD must be set")

        # Create auth header
        cred = f"{self.login}:{self.password}"
        encoded_cred = base64.b64encode(cred.encode("ascii")).decode("ascii")
        self.headers = {
            "Authorization": f"Basic {encoded_cred}",
            "Content-Type": "application/json",
        }

        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _loc(self, location_code: Optional[int] = None) -> int:
        """Resolve a location code, falling back to the client default"""
        return int(location_code) if location_code is not None else self.location_code

    def _lang(self, language_code: Optional[str] = None) -> str:
        """Resolve a language code, falling back to the client default"""
        return language_code or self.language_code

    def _post(self, endpoint: str, data: List[Dict]) -> Dict:
        """Make POST request to DataForSEO API"""
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def _first_task(self, response: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        tasks = response.get("tasks")
        if isinstance(tasks, list) and tasks:
            first = tasks[0]
            if isinstance(first, dict):
                return first
        return None

    def _first_result(self, task: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        result = task.get("result")
        if isinstance(result, list) and result:
            first = result[0]
            if isinstance(first, dict):
                return first
        return None

    def get_rankings(
        self,
        domain: str,
        keywords: List[str],
        location_code: Optional[int] = None,
        language_code: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get ranking positions for specific keywords

        Args:
            domain: Your domain (e.g., "castos.com")
            keywords: List of keywords to check
            location_code: DataForSEO location code (defaults to client setting)
            language_code: Language code

        Returns:
            List of ranking data for each keyword
        """
        tasks = []
        for keyword in keywords:
            tasks.append(
                {
                    "keyword": keyword,
                    "location_code": self._loc(location_code),
                    "language_code": self._lang(language_code),
                    "device": "desktop",
                    "os": "windows",
                }
            )

        response = self._post("/v3/serp/google/organic/live/advanced", tasks)

        results = []
        if response["status_code"] == 20000:
            for task in response.get("tasks", []):
                if task.get("status_code") == 20000:
                    keyword = task.get("data", {}).get("keyword")
                    result = self._first_result(task)
                    if not keyword or result is None:
                        continue
                    items = result.get("items", [])

                    # Find domain position
                    position = None
                    url = None
                    for i, item in enumerate(items, 1):
                        if domain in item.get("domain", ""):
                            position = i
                            url = item.get("url")
                            break

                    results.append(
                        {
                            "keyword": keyword,
                            "domain": domain,
                            "position": position,
                            "url": url,
                            "ranking": position is not None,
                            "search_volume": result.get("keyword_data", {})
                            .get("keyword_info", {})
                            .get("search_volume"),
                            "cpc": result.get("keyword_data", {})
                            .get("keyword_info", {})
                            .get("cpc"),
                        }
                    )

        return results

    def get_serp_data(
        self,
        keyword: str,
        location_code: Optional[int] = None,
        limit: int = 100,
        language_code: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get complete SERP data for a keyword

        Args:
            keyword: Search keyword
            location_code: DataForSEO location code
            limit: Number of results to return

        Returns:
            Dict with SERP data including all ranking pages
        """
        data = [
            {
                "keyword": keyword,
                "location_code": self._loc(location_code),
                "language_code": self._lang(language_code),
                "device": "desktop",
                "os": "windows",
                "depth": limit,
            }
        ]

        response = self._post("/v3/serp/google/organic/live/advanced", data)

        if response["status_code"] != 20000:
            return {"error": "API request failed"}

        task = self._first_task(response)
        if not task or task.get("status_code") != 20000:
            return {"error": "Task failed"}

        result = self._first_result(task)
        if result is None:
            return {"error": "Task returned no results"}

        # Extract organic results
        organic_results = []
        for item in result.get("items", []):
            if item["type"] == "organic":
                organic_results.append(
                    {
                        "position": item.get("rank_absolute"),
                        "url": item.get("url"),
                        "domain": item.get("domain"),
                        "title": item.get("title"),
                        "description": item.get("description"),
                        "breadcrumb": item.get("breadcrumb"),
                    }
                )

        # Extract SERP features
        features = []
        for item in result.get("items", []):
            if item["type"] != "organic":
                features.append(item["type"])

        keyword_data = result.get("keyword_data", {}).get("keyword_info", {})

        return {
            "keyword": keyword,
            "search_volume": keyword_data.get("search_volume"),
            "cpc": keyword_data.get("cpc"),
            "competition": keyword_data.get("competition"),
            "organic_results": organic_results,
            "features": list(set(features)),
            "total_results": result.get("items_count", 0),
        }

    def analyze_competitor(
        self,
        competitor_domain: str,
        keywords: List[str],
        your_domain: Optional[str] = None,
        location_code: Optional[int] = None,
        language_code: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Analyze competitor rankings vs yours

        Args:
            competitor_domain: Competitor's domain
            keywords: Keywords to compare
            your_domain: Your domain (optional)

        Returns:
            Comparative ranking analysis
        """
        tasks = []
        for keyword in keywords:
            tasks.append(
                {
                    "keyword": keyword,
                    "location_code": self._loc(location_code),
                    "language_code": self._lang(language_code),
                    "device": "desktop",
                }
            )

        response = self._post("/v3/serp/google/organic/live/advanced", tasks)

        comparison = []
        for i, task in enumerate(response.get("tasks", [])):
            if task.get("status_code") == 20000:
                keyword = keywords[i]
                result = self._first_result(task)
                if result is None:
                    continue
                items = result.get("items", [])

                competitor_pos = None
                your_pos = None

                for j, item in enumerate(items, 1):
                    domain = item.get("domain", "")
                    if competitor_domain in domain:
                        competitor_pos = j
                    if your_domain and your_domain in domain:
                        your_pos = j

                gap = None
                if competitor_pos and your_pos:
                    gap = your_pos - competitor_pos
                elif competitor_pos and not your_pos:
                    gap = "Not ranking"

                comparison.append(
                    {
                        "keyword": keyword,
                        "competitor_position": competitor_pos,
                        "your_position": your_pos,
                        "gap": gap,
                        "opportunity": "high"
                        if competitor_pos and not your_pos
                        else "medium"
                        if isinstance(gap, (int, float)) and gap > 10
                        else "low",
                    }
                )

        return {
            "competitor": competitor_domain,
            "your_domain": your_domain,
            "comparison": comparison,
        }

    def get_keyword_ideas(
        self,
        seed_keyword: str,
        location_code: Optional[int] = None,
        limit: int = 100,
        language_code: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get related keyword ideas

        Args:
            seed_keyword: Starting keyword
            location_code: Location code
            limit: Number of ideas to return

        Returns:
            List of related keywords with search volume, difficulty
        """
        data = [
            {
                "keyword": seed_keyword,
                "location_code": self._loc(location_code),
                "language_code": self._lang(language_code),
                "include_serp_info": True,
                "limit": limit,
            }
        ]

        response = self._post("/v3/dataforseo_labs/google/related_keywords/live", data)

        if response["status_code"] != 20000:
            return []

        task = self._first_task(response)
        if not task or task.get("status_code") != 20000:
            return []

        result = self._first_result(task)
        if result is None:
            return []

        keywords = []
        for item in result.get("items", []):
            keywords.append(
                {
                    "keyword": item.get("keyword_data", {}).get("keyword"),
                    "search_volume": item.get("keyword_data", {})
                    .get("keyword_info", {})
                    .get("search_volume"),
                    "cpc": item.get("keyword_data", {})
                    .get("keyword_info", {})
                    .get("cpc"),
                    "competition": item.get("keyword_data", {})
                    .get("keyword_info", {})
                    .get("competition"),
                    "avg_position": item.get("serp_info", {}).get("se_results_count"),
                }
            )

        # Sort by search volume
        keywords.sort(key=lambda x: x["search_volume"] or 0, reverse=True)

        return keywords

    def _market(
        self,
        location_code: Optional[int] = None,
        language_code: Optional[str] = None,
        worldwide: bool = False,
    ) -> Dict[str, Any]:
        """
        Market keys for a request payload.

        Worldwide runs omit both keys - that is how DataForSEO asks for global
        data, and it is the only way to size a topic whose demand sits outside
        the project's default country.
        """
        if worldwide:
            return {}
        return {
            "location_code": self._loc(location_code),
            "language_code": self._lang(language_code),
        }

    def get_search_volume(
        self,
        keywords: List[str],
        location_code: Optional[int] = None,
        language_code: Optional[str] = None,
        worldwide: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Get Google Ads search volume for exact keywords

        Uses the Google Ads data source rather than DataForSEO Labs. Labs only
        knows keywords it has crawled a SERP for, so long-tail phrases often
        come back missing entirely; Google Ads returns a row for every keyword
        asked about, with search_volume None or 0 when it is below threshold.

        Args:
            keywords: Exact keywords to look up (max 1000 per call)
            location_code: Location code
            language_code: Language code
            worldwide: Ignore the market and ask for global volume

        Returns:
            List of dicts with volume, CPC and competition, by volume desc
        """
        payload = {"keywords": keywords[:1000], "search_partners": False}
        payload.update(self._market(location_code, language_code, worldwide))

        response = self._post(
            "/v3/keywords_data/google_ads/search_volume/live", [payload]
        )

        if response["status_code"] != 20000:
            return []

        task = self._first_task(response)
        if not task or task.get("status_code") != 20000:
            return []

        volumes = []
        for item in task.get("result") or []:
            if not isinstance(item, dict):
                continue
            volumes.append(
                {
                    "keyword": item.get("keyword"),
                    "search_volume": item.get("search_volume"),
                    "cpc": item.get("cpc"),
                    "competition": item.get("competition"),
                    "competition_index": item.get("competition_index"),
                    "low_top_of_page_bid": item.get("low_top_of_page_bid"),
                    "high_top_of_page_bid": item.get("high_top_of_page_bid"),
                }
            )

        volumes.sort(key=lambda x: x["search_volume"] or 0, reverse=True)

        return volumes

    def get_keyword_overview(
        self,
        keywords: List[str],
        location_code: Optional[int] = None,
        language_code: Optional[str] = None,
        worldwide: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Get volume, CPC, competition, difficulty and intent for exact keywords

        Unlike get_keyword_ideas() this does not expand the seed - it returns
        metrics for the keywords passed in, so it is the cheap way to size a
        seed list. Keywords below the provider's volume threshold come back
        with search_volume None, which means "no data", not "no demand".

        Args:
            keywords: Exact keywords to look up (max 700 per call)
            location_code: Location code
            language_code: Language code

        Returns:
            List of dicts with metrics per keyword, sorted by search volume
        """
        payload = {"keywords": keywords[:700], "include_serp_info": False}
        payload.update(self._market(location_code, language_code, worldwide))
        data = [payload]

        response = self._post("/v3/dataforseo_labs/google/keyword_overview/live", data)

        if response["status_code"] != 20000:
            return []

        task = self._first_task(response)
        if not task or task.get("status_code") != 20000:
            return []

        result = self._first_result(task)
        if result is None:
            return []

        overview = []
        for item in result.get("items", []):
            info = item.get("keyword_info") or {}
            props = item.get("keyword_properties") or {}
            intent = item.get("search_intent_info") or {}
            overview.append(
                {
                    "keyword": item.get("keyword"),
                    "search_volume": info.get("search_volume"),
                    "cpc": info.get("cpc"),
                    "competition": info.get("competition"),
                    "competition_level": info.get("competition_level"),
                    "keyword_difficulty": props.get("keyword_difficulty"),
                    "main_intent": intent.get("main_intent"),
                    "monthly_searches": info.get("monthly_searches"),
                }
            )

        overview.sort(key=lambda x: x["search_volume"] or 0, reverse=True)

        return overview

    def get_keyword_suggestions(
        self,
        seed_keyword: str,
        location_code: Optional[int] = None,
        limit: int = 50,
        language_code: Optional[str] = None,
        worldwide: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Get long-tail keywords that contain the seed phrase

        Complements get_keyword_ideas(): suggestions are full-text matches on
        the seed, which is what surfaces demand hiding under a long-tail seed
        that has no volume of its own.

        Args:
            seed_keyword: Phrase the suggestions must contain
            location_code: Location code
            limit: Number of suggestions to return
            language_code: Language code

        Returns:
            List of keywords with volume, CPC, competition and difficulty
        """
        payload = {
            "keyword": seed_keyword,
            "include_seed_keyword": True,
            "limit": limit,
            "order_by": ["keyword_info.search_volume,desc"],
        }
        payload.update(self._market(location_code, language_code, worldwide))
        data = [payload]

        response = self._post(
            "/v3/dataforseo_labs/google/keyword_suggestions/live", data
        )

        if response["status_code"] != 20000:
            return []

        task = self._first_task(response)
        if not task or task.get("status_code") != 20000:
            return []

        result = self._first_result(task)
        if result is None:
            return []

        suggestions = []
        for item in result.get("items", []):
            info = item.get("keyword_info") or {}
            props = item.get("keyword_properties") or {}
            suggestions.append(
                {
                    "keyword": item.get("keyword"),
                    "search_volume": info.get("search_volume"),
                    "cpc": info.get("cpc"),
                    "competition": info.get("competition"),
                    "keyword_difficulty": props.get("keyword_difficulty"),
                }
            )

        suggestions.sort(key=lambda x: x["search_volume"] or 0, reverse=True)

        return suggestions

    def get_questions(
        self,
        keyword: str,
        location_code: Optional[int] = None,
        limit: int = 50,
        language_code: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get question-based queries related to keyword

        Args:
            keyword: Seed keyword
            location_code: Location code
            limit: Number of questions to return

        Returns:
            List of question queries
        """
        data = [
            {
                "keyword": keyword,
                "location_code": self._loc(location_code),
                "language_code": self._lang(language_code),
                "limit": limit,
            }
        ]

        response = self._post("/v3/dataforseo_labs/google/related_keywords/live", data)

        if response["status_code"] != 20000:
            return []

        task = self._first_task(response)
        if not task or task.get("status_code") != 20000:
            return []

        result = self._first_result(task)
        if result is None:
            return []

        questions = []
        for item in result.get("items", []):
            kw = item.get("keyword_data", {}).get("keyword", "")

            # Filter for questions
            if any(
                kw.lower().startswith(q)
                for q in [
                    "how",
                    "what",
                    "why",
                    "when",
                    "where",
                    "who",
                    "can",
                    "should",
                    "is",
                    "are",
                    "does",
                ]
            ):
                questions.append(
                    {
                        "question": kw,
                        "search_volume": item.get("keyword_data", {})
                        .get("keyword_info", {})
                        .get("search_volume"),
                        "cpc": item.get("keyword_data", {})
                        .get("keyword_info", {})
                        .get("cpc"),
                    }
                )

        # Sort by search volume
        questions.sort(key=lambda x: x["search_volume"] or 0, reverse=True)

        return questions

    def get_domain_metrics(
        self,
        domain: str,
        location_code: Optional[int] = None,
        language_code: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get domain overview metrics

        Args:
            domain: Domain to analyze

        Returns:
            Dict with domain metrics
        """
        data = [
            {
                "target": domain,
                "location_code": self._loc(location_code),
                "language_code": self._lang(language_code),
            }
        ]

        response = self._post("/v3/dataforseo_labs/google/domain_metrics/live", data)

        if response["status_code"] != 20000:
            return {}

        task = self._first_task(response)
        if not task or task.get("status_code") != 20000:
            return {}

        result = self._first_result(task)
        if result is None:
            return {}

        items = result.get("items", [])
        first_item = items[0] if items else {}
        metrics = first_item.get("metrics", {}) if isinstance(first_item, dict) else {}

        return {
            "domain": domain,
            "organic_keywords": metrics.get("organic", {}).get("count"),
            "organic_traffic": metrics.get("organic", {}).get("etv"),
            "domain_rank": metrics.get("organic", {}).get("rank"),
            "backlinks": metrics.get("backlinks", {}),
        }

    def check_ranking_history(
        self,
        domain: str,
        keyword: str,
        months_back: int = 3,
        location_code: Optional[int] = None,
        language_code: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """
        Get ranking history for a keyword (requires historical data)

        Args:
            domain: Your domain
            keyword: Keyword to track
            months_back: Months of history

        Returns:
            List of historical rankings
        """
        # Note: This requires DataForSEO's ranking tracking to be set up
        # This is a simplified version - actual implementation may vary

        data = [
            {
                "target": domain,
                "keyword": keyword,
                "location_code": self._loc(location_code),
                "language_code": self._lang(language_code),
            }
        ]

        try:
            response = self._post("/v3/serp/google/organic/ranking_history/live", data)

            if response["status_code"] == 20000:
                task = self._first_task(response)
                if task and task.get("status_code") == 20000:
                    result = self._first_result(task)
                    if result is not None:
                        return result.get("items", [])
        except:
            pass

        return []


# Example usage
if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv("data_sources/config/.env")

    dfs = DataForSEO()

    print("Checking rankings for Castos...")
    rankings = dfs.get_rankings(
        domain="castos.com",
        keywords=["podcast hosting", "podcast analytics", "private podcast"],
    )

    for rank in rankings:
        print(f"\nKeyword: {rank['keyword']}")
        print(f"Position: {rank['position'] or 'Not ranking'}")
        print(
            f"Search Volume: {rank['search_volume']:,}"
            if rank["search_volume"]
            else "Search Volume: N/A"
        )

    print("\n\nGetting SERP data for 'podcast monetization'...")
    serp = dfs.get_serp_data("podcast monetization")

    print(f"Search Volume: {serp['search_volume']:,}")
    print(f"SERP Features: {', '.join(serp['features'])}")
    print(f"\nTop 10 Results:")
    for result in serp["organic_results"][:10]:
        print(f"{result['position']}. {result['domain']}")
        print(f"   {result['url']}")

    print("\n\nRelated questions for 'podcast monetization':")
    questions = dfs.get_questions("podcast monetization")
    for q in questions[:10]:
        print(f"- {q['question']}")
        print(
            f"  Volume: {q['search_volume']:,}"
            if q["search_volume"]
            else "  Volume: N/A"
        )
