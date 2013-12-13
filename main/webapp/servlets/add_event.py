import flask
from flask import jsonify
from flask import redirect
from flask import request
from flask import render_template
from flask.ext import login
from webapp.forms import AddEventForm

from logic import eventlines

# TODO(dasarathi): Create a base servlet class that has all the common crap 
# setup, creating the display dictionary, importing stuff.
def run():
  form = AddEventForm()
  if not login.current_user.is_authenticated():
    flask.flash("Failed to add event, user not logged in")
    return jsonify()

  timeline_id = int(request.args.get('timeline', ''))
  if not timeline_id:
    flask.flash("Timeline not specified for adding event")
    return jsonify()
  if form.validate_on_submit():
    eventlines.add_event(user_id=login.current_user.id(),
                         timeline_id=timeline_id,
                         name=form.name.data,
                         description=form.description.data)
    return jsonify()
 
  return jsonify()  
