from flask import Flask, request, redirect
from firebase import firebase
from slackclient import SlackClient

import json
import twilio.twiml
import time

import firebase_paths as fb

app = Flask(__name__)

firebase_client  = firebase.FirebaseApplication('https://burning-torch-4695.firebaseio.com', None)
 
slack_client = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")

# update_channel does the following:
# - creates the channel if necessary.
# - sets the channel state 
# - 
def update_channel(channel_name):
    create_channel(channel_name)
    channel_state = firebase_client.get(fb.CHANNELS_PATH + "/" + channel_name + fb.CHANNELS_INFO_SUBDIR,
                                        fb.CHANNELS_INFO_KEY_STATE)
    print channel_state
    print fb.CHANNELS_INFO_VAL_STATE_WORKER_UNASSIGNED
    if channel_state != fb.CHANNELS_INFO_VAL_STATE_WORKER_UNASSIGNED:
        firebase_client.put(fb.CHANNELS_PATH + "/" + channel_name + fb.CHANNELS_INFO_SUBDIR, 
                            fb.CHANNELS_INFO_KEY_STATE, fb.CHANNELS_INFO_VAL_STATE_WAITING_FOR_WORKER, 
                            connection=None)

# create_channel checks if the channel already exists by checking in firebase
# else it creates the slack channel and then updates firebase.
# it also sets the state to WORKER_UNASSIGNED
def create_channel(channel_name):
    # Check in firebase for this channel.
    fb_result = firebase_client.get(fb.CHANNELS_PATH + "/" + channel_name + fb.CHANNELS_INFO_SUBDIR,
                                    fb.CHANNELS_INFO_KEY_STATE)
#    print "looking for channel"
#    print channel_name
#    print fb_result
    if fb_result:
        return
    # If doesn't exist, call channels API to create this channel and update it
    # in firebase
    response = slack_client.api_call("channels.create", name=channel_name)         
    response_dict = json.loads(response)
    if response_dict["ok"]:
        firebase_client.put(fb.CHANNELS_PATH + "/" + channel_name + fb.CHANNELS_INFO_SUBDIR, 
                            fb.CHANNELS_INFO_KEY_STATE, fb.CHANNELS_INFO_VAL_STATE_WORKER_UNASSIGNED, 
                            connection=None)
        return
    print "channel creation failed"


@app.route("/", methods=["GET", "POST"])
def hello():
    print "hello"
    number = request.values.get("From", None)
    # Get rid of the "+"
    slack_channel = str(number)[1:]
    # Do all the bookkeeping.
    update_channel(slack_channel)
    # Post the message in slack.
    message = request.values.get("Body", None)    
    resp = twilio.twiml.Response()
    sr = slack_client.api_call("chat.postMessage", channel="#" + slack_channel, text=message)
    # TODO(dosareddi): Check if this is necessary.
    return resp.message("")

@app.route("/register", methods=["GET", "POST"])
def register_worker():
    print "Worker register invoked"
    # Check token
    # Add worker to Firebase.
    return ""

if __name__ == "__main__":
    app.run(debug=True)

