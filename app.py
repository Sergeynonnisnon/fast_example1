import json
import asyncio
import random
from timeit import timeit
import os, psutil
from fastapi import FastAPI
from fastapi import WebSocket
import time

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    process = psutil.Process(os.getpid())
    while True:
        await websocket.send_json(
            [process.memory_info().rss, process.cpu_percent(), process.username(), process.connections()])
