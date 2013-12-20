from flask.ext import login
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, BooleanField, IntegerField
from wtforms import validators 
from wtforms.ext.dateutil.fields import DateTimeField

class CreateUserForm(Form):
  name = TextField('name', validators = [validators.Required()])
  user_id = TextField('user_id', validators = [validators.Required()])
  email = TextField('email', validators = [validators.Email()])

class CreateTimelineForm(Form):
  name = TextField('name', validators = [validators.Required()])
  description = TextAreaField('description', validators = [])
  
class AddEventForm(Form):
  name = TextField('name', validators = [validators.Required()])
  description = TextAreaField('description', 
                              validators = [validators.Required()])
