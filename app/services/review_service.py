"""
Contains business logic for managing reviews.
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.review import Review
from app.schemas.review import ReviewCreate

class ReviewService:
    """Service layer for handling review operations."""

    @staticmethod
    async def create_review(db: AsyncSession, book_id: int, review_data: ReviewCreate):
        """Creates and persists a new review."""
        review = Review(book_id=book_id, **review_data.dict())
        db.add(review)
        await db.commit()
        await db.refresh(review)
        return review

    @staticmethod
    async def get_reviews_by_book_id(db: AsyncSession, book_id: int):
        """Fetches all reviews associated with a book ID."""
        result = await db.execute(select(Review).where(Review.book_id == book_id))
        return result.scalars().all()
