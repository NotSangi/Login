from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange
from wtforms import ValidationError

class Register(FlaskForm):
    name = StringField('Name: ', validators=DataRequired())
    last_name = StringField('Last Name: ', validators=DataRequired())
    user_name = StringField('User Name: ', validators=DataRequired())
    age = IntegerField('Age: ', validators=[DataRequired(), NumberRange(15)])
    email = EmailField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('password_check', 'Passwords Dont Match')])
    password_check = PasswordField('Passwrod Check: ', validators=DataRequired())
    button = SubmitField('Register')
    
    def validate_email(self, email):
        from models.user import User
        if User.query.filter_by(email=email.data).firts():
            raise ValidationError('Error - This email already exists')
        
    def validate_user_name(self, user_name):
        from models.user import User
        if User.query.filter_by(user_name=user_name.data).firts():
            raise ValidationError('Error - This user name already exists')