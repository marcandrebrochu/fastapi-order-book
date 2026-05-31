from typing import Any

from fastapi import APIRouter

from app.models import ExecutedMarketOrderPublic, MarketOrderCreate


router = APIRouter(
    prefix="/market-orders",
    tags=["market orders"],
)


@router.post(
    "/",
    summary="Place a market order",
    response_model=ExecutedMarketOrderPublic,
)
def place_market_order(order_in: MarketOrderCreate) -> Any:
    pass