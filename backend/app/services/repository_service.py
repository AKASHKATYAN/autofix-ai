from sqlalchemy.orm import Session

from app.database.models import Repository

from app.schemas import RepositoryCreate
from app.services.github_service import GitHubService


class RepositoryService:

    @staticmethod
    def create_repository(
        db: Session,
        repository_data: RepositoryCreate
    ):

        # Check if repository already exists
        existing_repo = db.query(
            Repository
        ).filter(
            Repository.github_url == repository_data.github_url
        ).first()

        if existing_repo:
            return existing_repo

        # Extract owner and repo name
        owner_repo = GitHubService.extract_owner_repo(
            repository_data.github_url
        )

        owner = None
        language = None
        stars = None
        forks = None
        readme_content = None

        if owner_repo:

            owner_name, repo_name = owner_repo

            metadata = GitHubService.get_repository_metadata(
                owner_name,
                repo_name
            )

            if metadata:

                owner = metadata["owner"]["login"]

                language = metadata.get(
                    "language"
                )

                stars = metadata.get(
                    "stargazers_count"
                )

                forks = metadata.get(
                    "forks_count"
                )

            readme_content = GitHubService.get_readme(
                owner_name,
                repo_name
            )

        repository = Repository(
            name=repository_data.name,
            github_url=repository_data.github_url,
            description=repository_data.description,

            owner=owner,
            language=language,
            stars=stars,
            forks=forks,
            readme_content=readme_content
        )

        db.add(repository)

        db.commit()

        db.refresh(repository)

        return repository

    @staticmethod
    def get_all_repositories(
        db: Session
    ):

        return db.query(
            Repository
        ).all()

    @staticmethod
    def get_repository_by_id(
        db: Session,
        repository_id: int
    ):

        return db.query(
            Repository
        ).filter(
            Repository.id == repository_id
        ).first()

    @staticmethod
    def delete_repository(
        db: Session,
        repository_id: int
    ):

        repository = db.query(
            Repository
        ).filter(
            Repository.id == repository_id
        ).first()

        if not repository:
            return None

        db.delete(repository)

        db.commit()

        return repository