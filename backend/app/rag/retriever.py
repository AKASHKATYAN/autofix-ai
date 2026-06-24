from app.logging import logger

from app.rag.vector_store import (
    VectorStore
)


class Retriever:

    def __init__(
        self,
        collection_name: str = "autofix"
    ):

        self.vector_store = VectorStore(
            collection_name=collection_name
        )

    def retrieve(
        self,
        query: str,
        n_results: int = 5
    ):

        results = self.vector_store.search(
            query=query,
            n_results=n_results
        )

        logger.info(
            f"Retrieved {len(results['documents'])} chunks"
        )

        return results