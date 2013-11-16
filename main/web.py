"""
Handlers for the web application.
This is a thin layer over webapp.servlets, it should just call the run() module
in each servlet.
"""

import flask
from webapp.servlets import create_user
from webapp.servlets import index

app = flask.Flask(__name__)
app.config.from_object("flask_config")

@app.route("/")
@app.route("/index")
def index_handler():
  return index.run()  

@app.route("/create_user", methods = ["GET", "POST"])
def create_user_handler():
  return create_user.run() 

