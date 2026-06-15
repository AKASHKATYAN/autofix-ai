from app.database import SessionLocal

from app.schemas.repository import RepositoryCreate

from app.services.repository_service import RepositoryService


db = SessionLocal()

repo = RepositoryCreate(
    name="AutoFix AI",
    github_url="https://github.com/test/repo",
    description="Testing Service Layer"
)

created_repo = RepositoryService.create_repository(
    db=db,
    repository_data=repo
)

print(created_repo.id)
print(created_repo.name)

all_repos = RepositoryService.get_all_repositories(
    db=db
)

print(all_repos)

db.close()