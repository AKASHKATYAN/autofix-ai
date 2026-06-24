from pathlib import Path

from app.logging import logger


from pathlib import Path

from app.logging import logger
from app.services.llm_service import (
    LLMService
)


class RepositoryIntelligenceService:

    @staticmethod
    def detect_frameworks(
        repo_path: str
    ):

        framework_patterns = {
            "fastapi": "FastAPI",
            "django": "Django",
            "langchain": "LangChain",
            "langgraph": "LangGraph",
            "streamlit": "Streamlit",
            "flask": "Flask",
            "react": "React",
            "next": "Next.js"
        }

        frameworks = set()

        files_to_check = [
            "README.md",
            "requirements.txt",
            "pyproject.toml",
            "package.json"
        ]

        for file_name in files_to_check:

            file_path = (
                Path(repo_path)
                / file_name
            )

            if not file_path.exists():
                continue

            try:

                content = (
                    file_path.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    ).lower()
                )

                for keyword, framework in (
                    framework_patterns.items()
                ):

                    if keyword in content:

                        frameworks.add(
                            framework
                        )

            except Exception as e:

                logger.error(
                    f"Error reading {file_path}: {e}"
                )

        return sorted(
            list(frameworks)
        )

    @staticmethod
    def extract_purpose(
        repo_path: str
    ):

        readme_path = (
        Path(repo_path)
        / "README.md"
        )

        if not readme_path.exists():

            return "Unknown"

        try:
            content = (
                readme_path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            )
            content = content[:4000]
           
        except Exception as e:

            logger.error(
                f"Error reading README: {e}"
            )

            return "Unknown"

        prompt = f"""
        You are a software architect.

        Read the repository README and provide:

        1. Repository purpose
        2. Main technologies/frameworks
        3. Core functionality

        Keep the response under 150 words.

        README:

        {content}

        Summary:
        """        
        try:

            llm = LLMService()
            summary = (
                llm.generate_response(
                    prompt
                )
            )
            return summary

        except Exception as e:

            logger.error(
                f"README summarization failed: {e}"
            )

            return "Unknown"    
            