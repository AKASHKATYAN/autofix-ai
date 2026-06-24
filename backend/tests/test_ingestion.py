from app.rag.rag_service import (
    RAGService
)


def main():

    rag = RAGService(
        collection_name="autofix_langgraph",
        repo_path="repositories/langgraph"
    )

    answer = rag.ask(
        "What is LangGraph used for?"
    )

    print("\nRESULT:\n")

    print(answer)


if __name__ == "__main__":
    main()