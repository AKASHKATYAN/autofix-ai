from app.rag.ingestion import (
    IngestionPipeline
)

from app.rag.rag_service import (
    RAGService
)


def main():

    print(
        "\nIngesting LangGraph..."
    )

    IngestionPipeline.ingest_repository(
        github_url="https://github.com/langchain-ai/langgraph",
        collection_name="autofix_langgraph"
    )

    print(
        "\nTesting LangGraph Collection..."
    )

    rag = RAGService(
        collection_name="autofix_langgraph",
        repo_path="repositories/langgraph"
    )

    answer = rag.ask(
        "Give me an overview of this repository."
    )

    print("\nRESULT:\n")

    print(answer)


if __name__ == "__main__":

    main()