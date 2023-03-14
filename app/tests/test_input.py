import io, sys
from input import UserInputService, ParseArgsService


'''test input from user'''
def test_user_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('my test data input'))
    user_input = UserInputService()
    i = user_input.write_message()
    assert i == 'my test data input'

'''test delivery report'''
def test_delivery_report():
    user_input = UserInputService()
    response = user_input.delivery_report(err='error', msg='message')
    assert type(response) is str

'''test systen receive'''
def test_parse_args_recieve():
    # test coverage highlighter
    cmd = 'main.py receive --channel mytopic --start_from beginning --server localhost:9092 --group mygroup'
    
    sys.argv = cmd.split(' ')
    parse_args = ParseArgsService()
    result = parse_args.parse_args()
    assert result.channel == 'mytopic'
    assert result.server == 'localhost:9092'
    assert result.group == 'mygroup'