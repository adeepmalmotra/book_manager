"""
Defines Pydantic models (schemas) for review APIs.
"""
from typing import Optional#pylint: disable=unused-import
from pydantic import BaseModel

class ReviewCreate(BaseModel):
    """Schema for creating a review."""
    user_id: int
    review_text: str
    rating: int

class ReviewRead(ReviewCreate):
    """Schema for reading a review (includes ID and book_id)."""
    id: int
    book_id: int

    class Config:
        orm_mode = True
