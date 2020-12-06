import os
from sanic import Sanic
from simple_bcrypt import Bcrypt
from sanic_cors import CORS, cross_origin
from app.db import redis , postgres
from tortoise.contrib.sanic import register_tortoise
import asyncpg
import asyncio_redis
from app.api.api import api


def create_app():
    app = Sanic(__name__)
    app: asyncio_redis.Pool
    app.blueprint(api)
    bcrypt = Bcrypt(app)
    register_tortoise(app, generate_schemas=False ,config = postgres.config )
    CORS(app, automatic_options=True)
    # setup_cors(app)
    return app


# def setup_cors(app):
#     @app.middleware('response')
#     async def allow_cross_site(request, response):
#         response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
#         response.headers["Access-Control-Allow-Credentials"] = "true"
#         response.headers["Access-Control-Allow-Headers"] = "*"
