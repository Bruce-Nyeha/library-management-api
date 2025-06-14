from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
form sqlalchemy.ext.declarative import declarative_base
from .config import settings

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessinmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
    