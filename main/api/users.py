from db import user_db

def create_user(name, user_id, email):
  """Add a new user to the datastore.
  
  Arguments:
  name -- string
  user_id -- string.
  email -- string.

  Returns:
    TODO(dasarathi): Check and return error.
  """
  new_user = user_db.User(name=name, user_id=user_id, email=email)
  new_user.put()
  # TODO(dasarathi): Handle error cases.
  
  
  
  

  

