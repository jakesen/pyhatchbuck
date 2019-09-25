import os
import vcr
import unittest

from hatchbuck.api import HatchbuckAPI
from hatchbuck.objects import Contact


class TestCustomFields(unittest.TestCase):
    def setUp(self):
        # Fake key can be used with existing cassettes
        self.test_api_key = os.environ.get("HATCHBUCK_API_KEY", "ABC123")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_search_contact_with_customFields.yml',
        filter_query_parameters=['api_key']
    )
    def test_search_contact_with_customFields(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.contactId, contact_id)
        customFields = contact.customFields
        self.assertEqual(len(customFields), 2)
        self.assertEqual(customFields[0].name, "Custom1")
        self.assertEqual(customFields[0].type, "Integer")
        self.assertEqual(customFields[0].value, "42")
