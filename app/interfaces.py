from abc import ABC, abstractmethod
from models.models import PublisherRequest, PublisherResponse

class StreamingServiceInterface(ABC):
    @abstractmethod
    def publisher(self, req: PublisherRequest) -> PublisherResponse:
        pass

    @abstractmethod
    def subscriber(self, channel, start_from, server, group, running=None):
        pass

class UserInputDeliveryReportInterface(ABC):
    @abstractmethod
    def read_message(self):
        pass

    @abstractmethod
    def delivery_report(self, err, msg):
        pass

class ParseArgsInterface(ABC):
    @abstractmethod
    def parse_args(self):
        pass
