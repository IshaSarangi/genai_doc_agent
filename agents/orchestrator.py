from agents.planner import plan
from rag.retriever import retrieve
from agents.analyzer import generate_answer
from agents.validator import validate

def run_agent(query, vector_store):
    print("DEBUG: Vector store size:", len(vector_store.texts))

    if not vector_store.texts:
        return {
            "answer": "No documents uploaded yet.",
            "validation": "N/A",
            "sources": []
        }

    context = retrieve(query, vector_store)
    print("DEBUG: Retrieved context:", context)

    if not context:
        return {
            "answer": "No relevant context found.",
            "validation": "N/A",
            "sources": []
        }

    answer = generate_answer(query, context)
    validation = validate(answer, context)

    return {
        "answer": answer,
        "validation": validation,
        "sources": context
    }