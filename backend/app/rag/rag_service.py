from app.logging import logger

from app.rag.retriever import Retriever

from app.services.llm_service import (
    LLMService
)


class RAGService:

    def __init__(self):

        self.retriever = Retriever()

        self.llm = LLMService()

    def ask(
        self,
        question: str
    ):

        results = self.retriever.retrieve(
            question
        )

        chunks = results["documents"]

        sources = results["sources"]

        context = "\n\n".join(
            chunks
        )

        prompt = f"""
You are an expert software engineer.

Answer the question ONLY using the repository context provided below.

If the answer cannot be found in the repository context,
say so clearly.

Repository Context:
{context}

Question:
{question}

Answer:
"""

        logger.info(
            "Sending context to LLM."
        )

        answer = self.llm.generate_response(
            prompt
        )

        unique_sources = []

        seen = set()

        for source in sources:

            file_path = source.get(
                "source",
                "Unknown Source"
            )

            if file_path not in seen:

                seen.add(
                    file_path
                )

                unique_sources.append(
                    file_path
                )

        source_text = "\n".join(
            f"- {source}"
            for source in unique_sources
        )

        return (
            f"{answer}\n\n"
            f"Sources:\n"
            f"{source_text}"
        )