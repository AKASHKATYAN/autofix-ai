"""
Custom Exceptions for AutoFix AI

All project-specific exceptions should inherit from
AutoFixException.
"""


class AutoFixException(Exception):
    """
    Base exception for the entire project.
    """

    def __init__(
        self,
        message: str,
        status_code: int = 500
    ):
        self.message = message
        self.status_code = status_code

        super().__init__(message)

    def __str__(self):
        return self.message


# ==================================================
# GitHub Exceptions
# ==================================================


class GitHubAPIException(AutoFixException):
    """Raised when GitHub API fails."""
    pass


class RepositoryNotFoundException(AutoFixException):
    """Raised when repository does not exist."""
    pass


class IssueNotFoundException(AutoFixException):
    """Raised when issue does not exist."""
    pass


class PullRequestException(AutoFixException):
    """Raised when PR operations fail."""
    pass


# ==================================================
# Agent Exceptions
# ==================================================


class AgentExecutionException(AutoFixException):
    """Raised when an agent fails during execution."""
    pass


class AgentRoutingException(AutoFixException):
    """Raised when supervisor cannot route tasks."""
    pass


class AgentStateException(AutoFixException):
    """Raised when graph state becomes invalid."""
    pass


# ==================================================
# RAG Exceptions
# ==================================================


class EmbeddingException(AutoFixException):
    """Raised when embedding generation fails."""
    pass


class VectorStoreException(AutoFixException):
    """Raised when vector database fails."""
    pass


class RetrievalException(AutoFixException):
    """Raised when retrieval process fails."""
    pass


class DocumentProcessingException(AutoFixException):
    """Raised during document ingestion/chunking."""
    pass


# ==================================================
# Database Exceptions
# ==================================================


class DatabaseConnectionException(AutoFixException):
    """Raised when database connection fails."""
    pass


class DatabaseOperationException(AutoFixException):
    """Raised when CRUD operations fail."""
    pass


# ==================================================
# Human In The Loop Exceptions
# ==================================================


class ReviewQueueException(AutoFixException):
    """Raised when review queue operations fail."""
    pass


class ApprovalException(AutoFixException):
    """Raised when approval workflow fails."""
    pass


# ==================================================
# Authentication & Authorization
# ==================================================


class AuthenticationException(AutoFixException):
    """Raised when authentication fails."""
    pass


class AuthorizationException(AutoFixException):
    """Raised when access is denied."""
    pass


class RateLimitException(AutoFixException):
    """Raised when API rate limit is exceeded."""
    pass


# ==================================================
# LLM Exceptions
# ==================================================


class LLMException(AutoFixException):
    """Raised when LLM call fails."""
    pass


class TokenLimitException(AutoFixException):
    """Raised when token limit is exceeded."""
    pass


# ==================================================
# Validation Exceptions
# ==================================================


class ValidationException(AutoFixException):
    """Raised when validation fails."""
    pass


class ConfigurationException(AutoFixException):
    """Raised when configuration is invalid."""
    pass