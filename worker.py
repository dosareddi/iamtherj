from flask import Flask, request, redirect
from firebase import firebase
from slackclient import SlackClient
from twilio.rest import TwilioRestClient

import json
import twilio.twiml
import time

import firebase_paths as fb

TWILIO_ACCOUNT_SID="AC3de92c17107049aece1a2378b84b3e38"
TWILIO_AUTH_TOKEN="10f150926cea141e336ad7864b6488e6"

# THINGS TO FIX
# P0: No duplicates.
# P0: Get phone number from channel info.
# P2. Persist messages to DB, or at least the last timestamp

slack_client = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")


firebase_client  = firebase.FirebaseApplication('https://burning-torch-4695.firebaseio.com', None)


def get_channel_name(slack_channel_id):
    # Hack to prevent messages from other channels.
    if not slack_channel_id.startswith("1"):
        return None
    # Check in firebase for this channel.
    fb_result = firebase_client.get(fb.SLACK_ID_CHANNEL_NAME_PATH, slack_channel_id)
    if fb_result:
        return fb_result
    # If doesn't exist, call channels API to get info for this channel 
    # and update it in firebase
    response = slack_client.api_call("channels.info", channel=slack_channel_id)         
    response_dict = json.loads(response)
    if response_dict["ok"]:
        channel_name = response_dict["channel"]["name"]
        firebase_client.put(fb.SLACK_ID_CHANNEL_NAME_PATH, slack_channel_id, channel_name, connection=None)
        return channel_name
    return None

# TODO(dasarathi): Filter messages starting with "<"
def is_valid_message(message_dict):
    if (message_dict["type"] == "message" and 
        message_dict.get("subtype", "") != "bot_message"):
        return True
    return False
    
# Go through messages from workers and forward them to customers.    
def process_worker_messages(messages):
    for m in messages:
        if is_valid_message(m):
            client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            number = get_channel_name(m["channel"])
            if not number:
                continue
            timestamp = float(m["ts"])
            chkpoint = 0
            channel_timestamp = firebase_client.get(
                fb.CHANNELS_PATH + "/" + number + fb.CHANNELS_MESSAGEINFO_SUBDIR, 
                fb.CHANNELS_MESSAGEINFO_KEY_LAST_SENT_TS)
            if channel_timestamp:
                chkpoint = channel_timestamp
            if timestamp > chkpoint :
                message = client.messages.create(to="+" + number, from_="+12139153611",
                                                 body=m["text"])
                firebase_client.put(
                    fb.CHANNELS_PATH + "/" + number + fb.CHANNELS_MESSAGEINFO_SUBDIR, 
                    fb.CHANNELS_MESSAGEINFO_KEY_LAST_SENT_TS, 
                    timestamp, connection=None)

# TODO(dasarathi): Move this to a separate worker.
def broadcast_unassigned_channels():
    # Get all channels.
    all_channels = firebase_client.get(fb.CHANNELS_PATH, None)
    unassigned_channels = []
    for c, val in all_channels.iteritems():
        if val["info"]["state"] == fb.CHANNELS_INFO_VAL_STATE_WORKER_UNASSIGNED:
            unassigned_channels.append(c)
    # print unassigned_channels
    # TODO(dasarathi): Add the following logic here
    # - Bringing a bot in to ask the basics
    # - Checking whether worker is right match

    # Get all open workers.
    

slack_client.rtm_connect()
while True:
    process_worker_messages(slack_client.rtm_read())
    broadcast_unassigned_channels()
                
    time.sleep(0.5)
