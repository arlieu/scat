from flask import Flask, jsonify, abort, Request, Response, make_response
from flask_restful import Api, Resource
from twilio import twiml

from datastore.scat_database import db
from datastore.contact import Contact
from datastore.contact_type import ContactType
from text.new_contact_info import NewContactInfo
from text.existing_contact_info import ExistingContactInfo
from text.automatic_reply import unknownContactInquiry, existingContactInquiry
from text.info_parser_utility import parseInfo


app = Flask(__name__)
api = Api(app)

sid = ''
token = ''
client = ''


class ContactApi(Resource):
    # TODO:
    # 1) Update database with follow up responses
    # 2) Determine required info and remprompt trials
    # 3) Logging
    # 4) Error handling
    def get(self, phoneNumber):
        sms = Request.form
        contactInfo = self._determineContactInfo(sms)

        if (contactInfo is type(NewContactInfo)):
            self._registerContact(sms, contactInfo)
            return make_response(unknownContactInquiry[contactInfo])

        return make_response(existingContactInquiry[contactInfo])

    def post(self, phoneNumber):
        pass

    def _determineContactInfo(self, sms):
        inboundPhoneNumber = sms['From']
        contact = Contact.query.filter_by(phoneNumber=inboundPhoneNumber)

        if contact is None:
            newContactCity = sms['FromCity']
            newContactCountry = sms['FromCountry']

            if newContactCity and newContactCountry:
                return NewContactInfo.cityAndCountryKnown
            elif not newContactCity and newContactCountry:
                return NewContactInfo.cityUnknown
            elif newContactCity and not newContactCountry:
                return NewContactInfo.countryUnknown
            else:
                return NewContactInfo.allUnknown

        firstName = contact.firstName
        lastName = contact.lastName
        city = contact.city
        country = contact.country
        relationship = contact.contactType

        contactUpdate = None

        if firstName is None or lastName is None or relationship is None:
            contactUpdate = parseInfo(sms['body'])
        if firstName is None and relationship is None:
            return ExistingContactInfo.firstNameAndRelationshipUnknown
        elif firstName is None:
            return ExistingContactInfo.firstNameUnknown
        elif relationship == ContactType.unknown:
            return ExistingContactInfo.relationshipUnknown
        else:
            return ExistingContactInfo.recognized

    def _registerContact(self, sms, contactInfo):
        if contactInfo == NewContactInfo.cityAndCountryKnown:
            db.session.add(Contact(sms['From'], 'Unknown', city=sms['FromCity'], country=sms['FromCountry']))
        elif contactInfo == NewContactInfo.cityKnown:
            db.session.add(Contact(sms['From'], 'Unknown', city=sms['FromCity']))
        elif contactInfo == NewContactInfo.countryKnown:
            db.session.add(Contact(sms['From'], 'Unknown', country=sms['FromCountry']))
        else:
            db.session.add(Contact(sms['From'], 'Unknown'))

        db.commit()

    def _updateContact(self, sms, contactInfo):
        pass


if __name__ == '__main__':
    app.run()
