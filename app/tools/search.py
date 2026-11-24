from tavily import TavilyClient
from app.config.config import TAVILY_API_KEY
from app.memory.memory import save_memory

client = TavilyClient(api_key=TAVILY_API_KEY)


def web_search(parameters):

    query = parameters.get("query")

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=5
    )
    save_memory(
        command=query,
        tool="search",
        result="Web search completed"
    )
    return response