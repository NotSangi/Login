from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired
from app.models import User

class Login(FlaskForm):
    user_name = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    button = SubmitField('Sign In')
    
    def validate(self, extra_validators=None):
        if not super().validate():
            return False
        
        user = User.query.filter_by(user_name=self.user_name.data).first()

        if user is None:
            self.user_name.errors.append("Error | El usuario no existe")
            return False

        if not user.validate_password(self.password.data):
            self.password.errors.append("Error | Contraseña incorrecta")
            return False

        self.user = user
        return True