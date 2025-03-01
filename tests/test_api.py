import pytest
from httpx import AsyncClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

base_url = "http://127.0.0.1"

@pytest.mark.asyncio
@pytest.fixture
async def test_health_check():
    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

@pytest.mark.asyncio
@pytest.fixture
async def test_chat():
    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.post("/chat", json={
            "message": "Hello, how are you?",
            "difficulty": "beginner",
            "style": "formal",
            "evaluate": True
        })
    assert response.status_code == 200
    assert "response" in response.json()
    assert "evaluation" in response.json()