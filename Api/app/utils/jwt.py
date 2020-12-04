from functools import wraps
from sanic.response import json
from tortoise.transactions import in_transaction
import os
import jwt

def authorized():
	def decorator(f):
		@wraps(f)
		async def decorated_function(request, *args, **kwargs):
			token = await check_request_for_authorization_status(request)
			if token:
				access_token = token.split(" ")[1]
				try:
					user_payload =  jwt.decode(access_token, os.getenv('SECRET_KEY') )
					current_token = await check_blacklist(user_payload)
					if access_token != current_token['system_token']:
						return json({'status': 'token_blacklist'}, 401)
				except Exception as e :
					return json({'status': 'not_authorized'}, 401)
				response = await f(request,user_payload, *args, **kwargs)
				return response
			else:
				return json({'status': 'not_authorized'}, 401)
		return decorated_function
	return decorator
