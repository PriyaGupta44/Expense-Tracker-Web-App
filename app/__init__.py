from flask import Flask

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

    from app.auth import auth
    from app.dashboard import dashboard
    from app.expenses import expenses
    from app.routes import main

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(expenses)

    from app import models


@login_manager.user_loader
def load_user(user_id):

    from app.models import User

    return db.session.get(User, int(user_id))