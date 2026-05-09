import os
import requests
from langchain_tavily import TavilySearch


class GeoapifyPlaceSearchTool:
    def __init__(self):
        self.api_key = os.environ.get("GEOAPIFY_API_KEY")

    def _search(self, place: str, category: str):
        url = "https://api.geoapify.com/v2/places"

        params = {
            "categories": category,
            "filter": f"place:{place}",
            "limit": 5,
            "apiKey": self.api_key
        }

        response = requests.get(url, params=params)
        data = response.json()

        results = []

        for item in data.get("features", []):
            name = item["properties"].get("name", "Unknown")
            address = item["properties"].get("formatted", "No address")
            results.append(f"{name} - {address}")

        return results

    def search_attractions(self, place: str):
        return self._search(place, "tourism.attraction")

    def search_restaurants(self, place: str):
        return self._search(place, "catering.restaurant")

    def search_activity(self, place: str):
        return self._search(place, "entertainment")

    def search_transportation(self, place: str):
        return self._search(place, "public_transport")


class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str):
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_restaurants(self, place: str):
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_activity(self, place: str):
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str):
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result