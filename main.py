from cmds.input import (
    UserInputService,
    ParseArgsService
)
from messaging.servers import StreamingService
from app.app import ChatApplication

chat_application = ChatApplication(ParseArgsService(), StreamingService(UserInputService()))

chat_application.streams()