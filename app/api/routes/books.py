from datetime import datetime
from typing import Any

from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from app.api.deps import SessionDep
from app.models import Book, BookCreate, BookPublic, BooksPublic, ConflictMessage


router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.get(
    "",
    summary="Retrieve all order books",
    response_model=BooksPublic,
)
def read_books(session: SessionDep) -> Any:
    books = session.exec(select(Book)).all()
    return BooksPublic.from_books(list(books))


@router.get(
    "/{book_id}",
    summary="Retrieve an order book by its id",
    response_model=BookPublic,
)
def read_book(book_id: str) -> Any:
    pass


@router.post(
    "",
    summary="Create a new order book",
    response_model=BookPublic,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            "description": "A book with this base:quote pair already exists.",
            "model": ConflictMessage,
        },
    },
)
def create_book(book_in: BookCreate, session: SessionDep) -> Any:
    book = Book.model_validate(book_in)
    session.add(book)
    try:
        # No need to check for existing book with the same base:quote before trying to insert;
        # we can rely on sqlite's integrity checks for that, less work for us to do!..
        session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=ConflictMessage(
                message="a book with this base:quote pair already exists",
                since=datetime.now(),
            ).model_dump(mode="json"),
        )
    session.refresh(book)
    return BookPublic.from_book(book)