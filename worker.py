from flask import Flask, request, redirect
from firebase import firebase
from slackclient import SlackClient
from twilio.rest import TwilioRestClient

import twilio.twiml
import time

TWILIO_ACCOUNT_SID="AC3de92c17107049aece1a2378b84b3e38"
TWILIO_AUTH_TOKEN="10f150926cea141e336ad7864b6488e6"

# THINGS TO FIX
# P0: No duplicates.
# P0: Get phone number from channel info.
# P2. Persist messages to DB, or at least the last timestamp

slack_client = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")

def get_channel_number(channel_name):
    # Check in firebase for this channel.
    response = slack_client.api_call("channels.info", channel=slack_name)         
    # If doesn't exist, call channels API to get info for this channel 
    # and update it.
    print response


sc.rtm_connect()
while True:
    messages = sc.rtm_read()
    for m in messages:   
        if m["type"] == "message" and m.get("subtype", "") != "bot_message":
            client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            get_channel_number(m["channel"]
            message = client.messages.create(to="+" + "12134469422", from_="+12139153611",
                                             body=m["text"])
            
    time.sleep(0.5)
