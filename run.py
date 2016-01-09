from flask import Flask, request, redirect
from firebase import firebase
from slackclient import SlackClient

import twilio.twiml
import time

app = Flask(__name__)
 
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
    return resp.message(str(sr))

if __name__ == "__main__":
    app.run(debug=True)

