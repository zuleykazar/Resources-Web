from flask import Flask

from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()


from app.views import page
from app.models import User

def create_app(config):
    app.config.from_object(config)
    
    csrf.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = '.login'
    login_manager.login_message = 'Es necesario iniciar sesión.'
    
    app.register_blueprint(page)
    
    with app.app_context():
        db.init_app(app) 
        db.create_all()
    
    return app
