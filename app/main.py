from fastapi import FastAPI

from app.routers import orders
from app.routers import pairs

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

app.include_router(orders.router)
app.include_router(pairs.router)