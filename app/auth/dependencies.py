from fastapi import Depends, HTTPException, status
from fastapi.security import OAuthPasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from .database import get_db
from models import  user_models
from .config import settings
from .models import user_models
from .schemas import user_schemas
from .auth impot oauth 

oauth2_scheme = OAuthPasswordBearer(tokenURL="auth/login")
def get_current_user(token:str = Depends(oauth2_scheme), db: Session=Depends(get_db)):
    token_data = verify_access_token(token)
    user = db.query(user_models).filter(user_models.User.id==token_data.user_id).first()
    if not user:
        raise HTTPException(
            status_code=statu.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user
    