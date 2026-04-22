import faiss
import numpy as np
import pickle
from utils.embedder import model
import numpy as np


def save_to_faiss(embeddings, chunks):
    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    faiss.write_index(index, "vectorstore/index.faiss")

    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)


def load_faiss():
    index = faiss.read_index("vectorstore/index.faiss")

    with open("vectorstore/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    return index, chunks


def search_chunks(query, top_k=3):
    index, chunks = load_faiss()

    query_embedding = model.encode([query])

    D, I = index.search(np.array(query_embedding), top_k)

    results = [chunks[i] for i in I[0]]

    return results