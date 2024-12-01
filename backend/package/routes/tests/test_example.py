import pytest


@pytest.mark.asyncio
async def test_get(client):
    response = await client.get("/api_v1/example/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_post(client):
    response = await client.post("/api_v1/example/")
    response_json = await response.get_json()
    response_data = response_json.get("message")
    assert response_data == "Hello, World!"
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_ws(client):
    async with client.websocket("/api_v1/example/") as ws:
        await ws.send("Hello, World!")
        response = await ws.receive_json()
        assert response == {"echo": "Hello, World!"}
