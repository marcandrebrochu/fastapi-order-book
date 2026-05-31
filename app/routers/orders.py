from typing import Annotated, Union
import uuid

from fastapi import APIRouter
from pydantic import Field

from app.schemas.order import LimitOrder, MarketOrder

router = APIRouter()

@router.post(
    "/orders",
    summary="Place an order",
    tags=["orders"],
)
def place_order(
    order: Annotated[Union[LimitOrder, MarketOrder], Field(discriminator="type")],
    pair_id: str,
) -> LimitOrder | MarketOrder:
    return order

@router.put(
    "/orders/{order_id}",
    summary="Modify an order",
    tags=["orders"],
)
def modify_order(order_id: uuid.UUID):
    pass

@router.delete(
    "/orders/{order_id}",
    summary="Cancel an order",
    tags=["orders"],
)
def cancel_order(order_id: uuid.UUID):
    pass