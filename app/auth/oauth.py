from datetime import datetime.utcnow, timedelta
from jose import JWTError, jwt 
from config import settings
from fastapi import OAuthPasswordBearer
from sqlalchemy.orm import Session
from models import user_models
from database import get_db
from auth.oauth import verify_access_token

oauth2scheme = OAuthPasswordBearer(tokenUrl="login")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp:"expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        email: str = payload.get("email")
        role: str = payload.get("role")

        if not user_id or not email or not role:
            raise credentials_exception
        return {"id": user_id, "email": email, "role": role}
    except JWTError:
        raise credentials_exception
