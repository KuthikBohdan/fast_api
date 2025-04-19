from pydantic import BaseModel, Field
from typing import List
class UserCreate(BaseModel):
    login: str = Field(..., min_length=3, max_length=200)
    password: str = Field(..., min_length=3, max_length=200)

class UserDB(BaseModel):
    id: int
    class Config:
        orm_mode = True
class BookBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)
    pages: int = Field(..., gt=10)

class BookCreate(BookBase):
    

    author_name: str = Field(..., min_length=3, max_length=200)

class BookDB(BookBase):
    id: int
    class Config:
        orm_mode = True


class AuthorCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=200)


class AuthorDB(BaseModel):
    id: int
    name: str
    books: List[BookDB]= []

    class Config:
        orm_mode = True