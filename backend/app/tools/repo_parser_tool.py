from pathlib import Path

from git import Repo
from app.logging import logger

class RepoParserTool:

    BASE_REPO_PATH = Path(
        "repositories"
    )

    @staticmethod
    def clone_repository(
        github_url: str
    ):
        logger.info(
        f"Attempting to clone repository: {github_url}"
    )

        RepoParserTool.BASE_REPO_PATH.mkdir(
            exist_ok=True
        )

        repo_name = github_url.split(
            "/"
        )[-1]

        local_path = (
            RepoParserTool.BASE_REPO_PATH
            / repo_name
        )

        if local_path.exists():
            return str(local_path)

        Repo.clone_from(
        github_url,
        str(local_path),
        depth=1
        )
        logger.info(
        f"Repository cloned successfully: {local_path}"
    )

        return str(local_path)
    
    @staticmethod
    def get_source_files(
        repo_path: str
    ):

        extensions = {
            ".py",
            ".js",
            ".ts",
            ".tsx",
            ".java",
            ".cpp",
            ".go",
            ".rs"
        }

        files = []

        ignore_dirs = {
            ".git",
            ".venv",
            "venv",
            "__pycache__",
            "node_modules",
            ".next",
            "dist",
            "build"
        }
        logger.info(
         f"Scanning repository: {repo_path}")


        for path in Path(repo_path).rglob("*"):

            if any(
                ignored in path.parts
                for ignored in ignore_dirs
            ):
                continue

            if (
                path.is_file()
                and path.suffix in extensions
            ):
                files.append(
                    str(path)
                )
        logger.info(
        f"Found {len(files)} source files")
        

        return files