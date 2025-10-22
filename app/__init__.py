from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

bd = SQLAlchemy()
migrate = Migrate()
manager = LoginManager()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)
    
    bd.init_app(app)
    migrate.init_app(app, bd)
    manager.init_app(app)
    manager.login_view = 'auth.login'
    
    from app.models import User
    @manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.routes import auth_routes
    app.register_blueprint(auth_routes)
    
    return app

app = create_app()