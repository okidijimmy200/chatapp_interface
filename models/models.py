from typing import Tuple, Optional
from dataclasses import dataclass


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


@dataclass
class ConsumerRequest:
    channel: str
    start_from: str
    server: str
    group: str
    running: dict

@dataclass
class ConsumerResponse:
    msg: dict

class Namespace:
    channel: str
    command: str
    group: str
    server: str

    def __init__(self, channel: str, command: str, group: str, server: str) -> None:
        self.channel = channel
        self.command = command
        self.group = group
        self.server = server

class NamespaceReceive:
    command: str
    channel: str
    start_from: str 
    server: str
    group: str

    def __init__(self, command: str,channel: str, start_from: str, server: str, group: str) -> None:
        self.command = command
        self.channel = channel
        self.start_from = start_from
        self.server = server
        self.group = group
