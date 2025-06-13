fron pydantic import BaseModel
from typing import Optional
from datetime import date

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str]
    isbn: int 
    publish_at: Optional[date]
    quantity: Optional[int]

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    available: bool 
    owner_id: int

class Config:
    orm_mode = True 
    