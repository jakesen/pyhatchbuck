from hatchbuck.primatives import ApiObject, ApiObjectList
from hatchbuck.primatives import ApiStringAttribute, ApiListAttribute, ApiBooleanAttribute

class Address(ApiObject):
    street = ApiStringAttribute()
    city = ApiStringAttribute()
    state = ApiStringAttribute()
    zip = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class Campaign(ApiObject):
    pass

class CustomField(ApiObject):
    field = ApiStringAttribute()
    value = ApiStringAttribute()
    id = ApiStringAttribute()

class Email(ApiObject):
    id = ApiStringAttribute()
    address = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class InstantMessage(ApiObject):
    address = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class Phone(ApiObject):
    number = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class SocialNetwork(ApiObject):
    address = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class Status(ApiObject):
    name = ApiStringAttribute()
    id = ApiStringAttribute()

class Tag(ApiObject):
    pass

class Temperature(ApiObject):
    name = ApiStringAttribute()
    id = ApiStringAttribute()

class User(ApiObject):
    username = ApiStringAttribute()
    id = ApiStringAttribute()

class Contact(ApiObject):
    contactId = ApiStringAttribute()
    firstName = ApiStringAttribute()
    lastName = ApiStringAttribute()
    title = ApiStringAttribute()
    company = ApiStringAttribute()
    salesRep = User()
    emails = ApiObjectList(Email)
    phone = ApiObjectList(Phone)
    tags = ApiObjectList(Tag)
    campaign = ApiObjectList(Campaign)
    status = Status()
    temperature = Temperature()
    addresses = ApiObjectList(Address)
    socialNetworks = ApiObjectList(SocialNetwork)
    instantMessaging = ApiObjectList(InstantMessage)
    website = ApiListAttribute()
    customFields = ApiObjectList(CustomField)
    subscribed = ApiBooleanAttribute()
    timezone = ApiStringAttribute()
    referredBy = ApiStringAttribute()

    def __init__(self, api_key, json_data=None):
        super(Contact, self).__init__(json_data)
        self.api_key = api_key

    def save(self):
        from hatchbuck.api import HatchbuckAPI
        if self.contactId == "":
            self.load_dict(HatchbuckAPI(self.api_key).add_contact(self))
            return self.contactId != ""
