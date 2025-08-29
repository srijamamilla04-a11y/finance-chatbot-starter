from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from functools import lru_cache
from config import EMBED_MODEL_ID, HF_TOKEN

@lru_cache(maxsize=1)
def _load_model():
    tokenizer = AutoTokenizer.from_pretrained(EMBED_MODEL_ID, token=HF_TOKEN)
    model = AutoModel.from_pretrained(EMBED_MODEL_ID, token=HF_TOKEN)
    model.eval()
    return tokenizer, model

def embed_texts(texts):
    """Return a 2D numpy array (n_texts, dim)."""
    tokenizer, model = _load_model()
    with torch.no_grad():
        enc = tokenizer(
            texts,
            return_tensors="pt",
            padding=True,
            truncation=True
        )
        out = model(**enc)
        # mean pool last hidden state
        embs = out.last_hidden_state.mean(dim=1).cpu().numpy()
    return embs

def embed_text(text: str):
    return embed_texts([text])[0]
