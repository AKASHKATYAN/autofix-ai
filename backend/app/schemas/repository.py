from datetime import datetime

from pydantic import BaseModel
from pydantic import ConfigDict


class RepositoryCreate(BaseModel):

    name: str

    github_url: str

    description: str | None = None


class RepositoryResponse(BaseModel):

    id: int

    name: str

    github_url: str

    description: str | None

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )