from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas import (
    RepositoryCreate,
    RepositoryResponse
)

from app.services import RepositoryService


router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"]
)


@router.post(
    "/",
    response_model=RepositoryResponse
)
def create_repository(
    repository: RepositoryCreate,
    db: Session = Depends(get_db)
):

    return RepositoryService.create_repository(
        db=db,
        repository_data=repository
    )


@router.get(
    "/",
    response_model=list[RepositoryResponse]
)
def get_repositories(
    db: Session = Depends(get_db)
):

    return RepositoryService.get_all_repositories(
        db=db
    )


@router.get(
    "/{repository_id}",
    response_model=RepositoryResponse
)
def get_repository(
    repository_id: int,
    db: Session = Depends(get_db)
):

    repository = RepositoryService.get_repository_by_id(
        db=db,
        repository_id=repository_id
    )

    if not repository:
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    return repository


@router.delete(
    "/{repository_id}"
)
def delete_repository(
    repository_id: int,
    db: Session = Depends(get_db)
):

    repository = RepositoryService.delete_repository(
        db=db,
        repository_id=repository_id
    )

    if not repository:
        raise HTTPException(
            status_code=404,
            detail="Repository not found"
        )

    return {
        "message": "Repository deleted successfully"
    }