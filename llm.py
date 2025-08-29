from transformers import pipeline
from functools import lru_cache
from config import HF_TOKEN, LLM_MODEL_ID

@lru_cache(maxsize=1)
def _llm():
    return pipeline(
        "text-generation",
        model=LLM_MODEL_ID,
        token=HF_TOKEN
    )

def ask_with_context(query: str, context: str, max_new_tokens: int = 300) -> str:
    prompt = f"""You are a careful personal-finance assistant. Use the provided context to answer.
Cite facts only if implied by the context. If unknown, say so briefly.

Context:
{context}

Question:
{query}

Answer clearly and practically:
"""
    gen = _llm()(prompt, max_new_tokens=max_new_tokens, do_sample=True)
    return gen[0]["generated_text"]
