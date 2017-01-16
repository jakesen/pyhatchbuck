from .primatives import ApiObject, ApiStringAttribute, ApiObjectList

class Email(ApiObject):
    address = ApiStringAttribute()
    type = ApiStringAttribute()

class User(ApiObject):
    username = ApiStringAttribute()
    id = ApiStringAttribute()

class Contact(ApiObject):
    firstName = ApiStringAttribute()
    lastName = ApiStringAttribute()
    salesRep = User()
    emails = ApiObjectList(Email)
