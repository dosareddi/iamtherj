"""
Data model for user information.
"""

from google.appengine.ext import ndb

class User(ndb.Model):
  """Basic information about a user."""
  name = ndb.StringProperty(indexed=True, required=True)
  # TODO(dasarathi): For now a string, look into user id when adding auth 
  # support.
  user_id = ndb.StringProperty(indexed=True, required=True)
  email = ndb.StringProperty(indexed=True, required=True)
  # TODO(dasarathi): Look into this when adding auth support.
  # auth_ids = ndb.StringProperty(indexed=True, repeated=True)
  
  # TBD: Eventlines followed by a user. Consider splitting these out into a 
  # separate class.
  eventlines = ndb.KeyProperty(kind='Eventline', repeated=True)

