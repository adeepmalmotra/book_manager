"""
Defines the base class for all SQLAlchemy ORM models using async support.
"""
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

class Base(AsyncAttrs, DeclarativeBase):#pylint: disable=too-few-public-methods
    """Base class for all ORM models in the application."""
    pass#pylint: disable=unnecessary-pass
