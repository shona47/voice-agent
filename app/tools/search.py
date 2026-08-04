from tavily import TavilyClient
from app.config.config import TAVILY_API_KEY


client = TavilyClient(api_key=TAVILY_API_KEY)


def web_search(parameters):

    query = parameters.get("query")

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=5
    )

    return response