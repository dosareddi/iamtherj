from flask import redirect
from flask import render_template
from webapp.forms import CreateUserForm

def run():
  form = CreateUserForm()
  if form.validate_on_submit():
    print("name=" + form.name.data + "\n" +
          "user_id=" + form.user_id.data + "\n" +
          "email=" + form.email.data + "\n")
    return redirect('/index')
  display = {}
  display['form'] = form
  return render_template("create_user.html", display=display)

