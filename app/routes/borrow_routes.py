from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from crud import borrow_crud
from schemas import borrow_log_schemas
from dependencies import get_current_user
from schemas.user_schemas import UserResponse

router = APIRouter(
    prefix="/borrow",
    tags=["Borrow"]
)

@router.post("/", response_model=borrow_log_schemas.BorrowResponse)
def borrow_book(borrow_data: borrow_log_schemas.BorrowCreate, db: Session = Depends(get_db), current_user: UserResponse = Depends(get_current_user)):
    return borrow_crud.borrow_book(borrow_data, db)

@router.get("/", response_model=list[borrow_log_schemas.BorrowResponse])
def get_borrow_logs(db: Session = Depends(get_db)):
    return borrow_crud.get_all_borrow_logs(db)

@router.put("/{borrow_id}", response_model=borrow_log_schemas.BorrowResponse)
def return_book(borrow_id: int, db: Session = Depends(get_db)):
    return borrow_crud.return_book(borrow_id, db)
