from app.tools.search import web_search

result = web_search({
    "query": "Latest AI news"
})

print("\n========== SEARCH RESULTS ==========")
print(result)