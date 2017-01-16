
class ApiObject(object):

    def __init__(self, json_data):
        for k, v in json_data.iteritems():
            setattr(self, k, v)

class Contact(ApiObject):
    ahhhh = None
