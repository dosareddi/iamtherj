import flask
from flask.ext import login
from google.appengine import api
from logic import users

from models.user_db import User

import pprint

def run():
  google_user = api.users.get_current_user()
  if google_user is None:
    flask.flash(u'You denied the request to sign in.')
    return flask.redirect("/index")

  google_id = str(google_user.user_id())
  name = google_user.nickname()
  email = google_user.email()
  luser = users.get_user_by_google_id(google_id)
  if not luser:
    luser = users.create_user(name, email, google_id=google_id)
  if login.login_user(luser):
    flask.flash("Hello %s !!!" % (login.current_user.name))
  else:
    flask.flash("Login Fail")
  return flask.redirect("/index")
