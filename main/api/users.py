from db.user_db import User

# TBD: Should these be attributes of the user object
def create_user(name, user_id, email):
  """Add a new user to the datastore.
  
  Arguments:
  name -- string
  user_id -- string.
  email -- string.

  Returns:
    TODO(dasarathi): Check and return error.
  """
  new_user = User(name=name, user_id=user_id, email=email)
  new_user.put()
  # TODO(dasarathi): Handle error cases.


def get_user(user_id):
  """Fetch a user from the datastore.
  
  Arguments:
  user_id -- string.

  Returns:
    TODO(dasarathi): Check and return error.
  """
  # TODO(dasarathi): This is not fast since we only have one user by user_id.
  # Check https://developers.google.com/appengine/docs/python/ndb/queries#filter_by_prop
  return User.query(User.user_id == user_id).get()
  
  
  
  

  

