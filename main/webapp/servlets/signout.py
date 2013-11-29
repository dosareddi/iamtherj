import flask
from flask.ext import login

def run():
  login.logout_user()
  flask.flash(u"You have been signed out.", category="success")
  return flask.redirect("/index")
