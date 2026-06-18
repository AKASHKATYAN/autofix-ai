from app.rag.rag_service import (
    RAGService
)

rag = RAGService()

response = rag.ask(
    "How does checkpointing work?"
)

print(response)