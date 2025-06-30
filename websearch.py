import requests

def get_web_context(query):
    url = f"https://api.duckduckgo.com/?q={query}&format=json"
    resp = requests.get(url).json()
    return resp.get("AbstractText", "No result found.")
