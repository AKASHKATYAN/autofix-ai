from app.services.github_service import GitHubService

owner, repo = GitHubService.extract_owner_repo(
    "https://github.com/langchain-ai/langgraph"
)

data = GitHubService.get_repository_metadata(
    owner,
    repo
)

print(data["name"])
print(data["owner"]["login"])
print(data["stargazers_count"])
print(data["forks_count"])
print(data["language"])