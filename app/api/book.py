"""
Defines book-related API endpoints.
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.book import BookCreate, BookRead, BookUpdate
from app.services.book_service import BookService
from app.db.session import AsyncSessionLocal

router = APIRouter()

async def get_db():
    """Provides async database session."""
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()

@router.post("/", response_model=BookRead)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    """Creates a new book entry in the database."""
    return await BookService.create_book(db, book)

@router.get("/", response_model=List[BookRead])
async def list_books(db: AsyncSession = Depends(get_db)):
    """Retrieves a list of all books in the system."""
    return await BookService.get_all_books(db)

@router.get("/{book_id}", response_model=BookRead)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieves a single book by its ID."""
    book = await BookService.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookRead)
async def update_book(book_id: int, book_data: BookUpdate, db: AsyncSession = Depends(get_db)):
    """Updates the details of an existing book."""
    return await BookService.update_book(db, book_id, book_data)

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    """Deletes a book from the system by its ID."""
    await BookService.delete_book(db, book_id)
    return {"message": "Book deleted successfully"}
