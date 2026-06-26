from dataclasses import dataclass

from app.rag.repository_summary import (
    RepositorySummary
)

from app.rag.architecture import (
    Architecture
)


@dataclass
class RepositoryContext:

    repository_summary: RepositorySummary

    architecture: Architecture