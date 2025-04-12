"""
Initializes database by creating tables from ORM models.
"""
from app.db.session import engine
from app.db.base import Base
from app.models import book, review#pylint: disable=unused-import

async def init_db():
    """Creates all tables in the database based on defined models."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
