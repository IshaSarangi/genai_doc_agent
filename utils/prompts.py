GENERATOR_PROMPT = """
Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

VALIDATOR_PROMPT = """
Check if the answer is grounded in context.

Context:
{context}

Answer:
{answer}
"""