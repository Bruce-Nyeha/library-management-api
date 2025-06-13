from sqlalchemy import Integer, Column, String,Date, ForeignKey
from sqlalchemy.orm import relationship
from..database  import Base

class Borrow(Base):
    __tablename__ = "borrows"
 id = Column(Integer, primary_key=True, index=True)
 user_id = Column(Integer, ForeignKey=("users.id"))
 book_id = Column(Integer, ForeignKey=("books.id"))
 returned_at = Column(Date, nullable=True)
 returned = Column(Boolean, default=False)

 user = relationship("User", back_populates="borrows")
 book = relationship("Book", back_populates="borrows")
 