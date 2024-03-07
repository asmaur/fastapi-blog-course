from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    body = Column(String(5000))
    creator_id = Column(Integer, ForeignKey("users.id"))
    creator = Relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(50))
    password = Column(String(100))
    blogs = Relationship("Blog", back_populates="creator")
