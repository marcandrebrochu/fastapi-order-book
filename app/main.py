from fastapi import FastAPI

from app.api.main import api_router
from app.core.config import settings


app = FastAPI(
    title="Market Sim",
    description="Basic order book engine",
    version="0.0.1",
    license_info={
        "name": "The Unlicense",
        "identifier": "Unlicense",
    },
)

app.include_router(api_router, prefix=settings.API_V1_STR)