from flask import redirect
from flask import render_template
from webapp.forms import CreateTimelineForm

from logic import eventlines

# TODO(dasarathi): Create a base servlet class that has all the common crap 
# setup, creating the display dictionary, importing stuff.
def run():
  form = CreateTimelineForm()
  if form.validate_on_submit():
    print("user_id=" + form.user_id.data + "\n" +
          "name=" + form.name.data + "\n" +
          "description=" + form.description.data + "\n")
    eventlines.create_timeline(user_id=form.user_id.data, 
                               name=form.name.data, 
                               description=form.description.data)
    # TODO: Check and return errors.
    return redirect("/index")
  display = {}
  display["form"] = form
  return render_template("create_timeline.html", display=display)
