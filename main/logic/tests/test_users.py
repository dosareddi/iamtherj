import os
import pprint
import unittest

from logic import users, eventlines
from util.test_utils import EventlineTestBase


class UsersTest(EventlineTestBase):
    def test_create_user(self):
      user_key = users.create_user("foo", "1455", "a@a1.com")
      self.assertTrue(user_key != None)

      user = users.get_user("1455")
      self.assertTrue(user.name == "foo")
      self.assertTrue(user.user_id == "1455")
      self.assertTrue(user.email == "a@a1.com")

if __name__ == '__main__':
    unittest.main()
