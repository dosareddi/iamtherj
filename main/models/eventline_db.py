"""
Data models for events and timelines.
"""

from google.appengine.ext import ndb

# Basic information about an event. 
# An event is either standalone or a timeline composed of more events.
# TODO(dasarathi): Consider using the calendar DAV format for storing.
class Event(ndb.Model):
  name = ndb.StringProperty(indexed=True, required=True)

  description = ndb.StringProperty()
  start_time = ndb.DateTimeProperty(required=True)
  end_time = ndb.DateTimeProperty(required=True)

  # Optional: Key of timeline if this event is a timeline by itself.
  timeline_id = ndb.IntegerProperty()


# A timeline of events.
class Timeline(ndb.Model):
  name = ndb.StringProperty(indexed=True, required=True)
  description = ndb.StringProperty()
  tags = ndb.StringProperty(repeated=True)

  # These both can be derived from the list of its events if not specified.
  start_time = ndb.DateTimeProperty()
  end_time = ndb.DateTimeProperty()

  # Owner of this timeline. TBD: Need one for original author.
  user_id = ndb.IntegerProperty(indexed=True, required=True)

  events = ndb.LocalStructuredProperty(Event, repeated=True)  

  # Optional: Key of parent timeline if this timeline represents an event in
  # another timeline.
  parent_timeline_id = ndb.IntegerProperty()

  



