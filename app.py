import json
import asyncio
import random

from fastapi import FastAPI
from fastapi import WebSocket

app = FastAPI()
some_metrics = ([random.randint(1, 100) for i in range(1000)] for _ in range(10000))



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        await asyncio.sleep(0.1)
        await websocket.send_json(next(some_metrics))
