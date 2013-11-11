"""
Data models for events and timelines.
"""

from google.appengine.ext import ndb

class Event(ndb.Model):
  """Basic information about an event."""
  name = ndb.StringProperty(indexed=True, required=True)

  # TBD: Use the timestamp for this.. or some auto increment 
  event_id = ndb.IntegerProperty(indexed=True, required=True)

  description = ndb.StringProperty()
  start_time = ndb.DateTimeProperty(required=True)
  end_time = ndb.DateTimeProperty(required=True)
  
  # TODO(dasarathi): Consider using the calendar DAV format for storing.

class Timeline(ndb.Model):
  """Timeline is a series of events or sub-timelines."""
  name = ndb.StringProperty(indexed=True, required=True)

  # TBD: Use the timestamp for this.. or some auto increment 
  timeline_id = ndb.IntegerProperty(indexed=True, required=True)

  description = ndb.StringProperty()
  start_time = ndb.DateTimeProperty(required=True)
  end_time = ndb.DateTimeProperty(required=True)

  events = ndb.StructuredProperty(Event, repeated=True)
  
  # TBD: use keys or timeline ids?
  child_timelines = ndb.KeyProperty(kind='Timeline')
  



