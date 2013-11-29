from models.eventline_db import Timeline
from models.user_db import User

# Add a new user to the datastore.  
# Arguments:
#   name -- string
#   email -- string.
#   google_id -- string, google_user.user_id()
# Returns:
#   TODO(dasarathi): Check and return error.
# TBD: Should these be attributes of the user object
def create_user(name, email, google_id=None):
  new_user = User(name=name, email=email, google_id=google_id)
  if new_user.put():
    return new_user
  return None


# Fetch a user from the datastore given id.
# Arguments:
#   id -- string or integer form of NDB id.
# Returns:
#   User object if exists, None otherwise
def get_user(id):
  key_id = id
  if type(id) != int:
    key_id = int(id)
  return User.get_by_id(key_id)


# Fetch a user from the datastore given google id.
# Arguments:
#   google_id -- string form of google id.
# Returns:
#   User object if exists, None otherwise
def get_user_by_google_id(google_id):
  return User.query(User.google_id == google_id).get()

  
# Get all timelines belonging to this user from the datastore.
# Arguments:
#   user_id -- string.
# Returns:
#   List of Timeline objects.
def get_user_timelines(user_id):
  return Timeline.query(Timeline.user_id == user_id).fetch()

  
  
  

  

