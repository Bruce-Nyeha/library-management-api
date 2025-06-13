from pydantic import BaseModel, EmailStr
from .enums import RoleEnum

class UserBase(BaseModel):
    name: str 
    email: EmailStr
    role: RoleEnum

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: str

class Config:
    orm_mode = True
    