# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
# class TextRequest(db.Model):
#     messageId = db.Column(db.BigInteger)
#     urgency = db.Column(db.Integer)
#     type = db.Column(db.String(8))
#     message = db.Column(db.String(160))
