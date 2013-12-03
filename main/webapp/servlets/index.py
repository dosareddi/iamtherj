import flask
from flask.ext import login
from webapp.forms import CreateTimelineForm

import pprint

def run():
  form = CreateTimelineForm()
  return flask.render_template("index.html", form=form)
