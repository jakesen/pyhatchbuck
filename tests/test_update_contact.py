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
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.emails[0].address, "jill@pyhatchbuck.net")
        self.assertEqual(contact.emails[0].id, "SXU4LVZRWkFzM3UtMnZ4UGtrRTJtMmgyQWV2dnpUV19tNjFBaVFqRnk2QTE1")
        contact.emails[0].address = "jill.smith@pyhatchbuck.net"
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.emails[0].address, "jill.smith@pyhatchbuck.net")
        self.assertEqual(contact.emails[0].id, "SXU4LVZRWkFzM3UtMnZ4UGtrRTJtMmgyQWV2dnpUV19tNjFBaVFqRnk2QTE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_update_contact_address.yml',
        filter_query_parameters=['api_key']
    )
    def test_update_contact_address(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "TWlQd3RkSUNKc2h5dXg3UWtFbkZGZE1QZ3R4d0tUM3N0TjI0bDRUMS03MDE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.addresses[0].street, "123 Main Street")
        self.assertEqual(contact.addresses[0].id, "YlFxUEZPR3M5MGVDSW9XXzhEMDhqVmNVdzVHTUU3U2duT21lYk9tMnU1YzE1")
        contact.addresses[0].street = "555 Commerce Ave"
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.addresses[0].street, "555 Commerce Ave")
        self.assertEqual(contact.addresses[0].id, "YlFxUEZPR3M5MGVDSW9XXzhEMDhqVmNVdzVHTUU3U2duT21lYk9tMnU1YzE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_update_contact_temperature.yml',
        filter_query_parameters=['api_key']
    )
    def test_update_contact_temperature(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "TWlQd3RkSUNKc2h5dXg3UWtFbkZGZE1QZ3R4d0tUM3N0TjI0bDRUMS03MDE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.temperature.name, "Hot")
        contact.set_temperature(id="M2tyTXVQUmg1NUdKUDViWjkwOFUzQWtPSW9pZzV2STZkS29DeEdDS1ZlSTE1")
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.temperature.name, "On Fire")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_update_contact_phone.yml',
        filter_query_parameters=['api_key']
    )
    def test_update_contact_phone(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "TWlQd3RkSUNKc2h5dXg3UWtFbkZGZE1QZ3R4d0tUM3N0TjI0bDRUMS03MDE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.phones[0].number, "555-555-5555")
        self.assertEqual(contact.phones[0].id, "YzNZTGhZRjdadlNRMzl6Qlo1YkY3X1JmX09DNHp0RDZJT1lrMGl6NjJETTE1")
        contact.phones[0].number = "555-555-1234"
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.phones[0].number, "555-555-1234")
        self.assertEqual(contact.phones[0].id, "YzNZTGhZRjdadlNRMzl6Qlo1YkY3X1JmX09DNHp0RDZJT1lrMGl6NjJETTE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_update_contact_social_networks.yml',
        filter_query_parameters=['api_key']
    )
    def test_update_contact_social_networks(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "TWlQd3RkSUNKc2h5dXg3UWtFbkZGZE1QZ3R4d0tUM3N0TjI0bDRUMS03MDE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.socialNetworks[0].address, "@pyhatchbuck")
        self.assertEqual(contact.socialNetworks[0].id, "dGNZT0xWVVJSQlBKOWxLdnBlZS01MWdUQkxadk1XM2p1cG8yRWFhNjAyWTE1")
        contact.socialNetworks[0].address = "@alex.smith.pyhatchbuck"
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.socialNetworks[0].address, "@alex.smith.pyhatchbuck")
        self.assertEqual(contact.socialNetworks[0].id, "dGNZT0xWVVJSQlBKOWxLdnBlZS01MWdUQkxadk1XM2p1cG8yRWFhNjAyWTE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_update_contact_instant_messages.yml',
        filter_query_parameters=['api_key']
    )
    def test_update_contact_instant_messages(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "TWlQd3RkSUNKc2h5dXg3UWtFbkZGZE1QZ3R4d0tUM3N0TjI0bDRUMS03MDE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.instantMessaging[0].address, "alex.pyhatchbuck")
        self.assertEqual(contact.instantMessaging[0].id, "OWdYcHkzcVBwRE4zZEtzTEhJbFc4SVpLTm91WjJWd2tQUWxXcm9TdjdHazE1")
        contact.instantMessaging[0].address = "as.pyhatchbuck"
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.instantMessaging[0].address, "as.pyhatchbuck")
        self.assertEqual(contact.instantMessaging[0].id, "OWdYcHkzcVBwRE4zZEtzTEhJbFc4SVpLTm91WjJWd2tQUWxXcm9TdjdHazE1")

if __name__ == '__main__':
    unittest.main()
