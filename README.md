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

## TODOs

- [x] Search for contacts by email
- [x] VCR for tests
- [x] Search with other attributes
- [ ] Add contact
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
