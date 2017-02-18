import os
import vcr
import unittest

from hatchbuck.api import HatchbuckAPI
from hatchbuck.objects import Contact

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
        contact.add_email(address="jill@pyhatchbuck.net", type="Work")
        contact.set_status(name="Customer")
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.contactId, "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_add_full_contact.yml',
        filter_query_parameters=['api_key']
    )
    def test_add_full_contact(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact = hatchbuck.new_contact()
        contact.add_email(address="alex@pyhatchbuck.net", type="Work")
        contact.set_status(name="Customer")
        contact.firstName = "Alex"
        contact.lastName = "Smith"
        contact.title = "Account Manager"
        contact.company = "ACME Incorporated"
        contact.add_address(
            street="123 Main Street",
            city="Anytown",
            state="AL",
            zip="55555",
            country="United States",
            type="Work"
        )
        contact.timezone = "Pacific Standard Time"
        contact.set_temperature(id="QzlHRFRCXzBNN2s3SlppdlBfT2ttVklsRWwzVTFOM3d6SWNJV0xzZkFHODE1")
        contact.add_phone(number="555-555-5555", type="Work")
        contact.add_social_network(address="@pyhatchbuck", type="twitter")
        contact.add_instant_message_address(address="alex.pyhatchbuck", type="skype")
        contact.add_website(websiteUrl="www.pyhatchbuck.net")
        contact.sourceId = "UnVvT0c0dmxsVVdFYUR1MUZIOTVJeDFXSGxudTBaUG5uZ1QxdVo1aElUVTE1"
        success = contact.save()
        self.assertEqual(success, True)
        self.assertEqual(contact.contactId, "TWlQd3RkSUNKc2h5dXg3UWtFbkZGZE1QZ3R4d0tUM3N0TjI0bDRUMS03MDE1")
        self.assertEqual(contact.addresses[0].street, "123 Main Street")

if __name__ == '__main__':
    unittest.main()
