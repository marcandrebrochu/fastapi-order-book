from typing import Annotated

from fastapi import APIRouter, Path, Query, status

from app.schemas.pair import Pair

router = APIRouter()

@router.get(
    "/pairs",
    summary="Get the list of tradable all pairs",
    response_description="The list of all tradable pairs",
    tags=["pairs"],
)
def get_pairs() -> list[Pair]:
   return []

@router.post(
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
    return pair

@router.get(
    "/pairs/{pair_id}/book",
    summary="Get the order book associated with a tradable pair",
    tags=["pairs"],
)
def get_book_for_pair(
    pair_id: Annotated[str, Path(title="Pair identifier", description="A pair identifier, in the format `BASEASSET:QUOTEASSET`")],
    bid_ask_only: Annotated[bool, Query(description="Whether the query should produce the full order book, or just the bid/ask values")] = False,
):
    pass