import json
import requests

from hatchbuck.objects import Contact

BASE_URL = "https://api.hatchbuck.com/api/v1/"

class HatchbuckAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def search_contacts(self, **kwargs):
        data = {}
        if 'contactId' in kwargs:
            data['contactId'] = str(kwargs['contactId'])
        if 'firstName' in kwargs:
            data['firstName'] = str(kwargs['firstName'])
        if 'lastName' in kwargs:
            data['lastName'] = str(kwargs['lastName'])
        if 'emails' in kwargs and type(kwargs['emails']) == list:
            data['emails'] = [{'address': a} for a in kwargs['emails']]

        request_url = BASE_URL+'contact/search?api_key='+self.api_key
        response = requests.post(request_url, json=data)

        if response.status_code == 200:
            return [Contact(j) for j in json.loads(response.content)]
        else:
            return None
