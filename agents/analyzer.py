from groq import Groq
from config import LLM_MODEL
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, context):
    prompt = f"""
Answer ONLY using the provided context.

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content