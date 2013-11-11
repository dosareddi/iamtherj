"""
Data models for events and timelines.
"""

from google.appengine.ext import ndb

class Event(ndb.Model):
  """Basic information about an event."""
  name = ndb.StringProperty(indexed=True, required=True)

  description = ndb.StringProperty()
  start_time = ndb.DateTimeProperty(required=True)
  end_time = ndb.DateTimeProperty(required=True)
  
  # TODO(dasarathi): Consider using the calendar DAV format for storing.

# TBD: Call this timeline instead?
# Or: Have eventline object that is composed of multiple timelines?
class Eventline(ndb.Model):
  """A timeline of events or sub-timelines."""
  name = ndb.StringProperty(indexed=True, required=True)
  description = ndb.StringProperty()

  user_id = ndb.StringProperty(indexed=True, required=True)

  # TODO(dasarathi): Add tags.

  events = ndb.StructuredProperty(Event, repeated=True)  
  # TBD: use keys or timeline ids?
  child_eventlines = ndb.KeyProperty(kind='Eventline', repeated=True)
  



