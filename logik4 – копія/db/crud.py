from sqlalchemy.orm import Session
from .import schemas

from .models import Book, Author, User

def check_user(login:str, password:str, db: Session):
    user = db.query(Book).filter(User.login, User.password == password)
    return user


def get_all_books(db: Session):
    book = db.query(Book).all()
    return book




def create_book(book: schemas.BookCreate, db: Session):
    author = db.query(Author).filter(Author.name == book.author_name).first()
    if not author:
        author = Author(name=book.author_name)
        db.add(author)
        db.commit()
        db.refresh(author)

    db_book = Book(title=book.title, pages = book.pages, author_id = author.id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books_by_author(author_name: str, db: Session):
    author = db.query(Author).filter(Author.name == author.author_name).first()
    if author:
        return author.books
    return None


def delete_book(author_name:str, book_title:str, db:Session):
    book = db.query(Book).joun(Author).filter(Author.name==author_name, Book.title==book_title).first()
    if book:
        db.delate(book)
        db.commit()
        return True
    return False