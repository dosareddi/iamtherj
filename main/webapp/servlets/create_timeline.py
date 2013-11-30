import flask
from flask import redirect
from flask import render_template
from flask.ext import login
from webapp.forms import CreateTimelineForm

from logic import eventlines

# TODO(dasarathi): Create a base servlet class that has all the common crap 
# setup, creating the display dictionary, importing stuff.
def run():
  form = CreateTimelineForm()
  if form.validate_on_submit():
    eventlines.create_timeline(user_id=login.current_user.id(), 
                               name=form.name.data, 
                               description=form.description.data)
    flask.flash("Timeline created")
    return redirect(flask.url_for("index"))

  return render_template("create_timeline.html", form=form)
