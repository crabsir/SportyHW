from .base_request import BaseRequest


class MainRequest(BaseRequest):
    def __init__(self, *args, **kwargs):
        super(MainRequest, self).__init__(*args, **kwargs)
