from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(200), nullable=False, unique=True)
    password = Column(String, nullable=False)
    

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False, index=True)

    books = relationship("Book", back_populates='author' )

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    pages = Column(Integer, nullable=False, default=11)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates='books' )