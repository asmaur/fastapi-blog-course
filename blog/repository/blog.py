from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas


get_db = database.get_db


def list(db: Session):
    posts = db.query(models.Blog).all()
    return posts


def create(request: schemas.Blog, db: Session, current_user: models.User):
    user = db.query(models.User).filter(
            models.User.email == current_user.email
        ).first()
    new_blog = models.Blog(
        title=request.title,
        body=request.body,
        creator_id=user.id
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def retrieve(id: int, db: Session):
    post = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not post:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post não encontrado."
            )
    return post


def destroy(id: int, db: Session):
    post = db.query(models.Blog).filter(
        models.Blog.id == id
    )
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post não encontrado."
        )
    post.delete(synchronize_session=False)
    db.commit()
    return {"detail": "Post deletado com sucesso."}


def update(id: int, request: schemas.Blog, db: Session):
    post = db.query(models.Blog).filter(
        models.Blog.id == id
    )
    if not post.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post não encontrado."
        )
    post.update(request.model_dump())
    db.commit()
    return {"detail": "Post atualizado com sucesso."}
