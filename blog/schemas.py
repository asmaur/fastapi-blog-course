from pydantic import BaseModel
from typing import List, Optional


class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowBlogMini(BaseModel):
    id: int
    title: str


class ShowUser(BaseModel):
    id: int
    name: str
    email: str


class ShowDetailUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[ShowBlogMini]


class ShowBlog(BaseModel):
    id: int
    title: str
    creator: ShowUser


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
