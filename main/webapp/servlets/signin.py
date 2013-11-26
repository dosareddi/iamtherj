import flask
from google.appengine import api

def run():
  google_url = api.users.create_login_url("/authorized")
  return flask.redirect(google_url)
