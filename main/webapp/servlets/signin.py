import flask
from flask import request
from google.appengine import api

def run():
  google_url = api.users.create_login_url(
    flask.url_for("authorized", next=request.args.get("next")))
  return flask.redirect(google_url)
