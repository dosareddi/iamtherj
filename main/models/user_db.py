"""
Data model for user information.
"""

from google.appengine.ext import ndb

class User(ndb.Model):
  """Basic information about a user."""
  name = ndb.StringProperty(indexed=True, required=True)
  user_id = ndb.StringProperty(indexed=True, required=True)
  email = ndb.StringProperty(indexed=True, required=True)
  # TODO(dasarathi): Look into this when adding auth support.
  # auth_ids = ndb.StringProperty(indexed=True, repeated=True)
  
  # TBD: Timelines followed by a user. Consider splitting these out into a 
  # separate class.
  timeline_ids = ndb.IntegerProperty(repeated=True)

