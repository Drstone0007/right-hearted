from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'

def init_extensions(app):
    db.init_app(app)
    login.init_app(app)
