"""
Defines Pydantic models (schemas) for book APIs.
"""
from typing import Optional
from pydantic import BaseModel

class BookBase(BaseModel):
    """Shared fields for book operations."""
    title: str
    author: str
    genre: Optional[str]
    year_published: Optional[int]

class BookCreate(BookBase):
    """Schema for creating a new book."""
    pass

class BookUpdate(BookBase):
    """Schema for updating a book entry."""
    summary: Optional[str]

class BookRead(BookBase):
    """Schema for reading a book entry."""
    id: int
    summary: Optional[str]

    class Config:
        orm_mode = True
