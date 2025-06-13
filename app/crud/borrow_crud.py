from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime
from models import book_models, borrow_log_models
from schemas import borrow_log_schemas


def borrow_book(book_id: int, user_id: int, db:Session borrow_data: borrow_log_schemas.BorrowCreate)):
    #We check if the book first exist in our database
  borrowed = borrow_log_models.BorrowCreate(
    user_id=borrow_data.user_id
    book_id=borrow_data.book_id
    returned=False
    returned_at=None
  )
  db.add(borrowed)
  db.commit()
  db.refresh(borrowed)

#Get all borrowed books
def get_borrowed_books(db:Session):
    return db.query(borrow_log_models.Borrow).filter(borrow_log_models.Borrow).all()


def get_borrowed_book(db:Session, borrowed_id:int):
    return db.query(borrow_log_models.Borrow).filter(borrow_log_models.Book.id==borrowed_id).first()


#Return a borrowed
def return_borrowed_book(db: Session, borrowwed_id:int):
        borrow_log = db.query(borrow_log_models.Borrow).filter(borrow_log_models.Book.id==borrowed_id).first()
if borrow_log:
    borrow_log.returned = True
    borrow_log.returned_at = datetime.utcnow
    db.commit()
    db.refresh(borrow_log)
    return borrow_log

def delete_borrow_log(db: Session, borrow_id: int):
  borrow_log = db.query(borrow_log_models.Borrow).filter(borrow_log_models.Book.id==borrowed_id).first()
    if borrow_log:
        db.delete(borrow_log)
        db.commit()
    return borrow_log

    
