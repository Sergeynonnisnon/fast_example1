import asyncio
import time
import timeit
from time import sleep
import websockets


async def get_work():
    async with websockets.connect("ws://localhost:2000/ws") as websocket:
        a = 0
        f = open("bla", "a+")
        t = time.time()
        for _ in range(100000):
            await websocket.recv()
        print(time.time() - t)
        f.close()
        await websocket.close()


asyncio.run(get_work())
