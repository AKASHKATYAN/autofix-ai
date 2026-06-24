from app.logging import logger

from app.tools.repo_parser_tool import (
    RepoParserTool
)

from app.tools.file_reader_tool import (
    FileReaderTool
)

from app.rag.chunker import Chunker

from app.rag.vector_store import (
    VectorStore
)


class IngestionPipeline:

    @staticmethod
    def ingest_repository(
        github_url: str,
        collection_name: str
    ):

        logger.info(
            f"Starting ingestion for {github_url}"
        )

        repo_path = (
            RepoParserTool.clone_repository(
                github_url
            )
        )

        files = (
            RepoParserTool.get_source_files(
                repo_path
            )
        )

        documents = (
            FileReaderTool.create_documents(
                files
            )
        )

        chunks = (
            Chunker.chunk_documents(
                documents
            )
        )

        vector_store = VectorStore(
        collection_name=collection_name
    )

        vector_store.add_documents(
            chunks
        )

        logger.info(
            f"Ingestion completed for {github_url}"
        )

        return len(chunks)