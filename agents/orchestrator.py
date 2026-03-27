from agents.planner import plan
from rag.retriever import retrieve
from agents.analyzer import generate_answer
from agents.validator import validate

def run_agent(query, vector_store):
    context = retrieve(query, vector_store)
    answer = generate_answer(query, context)
    validation = validate(answer, context)

    return {
        "answer": answer,
        "validation": validation,
        "sources": context
    }