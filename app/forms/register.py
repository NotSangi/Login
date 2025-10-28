from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange
from wtforms import ValidationError
from app.models import User

class Register(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    user_name = StringField('User Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(15)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_check', 'Passwords Dont Match')])
    password_check = PasswordField('Passwrod Check', validators=[DataRequired()])
    button = SubmitField('Register')
    
    def validate(self, extra_validators=None):
        if not super().validate():
            return False
        
        user = User.query.filter_by(user_name=self.user_name.data).first()
        if user:
            self.user_name.errors.append("Error | El usuario ya se encuentra en uso.")
            return False

        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Error | El email ya se encuentra en uso.")
            return False
        
        self.user = user
        return True 
    
    