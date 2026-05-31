import uuid
from enum import Enum
from pydantic import BaseModel
from typing import Literal

class OrderSide(str, Enum):
    buy = "buy"
    sell = "sell"
    
class BaseOrder(BaseModel):
    id: uuid.UUID
    side: OrderSide
    quantity: int

class MarketOrder(BaseOrder):
    type: Literal["market"]

class LimitOrder(BaseOrder):
    type: Literal["limit"]
    price: int