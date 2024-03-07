from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, hashing


def create(request: schemas.User, db: Session):
    data = request.model_dump()
    password = data.pop("password")
    new_user = models.User(
            **data,
            password=hashing.Hash.bcrypt(password)
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def retrieve(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado."
        )
    return user
