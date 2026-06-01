from datetime import datetime
from typing import Any

from fastapi import APIRouter, HTTPException, status
from sqlmodel import select

from app import utils
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
def read_book(book_id: str, session: SessionDep) -> Any:
    pair = utils.split_book_id(book_id)
    if pair is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="invalid book id format",
        )
    book = session.get(Book, pair)
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="book not found",
        )
    return BookPublic(**book.model_dump(), id=book_id)


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
    # Try to find a book having the same id as the user-given one.
    # TODO(mab): refactor to avoid having to remember which asset comes first when "deriving" the book id from the assets' symbols
    conficting_book = session.get(Book, (book_in.base_asset, book_in.quote_asset))
    if conficting_book is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=ConflictMessage(
                message="a book with this base:quote pair already exists",
                since=conficting_book.created_at,
            ).model_dump(mode="json"),
        )
    book = Book.model_validate({**book_in.model_dump(), "created_at": datetime.now()})
    session.add(book)
    session.commit()
    session.refresh(book)
    return BookPublic.from_book(book)