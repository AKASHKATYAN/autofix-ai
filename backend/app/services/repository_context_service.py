from app.services.repository_summary_service import (
    RepositorySummaryService
)

from app.services.architecture_service import (
    ArchitectureService
)

from app.rag.repository_context import (
    RepositoryContext
)


class RepositoryContextService:

    @staticmethod
    def generate(
        repo_path: str
    ):

        repository_summary = (
            RepositorySummaryService.generate_summary(
                repo_path
            )
        )

        architecture = (
        ArchitectureService.analyze(
        repo_path=repo_path,
        repository_summary=repository_summary
        )
      )

        return RepositoryContext(
            repository_summary=repository_summary,
            architecture=architecture
        )