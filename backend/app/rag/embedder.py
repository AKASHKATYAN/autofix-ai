from sentence_transformers import (
    SentenceTransformer
)

from app.logging import logger


class Embedder:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        logger.info(
            "Embedding model loaded."
        )

    def embed_texts(
        self,
        texts: list[str]
    ):

        embeddings = self.model.encode(
            texts
        )

        return embeddings.tolist()