from flask import Flask, request, redirect
from firebase import firebase
import twilio.twiml
 
app = Flask(__name__)
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    number = request.values.get('From', None)
    message = request.values.get('Body', None)
    path = "/conversations/" + str(number)
    fb = firebase.FirebaseApplication('https://burning-torch-4695.firebaseio.com', None)
    result = fb.post(path, {'msg': message})
    print result
    resp = twilio.twiml.Response()
    resp.message(str(result))
 
    return str(resp)
  
if __name__ == "__main__":
    app.run(debug=True)
