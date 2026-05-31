from typing import Any
import uuid

from fastapi import APIRouter, status

from app.models import LimitOrderCreate, LimitOrderPublic


router = APIRouter(
    prefix="/limit-orders",
    tags=["limit orders"],
)


@router.get(
    "/{order_id}",
    summary="Retrieve a limit order by its id",
    response_model=LimitOrderPublic,
)
def read_limit_order(order_id: uuid.UUID) -> Any:
    pass


@router.post(
    "/",
    summary="Place a limit order",
    response_model=LimitOrderPublic,
    status_code=status.HTTP_202_ACCEPTED,
)
def place_limit_order(
    order_in: LimitOrderCreate,
    book_id: str,
) -> Any:
    pass


@router.patch(
    "/{order_id}/price",
    summary="Modify a limit order's price",
)
def modify_limit_order_price(order_id: uuid.UUID) -> Any:
    pass


@router.patch(
    "/{order_id}/quantity",
    summary="Modify a limit order's quantity",
)
def modify_limit_order_quantity(order_id: uuid.UUID) -> Any:
    pass


@router.delete(
    "/{order_id}",
    summary="Cancel a limit order",
)
def cancel_limit_order(order_id: uuid.UUID) -> Any:
    pass