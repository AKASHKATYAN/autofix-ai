import chromadb
import uuid
from app.logging import logger


class VectorStore:

    def __init__(
        self,
        collection_name: str = "autofix"
    ):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=collection_name
            )
        )

        logger.info(
            f"Vector store initialized: {collection_name}"
        )
        
    def add_documents(
        self,
        documents: list
    ):

        ids = []
        texts = []

        for index, document in enumerate(
            documents
        ):

            ids.append(
                str(uuid.uuid4())
            )

            texts.append(
                document.content
            )

        self.collection.add(
            ids=ids,
            documents=texts
        )

        logger.info(
            f"Stored {len(documents)} documents"
        ) 
        
    def search(
    self,
    query: str,
    n_results: int = 5
    ):

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )

        logger.info(
            f"Retrieved {n_results} results"
        )

        return results       