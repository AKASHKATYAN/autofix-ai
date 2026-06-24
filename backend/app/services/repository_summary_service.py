from pathlib import Path

from app.logging import logger

from app.rag.repository_summary import (
    RepositorySummary
)
from app.services.repository_intelligence_service import (
    RepositoryIntelligenceService
)

class RepositorySummaryService:

    @staticmethod
    def generate_summary(
        repo_path: str
    ):

        language_map = {
            ".py": "Python",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".tsx": "TypeScript",
            ".java": "Java",
            ".cpp": "C++",
            ".go": "Go",
            ".rs": "Rust"
        }

        ignore_dirs = {
            ".git",
            ".github",
            ".venv",
            "venv",
            "__pycache__",
            "node_modules",
            ".next",
            "dist",
            "build"
        }

        total_files = 0

        languages = {}

        for path in Path(repo_path).rglob("*"):

            if any(
                ignored in path.parts
                for ignored in ignore_dirs
            ):
                continue

            if not path.is_file():
                continue

            total_files += 1

            suffix = path.suffix.lower()

            if suffix in language_map:

                language = language_map[
                    suffix
                ]

                languages[language] = (
                    languages.get(
                        language,
                        0
                    ) + 1
                )

        important_directories = []

        for item in Path(
            repo_path
        ).iterdir():

            if (
                item.is_dir()
                and item.name
                not in ignore_dirs
            ):

                important_directories.append(
                    item.name
                )
        frameworks = (
        RepositoryIntelligenceService.detect_frameworks(
        repo_path)
        )

        purpose = (
            RepositoryIntelligenceService.extract_purpose(
                repo_path
            )
        )
        summary = RepositorySummary(
        repository_name=Path(
            repo_path
        ).name,

        total_files=total_files,

        languages=languages,

        important_directories=sorted(
            important_directories
        ),

        purpose=purpose,

        frameworks=frameworks
       )

        logger.info(
            f"Generated summary for {summary.repository_name}"
        )

        return summary