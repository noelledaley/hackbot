from slackclient import SlackClient
import os
import time

bot = os.environ['SLACK_TOKEN']
token = os.environ['SLACK_AUTH']
sc = SlackClient(bot)

print sc.api_call("auth.test")

sc.rtm_connect()
while True:
    print sc.rtm_read()
    time.sleep(1)
