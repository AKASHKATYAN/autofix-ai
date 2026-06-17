from app.tools.file_reader_tool import (
    FileReaderTool
)

from app.tools.repo_parser_tool import (
    RepoParserTool
)


repo_path = RepoParserTool.clone_repository(
    "https://github.com/langchain-ai/langgraph"
)

files = RepoParserTool.get_source_files(
    repo_path
)

first_file = files[0]

print("File:", first_file)

content = FileReaderTool.read_file(
    first_file
)

print(content[:1000])