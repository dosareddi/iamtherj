import flask
from flask import render_template

app = flask.Flask(__name__)

################################################################################
# Main page
################################################################################
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

