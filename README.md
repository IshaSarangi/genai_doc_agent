An Agentic RAG-based system that allows users to upload enterprise documents and query them using AI agents for retrieval, reasoning, and validation.

Architecture: 
User (Streamlit UI) → FastAPI Backend → Agent Orchestrator → Retriever (FAISS) → LLM (Groq) → Validator Agent → Response

Workflow:
1. Upload document
2. Chunk text
3. Generate embeddings
4. Store in vector database
5. Query input
6. Retrieve relevant chunks
7. Generate answer using LLM
8. Validate response
9. Return answer with sources

Use Cases:
- Enterprise document Q&A
- Financial analysis
- Legal document review
- Knowledge assistants
