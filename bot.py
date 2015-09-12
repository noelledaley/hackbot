from slackclient import SlackClient
import os
import time
import random

class Hackbot(object):
    """
    An instance of Hackbot, the Hackbright XI Slack bot. Also known as Balloonicorn.
    """

    def __init__(self, token):
        self.token = token
        self.client = None

    def connect(self):
        """Set up SlackClient and connect to Real Time Messaging API."""
        self.client = SlackClient(self.token)
        self.client.rtm_connect()

    def read(self):
        """
        Read all events from Real Time Messaging API.
        Checks if balloonicorn is mentioned.
        """
        while True:
            for response in self.client.rtm_read():
                print response

                if response.get('type') == 'message':
                    message = response.get('text')
                    if 'balloonicorn' in message:
                        channel = response.get('channel')
                        self.reply(message, channel)
                time.sleep(1)

    def reply(self, message, channel):
        """
        When balloonicorn is mentioned, returns a random choice from a list of reponses.
        """

        reply = random.choice(['Hi there!', 'Yes?', ';)'])
        self.client.rtm_send_message(channel, reply)


if __name__ == '__main__':
    token = os.environ['SLACK_TOKEN']
    balloonicorn = Hackbot(token)
    balloonicorn.connect()
    balloonicorn.read()
