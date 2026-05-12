def run(query: str) -> str:
    from duckduckgo_search import DDGS
    results = DDGS().text(query, max_results=5)
    return "\n".join(f"{r['title']}: {r['href']}" for r in results)
