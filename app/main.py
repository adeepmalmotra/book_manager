"""
Main FastAPI application entry point with lifespan setup.
Initializes database tables on startup.
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api import book_router
from app.db.init_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):#pylint: disable=redefined-outer-name,unused-argument
    """Handles application startup and shutdown events."""
    await init_db()
    yield

app = FastAPI(title="Book Management System with Gen AI", lifespan=lifespan)

app.include_router(book_router)

@app.get("/")
def read_root():
    """Health check route."""
    return {"message": "Welcome to the Book Management API"}
