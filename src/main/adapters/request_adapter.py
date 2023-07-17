from typing import Callable
from flask import request as FlaskRequest
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse

def request_adapter(request: FlaskRequest, controller: Callable) -> HttpResponse:

    body = None
    if request.data: body = request.json

    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.vire_args,
        url=request.full_path
    )


    http_response = controller(http_request)
    return http_response
