from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/search")
def search_web(query: str):
    url = f"https://duckduckgo.com/html/?q={query}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("a", class_="result__a")
    if results:
        return {"answer": results[0].get_text()}
    return {"answer": "No search result found."}
