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

contacts, found = hatchbuck.search_contacts("jack@pyhatchbuck.net")

>>> print contacts[0].firstName
"Jack"
```
