from sqlalchemy import Column, Integer, String

from .database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, unique=True)
    subtitle = Column(String)
    description = Column(String)
    image = Column(String, unique=True)
    parent_id = Column(Integer, index=True)


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    url = Column(String, unique=True)
    category_id = Column(Integer, index=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True, unique=True)
    name = Column(String, unique=True)
    password = Column(String)
