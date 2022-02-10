from functools import wraps

from flask import request
from flask_restx import abort
from jwt import PyJWTError

from tools.jwt_token import JwtToken


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            abort(401)

        try:
            token = auth_header.split('Bearer ')[-1]
            data = JwtToken.decode_token(token)
        except PyJWTError:

    return wrapper()
