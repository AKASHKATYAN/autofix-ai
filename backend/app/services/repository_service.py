from sqlalchemy.orm import Session

from app.database.models import Repository

from app.schemas import RepositoryCreate


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

        repository = Repository(
            name=repository_data.name,
            github_url=repository_data.github_url,
            description=repository_data.description
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