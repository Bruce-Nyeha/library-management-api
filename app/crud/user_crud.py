from fastapi import HTTPException,status
from schemas import user_schemas
from models import user_models
from sqlalchemy.orm import Session
from auth.utils import hash_password
from ... import models, schemas


def create_user(db:Session, user:UserCreate):
    db_user = db.query(user_models.User).filter(user_models.User.email==user.email).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed_password = hash_password(user.hashed_password)
    new_user = user_models.User(
        name = user.name
        email = user.email
        hashed_password = hashed_password
        role = user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

    #Getting user by id
def get_user(db:Session, user_id:int):
    db_user = db.query(user_models.User).filter(user_model.User.id==user_id).first()
    return db_user

    #Getting all the users
def get_all_users(db:Session):
        db_user = db.query(user_models.User).filter(user_models.User).all()
        return db_user


def delete_user(db:Session, user_id:int):
    db_user = db.query(user_models.User).filter(user_models.User.id==user_id)
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
    