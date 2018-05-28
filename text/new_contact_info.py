from enum import Enum


class NewContactInfo(Enum):
    allUnknown = 0
    cityKnown = 1
    countryKnown = 2
    cityAndCountryKnown = 3