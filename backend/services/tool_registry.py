from langchain.tools import Tool
from duckduckgo_search import DDGS

def web_search(query: str) -> str:
    results = DDGS().text(query, max_results=5)
    return "\n".join(f"{r['title']}: {r['href']}" for r in results)

def get_all_tools():
    return [
        Tool(name="WebSearch", func=web_search, description="Search the web for a query")
    ]
