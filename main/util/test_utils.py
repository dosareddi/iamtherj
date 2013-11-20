from ndb_test_utils import NDBTest

class EventlineTestBase(NDBTest):
  def ResetKindMap(self):
    # Overridden to disable the kind map reset in NDBTest.
    pass
