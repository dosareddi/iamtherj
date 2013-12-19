from functools import wraps
from flask import request
from flask import render_template

from webapp import forms

def templated(template):
  def decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      template_name = template
      ctx = f(*args, **kwargs)
      if ctx is None:
        ctx = {}
      elif not isinstance(ctx, dict):
        # This will thrown a ISE.
        return ctx
      # Init the create_timeline form here so that it's available to all 
      # pages.  
      ctx["create_timeline_form"]  = forms.CreateTimelineForm()
      print ctx
      return render_template(template_name, **ctx)
    return decorated_function
  return decorator
