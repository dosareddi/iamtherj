import flask
from flask import render_template

webapp = flask.Flask(__name__)

################################################################################
# Main page
################################################################################
@webapp.route('/')
@webapp.route('/index')
def index():
  return render_template('index.html')

