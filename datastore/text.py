from datastore.scat_database import db


class Text(db.Model):
    db.__tablename__ = 'text'

    id = db.Column(db.Integer, primary_key=True)
    phoneNumber = db.Column('phone_number', db.String(50), primary_key=True)
    timestamp = db.Column('timestamp', db.TIMESTAMP, primary_key=True)
    message = db.Column('message', db.String(160), nullable = False)

    db.ForeignKeyConstraint(['id', 'phone_number'], ['contact.id', 'contact.phone_number'])

    def __repr__(self):
        return 'ID: ' + str(self.id) + \
               '\nPhone Number: ' + str(self.phoneNumber) + \
               '\n[' + self.timestamp + ']: ' + self.message