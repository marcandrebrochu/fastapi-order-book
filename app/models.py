from datetime import datetime
from enum import Enum
import uuid

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class BookBase(SQLModel):
    base_asset: str = Field(primary_key=True)
    quote_asset: str = Field(primary_key=True)


class Book(BookBase, table=True):
    created_at: datetime


class BookPublic(BookBase):
    id: str # "base:quote", for client convenience
    created_at: datetime

    @classmethod
    def from_book(cls, book: Book) -> "BookPublic":
        return cls(**book.model_dump(), id=f"{book.base_asset}:{book.quote_asset}")


class BooksPublic(SQLModel):
    data: list[BookPublic]
    count: int

    @classmethod
    def from_books(cls, books: list[Book]) -> "BooksPublic":
        return cls(data=list(map(BookPublic.from_book, books)), count=len(books))


class BookCreate(BookBase):
    pass


class OrderSide(str, Enum):
    buy = "buy"
    sell = "sell"


class OrderBase(SQLModel):
    side: OrderSide
    quantity: int


class MarketOrderCreate(OrderBase):
    pass


class ExecutedMarketOrderPublic(SQLModel):
    # was the order fully filled? (if not the user needs to know about it)
    # which were the trades that happened so this order could be filled?
    # how much slippage incurred?
    pass


class LimitOrderCreate(OrderBase):
    price: int


class LimitOrderPublic(OrderBase):
    id: uuid.UUID
    book_id: str
    accepted_at: datetime
    filled: int


class LimitOrder(OrderBase): # table=True
    id: uuid.UUID
    book_id: str


class ConflictMessage(BaseModel):
    message: str
    since: datetime