from typing import Annotated
from fastapi import FastAPI, Path, Query, status
from pydantic import BaseModel

app = FastAPI(
    title="Market Sim",
    description="Basic market and order book engine",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "pairs",
            "description": "Operations with asset pairs",
        },
        {
            "name": "orders",
            "description": "Operations with orders",
        },
    ],
    license_info={
        "name": "The Unlicense",
        "identifier": "Unlicense",
    },
)

class Pair(BaseModel):
    base: str
    quote: str

@app.get(
    "/pairs",
    summary="Get the list of tradable all pairs",
    response_description="The list of all tradable pairs",
    tags=["pairs"],
)
def get_pairs() -> list[Pair]:
   return []

@app.post(
    "/pairs",
    summary="Add a new tradable pair",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "description": "Added the pair successfully",
        },
        status.HTTP_409_CONFLICT: {
            "description": "Failed to add the pair because it is already tradable",
            "content": {
                "application/json": {
                    "example": {"tradable_since": "2024-01-01"}
                },
            },
        },
    },
    tags=["pairs"],
)
def add_pair(pair: Pair) -> Pair:
    pass

@app.get(
    "/pairs/{pair_id}/book",
    summary="Get the order book associated with a tradable pair",
    tags=["pairs"],
)
def get_book_for_pair(
    pair_id: Annotated[str, Path(title="Pair identifier", description="A pair identifier, in the format `BASEASSET:QUOTEASSET`")],
    bid_ask_only: Annotated[bool, Query(description="Whether the query should produce the full order book, or just the bid/ask values")] = False,
):
    pass

@app.post(
    "/orders",
    summary="Place an order",
    tags=["orders"],
)
def place_order(pair_id: str):
    pass

@app.put(
    "/orders/{order_id}",
    summary="Modify an order",
    tags=["orders"],
)
def modify_order(order_id: str):
    pass

@app.delete(
    "/orders/{order_id}",
    summary="Cancel an order",
    tags=["orders"],
)
def cancel_order(order_id: str):
    pass