from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    
    #Checked and its 102
    password_hash = db.Column(db.String(102))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user(username):
        return User.query.filter_by(username=username).first()

    def __repr__(self):
        return '<User {}>'.format(self.username)

#Returns users? idk
@login.user_loader
def load_user(id):
    return User.query.get(int(id))