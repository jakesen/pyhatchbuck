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
            return [Contact(self.api_key, j) for j in json.loads(response.content)]
        else:
            return None

    def new_contact(self):
        return Contact(self.api_key)

    def add_contact(self, contact):
        data = contact.as_dict()
        request_url = BASE_URL+'contact?api_key='+self.api_key
        response = requests.post(request_url, json=data)

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return None

    def update_contact(self, contact):
        data = contact.as_dict()
        request_url = BASE_URL+'contact?api_key='+self.api_key
        response = requests.put(request_url, json=data)

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return None

    def get_tags(self, contact_id_or_email):
        from hatchbuck.primatives import ApiObjectList
        from hatchbuck.objects import Tag
        request_url = BASE_URL+'contact/'+contact_id_or_email+'/Tags?api_key='+self.api_key
        response = requests.get(request_url)
        if response.status_code == 200:
            return ApiObjectList(Tag, json.loads(response.content))
        else:
            return None

    def add_tags(self, contact_id_or_email, tags):
        from hatchbuck.primatives import ApiObjectList
        from hatchbuck.objects import Tag
        if not isinstance(tags, ApiObjectList):
            tags = ApiObjectList(Tag, tags)
        data = tags.as_dict_list()
        request_url = BASE_URL+'contact/'+contact_id_or_email+'/Tags?api_key='+self.api_key
        response = requests.post(request_url, json=data)

        if response.status_code == 201:
            return True
        else:
            return False

    def delete_tags(self, contact_id_or_email, tags):
        from hatchbuck.primatives import ApiObjectList
        from hatchbuck.objects import Tag
        if not isinstance(tags, ApiObjectList):
            tags = ApiObjectList(Tag, tags)
        data = tags.as_dict_list()
        request_url = BASE_URL+'contact/'+contact_id_or_email+'/Tags?api_key='+self.api_key
        response = requests.delete(request_url, json=data)

        if response.status_code == 200:
            return True
        else:
            return False
