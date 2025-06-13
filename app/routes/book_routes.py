from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import book_schemas
from crud import book_crud
from dependencies import get_current_user

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("/", response_model=book_schemas.BookResponse)
def create_book(book: book_schemas.BookCreate, db: Session = Depends(get_db)):
    return book_crud.create_book(book, db)

@router.get("/", response_model=list[book_schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return book_crud.get_all_books(db)

@router.get("/{book_id}", response_model=book_schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return book_crud.get_book(book_id, db)

@router.put("/{book_id}", response_model=book_schemas.BookResponse)
def update_book(book_id: int, book: book_schemas.BookUpdate, db: Session = Depends(get_db)):
    return book_crud.update_book(book_id, book, db)

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return book_crud.delete_book(book_id, db)
