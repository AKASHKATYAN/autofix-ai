from app.tools.repo_parser_tool import (
    RepoParserTool
)

from app.tools.file_reader_tool import (
    FileReaderTool
)

from app.rag.chunker import Chunker

from app.rag.vector_store import (
    VectorStore
)


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

vector_store = VectorStore()

vector_store.add_documents(
    chunks
)

results = vector_store.search(
    "How are messages handled?"
)

print(
    results["documents"][0][:3]
)