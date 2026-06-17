from app.logging import logger
from app.rag.document import Document


class Chunker:

    @staticmethod
    def chunk_documents(
        documents: list[Document],
        chunk_size: int = 1000
    ):

        chunks = []

        for document in documents:

            content = document.content

            for i in range(
                0,
                len(content),
                chunk_size
            ):

                chunk = content[
                    i:i + chunk_size
                ]

                chunks.append(
                    Document(
                        content=chunk,
                        source=document.source
                    )
                )

        logger.info(
            f"Created {len(chunks)} chunks"
        )

        return chunks