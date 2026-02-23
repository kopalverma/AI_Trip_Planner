import os
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
from utils.place_info_search import GeoapifyPlaceSearchTool, TavilyPlaceSearchTool


class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.geoapify_places_search = GeoapifyPlaceSearchTool()
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""

        @tool
        def search_attractions(place: str) -> str:
            """Search attractions of a place"""
            try:
                results = self.geoapify_places_search.search_attractions(place)
                if results:
                    return f"Top attractions in {place}: {results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Geoapify failed due to {e}. \nFallback results: {tavily_result}"

        @tool
        def search_restaurants(place: str) -> str:
            """Search restaurants of a place"""
            try:
                results = self.geoapify_places_search.search_restaurants(place)
                if results:
                    return f"Top restaurants in {place}: {results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Geoapify failed due to {e}. \nFallback results: {tavily_result}"

        @tool
        def search_activities(place: str) -> str:
            """Search activities of a place"""
            try:
                results = self.geoapify_places_search.search_activity(place)
                if results:
                    return f"Top activities in {place}: {results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Geoapify failed due to {e}. \nFallback results: {tavily_result}"

        @tool
        def search_transportation(place: str) -> str:
            """Search transportation of a place"""
            try:
                results = self.geoapify_places_search.search_transportation(place)
                if results:
                    return f"Transportation options in {place}: {results}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Geoapify failed due to {e}. \nFallback results: {tavily_result}"

        return [
            search_attractions,
            search_restaurants,
            search_activities,
            search_transportation
        ]