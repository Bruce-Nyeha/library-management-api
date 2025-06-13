from fastapi import FastAPI
from routes import auth, user_routes, book_routes, borrow_routes
from app.database import engine, Base

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(user_routes.router)
app.include_router(book_routes.router)
app.include_router(borrow_routes.router)

# Create all tables
Base.metadata.create_all(bind=engine)
