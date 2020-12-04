import os
import logging
import asyncio
from app.core import create_app
from sanic.websocket import WebSocketProtocol
from websockets.exceptions import ConnectionClosed
from websockets import exceptions
from sanic import response
from sanic.log import logger
from app.db import redis
import json
import concurrent
import ssl

app = create_app()
app.static("/", "./sample.html")




@app.websocket('/init_socket/<user_public_id>')
async def init_socket(request, ws , user_public_id):
    try:
        connection_redis = await redis.create_connection_pool()
        logger.debug(f"/init_socket connected from {request.ip} {user_public_id}")
        await ws.send(json.dumps({ "system_event": " hello world" }))
        c = await redis.subscribe_channel(connection_redis , user_public_id)
        logger.debug(f" test {c}")
        while True:
            reply = await redis.receive_message(c)
            await ws.send(reply.value)
    except exceptions.ConnectionClosedOK:
        connection_redis.close()
        logger.debug("/ws1 ConnectionClosedOK")
    except exceptions.ConnectionClosedError:
        connection_redis.close()
        logger.debug("/ws1 ConnectionClosedError")
    except ConnectionClosed:
        connection_redis.close()
        logger.debug("/ws1 ConnectionClosed: " + str(e))
    except exceptions.WebSocketException as e:
        connection_redis.close()
        logger.debug("/ws1 WebSocketException: " + str(e))
    except concurrent.futures.CancelledError:
        connection_redis.close()
        logger.debug("/ws1 CancelledError") # ws.recv() raised this

 


if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=8999 ,debug=True, workers=2  ,protocol=WebSocketProtocol )
    # context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
    # context.load_cert_chain("/home/ubuntu/cert.pem", keyfile="/home/ubuntu/key.pem")
    # app.run(host="0.0.0.0" , port=8080 ,debug=True,workers=2,protocol=WebSocketProtocol , ssl=context )