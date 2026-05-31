from collections.abc import Generator

from app.main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as c:
        yield c