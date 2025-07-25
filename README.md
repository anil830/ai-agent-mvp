🤖 -AI Agent MVP

A minimal AI assistant that can answer user queries using a domain-specific knowledge base, fall back to web search when needed, and maintain chat history. Built using FastAPI, ChromaDB, and DuckDuckGo.

🏗️ Architecture

               ┌───────────────┐
               │  Chat Service │
               └──────┬────────┘
                      │
    ┌─────────────────┼─────────────────┐
    ▼                 ▼                 ▼
Knowledge Base   Web Search        History Service
    Service        Service

🧠 Microservices

Service            | Port  | Description
-------------------|-------|-------------------------------------------------------
Chat Service       | 8001  | Orchestrator: Handles user queries and coordination
Knowledge Base     | 8002  | Stores documents, performs semantic search
Search Service     | 8003  | Fallback to DuckDuckGo API for answers
History Service    | 8004  | Maintains conversation history

⚙️ Technologies Used

- FastAPI (API framework)
- ChromaDB (Vector DB for Knowledge Base)
- DuckDuckGo Search API (Web fallback)
- MongoDB (Chat history storage)
- Uvicorn (ASGI server)
- Python 3.10+ (Recommended: 3.10 or 3.11)

🧩 Installation Instructions

1. Clone the Repository

git clone https://github.com/anil830/ai-agent-mvp.git
cd ai-agent-mvp

2. Set Up Python Environment (Optional but Recommended)

python -m venv venv
venv\Scripts\activate  (On Windows)
OR
source venv/bin/activate  (On Linux/Mac)

3. Install All Required Dependencies

pip install -r requirements.txt

If requirements.txt is not present, install manually for each microservice:

For all services:

pip install fastapi uvicorn httpx
------------------------------------------------

For Knowledge Base service:

pip install chromadb sentence-transformers
-------------------------------------------------

For Search service:

pip install beautifulsoup4 duckduckgo-search
-------------------------------------------------

For History service:

pip install pymongo

-------------------------------------------------

🚀 Running the Project

Start all microservices in separate terminals:

1. Start the Knowledge Base Service

cd knowledge_base_service
uvicorn main:app --reload --port 8002

2. Start the Search Service

cd ../search_service
uvicorn main:app --reload --port 8003

3. Start the History Service

cd ../history_service
uvicorn main:app --reload --port 8004

4. Start the Chat Service (Main Service)

cd ../chat_service
uvicorn main:app --reload --port 8001

🧪 API Testing

Open in browser:

Service        | Docs URL
---------------|-------------------------------
Chat           | http://127.0.0.1:8001/docs
Knowledge Base | http://127.0.0.1:8002/docs
Search         | http://127.0.0.1:8003/docs
History        | http://127.0.0.1:8004/docs

Example: Chat Endpoint

POST /chat

{
  "chat_id": "test123",
  "message": "What is the capital of France?"
}

📁 Folder Structure

ai-agent-mvp/
├── chat_service/
│   └── main.py
├── knowledge_base_service/
│   └── main.py
├── search_service/
│   └── main.py
├── history_service/
│   └── main.py
└── README.md

🧠 Sample Knowledge Base Ingestion (Optional)

Use the POST /ingest endpoint of knowledge_base_service to upload your documents.

{
  "documents": [
    {
      "id": "doc1",
      "text": "AI agents are systems that can autonomously perform tasks."
    }
  ]
}

⚠️ Common Issues

Issue                         | Solution
------------------------------|-------------------------------------------------------------
ModuleNotFoundError           | Run pip install for the missing package
'uvicorn' not recognized      | Try python -m uvicorn ... instead or check if it's installed
chromadb not found            | Run pip install chromadb
Long file path error (Windows)| Enable long path support: https://pip.pypa.io/warnings/enable-long-paths

📝 License

MIT License. Free to use and modify.

🙋‍♂️ Author

Anil Rathod
B.Tech Final Year, Anand Agricultural University
Python, PHP, MERN Stack, AI/ML Enthusiast

🌐 Project Demo 




