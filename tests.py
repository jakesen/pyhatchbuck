import os
import unittest

from hatchbuck import HatchbuckAPI

class TestStuff(unittest.TestCase):

    def setUp(self):
        self.test_api_key = os.environ.get("HATCHBUCK_API_KEY")

    def test_search_by_email_with_results(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contacts, found = hatchbuck.search_contacts("jack@pyhatchbuck.net")
        self.assertEqual(found, True)

    def test_search_by_email_with_no_results(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contacts, found = hatchbuck.search_contacts("joe@pyhatchbuck.net")
        self.assertEqual(found, False)

if __name__ == '__main__':
    unittest.main()
