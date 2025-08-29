# Finance Chatbot (RAG + Budget Advisor)

This starter packs a FastAPI backend + Streamlit frontend, using **IBM Granite** embeddings and an LLM from Hugging Face.
It performs Retrieval-Augmented Generation (RAG) over your finance PDF and can also produce a budget summary.

## Features
- 📚 RAG over `data/knowledge_base/*`
- 🔤 Embeddings: `ibm-granite/granite-embedding-english-r2`
- 🧠 LLM (default): `ibm-granite/granite-13b-instruct` (change via `LLM_MODEL_ID` env)
- 🧮 Budget summary mode

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Set your Hugging Face token
export HF_TOKEN=hf_xxx   # Windows PowerShell: $Env:HF_TOKEN="hf_xxx"

pip install -r requirements.txt
```

> If you have GPU/CUDA, install the matching PyTorch build from https://pytorch.org/get-started/locally/

## Run

Terminal 1 (API):
```bash
uvicorn main:app --reload
```

Terminal 2 (UI):
```bash
streamlit run app.py
```

Browse: http://127.0.0.1:8501

## Customize
- Put PDFs into `data/knowledge_base/` and update `DOC_PATH` in `main.py` if needed.
- Change models in `config.py` or via env:
  - `export LLM_MODEL_ID="ibm-granite/granite-8b-instruct"`
