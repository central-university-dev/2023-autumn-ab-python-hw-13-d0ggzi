import json
# import pprint

from .types import Response
from .parser import RequestParser


async def app(scope, receive, send) -> None:
    event = await receive()
    # pprint.pprint(event)
    # print("------------------------")
    # pprint.pprint(scope)
    body = json.loads(event['body'].decode('utf-8')) if len(event['body']) else {}
    query_string = scope['query_string'].decode('utf-8')
    for element in query_string.split("&"):
        key, value = element.split("=")
        body[key] = value

    response: Response = RequestParser(body, scope['method'], scope['path'], scope['headers']).parse()

    await send(
        {
            "type": "http.response.start",
            "status": response.status_code,
            "headers": response.headers
        }
    )

    await send(
        {
            "type": "http.response.body",
            "body": response.body
        }
    )

