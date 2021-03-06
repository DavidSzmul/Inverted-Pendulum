#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets

logging.basicConfig()

STATE = {"counter": 0, "slider": "0"}
USERS = set()


def state_event():
    return json.dumps({"type": "state", **STATE})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            keys = list(data.keys())
            for key in keys:
                if key == "action":

                    if data["action"] == "minus":
                        STATE["counter"] -= 1
                    elif data["action"] == "plus":
                        STATE["counter"] += 1

                elif key == "slider":
                    STATE["slider"] = data["slider"]

                else:
                    logging.error("unsupported event: {}", key)
            await notify_state()

    finally:
        await unregister(websocket)


# start_server = websockets.serve(counter, "localhost", 6789)
start_server = websockets.serve(counter, "192.168.1.12", 80)
print("WebSocket launched")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()