from slackclient import SlackClient
import os

token = os.environ['SLACK_AUTH']
sc = SlackClient(token)

print sc.api_call("auth.test")
print sc.api_call("channels.list")
