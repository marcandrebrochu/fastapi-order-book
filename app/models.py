from datetime import datetime
from enum import Enum
import uuid

from sqlmodel import SQLModel


class BookBase(SQLModel):
    base_asset: str
    quote_asset: str


class BookPublic(BookBase):
    id: str # "base:quote", for client convenience


class BooksPublic(SQLModel):
    data: list[BookPublic]
    count: int


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