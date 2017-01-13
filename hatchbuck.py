import json
import urllib
import requests

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
        r = requests.post(request_url, json=data)

        if r.status_code == 200:
            contacts_found = True
        else:
            contacts_found = False
        return (r.content, contacts_found)
