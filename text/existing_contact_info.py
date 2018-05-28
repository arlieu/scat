from enum import Enum


class ExistingContactInfo(Enum):
    allUnknown = 0
    firstNameAndRelationshipUnknown = 0
    firstNameUnknown = 1
    relationshipUnknown = 2
    recognized = 3