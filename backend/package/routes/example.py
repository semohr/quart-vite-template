"""Example routes.

This example shows how to add routes as a blueprint to the quart
app. Adds the 'api_v1/example' route.
"""

import asyncio

from quart import Blueprint, websocket

example_bp = Blueprint("example", __name__, url_prefix="/example")


@example_bp.route("/", methods=["GET"])
async def get():
    return {"message": "Hello, World!"}


@example_bp.route("/", methods=["POST"])
async def post():
    return {"message": "Hello, World!"}


@example_bp.websocket("/")
async def ws():
    try:
        while True:
            # Simple echo
            data = await websocket.receive()
            await websocket.send_json({"echo": data})
    except asyncio.CancelledError:
        # Handle disconnection here
        raise
