import re
import requests

from app.core.config import settings
import base64
from app.logging import logger

class GitHubService:

    @staticmethod
    def extract_owner_repo(
        github_url: str
    ):
        logger.info(
        f"Extracting owner and repository from URL: {github_url}")


        pattern = r"https://github\.com/([^/]+)/([^/]+)"

        match = re.match(
            pattern,
            github_url
        )

        if not match:
            return None

        owner = match.group(1)
        repo = match.group(2)
        logger.info(
        f"Owner: {owner}, Repository: {repo}")

        return owner, repo

    @staticmethod
    def get_repository_metadata(
        owner: str,
        repo: str
    ):
        

        url = f"https://api.github.com/repos/{owner}/{repo}"

        headers = {}

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = (
                f"Bearer {settings.GITHUB_TOKEN}"
            )
        logger.info(
        f"Owner: {owner}, Repository: {repo}")

    

        response = requests.get(
            url,
            headers=headers
        )

        if response.status_code != 200:
            return None
        logger.info(
        f"Metadata fetched successfully for {owner}/{repo}")
        logger.info(
        f"Metadata fetched successfully for {owner}/{repo}")


        return response.json()

    @staticmethod
    def get_readme(
        owner: str,
        repo: str
    ):

        url = (
            f"https://api.github.com/repos/"
            f"{owner}/{repo}/readme"
        )

        headers = {}

        if settings.GITHUB_TOKEN:
            headers["Authorization"] = (
                f"Bearer {settings.GITHUB_TOKEN}"
            )
        logger.info(
        f"Fetching README for {owner}/{repo}")

        response = requests.get(
            url,
            headers=headers
        )

        if response.status_code != 200:
            return None

        data = response.json()

        content = base64.b64decode(
            data["content"]
        ).decode(
            "utf-8",
            errors="ignore"
        )
        logger.info(
        f"README fetched successfully for {owner}/{repo}")

        return content    