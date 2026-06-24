from dataclasses import dataclass

@dataclass
class RepositorySummary:

    repository_name: str

    total_files: int

    languages: dict[str, int]

    important_directories: list[str]

    purpose: str = "Unknown"

    frameworks: list[str] | None = None