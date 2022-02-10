from calendar import timegm
from datetime import datetime, timedelta

import jwt
from typing import Dict, Any
from flask import current_app


class JwtToken:
    def __init__(self, data: Dict[str, Any]):
        self._now = datetime.now()
        self._data = data
        self._access_token_expiration = 10
        self._refresh_token_expiration = 30


    def get_token(self, time_delta: timedelta):
        self._data.update({
            'exp': timegm((self._now + time_delta).timetuple())

        })
        return jwt.encode(
            self._data, current_app.config['SECRET_HERE'], algorithm='H256')

    @property
    def refresh_token(self):
        return self.get_token(time_delta=timedelta(days=self._refresh_token_expiration))

    @property
    def access_token(self):
        return self.get_token(time_delta=timedelta(days=self._access_token_expiration))

    def get_tokens(self):
        return {
            'refresh_token' : self.refresh_token,
            'access_token' : self.access_token

        }

    @staticmethod
    def decode_token(token: str):
        return jwt.decode(token, current_app.config['SECRET_HERE'], algorithms='H256')