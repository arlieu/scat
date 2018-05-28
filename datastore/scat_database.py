from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scat.db'
db = SQLAlchemy(app)


# if __name__ == '__main__':
#     db.drop_all()
#     db.create_all()
#     x = Contact("1111111111", "Avery", "Lieu", "Chicago", "USA", ContactType.me)
#     db.session.add(x)
#     db.session.commit()