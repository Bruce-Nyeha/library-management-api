from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth import oauth
from auth import utils
from schemas import user_schemas
from database import get_db
from crud import auth_crud

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=user_schemas.UserResponse)
def register_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    return auth_crud.register_user(user, db)

@router.post("/login")
def login(user_credentials: user_schemas.UserLogin, db: Session = Depends(get_db)):
    return auth_crud.login_user(user_credentials, db)
