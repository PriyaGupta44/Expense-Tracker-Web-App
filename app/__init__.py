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
    from app.routes import main
    from app.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    # Ensure models are imported for SQLAlchemy/migrations.
    from app import models