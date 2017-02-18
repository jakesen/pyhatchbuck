import os
import vcr
import unittest

from hatchbuck.api import HatchbuckAPI
from hatchbuck.objects import Contact

class TestUpdateContact(unittest.TestCase):

    def setUp(self):
        # Fake key can be used with existing cassettes
        self.test_api_key = os.environ.get("HATCHBUCK_API_KEY", "ABC123")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_update_basic_contact.yml',
        filter_query_parameters=['api_key']
    )
    def test_update_basic_contact(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact = hatchbuck.new_contact()
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.contactId, contact_id)
        contact.firstName = "Jill"
        contact.lastName = "Smith"
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.firstName, "Jill")
        self.assertEqual(contact.lastName, "Smith")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_update_contact_email.yml',
        filter_query_parameters=['api_key']
    )
    def test_update_contact_email(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact = hatchbuck.new_contact()
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.emails[0].address, "jill@pyhatchbuck.net")
        contact.emails[0].address = "jill.smith@pyhatchbuck.net"
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.emails[0].address, "jill.smith@pyhatchbuck.net")


if __name__ == '__main__':
    unittest.main()
