import io
from unittest import mock
from app.app import ChatApplication
from models.models import Namespace, NamespaceReceive

@mock.patch('cmds.input.ParseArgsService')
@mock.patch('messaging.servers.StreamingService')
def test_chat_application_send(stream_serv, args, monkeypatch):
    res = ChatApplication(args, stream_serv)
    res.args.parse_args.return_value = Namespace(channel='mychannel', command='send', group='mygroup', server='localhost:9092')
    # monkeypatch.setattr('sys.stdin', io.StringIO('my test data input'))
    res.stream_serv.publisher.return_value = 'my test data input'
    monkeypatch.setattr('sys.stdin', io.StringIO('my test data input'))
    output = res.streams()
    assert output == 'my test data input'

@mock.patch('cmds.input.ParseArgsService')
@mock.patch('messaging.servers.StreamingService')
def test_chat_application_receive(stream_serv, args):
    res = ChatApplication(args, stream_serv)
    res.args.parse_args.return_value = NamespaceReceive(command='receive', channel='mychannel', start_from='beginning',server='localhost:9092', group='mygroup')
    res.stream_serv.subscriber.return_value = 'test data'
    output = res.streams()
    assert output == 'test data'

