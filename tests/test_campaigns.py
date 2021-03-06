from __future__ import absolute_import
import os
import vcr
import unittest

from hatchbuck.api import HatchbuckAPI
from hatchbuck.objects import Contact

class TestCampaigns(unittest.TestCase):

    def setUp(self):
        # Fake key can be used with existing cassettes
        self.test_api_key = os.environ.get("HATCHBUCK_API_KEY", "ABC123")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_get_contact_campaigns.yml',
        filter_query_parameters=['api_key']
    )
    def test_get_contact_campaigns(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.contactId, contact_id)
        campaigns = contact.get_campaigns()
        self.assertEqual(campaigns[0].name, "Brochure Request Followup")
        self.assertEqual(campaigns[0].step, 0)
        self.assertEqual(campaigns[0].id, "b1BFUnM1Unh0MDVVOVJEWUc1d0pTM0pUSVY4QS0xOW5GRHRsS05DXzNXazE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_get_contact_campaigns_by_email.yml',
        filter_query_parameters=['api_key']
    )
    def test_get_contact_campaigns_by_email(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_email = "jill.smith@pyhatchbuck.net"
        campaigns = hatchbuck.get_campaigns(contact_email)
        self.assertEqual(campaigns[0].name, "Brochure Request Followup")
        self.assertEqual(campaigns[0].step, 0)
        self.assertEqual(campaigns[0].id, "b1BFUnM1Unh0MDVVOVJEWUc1d0pTM0pUSVY4QS0xOW5GRHRsS05DXzNXazE1")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_start_contact_campaigns.yml',
        filter_query_parameters=['api_key']
    )
    def test_start_contact_campaigns(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.contactId, contact_id)
        success = contact.start_campaigns([{'name': 'Trial Request Followup'}])
        self.assertEqual(success, True)
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.campaigns[0].name, "Brochure Request Followup")
        self.assertEqual(contact.campaigns[0].step, 0)
        self.assertEqual(contact.campaigns[0].id, "958650")
        self.assertEqual(contact.campaigns[1].name, "Trial Request Followup")
        self.assertEqual(contact.campaigns[1].step, 0)
        self.assertEqual(contact.campaigns[1].id, "958651")

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_start_contact_campaigns_by_email.yml',
        filter_query_parameters=['api_key']
    )
    def test_start_contact_campaigns_by_email(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_email = "jill.smith@pyhatchbuck.net"
        campaigns = [
            {'id': 'b1BFUnM1Unh0MDVVOVJEWUc1d0pTM0pUSVY4QS0xOW5GRHRsS05DXzNXazE1'}
        ]
        success = hatchbuck.start_campaigns(contact_email, campaigns)
        self.assertEqual(success, True)

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_stop_contact_campaigns.yml',
        filter_query_parameters=['api_key']
    )
    def test_stop_contact_campaigns(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_id = "d1F4Tm1tcUxVRmdFQmVIT3lhVjNpaUtxamprakk5S3JIUGRmVWtHUXJaRTE1"
        contact = hatchbuck.search_contacts(contactId=contact_id)[0]
        self.assertEqual(contact.contactId, contact_id)
        success = contact.stop_campaigns([{'name': 'Brochure Request Followup'}])
        self.assertEqual(success, True)

    @vcr.use_cassette(
        'tests/fixtures/cassettes/test_stop_contact_campaigns_by_email.yml',
        filter_query_parameters=['api_key']
    )
    def test_stop_contact_campaigns_by_email(self):
        hatchbuck = HatchbuckAPI(self.test_api_key)
        contact_email = "jill.smith@pyhatchbuck.net"
        campaigns = [
            {'id': 'eVFMdnphWjZSR2UtUllRYlRDYVpOMTd1aDMyZDhDSV9haExIcmpqdU85dzE1'}
        ]
        success = hatchbuck.stop_campaigns(contact_email, campaigns)
        self.assertEqual(success, True)

if __name__ == '__main__':
    unittest.main()
