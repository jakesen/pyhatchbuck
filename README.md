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

[hatchbuck]: http://www.hatchbuck.com

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

## TODOs

- [x] Search for contacts by email
- [x] VCR for tests
- [x] Search with other attributes
- [x] Add contact
- [ ] Update contact
- [ ] Get tags
- [ ] Add tags
- [ ] Delete tags
- [ ] Get campaign
- [ ] Start campaign
- [ ] Stop campaign
- [ ] More complete documentation
- [ ] Publish for PIP
- [ ] Docstrings
