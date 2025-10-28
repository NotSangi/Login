from app import bd
from flask import flash,render_template, redirect, url_for, request, Blueprint
from flask_login import login_user, login_required, logout_user
from app.forms import Login
from app.forms import Register
from app.models import User

auth_routes = Blueprint('auth', __name__)

@auth_routes.route("/")
def index():
    return render_template('index.html')

@auth_routes.route("/welcome")
@login_required
def welcome():
    return render_template('welcome.html')

@auth_routes.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user is not None:
            if user.validate_password(form.password.data):
                login_user(user)
                next_page = request.args.get('next')
                    
                if next_page is None or not next_page[0] == '/':
                    next_page = url_for('auth.welcome')
                return redirect(next_page)
    return render_template('auth/login.html', form=form)

@auth_routes.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))

@auth_routes.route("/register", methods=['GET', 'POST'])
def register():
    form = Register() 
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            last_name=form.last_name.data,
            user_name=form.user_name.data,
            age=form.age.data,
            email=form.email.data,
            password=form.password.data
        )
        
        bd.session.add(user)
        bd.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

            
            
