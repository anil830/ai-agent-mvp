from fastapi import FastAPI, Request
import httpx
import uuid

app = FastAPI()

CHAT_HISTORY_URL = "http://localhost:8004/history"
KNOWLEDGE_QUERY_URL = "http://localhost:8002/query"
SEARCH_URL = "http://localhost:8003/search"

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data["query"]
    chat_id = data.get("chat_id", str(uuid.uuid4()))

    async with httpx.AsyncClient() as client:
        kb_res = await client.post(KNOWLEDGE_QUERY_URL, json={"query": query})
        kb_data = kb_res.json()

        if kb_data.get("answer"):
            answer = kb_data["answer"]
        else:
            search_res = await client.get(f"{SEARCH_URL}?query={query}")
            answer = search_res.json().get("answer", "No answer found.")

        await client.post(CHAT_HISTORY_URL, json={"chat_id": chat_id, "query": query, "answer": answer})

    return {"chat_id": chat_id, "answer": answer}

@app.get("/chat/{chat_id}")
async def get_history(chat_id: str):
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{CHAT_HISTORY_URL}/{chat_id}")
        return res.json()
