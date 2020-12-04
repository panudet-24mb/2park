from sanic import response , Blueprint
import os
import asyncpg
from sanic.websocket import WebSocketCommonProtocol
from websockets.exceptions import ConnectionClosed
from sanic.log import logger
from app.db import redis
import asyncio_redis
from tortoise.transactions import in_transaction
import json
import datetime, pytz
import uuid
from app.utils.json import  UUIDEncoder
tz = pytz.timezone('Asia/Bangkok')
event_service = Blueprint(name="event_service")



@event_service.route("/event/<room_id>" , methods=['POST'])
async def send_event(request , room_id):
  params = request.json
  c = await redis.send_message(int(room_id),json.dumps(params))
  async with in_transaction() as conn:
    uuid_entry = str( uuid.uuid4() ) 
    dt = datetime.datetime.now(tz)
    insert_statement = await conn.execute_query(
        " insert into event( event_name ,event_public_id , timestamp ,event_license_plate , event_picture ) "
        " VALUES ( $1 , $2 , $3 ,$4 ,$5 ) "  , 
        [params['event_name'] , uuid_entry , dt ,params['event_license_plate'] ,params['event_picture']]
      )
  return response.json(c)


@event_service.route("/event/<room_id>" , methods=['GET'])
async def send_event(request , room_id):
  async with in_transaction() as conn:
    rv = await conn.execute_query_dict(
        "select * from event order by event_id DESC"
      )
  json_data = json.dumps(rv , cls=UUIDEncoder)
  return response.json(json.loads(json_data))


