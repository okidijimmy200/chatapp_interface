from interfaces import (
    UserInputDeliveryReportInterface,
    ParseArgsInterface,
    StreamingServiceInterface
)
from input import (
    UserInputService,
    ParseArgsService
)
from servers import StreamingService

class ChatApplication():
    def __init__(
            self,
            args: ParseArgsInterface,
            input: UserInputDeliveryReportInterface,
            stream_serv: StreamingServiceInterface) -> None:
        
        self.args = args.parse_args()
        self.arg_command = args.parse_args().command
        self.input = input
        self.stream_serv = stream_serv
        

    def streams(self):
        if self.arg_command == 'send':
            return self.stream_serv.publisher(channel=self.args.channel, server=self.args.server, group=self.args.group)
        
        elif self.arg_command == 'receive':
            return self.stream_serv.subscriber(channel=self.args.channel, start_from=self.args.start_from, server=self.args.server, group=self.args.group)
        
chat_application = ChatApplication(ParseArgsService(), UserInputService(), StreamingService(UserInputService()))

chat_application.streams()