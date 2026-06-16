from app.database import SessionLocal

from app.schemas import RepositoryCreate

from app.services import RepositoryService


db = SessionLocal()

repo = RepositoryCreate(
    name="LangGraph",
    github_url="https://github.com/langchain-ai/langgraph",
    description="Agent framework"
)

repository = RepositoryService.create_repository(
    db=db,
    repository_data=repo
)

print("Name:", repository.name)
print("Owner:", repository.owner)
print("Language:", repository.language)
print("Stars:", repository.stars)
print("Forks:", repository.forks)

print(
    "README Length:",
    len(repository.readme_content)
)

db.close()