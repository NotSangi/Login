from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

bd = SQLAlchemy()
migrate = Migrate()
manager = LoginManager()

def create_app(config='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config)
    
    bd.init_app(app)
    migrate.init_app(app, bd)
    manager.init_app(app)
    
app = create_app()
