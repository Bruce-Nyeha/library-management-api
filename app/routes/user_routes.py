from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import user_schemas
from crud import user_crud
from dependencies import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", response_model=list[user_schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return user_crud.get_all_users(db)

@router.get("/me", response_model=user_schemas.UserResponse)
def get_logged_in_user(current_user: user_schemas.UserResponse = Depends(get_current_user)):
    return current_user
