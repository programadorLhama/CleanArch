class HttpResponse:

    def __init__(self, status_code, body) -> None:
        self.status_code = status_code
        self.body = body
