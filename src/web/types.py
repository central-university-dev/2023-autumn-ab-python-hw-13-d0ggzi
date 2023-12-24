import json
from typing import Dict, Any

default_headers = [
                (b"Accept", b"application/json"),
                (b"Access-Control-Allow-Origin", b"*"),
                (b"X-Requested-With", b"XMLHttpRequest"),
                (b"Access-Control-Allow-Methods", b"GET,POST,PUT,DELETE,OPTIONS"),
                (b"Access-Control-Allow-Headers", b"Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")
            ]


class Response:
    def __init__(self, status_code: int, body: str | Dict[Any, Any] = None, headers=None) -> None:
        if headers is None:
            headers = [[b"content-type", b"application/text"]]
        self.status_code = status_code
        self.body = bytes(body, encoding="raw_unicode_escape") if isinstance(body, str) else json.dumps(body).encode()
        self.headers = headers + default_headers

