from app.tools.repo_parser_tool import (
    RepoParserTool
)

path = RepoParserTool.clone_repository(
    "https://github.com/langchain-ai/langgraph"
)

print(path)