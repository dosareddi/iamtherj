from models.eventline_db import Timeline
from models.user_db import User

# Add a new user to the datastore.  
# Arguments:
#   name -- string
#   user_id -- string.
#   email -- string.
# Returns:
#   TODO(dasarathi): Check and return error.
# TBD: Should these be attributes of the user object
def create_user(name, user_id, email):
  new_user = User(name=name, user_id=user_id, email=email)
  if new_user.put():
    return new_user
  return None


# Fetch a user from the datastore.
# Arguments:
#   user_id -- string.
# Returns:
# TODO(dasarathi): Check and return error.
def get_user(user_id):
  # TODO(dasarathi): This is not fast since we only have one user by user_id.
  # Check https://developers.google.com/appengine/docs/python/ndb/queries#filter_by_prop
  return User.query(User.user_id == user_id).get()

  
# Get all timelines belonging to this user from the datastore.
# Arguments:
#   user_id -- string.
# Returns:
#   List of Timeline objects.
def get_user_timelines(user_id):
  return Timeline.query(Timeline.user_id == user_id).fetch()

  
  
  

  

