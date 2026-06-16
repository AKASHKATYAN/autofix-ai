from app.services.github_service import GitHubService

result = GitHubService.extract_owner_repo(
    "https://github.com/langchain-ai/langgraph"
)

print(result)