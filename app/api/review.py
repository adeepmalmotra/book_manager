"""
Defines review-related API endpoints.
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException#pylint: disable=unused-import
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.review import ReviewCreate, ReviewRead
from app.services.review_service import ReviewService
from app.db.session import AsyncSessionLocal

router = APIRouter()

async def get_db():
    """Provides database session dependency."""
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()

@router.post("/{book_id}/reviews", response_model=ReviewRead)
async def create_review(book_id: int, review: ReviewCreate, db: AsyncSession = Depends(get_db)):
    """Creates a new review for a specific book."""
    return await ReviewService.create_review(db, book_id, review)

@router.get("/{book_id}/reviews", response_model=List[ReviewRead])
async def get_reviews(book_id: int, db: AsyncSession = Depends(get_db)):
    """Retrieves all reviews for a specific book."""
    return await ReviewService.get_reviews_by_book_id(db, book_id)
