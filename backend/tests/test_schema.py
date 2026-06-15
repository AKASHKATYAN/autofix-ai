from app.schemas.repository import RepositoryCreate

repo = RepositoryCreate(
    name="AutoFix AI",
    github_url="https://github.com/test/repo"
)

print(repo)