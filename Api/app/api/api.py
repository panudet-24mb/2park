from sanic import Blueprint
from app.api.event.view import event_service


api = Blueprint.group(event_service, url_prefix='/api/v1')

