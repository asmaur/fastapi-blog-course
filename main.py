from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"os {limit} primeiros posts publicados"}
    return {"data": f"os {limit} primeiros posts"}


@app.get("/blog/published")
def published():
    return {"data": "publicados"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments():
    # buscar todos os comentarios para os blog de id = id
    return {"data": "todos os commentarios."}


@app.get("/sobre")
def about():
    return {"data": "pagina de sobre nós.!"}
