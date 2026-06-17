from app.rag.embedder import (
    Embedder
)

embedder = Embedder()

embeddings = embedder.embed_texts(
    [
        "FastAPI application",
        "Machine learning model"
    ]
)

print(
    len(embeddings)
)

print(
    len(embeddings[0])
)