# This file has renderers for all kinds of items.

# Renderer for an event within a timeline.
# Class members:
#   name: string
#   description: string
#   start_time: datetime
#   end_time: datetime 
class EventRenderer:
  def __init__(self, name, description, start_time, end_time):
    self.name = name 
    self.description = description
    self.start_time = start_time
    self.end_time = end_time


# Renderer for a timeline.
# Class members:
#   name: string
#   TODO(dasarathi): This is needed for adding events to the timeline, needs to
#   be encrypted.
#   id: integer 
#   description: string
#   start_time: datetime
#   end_time: datetime
#   events: list of EventRenderer
#   TODO:
#     Renderers for user information, comments etc.
class TimelineRenderer:
  def __init__(self, name, id, description, start_time, end_time, events):
    self.name = name 
    self.id = id
    self.description = description
    self.start_time = start_time
    self.end_time = end_time
    self.events = events
