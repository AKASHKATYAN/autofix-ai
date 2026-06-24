from app.logging import logger

from app.rag.retriever import Retriever

from app.services.llm_service import (
    LLMService
)
from app.services.repository_summary_service import (
    RepositorySummaryService
)


class RAGService:

    def __init__(
    self,
    collection_name: str = "autofix",
    repo_path: str | None = None
):
        self.retriever = Retriever(
            collection_name=collection_name
        )
        self.llm = LLMService()
        self.repo_path = repo_path
        
    def ask(
        self,
        question: str
    ):

        results = self.retriever.retrieve(
            question
        )
        summary_text = ""

        if self.repo_path:

            summary = (
                RepositorySummaryService.generate_summary(
                    self.repo_path
                )
            )

            summary_text = f"""
        Repository Name:
        {summary.repository_name}

        Total Files:
        {summary.total_files}

        Languages:
        {summary.languages}

        Directories:
        {", ".join(summary.important_directories)}
        """

        chunks = results["documents"]

        sources = results["sources"]

        context = "\n\n".join(
            chunks
        )

        prompt = f"""
You are an expert software engineer.

Answer the question ONLY using the repository information provided.

If the answer cannot be found,
say so clearly.

Repository Summary:
{summary_text}

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