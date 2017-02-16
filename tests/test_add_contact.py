import os
import vcr
import unittest

from hatchbuck.api import HatchbuckAPI
from hatchbuck.objects import Contact, Email, Status

class TestAddContact(unittest.TestCase):

    def setUp(self):
        # Fake key can be used with existing cassettes
        self.test_api_key = os.environ.get("HATCHBUCK_API_KEY", "ABC123")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_add_basic_contact.yml',
        filter_query_parameters=['api_key']
    )
    def test_add_basic_contact(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact = hatchbuck.new_contact()
        self.assertEqual(contact.contactId, "")
        contact.emails.append(Email({'address': "jill@pyhatchbuck.net", 'type': "Work"}))
        contact.status = Status({'name': "Customer"})
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.contactId, "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1")

if __name__ == '__main__':
    unittest.main()
