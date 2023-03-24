import io, sys, pytest
from cmds.input import UserInputService, ParseArgsService

class Message():
    @staticmethod
    def topic():
        return 'mess'

    @staticmethod
    def partition():
        return 'age'

@pytest.fixture
def messg():
    return Message


'''test input from user'''
def test_user_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('my test data input'))
    user_input = UserInputService()
    i = user_input.read_message()
    assert i == 'my test data input'

'''test delivery report'''
def test_delivery_report(messg):
    test_table =[
        {
        "name": "pass",
        "msg": messg,
        "error": None,
        "output": "Message delivered to mess [age]"
        },
        {
        "name": "fail",
        "msg": "message",
        "error": 'error',
        "output": "Message delivery failed: error"
        }
    ]
    for test_case in test_table:
        user_input = UserInputService()
        response = user_input.delivery_report(err=test_case['error'], msg=test_case['msg'])
        assert response == test_case['output']

'''test systen receive'''
def test_parse_args():
    test_table = [
        {
        "name": "send",
        "cmd": "main.py send --channel mytopic --server localhost:9092 --group mygroup",
        "command": "send"
        },
        {
        "name": "receive",
        "cmd": "main.py receive --channel mytopic --start_from beginning --server localhost:9092 --group mygroup",
        "command": 'receive'
        }
    ]
    for test_case in test_table:
        
        sys.argv = test_case['cmd'].split(' ')
        parse_args = ParseArgsService()
        result = parse_args.parse_args()
        assert result.channel == 'mytopic'
        assert result.server == 'localhost:9092'
        assert result.group == 'mygroup'
        assert result.command == test_case['command']
