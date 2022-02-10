import base64
import hashlib
import hmac
from typing import Union

from flask import current_app


def get_password_digest(password: str):
    return hashlib.pbkdf2_hmac(
        hash_name='sha256',
        pasword=password.encode('utf=8'),
        salt = current_app.config('PWD_SALT'),
        iterations = current_app.config('PWD_ITERATIONS'),

    )

def get_password_hash(password: str):
    return base64.b64encode(get_password_digest(password)).decode('utf-8')

def compare_password(hash_password: Union[str, bytes], password: str):
    return hmac.compare_digest(
            base64.b64decode(hash_password),
            get_password_digest(password)

    )
