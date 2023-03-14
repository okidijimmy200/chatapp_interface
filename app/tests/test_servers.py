import  time, threading
from unittest import mock
from servers import StreamingService


@mock.patch('input.UserInputService')
@mock.patch('servers.Producer')
def test_producer(Producer, user_input):
    res = StreamingService(user_input)
    p = Producer({'bootstrap.servers': 'server'})
    p.flush.return_value = 'test work'
    output = res.publisher('localhost:9092', 'mychannel', 'mygroup')
    assert output == 'test work'


@mock.patch('input.UserInputService')
@mock.patch('servers.Consumer')
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