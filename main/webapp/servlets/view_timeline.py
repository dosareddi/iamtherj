import flask

from flask import redirect
from flask import render_template
from flask import request
from clientware import eventlines
from pprint import pprint 
from webapp import forms


# TODO(dasarathi): Create a base servlet class that has all the common crap 
# setup, creating the display dictionary, importing stuff.
def run():
  timeline_id = request.args.get('timeline', '')
  if not timeline_id:
    return redirect("/index")
  
  timeline_renderer = eventlines.get_timeline_renderer(int(timeline_id))
  # TODO(dasarathi): better error handling instead of redirecting.
  if not timeline_renderer:
    flask.flash("Failed to retrieve timeline")
    return redirect("/index")

  add_event_form = forms.AddEventForm()
  return render_template("view_timeline.html", 
                         timeline=timeline_renderer, 
                         add_event_form=add_event_form)
