from datastore.scat_database import db
from datastore.contact_type import ContactType


class Contact(db.Model):
    db.__tablename__ = 'contact'

    db.__table_args__ = {'sqlite_autoincrement': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phoneNumber = db.Column('phone_number', db.String(50), unique=True, nullable=False)
    firstName = db.Column('first_name', db.String(50))
    lastName = db.Column('last_name', db.String(50))
    city = db.Column('city', db.String(50))
    country = db.Column('country', db.String(50))
    contactType = db.Column('contact_type', db.Enum(ContactType), nullable=False)

    def __init__(self, phoneNumber, contactType, firstName=None, lastName=None, city=None, country=None):
        self.phoneNumber = phoneNumber
        self.firstName = firstName
        self.lastName = lastName
        self.city = city
        self.country = country
        self.contactType = contactType

    def __repr__(self):
        return 'ID: ' + str(self.id) + \
               '\nPhone Number: ' + str(self.phoneNumber) + \
               '\nContact Name: ' + self.firstName + ' ' + self.lastName