from rag.embeddings import get_embedding

def retrieve(query, vector_store, top_k=5):
    q_emb = get_embedding(query)
    return vector_store.search(q_emb, top_k)