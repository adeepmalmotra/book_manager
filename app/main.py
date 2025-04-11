from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api import book_router
from app.db.init_db import init_db

app = FastAPI(title="Book Management System with Gen AI")

app.include_router(book_router)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Management API"}

