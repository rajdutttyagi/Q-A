from vector import retrieve_docs
def should_use_websearch(text_results, table_results):
    # If both are empty, switch to web
    return len(text_results.get("documents", [])) == 0 and len(table_results.get("documents", [])) == 0


def route_query(user_query):
    text_results, table_results = retrieve_docs(user_query)
    if should_use_websearch(text_results, table_results):
        return "web"
    return "local"
