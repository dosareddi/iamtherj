from flask import Flask, request, redirect
from firebase import firebase
from slackclient import SlackClient
from twilio.rest import TwilioRestClient

import json
import twilio.twiml
import time

TWILIO_ACCOUNT_SID="AC3de92c17107049aece1a2378b84b3e38"
TWILIO_AUTH_TOKEN="10f150926cea141e336ad7864b6488e6"

# THINGS TO FIX
# P0: No duplicates.
# P0: Get phone number from channel info.
# P2. Persist messages to DB, or at least the last timestamp

slack_client = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")

FIREBASE_CHANNEL_NUMBERS_PATH = "/channel_numbers"
FIREBASE_CHANNEL_TIMESTAMP_PATH = "/channel_timestamp"
firebase_client  = firebase.FirebaseApplication('https://burning-torch-4695.firebaseio.com', None)


def get_channel_number(channel_name):
    # Check in firebase for this channel.
    fb_result = firebase_client.get(FIREBASE_CHANNEL_NUMBERS_PATH, channel_name)
    if fb_result:
        return fb_result
    # If doesn't exist, call channels API to get info for this channel 
    # and update it in firebase
    response = slack_client.api_call("channels.info", channel=channel_name)         
    response_dict = json.loads(response)
    if response_dict["ok"]:
        number = response_dict["channel"]["name"]
        firebase_client.put(FIREBASE_CHANNEL_NUMBERS_PATH, channel_name, number, connection=None)
        return number
    return None


slack_client.rtm_connect()
while True:
    messages = slack_client.rtm_read()
    for m in messages:
        if m["type"] == "message" and m.get("subtype", "") != "bot_message":
            client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            number = get_channel_number(m["channel"])
            if not number:
                continue
            timestamp = float(m["ts"])
            chkpoint = 0
            channel_timestamp = firebase_client.get(FIREBASE_CHANNEL_TIMESTAMP_PATH, number)
            if channel_timestamp:
                chkpoint = channel_timestamp
            if timestamp > chkpoint :
                message = client.messages.create(to="+" + number, from_="+12139153611",
                                                 body=m["text"])
                firebase_client.put(FIREBASE_CHANNEL_TIMESTAMP_PATH, number, timestamp, connection=None)
                
    time.sleep(0.5)
