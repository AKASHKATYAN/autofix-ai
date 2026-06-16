from app.tools.repo_parser_tool import (
    RepoParserTool
)

repo_path = RepoParserTool.clone_repository(
    "https://github.com/langchain-ai/langgraph"
)

files = RepoParserTool.get_source_files(
    repo_path
)

print(len(files))

for file in files[:10]:
    print(file)