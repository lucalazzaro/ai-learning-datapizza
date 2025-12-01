# tools.py
from ddgs import DDGS
from datapizza.tools import tool

@tool
def web_search(query: str) -> str:
    """
    Simple DuckDuckGo search tool.

    The agent will call this tool when it needs fresh information.
    It returns a short, text-only summary of results.
    """
    if not query:
        return "No query provided."

    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            title = (r.get("title") or "").strip()
            snippet = (r.get("body") or "").strip()
            url = (r.get("href") or "").strip()

            if not title and not snippet:
                continue

            results.append(f"- {title}\n  {snippet}\n  {url}")

    if not results:
        return "No results found."

    return "Web Search Results:\n" + "\n\n".join(results)


