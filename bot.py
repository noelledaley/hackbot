from slackclient import SlackClient
import os
import time

bot = os.environ['SLACK_TOKEN']
sc = SlackClient(bot)

print sc.api_call("auth.test")

sc.rtm_connect()
while True:
    print sc.rtm_read()
    time.sleep(1)
