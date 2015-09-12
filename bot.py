from slackclient import SlackClient
import os
import time

class Hackbot(object):

    def __init__(self, token):
        self.token = token
        self.client = None

    def connect(self):
        self.client = SlackClient(self.token)
        self.client.rtm_connect()

    def read(self):
        while True:
            for response in self.client.rtm_read():
                print response
                
                if response.get('type') == 'message':
                    message = response.get('text')
                    channel = response.get('channel')
                    self.reply(message, channel)
                time.sleep(1)

    def reply(self, message, channel):
        if message == 'hello':
            self.client.rtm_send_message(channel, 'Hi there!')

# sc.rtm_connect()
# while True:
#     print sc.rtm_read()
#     if sc.rtm_read():
#         if sc.rtm_read()[0].get('text') and sc.rtm_read()[0].get('type') == 'message':
#             channel = sc.rtm_read()[0].get('channel')
#             sc.rtm_send_message(channel, 'Hello!')

    # [{u'text': u'are you listening?', u'ts': u'1442096766.000004', u'user': u'U076UD6J1', u'team': u'T06TYHMD4', u'type': u'message', u'channel': u'D0AJ3031V'}]

if __name__ == '__main__':
    token = os.environ['SLACK_TOKEN']
    balloonicorn = Hackbot(token)
    balloonicorn.connect()
