"""
SQLAlchemy ORM model for Review.
"""
from sqlalchemy import Integer, Text, ForeignKey, Column
from app.db.base import Base

class Review(Base):#pylint: disable=too-few-public-methods
    """Review table linked to a specific book via book_id."""
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, nullable=False)
    review_text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
