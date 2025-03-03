from .base import BaseTool
from langchain_community.tools import GoogleSerperRun
from langchain_community.utilities import GoogleSerperAPIWrapper


class WebSearchTool(BaseTool):
    """Performs a web search using the Google Serper API.

    - Input: {"input_data": "A search query as a text string."}
    - Output: Search results in JSON format.
    """

    def __init__(self, api_key: str):
        self.api = api_key
        api_wrapper = GoogleSerperAPIWrapper(
            type="search", tbs="qdr:w1", serper_api_key=api_key
        )
        self.search = GoogleSerperRun(api_wrapper=api_wrapper)

    def __search_query(self, query: str) -> str:
        result = self.search.run(query)

        return result

    def execute(self, input_data: str) -> str:
        return self.__search_query(input_data)
