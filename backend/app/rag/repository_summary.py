from dataclasses import dataclass

@dataclass
class RepositorySummary:

    repository_name: str

    total_files: int

    languages: list[str]

    important_directories: list[str]