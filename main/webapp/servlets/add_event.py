from flask import redirect
from flask import render_template
from webapp.forms import AddEventForm

from api import eventlines

# TODO(dasarathi): Create a base servlet class that has all the common crap 
# setup, creating the display dictionary, importing stuff.
def run():
  form = AddEventForm()
  if form.validate_on_submit():
    print("name=" + form.name.data + "\n" +
          "user_id=" + form.user_id.data + "\n" +
          "description=" + form.description.data + "\n")
    eventlines.add_event(user_id=form.user_id.data,
                         timeline_id=form.timeline_id.data,
                         name=form.name.data,
                         description=form.description.data,
                         start_time=form.start_time.data,
                         end_time=form.end_time.data)
    # TODO: Check and return errors.
    return redirect("/index")
  display = {}
  display["form"] = form
  return render_template("add_event.html", display=display)

