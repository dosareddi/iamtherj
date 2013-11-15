"""
Handlers for the web application.
This is a thin layer over webapp.servlets, it should just call the run() module
in each servlet.
"""

import flask
from flask import render_template
from webapp.servlets import create_user
from webapp.servlets import index

app = flask.Flask(__name__)
app.config.from_object('flask_config')

@app.route('/')
@app.route('/index')
def index_handler():
  index.run()  
  return render_template('index.html')

@app.route('/create_user')
def create_user_handler():
  create_user.run()  
  return render_template('create_user.html')

