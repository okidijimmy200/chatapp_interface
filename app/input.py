import sys, argparse
from interfaces import UserInputDeliveryReportInterface, ParseArgsInterface


class UserInputService(UserInputDeliveryReportInterface):
    def write_message(self):
        print('Please enter a message')

        try:
            user_input = ''
            for line in sys.stdin:
                if line == '\n':
                    break
                user_input += line
            return user_input

        except:
            sys.stderr.write('Exception Occurred in the system input!\n')

    def delivery_report(self, err, msg):
        try:
            if err is not None:
                x = 'Message delivery failed: {}'.format(err)
                return x
            else:
                y = 'Message delivered to {} [{}]'.format(msg.topic(), msg.partition())
                return y
        except NameError:
            return "NameError occurred. err or msg isn't defined."
        
class ParseArgsService(ParseArgsInterface):
    def parse_args(self):
        try:
            parser = argparse.ArgumentParser()
            subparser = parser.add_subparsers(dest='command')
            send = subparser.add_parser('send')
            receive = subparser.add_parser('receive')

            send.add_argument('--channel', type=str, required=True)
            send.add_argument('--server', type=str, required=True)
            send.add_argument('--group', type=str, required=False)

            receive.add_argument('--channel', type=str, required=True)
            receive.add_argument('--start_from', type=str, required=True)
            receive.add_argument('--server', type=str, required=True)
            receive.add_argument('--group', type=str, required=True)

            args = parser.parse_args()
            return args  
        except SystemExit:
            print("System exit error.")
