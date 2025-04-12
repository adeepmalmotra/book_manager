"""
Business logic and services for book management.
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound#pylint: disable=unused-import
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate

class BookService:
    """Service layer for handling book-related operations."""
    @staticmethod
    async def create_book(db: AsyncSession, book_data: BookCreate):
        """Creates and stores a new book record."""
        new_book = Book(**book_data.dict())
        db.add(new_book)
        await db.commit()
        await db.refresh(new_book)
        return new_book

    @staticmethod
    async def get_all_books(db: AsyncSession):
        """Fetches all books from the database."""
        result = await db.execute(select(Book))
        return result.scalars().all()

    @staticmethod
    async def get_book_by_id(db: AsyncSession, book_id: int):
        """Fetches a single book by its ID."""
        result = await db.execute(select(Book).where(Book.id == book_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_book(db: AsyncSession, book_id: int, book_data: BookUpdate):
        """Updates an existing book with new data."""
        result = await db.execute(select(Book).where(Book.id == book_id))
        book = result.scalar_one_or_none()
        if not book:
            return None
        for field, value in book_data.dict(exclude_unset=True).items():
            setattr(book, field, value)
        await db.commit()
        await db.refresh(book)
        return book

    @staticmethod
    async def delete_book(db: AsyncSession, book_id: int):
        """Deletes a book by its ID."""
        result = await db.execute(select(Book).where(Book.id == book_id))
        book = result.scalar_one_or_none()
        if book:
            await db.delete(book)
            await db.commit()
