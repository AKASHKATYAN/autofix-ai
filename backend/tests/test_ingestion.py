from app.rag.ingestion import (
    IngestionPipeline
)

chunks = (
    IngestionPipeline.ingest_repository(
        "https://github.com/langchain-ai/langgraph"
    )
)

print(
    f"Chunks Stored: {chunks}"
)