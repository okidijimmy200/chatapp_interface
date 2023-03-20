import  time, threading
from unittest import mock
from messaging.servers import StreamingService
from models.models import PublisherRequest

@mock.patch('cmds.input.UserInputService')
@mock.patch('messaging.servers.Producer')
def test_producer(Producer, user_input):
    res = StreamingService(user_input)
    p = Producer({'bootstrap.servers': 'server'})
    # p.flush.return_value = 'test work'
    # how to mock method implementations in python
    p.flush.return_value = 'test work'
    output = res.publisher(PublisherRequest('localhost:9092', 'mychannel', 'group'))
    assert output == 'test work'


@mock.patch('cmds.input.UserInputService')
@mock.patch('messaging.servers.Producer')
def test_consumer(Consumer, user_input, capsys):
    res = StreamingService(user_input)
    Consumer.poll.error.return_value = 'test error'
    Consumer.poll.value.return_value = 'test message'

    def switch(running):
        time.sleep(.001)
        running['running'] = False

    running = {
        'running': True
    }
    t = threading.Thread(
        target=switch,
        args=(running,)
    )
    t.start()
    res.subscriber('mychannel', 'beginning', 'localhost:9092', 'mygroup', running)
    captured = capsys.readouterr()

    x = list(captured.out)
    output = []
    for i in x:
        if i == '\n':
            break
        output.append(i)