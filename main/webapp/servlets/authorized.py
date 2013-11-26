import flask
from google.appengine import api
from logic import users

import pprint

def run():
  google_user = api.users.get_current_user()
  if google_user is None:
    flask.flash(u'You denied the request to sign in.')
    return flask.redirect("/index")
  pprint.pprint(google_user)
  user_id = google_user.user_id()
  name = google_user.nickname()
  email = google_user.email()
  luser = users.get_user(user_id)
  if not luser:
    luser = users.create_user(name, user_id, email)

  flask.flash("Hello %s !!!" % (name))
  
  return flask.redirect("/index")
