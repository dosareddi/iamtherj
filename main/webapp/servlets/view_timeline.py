from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request

from api import eventlines

# TODO(dasarathi): Create a base servlet class that has all the common crap 
# setup, creating the display dictionary, importing stuff.
def run():
  timeline_id = request.args.get('timeline', '')
  if not timeline_id:
    return redirect("/index")
  
  timeline = eventlines.get_timeline(int(timeline_id))
  # TODO(dasarathi): better error handling instead of redirecting.
  if not timeline:
    return redirect("/index")
    
  display = {}
  display["timeline"] = timeline

  return render_template("view_timeline.html", display=display)
