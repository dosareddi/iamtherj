from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, IntegerField
from wtforms import validators 
from wtforms.ext.dateutil.fields import DateTimeField

class CreateUserForm(Form):
  name = TextField('name', validators = [validators.Required()])
  user_id = TextField('user_id', validators = [validators.Required()])
  email = TextField('email', validators = [validators.Email()])

class CreateTimelineForm(Form):
  name = TextField('name', validators = [validators.Required()])
  user_id = TextField('user_id', validators = [validators.Required()])
  description = TextField('description', validators = [validators.Required()])
  
class AddEventForm(Form):
  user_id = TextField('user_id', validators = [validators.Required()])
  timeline_id = IntegerField('timeline_id', 
                             validators = [validators.Required()])
  name = TextField('name', validators = [validators.Required()])
  description = TextField('description', validators = [validators.Required()])
  start_time = DateTimeField('start_time', validators = [validators.Required()],
                              display_format='%Y-%m-%d')
  end_time = DateTimeField('end_time', validators = [validators.Required()],
                           display_format='%Y-%m-%d')
