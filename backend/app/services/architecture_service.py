from pathlib import Path

from app.logging import logger

from app.rag.architecture import (
    Architecture
)

from app.services.llm_service import (
    LLMService
)


from app.rag.repository_summary import (
    RepositorySummary
)

class ArchitectureService:

    llm = LLMService()

    @staticmethod
    @staticmethod
    def analyze(
    repo_path: str,
    repository_summary: RepositorySummary
    ):

        ignore_dirs = {
            ".git",
            ".github",
            "__pycache__",
            "venv",
            ".venv",
            "node_modules",
            "dist",
            "build"
        }

        ignore_module_children = {
            "examples",
            "docs"
        }

        modules = []

        root = Path(repo_path)

        for directory in root.rglob("*"):

            if not directory.is_dir():
                continue

            if any(
                ignored in directory.parts
                for ignored in ignore_dirs
            ):
                continue

            relative_path = (
                directory.relative_to(root)
            )

            if len(relative_path.parts) > 2:
                continue

            if (
                len(relative_path.parts) > 1
                and relative_path.parts[0]
                in ignore_module_children
            ):
                continue

            modules.append(
                str(relative_path)
            )

        logger.info(
            f"Found {len(modules)} modules"
        )

    

        prompt = (
            ArchitectureService
            ._build_architecture_prompt(
                repository_summary,
                modules
            )
        )

        logger.info(
            "Generating architecture summary."
        )

        architecture_summary = (
            ArchitectureService.llm.generate_response(
                prompt
            )
        )

        return Architecture(
            repository_name=root.name,
            modules=sorted(modules),
            architecture_summary=architecture_summary
        )

    @staticmethod
    def _build_architecture_prompt(
        repository_summary,
        modules: list[str]
    ):

        return f"""
You are an expert software architect.

Analyze the repository information below.

Repository Name:
{repository_summary.repository_name}

Purpose:
{repository_summary.purpose}

Frameworks:
{", ".join(repository_summary.frameworks)}

Languages:
{repository_summary.languages}

Modules:
{chr(10).join(sorted(modules))}

Explain:

1. Overall architecture.
2. Responsibilities of the major modules.
3. How the repository is organized.
4. Keep the explanation concise (5–8 sentences).
"""