from flask import Flask
from app.models import User
from app import models

from app.extensions import db, login_manager, migrate
from config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    initialize_extensions(app)
    register_blueprints(app)

    return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


def register_blueprints(app):
    from app.routes import main
    from app.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
