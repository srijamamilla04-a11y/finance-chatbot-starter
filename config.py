import os

# Hugging Face
HF_TOKEN = os.getenv("HF_TOKEN", "")  # export HF_TOKEN=hf_xxx
EMBED_MODEL_ID = "ibm-granite/granite-embedding-english-r2"

# Optional: change LLM if you have access to a different Granite model
LLM_MODEL_ID = os.getenv("LLM_MODEL_ID", "ibm-granite/granite-13b-instruct")
