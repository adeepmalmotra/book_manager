from sqlalchemy import Integer, Text, ForeignKey, Column
from app.db.base import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    user_id = Column(Integer, nullable=False)
    review_text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)