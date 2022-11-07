import pytest
from httpx import AsyncClient

from src.main import app


@pytest.mark.asyncio
async def test_client():
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        response = await client.get("/api/v1/users/")

    assert response.status_code == 200
