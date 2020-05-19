from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Films(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    age = db.Column(db.String(3), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    formating = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(500), nullable=False, unique=True)
    code = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        return ''.join([
            'Title: ', self.title, '(', self.year, ')', '\r\n',
            self.content
            ])

class Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    films_id = db.Column(db.Integer, db.ForeignKey('films.id'), nullable=False)
    own = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return ''.join([
            'user ID: ', str(self.user_id), '\r\n',
            'Title: ', self.films_title, self.films_age, '\r\n',
            self.films_description, '\r\n',
            'Own This Movie: ', self.own            
            ])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    Films = db.relationship('Collection', backref='owner', lazy=True) # relats table to Collection table

    def __repr__(self):
        return ''.join([
            'user ID: ', str(self.id), '\r\n',
            'Email: ', self.email, 'user: ', self.first_name, ' ' , self.last_name, '\r\n'
            ])
