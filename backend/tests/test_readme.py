from app.services.github_service import GitHubService

owner, repo = GitHubService.extract_owner_repo(
    "https://github.com/langchain-ai/langgraph"
)

readme = GitHubService.get_readme(
    owner,
    repo
)

print(readme[:1000])