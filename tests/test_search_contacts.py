import os
import vcr
import unittest

from hatchbuck.api import HatchbuckAPI

class TestSearchContacts(unittest.TestCase):

    def setUp(self):
        # Fake key can be used with existing cassettes
        self.test_api_key = os.environ.get("HATCHBUCK_API_KEY", "ABC123")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_search_by_email_with_results.yml',
        filter_query_parameters=['api_key']
    )
    def test_search_by_email_with_results(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contacts = hatchbuck.search_contacts(emails=["jack@pyhatchbuck.net"])
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0].firstName, "Jack")
        self.assertEqual(contacts[0].lastName, "Spratt")
        self.assertEqual(contacts[0].salesRep.username, "jakesen")
        self.assertEqual(contacts[0].status.name, "Lead")
        self.assertEqual(contacts[0].emails[0].address, "jack@pyhatchbuck.net")
        self.assertEqual(contacts[0].emails[0].type, "Work")
        self.assertEqual(contacts[0].subscribed, True)
        self.assertEqual(contacts[0].timezone, "Central Standard Time")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_search_by_email_with_no_results.yml',
        filter_query_parameters=['api_key']
    )
    def test_search_by_email_with_no_results(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contacts = hatchbuck.search_contacts(emails=["joe@pyhatchbuck.net"])
        self.assertEqual(contacts, None)

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_search_by_contact_id_with_results.yml',
        filter_query_parameters=['api_key']
    )
    def test_search_by_contact_id_with_results(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "NlNfOTJrVFFtd0E4NVhXWGdmSy0ySVdBSHhpZ01hS1NCSFFxMVBTTmlKVTE1"
        contacts = hatchbuck.search_contacts(contactId=contact_id)
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0].contactId, contact_id)
        self.assertEqual(contacts[0].firstName, "Jack")
        self.assertEqual(contacts[0].lastName, "Spratt")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_search_by_name_with_results.yml',
        filter_query_parameters=['api_key']
    )
    def test_search_by_name_with_results(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contacts = hatchbuck.search_contacts(
            firstName="Jack",
            lastName="Spratt"
        )
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0].firstName, "Jack")
        self.assertEqual(contacts[0].lastName, "Spratt")

if __name__ == '__main__':
    unittest.main()
