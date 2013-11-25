from flask import redirect
from flask import render_template
from flask import request

from clientware import eventlines
from pprint import pprint 

# TODO(dasarathi): Create a base servlet class that has all the common crap 
# setup, creating the display dictionary, importing stuff.
def run():
  timeline_id = request.args.get('timeline', '')
  if not timeline_id:
    return redirect("/index")
  
  timeline_renderer = eventlines.get_timeline_renderer(int(timeline_id))
  # TODO(dasarathi): better error handling instead of redirecting.
  if not timeline_renderer:
    return redirect("/index")
    
  pprint(timeline_renderer.__dict__)
  return render_template("view_timeline.html", 
                         timeline=timeline_renderer)
