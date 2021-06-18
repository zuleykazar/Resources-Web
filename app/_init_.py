from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
csrf = CSRFProtect()
db = SQLAlchemy()


from app.views import page
from app.models import User

def create_app(config):
    app.config.from_object(config)
    
    csrf.init_app(app)
    
    app.register_blueprint(page)
    
    with app.app_context():
        db.init_app(app) 
        db.create_all()
    
    return app
