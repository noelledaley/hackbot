from slackclient import SlackClient
import os

bot = os.environ['SLACK_TOKEN']
token = os.environ['SLACK_AUTH']
sc = SlackClient(token)

print sc.api_call("auth.test")

SlackClient.rtm_connect()
print 'Connected to websocket.\n'
