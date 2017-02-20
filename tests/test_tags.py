import os
import vcr
import unittest

from hatchbuck.api import HatchbuckAPI
from hatchbuck.objects import Contact

class TestTags(unittest.TestCase):

    def setUp(self):
        # Fake key can be used with existing cassettes
        self.test_api_key = os.environ.get("HATCHBUCK_API_KEY", "ABC123")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_get_contact_tags.yml',
        filter_query_parameters=['api_key']
    )
    def test_get_contact_tags(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.contactId, contact_id)
        tags = contact.get_tags()
        self.assertEqual(tags[0].name, "Possible Client")
        self.assertEqual(tags[0].score, 1)
        self.assertEqual(tags[0].id, "WjFmbDktWGpDVV9OMEtHdjY0Mm83ZVJUT0w5UDVKRTNmN0NRcXdrSGhMMDE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_get_contact_tags_by_email.yml',
        filter_query_parameters=['api_key']
    )
    def test_get_contact_tags_by_email(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_email = "jill.smith@pyhatchbuck.net"
        tags = hatchbuck.get_tags(contact_email)
        self.assertEqual(tags[0].name, "Possible Client")
        self.assertEqual(tags[0].score, 1)
        self.assertEqual(tags[0].id, "WjFmbDktWGpDVV9OMEtHdjY0Mm83ZVJUT0w5UDVKRTNmN0NRcXdrSGhMMDE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_add_contact_tags.yml',
        filter_query_parameters=['api_key']
    )
    def test_add_contact_tags(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.contactId, contact_id)
        success = contact.add_tags([{'name': 'Old Contact List'}])
        self.assertEqual(success, True)
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.tags[0].name, "Possible Client")
        self.assertEqual(contact.tags[0].score, 1)
        self.assertEqual(contact.tags[0].id, "WjFmbDktWGpDVV9OMEtHdjY0Mm83ZVJUT0w5UDVKRTNmN0NRcXdrSGhMMDE1")
        self.assertEqual(contact.tags[1].name, "Old Contact List")
        self.assertEqual(contact.tags[1].score, 3)
        self.assertEqual(contact.tags[1].id, "elZDN1dSa3ZmSDJ1MjNrRVBabDhoNmdKbmthUmY1YTVOYkx5TmhwYVZfSTE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_delete_contact_tags.yml',
        filter_query_parameters=['api_key']
    )
    def test_delete_contact_tags(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.contactId, contact_id)
        success = contact.delete_tags([{'name': 'Possible Client'}])
        self.assertEqual(success, True)
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(len(contact.tags), 1)
        self.assertEqual(contact.tags[0].name, "Old Contact List")
        self.assertEqual(contact.tags[0].score, 3)
        self.assertEqual(contact.tags[0].id, "elZDN1dSa3ZmSDJ1MjNrRVBabDhoNmdKbmthUmY1YTVOYkx5TmhwYVZfSTE1")

if __name__ == '__main__':
    unittest.main()
