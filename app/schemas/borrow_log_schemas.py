from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BorrowBase(BaseModel):
    user_id: int 
    book_id: int 

class BorrowCreate(BorrowBase):
    pass

class BorrowResponse(BorrowBase):
    id: int
    returned: bool 
    returned_at: Optional[date] 

class Config:
    orm_mode = True
    