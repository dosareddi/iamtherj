from flask import Flask, request, redirect
from flask_slackbot import SlackBot
from firebase import firebase
from slackclient import SlackClient
from twilio.rest import TwilioRestClient

import twilio.twiml
import time

TWILIO_ACCOUNT_SID="AC3de92c17107049aece1a2378b84b3e38"
TWILIO_AUTH_TOKEN="10f150926cea141e336ad7864b6488e6"

app = Flask(__name__)
app.config["SLACK_TOKEN"] = "xoxp-12574501523-12578409008-17628102802-e267e28b16"
# if you need to use slacker you should give a slack chat token
app.config["SLACK_CHAT_TOKEN"] = 'yD1MPDH6wyef9jU92QbQLBvm'
app.config["SLACK_CALLBACK"] = '/slack_outgoing'
app.debug = True
slackbot = SlackBot(app)

 
@app.route("/", methods=["GET", "POST"])
def hello():
    number = request.values.get("From", None)
    slack_channel = "#" + str(number)[1:]
    message = request.values.get("Body", None)
    
    resp = twilio.twiml.Response()
    sc = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")
    
    if sc != None:
        sr = sc.api_call("chat.postMessage", channel=slack_channel, text=message)         
    else:
        return resp.message("fail")
    sr = sc.api_call("channels.create", name="12134468877")
    return resp.message(str(sr))

if __name__ == "__main__":
    app.run(debug=True)

