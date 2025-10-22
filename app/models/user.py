from flask_bcrypt import Bcrypt
from flask_login import UserMixin
from app import bd

encryptor = Bcrypt()

class User(bd.Model, UserMixin):
    id = bd.Column(bd.Integer, primary_key=True)
    name = bd.Column(bd.String(64), nullable=False)
    last_name = bd.Column(bd.String(64), nullable=False)
    user_name = bd.Column(bd.String(64), nullable=False, unique=True)
    age = bd.Column(bd.Integer, nullable=False)
    email = bd.Column(bd.String(64), unique=True)
    password = bd.Column(bd.String(218))
    
    def __init__(self, name, last_name, user_name, age, email, password):
        self.name = name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age
        self.email = email
        self.password = encryptor.generate_password_hash(password.encode('utf-8'))
        
    def validate_password(self, password):
        return encryptor.check_password_hash(self.password, password)
            