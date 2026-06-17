from app.tools.repo_parser_tool import (
    RepoParserTool
)

from app.tools.file_reader_tool import (
    FileReaderTool
)


repo_path = RepoParserTool.clone_repository(
    "https://github.com/langchain-ai/langgraph"
)

files = RepoParserTool.get_source_files(
    repo_path
)

print(
    f"Source Files Found: {len(files)}"
)

documents = FileReaderTool.create_documents(
    files[:10]
)

print(
    f"Documents Created: {len(documents)}"
)

print(
    documents[0].source
)

print(
    documents[0].content[:500]
)