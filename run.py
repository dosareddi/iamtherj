from flask import Flask, request, redirect
from firebase import firebase
from slackclient import SlackClient

import json
import twilio.twiml
import time

app = Flask(__name__)

FIREBASE_CHANNEL_VERIFY_PATH = "/channels"
firebase_client  = firebase.FirebaseApplication('https://burning-torch-4695.firebaseio.com', None)
 
slack_client = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")

def create_channel(channel_name):
    # Check in firebase for this channel.
    fb_result = firebase_client.get(FIREBASE_CHANNEL_VERIFY_PATH, channel_name)
    if fb_result:
        return
    # If doesn't exist, call channels API to create this channel and update it
    # in firebase
    response = slack_client.api_call("channels.create", name=channel_name)         
    print response
    response_dict = json.loads(response)
    if response_dict["ok"]:
        firebase_client.put(FIREBASE_CHANNEL_VERIFY_PATH, channel_name, True, connection=None)
        print "channel created"
        return
    print channel_name
    print response
    print "channel creation failed"


@app.route("/", methods=["GET", "POST"])
def hello():
    number = request.values.get("From", None)
    slack_channel = str(number)[1:]
    create_channel(slack_channel)
    message = request.values.get("Body", None)
    
    resp = twilio.twiml.Response()
    sr = slack_client.api_call("chat.postMessage", channel="#" + slack_channel, text=message)         
    return resp.message("")

if __name__ == "__main__":
    app.run(debug=True)

