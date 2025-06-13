from sqlalchemy import Column,Integer,String,Enum
from ..database import Base
from .enums import RoleEnum

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), default = RoleEnum.USER, nullable=False)

books= relationship("Book", back_populates="owner")
borrows = relationship("Borrow", back_populates="user")
