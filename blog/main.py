from fastapi import (
    FastAPI
)
from . import models
from .database import engine
from .routers import blog_router, user_router, authentication

app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog_router.router)
app.include_router(user_router.router)


models.Base.metadata.create_all(bind=engine)
