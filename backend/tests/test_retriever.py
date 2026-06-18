from app.rag.retriever import (
    Retriever
)

retriever = Retriever()

results = retriever.retrieve(
    "How does checkpointing work?"
)

print()

for index, result in enumerate(
    results,
    start=1
):

    print(
        f"\nResult {index}\n"
    )

    print(
        result[:500]
    )