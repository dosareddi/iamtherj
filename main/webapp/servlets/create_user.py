from flask import redirect
from flask import render_template
from webapp.forms import CreateUserForm

from logic import users

# TODO(dasarathi): Create a base servlet class that has all the common crap 
# setup, creating the display dictionary, importing stuff.
def run():
  form = CreateUserForm()
  if form.validate_on_submit():
    print("name=" + form.name.data + "\n" +
          "user_id=" + form.user_id.data + "\n" +
          "email=" + form.email.data + "\n")
    users.create_user(name=form.name.data, user_id=form.user_id.data,
                      email=form.email.data)
    # TODO: Check and return errors.
    return redirect("/index")
  display = {}
  display["form"] = form
  return render_template("create_user.html", display=display)

