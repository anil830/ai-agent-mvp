from fastapi import FastAPI, Request
from chromadb import Client
from sentence_transformers import SentenceTransformer
import uuid

app = FastAPI()
client = Client()
collection = client.get_or_create_collection("kb")
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.post("/ingest")
async def ingest_doc(request: Request):
    data = await request.json()
    text = data["text"]
    embedding = model.encode(text).tolist()
    collection.add(documents=[text], embeddings=[embedding], ids=[str(uuid.uuid4())])
    return {"status": "ingested"}

@app.post("/query")
async def query_doc(request: Request):
    data = await request.json()
    query = data["query"]
    embedding = model.encode(query).tolist()
    results = collection.query(query_embeddings=[embedding], n_results=1)
    if results["documents"]:
        return {"answer": results["documents"][0][0]}
    return {"answer": None}
