from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, schemas, models, jwt_token
from ..hashing import Hash

router = APIRouter(
    tags=["Auth"]
)

get_db = database.get_db


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
            models.User.email == request.username
        ).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Credenciais inválidas."
        )
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Credenciais inválidas."
        )
    access_token = jwt_token.create_access_token(
        data={"sub": user.email}
    )
    return schemas.Token(
        access_token=access_token, token_type="bearer"
    )
