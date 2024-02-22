from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import database, schemas
from ..repository import user


router = APIRouter(
    tags=["Users"],
    prefix="/users"
)
get_db = database.get_db


@router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        response_model=schemas.ShowUser
    )
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request=request, db=db)


@router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
        response_model=schemas.ShowDetailUser
    )
def get_user(id: int, db: Session = Depends(get_db)):
    return user.retrieve(id=id, db=db)
