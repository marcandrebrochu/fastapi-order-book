from typing import Any

from fastapi import APIRouter, status

from app.models import BookCreate, BookPublic, BooksPublic


router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.get(
    "/",
    summary="Retrieve all order books",
    response_model=BooksPublic,
)
def read_books() -> Any:
    pass


@router.get(
    "/{book_id}",
    summary="Retrieve an order book by its id",
    response_model=BookPublic,
)
def read_book(book_id: str) -> Any:
    pass


@router.post(
    "/",
    summary="Create a new order book",
    response_model=BookPublic,
    status_code=status.HTTP_201_CREATED,
)
def create_book(book_in: BookCreate) -> Any:
    pass