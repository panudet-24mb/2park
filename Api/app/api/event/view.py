from sanic import response , Blueprint
import os
import asyncpg
from sanic.websocket import WebSocketCommonProtocol
from websockets.exceptions import ConnectionClosed
from sanic.log import logger
from app.db import redis
import asyncio_redis
import json

event_service = Blueprint(name="event_service")



@event_service.route("/event/<room_id>" , methods=['POST'])
async def send_event(request , room_id):
  params = request.json
  c = await redis.send_message(int(room_id),json.dumps(params))
  return response.json(c)


