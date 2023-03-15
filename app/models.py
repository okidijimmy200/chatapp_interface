from typing import Tuple, Optional


class PublisherRequest:
    server: str
    channel: str
    group: Optional[str]

    def __init__(self, server: str, channel: str, group: Optional[str]):
        self.server = server
        self.channel = channel
        self.group = group

class PublisherResponse:
    response: str

    def __init__(self, response: str):
        self.response = response