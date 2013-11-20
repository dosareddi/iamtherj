import datetime
import os
import pprint
import unittest

from logic import users, eventlines
from util.test_utils import EventlineTestBase


class TimelinesTest(EventlineTestBase):
    def test_all(self):
      user_key = users.create_user("foo", "1455", "a@a1.com")
      self.assertTrue(user_key != None)

      timeline_key = eventlines.create_timeline("1455", "timeline_foo", 
                                                "description for timeline")
      timeline_id = timeline_key.id()
      timeline = eventlines.get_timeline(timeline_id)
      self.assertTrue(timeline.name == "timeline_foo")
      self.assertTrue(timeline.user_id == "1455")
      self.assertTrue(timeline.description == "description for timeline")
      
      user = users.get_user("1455")
      self.assertTrue(user.timeline_ids == [timeline_id])
      
      key = eventlines.add_event(
        "1455", timeline_id, "event1", "event desc",
        datetime.datetime.strptime("2014/03/01", "%Y/%m/%d"),
        datetime.datetime.strptime("2014/03/01", "%Y/%m/%d"))
      self.assertTrue(key.id() == timeline_id)
      timeline = eventlines.get_timeline(timeline_id)
      self.assertTrue(timeline.events[0].name == "event1")
      

if __name__ == '__main__':
    unittest.main()
