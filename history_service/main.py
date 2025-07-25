from fastapi import FastAPI, Request
from pymongo import MongoClient

app = FastAPI()
client = MongoClient("mongodb://localhost:27017")
db = client["ai_agent"]
collection = db["history"]

@app.post("/history")
async def save_history(request: Request):
    data = await request.json()
    collection.insert_one(data)
    return {"status": "saved"}

@app.get("/history/{chat_id}")
async def get_history(chat_id: str):
    history = list(collection.find({"chat_id": chat_id}, {"_id": 0}))
    return {"history": history}
