from flask import Flask, request, redirect
from firebase import firebase
from slackclient import SlackClient

import twilio.twiml
import time


app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    number = request.values.get('From', None)
    slack_channel = "#" + str(number)
    message = request.values.get('Body', None)

#    Saving the conversation in firebase.
#    path = "/conversations/" + str(number)
#    fb = firebase.FirebaseApplication('https://burning-torch-4695.firebaseio.com', None)
#    result = fb.post(path, {'msg': message})
#    print result
#    resp = twilio.twiml.Response()
#    resp.message(str(result))

    sc = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")
    if sc != None:
        sc.api_call("chat.postMessage", channel=slack_channel, text=message) 
    return ""
  
if __name__ == "__main__":
    app.run(debug=True)
