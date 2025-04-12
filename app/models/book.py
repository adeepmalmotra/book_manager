"""
SQLAlchemy ORM model for Book.
"""
from sqlalchemy import String, Integer, Text, Column
from app.db.base import Base

class Book(Base):#pylint: disable=too-few-public-methods
    """Book table with basic metadata and summary."""
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    genre = Column(String(100))
    year_published = Column(Integer)
    summary = Column(Text)
