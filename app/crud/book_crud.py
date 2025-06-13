from fastapi import HTTPException, Depends, status
from sqlalachemy.orm import Session
from ... import models, schemas

#Create a new a book

def create_book(book: book_schemas.UserCreate, db: Session):
    existing_book = db.query(book_models.Book).filter(book_models.Book.isbn==book.isbn).first()
    if existing_book:
        raise HTTPException(
            status_code = status.HTTPS_400_BAD_REQUEST,
            detail = "Book with ISBN already exist"
        )
    new_book = book_models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)


    #Get a single book
def get_book(book_id: int, db: Session):
    db_book = db.query(book_models.Book).filter(book_models.Book.id==book_id).first()
    if not db_book:
        raise HTTPException(
            status_code = status.HTTPS_400_BAD_REQUEST
            detail = "Book not found"
        )
    return db_book

#Get all books
def get_all_book(db:Session):
    return db.query(book_models.Book).filter(book_models.Book).all()

#Update book
def update_book(db:Session, book_id: int, updated_book: book_schemas.BookCreate):
    existing_book = db.query(book_models.Book).filter(book_models.Book.id==book_id).first()
    if not existing_book:
        raise HTTPException(
            status_code = status.HTTPS_400_BAD_REQUEST
            detail = "Sorry, book not found"
        )
    for  key, value in updated_book.dict().items:
        setattr(book, key, value)

def delete_book(book_id: int, db: Session):
    book = db.query(book_models.Book).filter(book_models.Book.id==book_id).first()
    if not book:
        raise HTTPException(
            status_code = status.HTTPS_400_BAD_REQUEST
            detail = "Sorry, book not found"
        )
    db.delete(book)
    db.commit()
    return {"message": "Book successfully deleted"}
    