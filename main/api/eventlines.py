from db.eventline_db import Event
from db.eventline_db import Timeline
import users

# Add a new timeline for this user.
# Arguments:
#   user_id -- string, the user who creates this timeline.
#   name -- string, name of timeline.
#   description -- string, name of timeline.
# Returns:
#   key to the created timeline object.
def create_timeline(user_id, name, description):
  luser = users.get_user(user_id)
  if luser is None:
    # TODO(dasarathi): create error handling, throw exceptions?
    return
  timeline = Timeline(name=name, description=description, user_id=user_id)
  timeline_key = timeline.put()
  luser.timeline_ids.append(timeline_key.id())
  return luser.put()


# Add a new event to a timeline.
# Arguments:
#   timline_id -- integer_id of the timeline key.
#   name -- string, name of task.
#   description -- string, name of time.
#   start_time -- datetime, start of event
#   end_time -- datetime, start of event  
# Returns:
#   None, TBD: raise exception on error.
def add_event(user_id, timeline_id, name, description, start_time, end_time, 
              is_new_timeline=False):    
  timeline = Timeline.get_by_id(timeline_id)
  if timeline is None:
    # TODO(dasarathi): create error handling, throw exceptions?
    return

  event = Event(name=name, description=description, start_time=start_time,
                end_time=end_time)
  if is_new_timeline:
    # Also create a timeline, we duplicate name and description here but it 
    # makes viewing a timeline a one-query op.
    child_timeline = Timeline(user_id=user_id, name=name, 
                              description=description, 
                              start_time=start_time, end_time=end_time)
    event.timeline_id = child_timeline.put().id()

  timeline.events.append(event)
  timeline.put()

# Get timeline from DB.
# Arguments:
#   timeline_id -- string, the user who creates this timeline.
# Returns:
#   Timeline object.
def get_timeline(timeline_id):
  return Timeline.get_by_id(timeline_id)
