from hatchbuck.primatives import ApiObject, ApiObjectList, ApiIntegerAttribute
from hatchbuck.primatives import ApiStringAttribute, ApiBooleanAttribute

class Address(ApiObject):
    id = ApiStringAttribute()
    street = ApiStringAttribute()
    city = ApiStringAttribute()
    state = ApiStringAttribute()
    zip = ApiStringAttribute()
    country = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class Campaign(ApiObject):
    id = ApiStringAttribute()
    name = ApiStringAttribute()
    step = ApiIntegerAttribute()

class CustomField(ApiObject):
    name = ApiStringAttribute()
    value = ApiStringAttribute()
    id = ApiStringAttribute()

class Email(ApiObject):
    id = ApiStringAttribute()
    address = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class InstantMessage(ApiObject):
    id = ApiStringAttribute()
    address = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class Phone(ApiObject):
    id = ApiStringAttribute()
    number = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class SocialNetwork(ApiObject):
    id = ApiStringAttribute()
    address = ApiStringAttribute()
    type = ApiStringAttribute()
    typeId = ApiStringAttribute()

class Status(ApiObject):
    name = ApiStringAttribute()
    id = ApiStringAttribute()

class Tag(ApiObject):
    id = ApiStringAttribute()
    name = ApiStringAttribute()
    score = ApiIntegerAttribute()

class Temperature(ApiObject):
    name = ApiStringAttribute()
    id = ApiStringAttribute()

class User(ApiObject):
    username = ApiStringAttribute()
    id = ApiStringAttribute()

class Website(ApiObject):
    websiteUrl = ApiStringAttribute()
    id = ApiStringAttribute()

class Contact(ApiObject):
    contactId = ApiStringAttribute()
    sourceId = ApiStringAttribute()
    firstName = ApiStringAttribute()
    lastName = ApiStringAttribute()
    title = ApiStringAttribute()
    company = ApiStringAttribute()
    salesRep = User()
    emails = ApiObjectList(Email)
    phones = ApiObjectList(Phone)
    tags = ApiObjectList(Tag)
    campaigns = ApiObjectList(Campaign)
    status = Status()
    temperature = Temperature()
    addresses = ApiObjectList(Address)
    socialNetworks = ApiObjectList(SocialNetwork)
    instantMessaging = ApiObjectList(InstantMessage)
    website = ApiObjectList(Website)
    customFields = ApiObjectList(CustomField)
    subscribed = ApiBooleanAttribute()
    timezone = ApiStringAttribute()
    referredBy = ApiStringAttribute()

    def __init__(self, api_key, json_data=None):
        # make sure lists are instance attributes
        self.emails = ApiObjectList(Email)
        self.phones = ApiObjectList(Phone)
        self.tags = ApiObjectList(Tag)
        self.campaigns = ApiObjectList(Campaign)
        self.addresses = ApiObjectList(Address)
        self.socialNetworks = ApiObjectList(SocialNetwork)
        self.instantMessaging = ApiObjectList(InstantMessage)
        self.website = ApiObjectList(Website)
        self.customFields = ApiObjectList(CustomField)
        # call super to load json values
        super(Contact, self).__init__(json_data)
        # cache api key to use in save method
        self.api_key = api_key

    def add_email(self, address, type):
        self.emails.append(Email({'address': address, 'type': type}))

    def add_custom_field(self, name, value):
        self.customFields.append(
            CustomField({'name': name, 'value': value}))

    def set_status(self, name):
        self.status = Status({'name': name})

    def add_address(self, street, city, state, zip, country, type):
        self.addresses.append(Address({
            'street': street,
            'city': city,
            'state': state,
            'zip': zip,
            'country': country,
            'type': type
        }))

    def set_temperature(self, id):
        self.temperature = Temperature({'id': id})

    def add_phone(self, number, type):
        self.phones.append(Phone({
            'number': number,
            'type': type
        }))

    def add_social_network(self, address, type):
        self.socialNetworks.append(SocialNetwork({'address': address, 'type': type}))

    def add_instant_message_address(self, address, type):
        self.instantMessaging.append(InstantMessage({'address': address, 'type': type}))

    def add_website(self, websiteUrl):
        self.website.append(Website({'websiteUrl': websiteUrl}))

    def get_tags(self):
        from hatchbuck.api import HatchbuckAPI
        updated_tags = HatchbuckAPI(self.api_key).get_tags(self.contactId)
        if updated_tags != None:
            self.tags = updated_tags
            return self.tags
        else:
            return None

    def add_tags(self, tags):
        from hatchbuck.api import HatchbuckAPI
        return HatchbuckAPI(self.api_key).add_tags(self.contactId, tags)

    def delete_tags(self, tags):
        from hatchbuck.api import HatchbuckAPI
        return HatchbuckAPI(self.api_key).delete_tags(self.contactId, tags)

    def get_campaigns(self):
        from hatchbuck.api import HatchbuckAPI
        updated_campaigns = HatchbuckAPI(self.api_key).get_campaigns(self.contactId)
        if updated_campaigns != None:
            self.campaigns = updated_campaigns
            return self.campaigns
        else:
            return None

    def start_campaigns(self, campaigns):
        from hatchbuck.api import HatchbuckAPI
        return HatchbuckAPI(self.api_key).start_campaigns(self.contactId, campaigns)

    def stop_campaigns(self, campaigns):
        from hatchbuck.api import HatchbuckAPI
        return HatchbuckAPI(self.api_key).stop_campaigns(self.contactId, campaigns)

    def save(self):
        from hatchbuck.api import HatchbuckAPI
        new_data = None
        if self.contactId == "":
            new_data = HatchbuckAPI(self.api_key).add_contact(self)
        else:
            new_data = HatchbuckAPI(self.api_key).update_contact(self)
        if new_data != None:
            self.load_dict(new_data)
            return self.contactId != ""
        else:
            return False
