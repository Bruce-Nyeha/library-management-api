from sqlalchemy import Column, Integer, String, ForeignKey,Date, Text, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    author = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    isbn = Column(String, nullable=False)
    publish_at = Column(Date, nullable=True)
    quantity = Column(Integer, nullable=True)
    available = Column(Boolean, default = False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="books")
    borrows = relationship("Borrow", back_populates="book")

    