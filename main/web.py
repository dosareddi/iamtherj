"""
Handlers for the web application.
This is a thin layer over webapp.servlets, it should just call the run() module
in each servlet.
"""
import flask

from flask.ext import login
from logic import users
from webapp.servlets import add_event as add_event_handler
from webapp.servlets import authorized as authorized_handler
from webapp.servlets import create_user as create_user_handler
from webapp.servlets import create_timeline as create_timeline_handler
from webapp.servlets import index as index_handler
from webapp.servlets import signin as signin_handler
from webapp.servlets import signout as signout_handler 
from webapp.servlets import view_timeline as view_timeline_handler

from pprint import pprint

app = flask.Flask(__name__)
app.config.from_object("flask_config")
app.jinja_env.line_statement_prefix = "#"
app.jinja_env.line_comment_prefix = "##"

# Routing
# -------

@app.route("/")
@app.route("/index")
def index():
  return index_handler.run()  

@app.route("/create_user", methods = ["GET", "POST"])
def create_user():
  return create_user_handler.run() 

@app.route("/create_timeline", methods = ["GET", "POST"])
@login.login_required
def create_timeline():
  return create_timeline_handler.run() 

@app.route("/add_event", methods = ["GET", "POST"])
def add_event():
  return add_event_handler.run() 

@app.route("/view_timeline", methods = ["GET"])
def view_timeline():
  return view_timeline_handler.run() 

@app.route("/signin")
def signin():
  return signin_handler.run()

@app.route("/authorized")
def authorized():
  return authorized_handler.run()

@app.route("/signout")
def signout():
  return signout_handler.run()

# Logins
# ------
login_manager = login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/signin"

@login_manager.user_loader
def load_user(user_id):
  return users.get_user(user_id)
