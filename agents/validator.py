from groq import Groq
from config import LLM_MODEL
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def validate(answer, context):
    prompt = f"""
Check if the answer is grounded in the context.

Context:
{context}

Answer:
{answer}
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content