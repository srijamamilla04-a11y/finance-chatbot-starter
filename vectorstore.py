from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import EMBED_MODEL_ID, HF_TOKEN

def get_embedding_fn():
    # Use HF embeddings wrapper that calls the model via transformers
    return HuggingFaceEmbeddings(
        model_name=EMBED_MODEL_ID,
        model_kwargs={"token": HF_TOKEN}
    )

def build_vectorstore(docs):
    embeddings = get_embedding_fn()
    return FAISS.from_documents(docs, embeddings)

def similarity_search(query, vectorstore, k: int = 3):
    return vectorstore.similarity_search(query, k=k)
