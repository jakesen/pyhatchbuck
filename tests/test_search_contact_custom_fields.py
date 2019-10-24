import os
import vcr
import unittest

from hatchbuck.api import HatchbuckAPI


CONTACT_ID = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"


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
        contact = hatchbuck.search_contacts(contactId=CONTACT_ID)[0]
        self.assertEqual(contact.contactId, CONTACT_ID)
        customFields = contact.customFields
        self.assertEqual(len(customFields), 2)
        self.assertEqual(customFields[0].name, "Company Size")
        self.assertEqual(customFields[0].value, "42")

    @vcr.use_cassette(
      'tests/fixtures/cassettes/test_search_contact_without_customFields.yml',
      filter_query_parameters=['api_key']
    )
    def test_search_contact_without_customFields(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact = hatchbuck.search_contacts(contactId=CONTACT_ID)[0]
        self.assertEqual(contact.contactId, CONTACT_ID)
        customFields = contact.customFields
        self.assertEqual(len(customFields), 0)

    @vcr.use_cassette(
      'tests/fixtures/cassettes/test_add_custom_fields.yml',
      filter_query_parameters=['api_key']
    )
    def test_add_custom_fields(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact = hatchbuck.new_contact()
        contact.add_custom_field(name='Company Size', value=42)
        contact.add_custom_field(name='Gender', value='Female')
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(len(contact.customFields), 2)
        self.assertEqual(contact.customFields[0].name, "Company Size")
        self.assertEqual(contact.customFields[0].value, "42")
