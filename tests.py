import os
import unittest

from hatchbuck.api import HatchbuckAPI

class TestApiCommands(unittest.TestCase):

    def setUp(self):
        self.test_api_key = os.environ.get("HATCHBUCK_API_KEY")

    def test_search_by_email_with_results(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contacts, found = hatchbuck.search_contacts("jack@pyhatchbuck.net")
        self.assertEqual(found, True)
        self.assertEqual(contacts[0].firstName, "Jack")
        self.assertEqual(contacts[0].lastName, "Spratt")
        self.assertEqual(contacts[0].salesRep.username, "jakesen")
        self.assertEqual(contacts[0].status.name, "Lead")
        self.assertEqual(contacts[0].emails[0].address, "jack@pyhatchbuck.net")
        self.assertEqual(contacts[0].emails[0].type, "Work")
        self.assertEqual(contacts[0].subscribed, True)
        self.assertEqual(contacts[0].timezone, "Central Standard Time")


    def test_search_by_email_with_no_results(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contacts, found = hatchbuck.search_contacts("joe@pyhatchbuck.net")
        self.assertEqual(found, False)

if __name__ == '__main__':
    unittest.main()
