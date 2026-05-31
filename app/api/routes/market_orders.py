from typing import Annotated, Any

from fastapi import APIRouter, Query

from app.models import ExecutedMarketOrderPublic, MarketOrderCreate


router = APIRouter(
    prefix="/market-orders",
    tags=["market orders"],
)


@router.post(
    "",
    summary="Place a market order",
    response_model=ExecutedMarketOrderPublic,
)
def place_market_order(
    order_in: MarketOrderCreate,
    max_slippage: Annotated[float | None, Query(
        ge=0.0,
        le=100.0,
        description=(
            "Maximum slippage accepted, as a percentage. "
            "If not specified, the order will proceed without a slippage limit, "
            "which could incur significant losses."
        ),
    )] = None,
) -> Any:
    pass