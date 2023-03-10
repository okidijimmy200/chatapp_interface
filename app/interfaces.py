from abc import ABC, abstractmethod
from typing import Tuple

class StreamingServiceInterface(ABC):
    @abstractmethod
    def publisher(self, server, channel, group=None):
        pass

    @abstractmethod
    def subscriber(self, channel, start_from, server, group):
        pass

class UserInputDeliveryReportInterface(ABC):
    @abstractmethod
    def write_message(self):
        pass

    @abstractmethod
    def delivery_report(self, err, msg):
        pass

class ParseArgsInterface(ABC):
    @abstractmethod
    def parse_args(self):
        pass