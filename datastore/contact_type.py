from enum import Enum


class ContactType(Enum):
    unknown = 1
    acquaintance = 2
    friend = 3
    family = 4
    client = 5
    work = 6
    me = 7