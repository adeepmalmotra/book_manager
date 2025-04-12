"""
Initializes API routers for books and reviews.
"""
from fastapi import APIRouter
from app.api.book import router as book_routes
from app.api.review import router as review_routes

book_router = APIRouter()
book_router.include_router(book_routes, prefix="/books", tags=["Books"])
book_router.include_router(review_routes, prefix="/books", tags=["Reviews"])
