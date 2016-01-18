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

SLACK_REGISTER_TOKEN = "r113P15z32hFS9ym7GFwBfR1"
SLACK_ASSIGN_CHANNEL_TOKEN = "amtyr1lSab5DTTjqSqYqQ0yE"

#TODO:
# - Don't expose phone number for channel

# update_channel does the following:
# - creates the channel if necessary.
# - sets the channel state 
# - 
def update_channel(channel):
    create_channel(channel)

# create_channel checks if the channel already exists by checking in firebase
# else it creates the slack channel and then updates firebase.
# it also sets the state to WORKER_UNASSIGNED
def create_channel(channel):
    print "Creating channel"
    # Check in firebase for this channel.
    fb_result = firebase_client.get(fb.CHANNEL_WORKER_PATH, channel)
    if fb_result:
        return
    # If doesn't exist, call channels API to create this channel and update it
    # in firebase
    response = slack_client.api_call("channels.create", name=channel)
    print response
    response_dict = json.loads(response)
    if response_dict["ok"]:
        firebase_client.put(fb.CHANNEL_WORKER_PATH,
                            channel, "0", connection=None)
        firebase_client.put(fb.CHANNEL_SLACK_ID_PATH,
                            channel, response_dict["id"], connection=None)
        return
    print "channel creation failed"


@app.route("/", methods=["GET", "POST"])
def hello():
    print "invoking hello"
    number = request.values.get("From", None)
    # Get rid of the "+"
    slack_channel = str(number)[1:]

    # Do all the bookkeeping.
    update_channel(slack_channel)

    # Post the message in slack.
    message = request.values.get("Body", None)    
    resp = twilio.twiml.Response()
    sr = slack_client.api_call("chat.postMessage", channel="#" + slack_channel,
                               text=message)

    # TODO(dosareddi): Check if this is necessary.
    return resp.message("")

@app.route("/register", methods=["GET", "POST"])
def register_worker():
    # Check token
    token = request.values.get("token", None)
    if token != SLACK_REGISTER_TOKEN:
        print "Invalid token\n"
        return None

    # Add worker to DB.
    user_id = request.values.get("user_id", None)
    user_name = request.values.get("user_name", None)
    firebase_client.put(fb.WORKERS_PATH + "/" + user_id + "/", 
                        fb.WORKERS_KEY_NAME, user_name, 
                        connection=None)
    return "Worker registered"

@app.route("/assign", methods=["GET", "POST"])
def assign():
    print "Assign channel invoked"
    # Check token
    token = request.values.get("token", None)
    if token != SLACK_ASSIGN_CHANNEL_TOKEN:
        print "Invalid token\n"
        return None

    print "valid token"
    
    # Check if worker is in DB.
    worker_id = request.values.get("user_id", None)
    worker = firebase_client.get(fb.WORKERS_PATH, worker_id)
    if not worker:
        return "You are not registered, please register first"
    print "worker registered"
    
    # Look at what channels are open.
    all_channels = firebase_client.get(fb.CHANNEL_WORKER_PATH, None)
    for channel, cur_worker in all_channels.iteritems():
        print "channel is " + channel
        if cur_worker != "0":
            continue

        # Put worker id in channel DB.
        firebase_client.put(fb.CHANNEL_WORKER_PATH, channel, worker_id,
                            connection=None)

        # Invite worker to channel.
        sr = slack_client.api_call("channels.invite",
                                   channel="#" + channel,
                                   user=worker_id)

        # TODO(dasarathi):
        # - Set topic to count of open channels. 
        print "found channel " + channel
        return "Channel Allocated"
    
    return "No Channel Found"


if __name__ == "__main__":
    app.run(debug=True)

