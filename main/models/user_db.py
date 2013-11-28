"""
Data model for user information.
"""

from google.appengine.ext import ndb

class User(ndb.Model):
  """Basic information about a user."""
  name = ndb.StringProperty(indexed=True, required=True)
  email = ndb.StringProperty(indexed=True, required=True)

  # These are ids from logins we want to support, like google, facebook etc. 
  google_id = ndb.StringProperty(indexed=True, required=False)
    
  # TBD: Timelines followed by a user. Consider splitting these out into a 
  # separate class.
  timeline_ids = ndb.IntegerProperty(repeated=True)

  # Routines required for flask login implementation.
  def is_authenticated(self):
    return True
   
  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    return unicode(self.key.id())
