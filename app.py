from fastapi import FastAPI, UploadFile, File
import shutil
from ingestion.loader import load_document
from rag.chunking import chunk_text
from rag.embeddings import get_embedding
from rag.vector_store import VectorStore
from agents.orchestrator import run_agent

app = FastAPI()
vector_store = VectorStore()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = load_document(path)
    chunks = chunk_text(text)

    embeddings = [get_embedding(c) for c in chunks]
    vector_store.add(embeddings, chunks)

    return {"message": "Document processed"}

@app.get("/query/")
def query(q: str):
    return run_agent(q, vector_store)