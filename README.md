# pyhatchbuck

[![CircleCI](https://circleci.com/gh/jakesen/pyhatchbuck.svg?style=svg)](https://circleci.com/gh/jakesen/pyhatchbuck)

This library is intended to provide a full python wrapper for the [Hatchbuck][hatchbuck] API. When finished it should provide access to all the Hatchbuck API functions:

* search contacts
* add contact
* update contact
* get tags
* add tags
* delete tags
* get campaign
* start campaign
* stop campaign

The API version supported is v1. API documentation can be found [here][hatchbuck-api-docs].

[hatchbuck]: http://www.hatchbuck.com
[hatchbuck-api-docs]: https://hatchbuck.freshdesk.com/support/solutions/articles/5000578765-hatchbuck-api-documentation

## Usage (so far)

```py
from hatchbuck.api import HatchbuckAPI

hatchbuck = HatchbuckAPI(api_key)

contacts = hatchbuck.search_contacts(emails=["jack@pyhatchbuck.net"])

>>> print contacts[0].firstName
"Jack"
```

## Searching for Contacts

You can search by `contactId`, `firstName`, `lastName` and one or more `emails`. The emails must be in list form.

```py
contacts = hatchbuck.search_contacts(
  contactId="ABCDEF123456",
  firstName="Jack",
  lastName="Spratt",
  emails=["jack@pyhatchbuck.net"]
)
```

## Adding a Contact

When adding a contact at least one `email` and a `status` are required. Calling save on a new contact will return `True` if successful, and the contact data will be reloaded from the API response.

```py
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
    type="Work"
)
contact.timezone = "Central Standard Time"
contact.set_temperature(id="QzlHRFRCXzBNN2s3SlppdlBfT2ttVklsRWwzVTFOM3d6SWNJV0xzZkFHODE1")
contact.add_phone(number="555-555-5555", type="Work")
contact.add_social_network(address="@pyhatchbuck", type="twitter")
contact.add_instant_message_address(address="alex.pyhatchbuck", type="skype")
contact.add_website(websiteUrl="www.pyhatchbuck.net")
contact.sourceId = "UnVvT0c0dmxsVVdFYUR1MUZIOTVJeDFXSGxudTBaUG5uZ1QxdVo1aElUVTE1"
success = contact.save()
```

## Updating a Contact

Calling save to update an existing contact will return `True` if successful, and the contact data will be reloaded from the API response.

```py
contact = hatchbuck.search_contacts(contactId=contact_id)[0]
contact.emails[0].address = "alex@pyhatchbuck.net"
contact.phones[0].number = "555-555-5555"
#...ETC...
success = contact.save()
```

## Getting Tags

You can get tags by email or by contact id.

```py
contact = hatchbuck.search_contacts(contactId=contact_id)[0]
tags = contact.get_tags()
# or
tags = hatchbuck.get_tags("alex@pyhatchbuck.net")

>>> print tags[0].name
"Tag Name"
>>> print tags[0].id
"ABCDEF123456"
```

## Adding Tags

You can add tags by email or by contact id. You must give a list of tags to add with each tag's name or id.

```py
contact = hatchbuck.search_contacts(contactId=contact_id)[0]
tags = contact.add_tags([{'name': "New Tag"}])
# or
tags = hatchbuck.add_tags("alex@pyhatchbuck.net", [{'name': "New Tag"}])
# or
tags = hatchbuck.add_tags("alex@pyhatchbuck.net", [{'id': "ABCDEF123456"}])
```

## Deleting Tags

You can delete tags by email or by contact id. You must give a list of tags to delete with each tag's name or id.

```py
contact = hatchbuck.search_contacts(contactId=contact_id)[0]
tags = contact.delete_tags([{'name': "Old Tag"}])
# or
tags = hatchbuck.delete_tags("alex@pyhatchbuck.net", [{'name': "Old Tag"}])
# or
tags = hatchbuck.delete_tags("alex@pyhatchbuck.net", [{'id': "ABCDEF123456"}])
```


## TODOs

- [x] Search for contacts by email
- [x] VCR for tests
- [x] Search with other attributes
- [x] Add contact
- [x] Update contact
- [x] Get tags
- [x] Add tags
- [x] Delete tags
- [ ] Get campaign
- [ ] Start campaign
- [ ] Stop campaign
- [ ] More complete documentation
- [ ] Publish for PIP
- [ ] Docstrings
