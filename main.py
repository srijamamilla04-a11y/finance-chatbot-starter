from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from retriever.loader import load_and_split_pdf
from retriever.vectorstore import build_vectorstore, similarity_search
from models.llm import ask_with_context
from utils.prompts import build_budget_prompt
from utils.validation import validate_expenses

# Load knowledge base into FAISS on startup
DOC_PATH = "data/knowledge_base/Personal Finance Chatbot Intelligent Guidance for Savings, Taxes, and Investments.pdf"
docs = []
vectorstore = None

app = FastAPI(title="Finance Chatbot API", version="0.1.0")

@app.on_event("startup")
def _startup():
    global docs, vectorstore
    try:
        docs = load_and_split_pdf(DOC_PATH)
        vectorstore = build_vectorstore(docs)
        print(f"Loaded {len(docs)} chunks into vector store")
    except Exception as e:
        print("Vector store load failed:", e)

class AskRequest(BaseModel):
    query: str
    k: int = 3

@app.post("/ask")
def ask(req: AskRequest):
    if vectorstore is None:
        return {"error": "Vector store not available"}
    results = similarity_search(req.query, vectorstore, k=req.k)
    context = "\n\n".join([r.page_content for r in results])
    answer = ask_with_context(req.query, context)
    return {"answer": answer, "context": context}

class BudgetRequest(BaseModel):
    income: float
    expenses: Dict[str, float]
    goal: str
    persona: str = "student"

@app.post("/budget-summary")
def budget_summary(req: BudgetRequest):
    expenses = validate_expenses(req.expenses)
    prompt = build_budget_prompt(req.income, expenses, req.goal, req.persona)
    # Reuse LLM with no retrieval
    answer = ask_with_context(prompt, context="")
    return {"summary": answer}
