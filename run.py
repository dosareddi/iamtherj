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

'''
The parameter of the callback function is a dict returns from the slack's outgoing api.
Here is the detail:
kwargs
{
    'token': token,
    'team_id': team_id,
    'team_domain': team_domain,
    'channel_id': channel_id,
    'channel_name': channel_name,
    'timestamp': timestamp,
    'user_id': user_id,
    'user_name': user_name,
    'text': text,
    'trigger_word': trigger_word
}'''
def process_slack(kwargs):
    '''
    This function shows response the slack post directly without an extra post.
    In this case, you need to return a dict.'''
    client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(to="+" + channel_name, from_="+12139153611",
                                     body=kwargs[text])
    return {'text': '!sent'}

def filter_slack(text):
    '''
    This function is a filter, which makes our bot ignore the text sent from itself.'''
    return text.startswith('!')

 
@app.route("/", methods=["GET", "POST"])
def hello():
    number = request.values.get('From', None)
    slack_channel = "#" + str(number)[1:]
    message = request.values.get('Body', None)

#    Saving the conversation in firebase.
#    path = "/conversations/" + str(number)
#    fb = firebase.FirebaseApplication('https://burning-torch-4695.firebaseio.com', None)
#    result = fb.post(path, {'msg': message})
#    print result

    resp = twilio.twiml.Response()

    sc = SlackClient("xoxp-12574501523-12578409008-17628102802-e267e28b16")
    if sc != None:
        sr = sc.api_call("chat.postMessage", channel=slack_channel, text=message)         
        resp.message(slack_channel)
    else:
        resp.message("fail")
    return str(resp)

slackbot.set_handler(process_slack)
slackbot.filter_outgoing(filter_slack)
  
if __name__ == "__main__":
    app.run(debug=True)
