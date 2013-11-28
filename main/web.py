"""
Handlers for the web application.
This is a thin layer over webapp.servlets, it should just call the run() module
in each servlet.
"""
import flask

from flask.ext import login
from logic import users
from webapp.servlets import add_event
from webapp.servlets import authorized
from webapp.servlets import create_user
from webapp.servlets import create_timeline
from webapp.servlets import index
from webapp.servlets import signin
from webapp.servlets import view_timeline

from pprint import pprint

app = flask.Flask(__name__)
app.config.from_object("flask_config")
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = '##'

# Routing
# -------

@app.route("/")
@app.route("/index")
def index_handler():
  return index.run()  

@app.route("/create_user", methods = ["GET", "POST"])
def create_user_handler():
  return create_user.run() 

@app.route("/create_timeline", methods = ["GET", "POST"])
def create_timeline_handler():
  return create_timeline.run() 

@app.route("/add_event", methods = ["GET", "POST"])
def add_event_handler():
  return add_event.run() 

@app.route("/view_timeline", methods = ["GET"])
def view_timeline_handler():
  return view_timeline.run() 

@app.route('/signin')
def signin_handler():
  return signin.run()

@app.route('/authorized')
def authorized_handler():
  return authorized.run()

# Logins
# ------
login_manager = login.LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
  return users.get_user(user_id)
