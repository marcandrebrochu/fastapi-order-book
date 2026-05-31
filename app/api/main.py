from fastapi import APIRouter

from app.api.routes import books, limit_orders, market_orders


api_router = APIRouter()

api_router.include_router(limit_orders.router)
api_router.include_router(market_orders.router)
api_router.include_router(books.router)