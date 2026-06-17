from app.tools.repo_parser_tool import RepoParserTool
from app.tools.file_reader_tool import FileReaderTool

from app.rag.chunker import Chunker


repo_path = RepoParserTool.clone_repository(
    "https://github.com/langchain-ai/langgraph"
)

files = RepoParserTool.get_source_files(
    repo_path
)

documents = FileReaderTool.create_documents(
    files[:5]
)

chunks = Chunker.chunk_documents(
    documents
)

print(
    f"Documents: {len(documents)}"
)

print(
    f"Chunks: {len(chunks)}"
)

print(
    chunks[0].content[:300]
)