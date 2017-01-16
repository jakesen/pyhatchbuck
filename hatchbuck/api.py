import json
import urllib
import requests

from .objects import Contact

BASE_URL = "https://api.hatchbuck.com/api/v1/"

class HatchbuckAPI(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def search_contacts(self, email):
        data = {
            "emails": [
                {
                    "address": email
                }
            ]
        }

        request_url = BASE_URL+'contact/search?api_key='+self.api_key
        response = requests.post(request_url, json=data)

        if response.status_code == 200:
            return [Contact(j) for j in json.loads(response.content)], True
        else:
            return [], False
