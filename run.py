from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    from_number = request.values.get('From', None)
 
    resp = twilio.twiml.Response()
    # Greet the caller by name
    resp.message("Hello ")
 
    return str(resp)
  
if __name__ == "__main__":
    app.run(debug=True)
