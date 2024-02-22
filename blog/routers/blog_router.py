from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List

from blog.oauth2 import get_current_user
from .. import schemas, database, models
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)
get_db = database.get_db


@router.get(
        "/",
        response_model=List[schemas.ShowBlog],
    )
def list(
            db: Session = Depends(get_db),
            current_user: models.User = Depends(get_current_user)
        ):
    return blog.list(db)


@router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
    )
def create(
        request: schemas.Blog,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
        ):
    return blog.create(request, db, current_user)


@router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
        response_model=schemas.ShowBlog
    )
def retrieve(
            id: int,
            db: Session = Depends(get_db),
            current_user: models.User = Depends(get_current_user)
        ):
    return blog.retrieve(id, db)


@router.delete(
        "/{id}",
        status_code=status.HTTP_204_NO_CONTENT,
    )
def destroy(
            id: int,
            db: Session = Depends(get_db),
            current_user: models.User = Depends(get_current_user)
        ):
    return blog.destroy(id, db)


@router.put(
        "/{id}",
        status_code=status.HTTP_202_ACCEPTED,
    )
def update(
            id: int,
            request: schemas.Blog,
            db: Session = Depends(get_db),
            current_user: models.User = Depends(get_current_user)
        ):
    return blog.update(id, request, db)
