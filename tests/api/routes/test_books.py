from fastapi.testclient import TestClient
from fastapi import status

from app.core.config import settings


def test_create_book(client: TestClient) -> None:
    data = {"base_asset": "ABC", "quote_asset": "XYZ"}
    response = client.post(
        f"{settings.API_V1_STR}/books",
        json=data,
    )
    assert response.status_code == status.HTTP_201_CREATED
    content = response.json()
    assert content["base_asset"] == data["base_asset"]
    assert content["quote_asset"] == data["quote_asset"]
    assert "id" in content