from db.eventline_db import Event
from db.eventline_db import Eventline
import users

def create_eventline(user_id, name, description):
  """Add a new eventline for this user.
  
  Arguments:
  user_id -- string, the user who creates this eventline.
  name -- string, name of eventline.
  description -- string, name of timeline.
  
  Returns:
    Key to the created timeline object.
  """

  luser = users.get_user(user_id)
  if luser is None:
    # TODO(dasarathi): create error handling, throw exceptions?
    return
  eventline = Eventline(name=name, description=description, user_id=user_id)
  key = eventline.put()
  luser.eventlines.append(key)
  luser.put()

