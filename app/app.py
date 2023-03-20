import threading
from app.interfaces import (
    ParseArgsInterface,
    StreamingServiceInterface
)
from models.models import PublisherRequest

class ChatApplication():
    def __init__(
            self,
            args: ParseArgsInterface,
            stream_serv: StreamingServiceInterface) -> None:
        
        self.args = args
        self.stream_serv = stream_serv

    def streams(self):
        if self.args.parse_args().command == 'send':
            return self.stream_serv.publisher(
                PublisherRequest(
                self.args.channel,
                self.args.server, 
                self.args.group
                ))
        
        elif self.args.parse_args().command == 'receive':
            def switch(running):
                running['running'] = True

            running = {
                'running': True
            }
            p = threading.Thread(
                target=switch,
                args=(running,)
            )
            p.start()
            return self.stream_serv.subscriber(channel=self.args.channel, start_from=self.args.start_from, server=self.args.server, group=self.args.group, running=running)
        