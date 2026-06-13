import os
from pathlib import Path
import logging

# ==========================================
# Logging Configuration
# ==========================================

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s"
)

logger = logging.getLogger(__name__)

# ==========================================
# Project Structure
# ==========================================

list_of_files = [

    # ==========================
    # GitHub
    # ==========================
    ".github/workflows/ci.yml",

    # ==========================
    # Backend API
    # ==========================
    "backend/app/api/__init__.py",
    "backend/app/api/dependencies.py",

    "backend/app/api/routes/__init__.py",
    "backend/app/api/routes/repositories.py",
    "backend/app/api/routes/issues.py",
    "backend/app/api/routes/reviews.py",
    "backend/app/api/routes/chat.py",
    "backend/app/api/routes/health.py",

    # ==========================
    # Agents
    # ==========================
    "backend/app/agents/__init__.py",
    "backend/app/agents/supervisor.py",
    "backend/app/agents/triage_agent.py",
    "backend/app/agents/rag_agent.py",
    "backend/app/agents/developer_agent.py",
    "backend/app/agents/review_agent.py",
    "backend/app/agents/interview_agent.py",
    "backend/app/agents/content_agent.py",

    # ==========================
    # Workflows
    # ==========================
    "backend/app/workflows/__init__.py",
    "backend/app/workflows/issue_workflow.py",
    "backend/app/workflows/review_workflow.py",
    "backend/app/workflows/hitl_workflow.py",

    # ==========================
    # Tools
    # ==========================
    "backend/app/tools/__init__.py",
    "backend/app/tools/github_tool.py",
    "backend/app/tools/vector_search_tool.py",
    "backend/app/tools/repo_parser_tool.py",
    "backend/app/tools/code_analysis_tool.py",
    "backend/app/tools/file_reader_tool.py",

    # ==========================
    # RAG
    # ==========================
    "backend/app/rag/__init__.py",
    "backend/app/rag/ingestion.py",
    "backend/app/rag/chunker.py",
    "backend/app/rag/embedder.py",
    "backend/app/rag/retriever.py",
    "backend/app/rag/vector_store.py",

    # ==========================
    # Services
    # ==========================
    "backend/app/services/__init__.py",
    "backend/app/services/github_service.py",
    "backend/app/services/repository_service.py",
    "backend/app/services/issue_service.py",
    "backend/app/services/review_service.py",
    "backend/app/services/rag_service.py",
    "backend/app/services/llm_service.py",

    # ==========================
    # Database
    # ==========================
    "backend/app/database/__init__.py",
    "backend/app/database/database.py",
    "backend/app/database/base.py",

    "backend/app/database/models/__init__.py",
    "backend/app/database/models/repository.py",
    "backend/app/database/models/issue.py",
    "backend/app/database/models/document.py",
    "backend/app/database/models/chunk.py",
    "backend/app/database/models/review.py",
    "backend/app/database/models/agent_run.py",

    # ==========================
    # Schemas
    # ==========================
    "backend/app/schemas/__init__.py",
    "backend/app/schemas/repository.py",
    "backend/app/schemas/issue.py",
    "backend/app/schemas/review.py",
    "backend/app/schemas/chat.py",

    # ==========================
    # Human In The Loop
    # ==========================
    "backend/app/hitl/__init__.py",
    "backend/app/hitl/review_queue.py",
    "backend/app/hitl/approval_service.py",

    # ==========================
    # Observability
    # ==========================
    "backend/app/observability/__init__.py",
    "backend/app/observability/langfuse_client.py",
    "backend/app/observability/metrics.py",
    "backend/app/observability/tracing.py",

    # ==========================
    # Middleware
    # ==========================
    "backend/app/middleware/__init__.py",
    "backend/app/middleware/request_logger.py",

    # ==========================
    # Exceptions
    # ==========================
    "backend/app/exceptions/__init__.py",
    "backend/app/exceptions/custom_exceptions.py",
    "backend/app/exceptions/exception_handler.py",

    # ==========================
    # Logging
    # ==========================
    "backend/app/logging/__init__.py",
    "backend/app/logging/logger.py",

    # ==========================
    # Core
    # ==========================
    "backend/app/core/__init__.py",
    "backend/app/core/config.py",
    "backend/app/core/constants.py",
    "backend/app/core/security.py",

    # ==========================
    # FastAPI Entry
    # ==========================
    "backend/app/main.py",

    # ==========================
    # Tests
    # ==========================
    "backend/tests/test_health.py",
    "backend/tests/test_agents.py",
    "backend/tests/test_rag.py",
    "backend/tests/test_github.py",

    # ==========================
    # Alembic
    # ==========================
    "backend/alembic/.gitkeep",

    # ==========================
    # Logs
    # ==========================
    "backend/logs/.gitkeep",

    # ==========================
    # Backend Root Files
    # ==========================
    "backend/requirements.txt",
    "backend/.env",
    "backend/.env.example",

    # ==========================
    # Frontend
    # ==========================
    "frontend/src/pages/.gitkeep",
    "frontend/src/components/.gitkeep",
    "frontend/src/services/.gitkeep",
    "frontend/src/hooks/.gitkeep",
    "frontend/src/utils/.gitkeep",

    "frontend/package.json",

    # ==========================
    # Docs
    # ==========================
    "docs/architecture.md",
    "docs/roadmap.md",
    "docs/api_reference.md",
    "docs/setup_guide.md",

    # ==========================
    # Docker
    # ==========================
    "docker/backend.Dockerfile",
    "docker/frontend.Dockerfile",

    # ==========================
    # Scripts
    # ==========================
    "scripts/seed_database.py",
    "scripts/ingest_repository.py",

    # ==========================
    # Root Files
    # ==========================
    "docker-compose.yml",
    "README.md",
    ".gitignore",
    "LICENSE",
]


# ==========================================
# Create Files & Directories
# ==========================================

for filepath in list_of_files:

    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)

        logger.info(
            f"Created directory: {filedir}"
        )

    if (
        not os.path.exists(filepath)
        or os.path.getsize(filepath) == 0
    ):

        with open(filepath, "w", encoding="utf-8"):
            pass

        logger.info(
            f"Created file: {filepath}"
        )

    else:

        logger.info(
            f"Already exists: {filepath}"
        )

print("\n✅ AutoFix AI project structure created successfully!")