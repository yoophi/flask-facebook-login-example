import os

from flask import Flask
from flask_login import LoginManager

from myapp.database import db
from myapp.models import User


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        os.environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite:///myapp.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_db(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    # Flask-Login helper to retrieve a user from our db
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

    init_extensions(app)
    init_blueprints(app)

    return app


def init_db(app):
    db.init_app(app)


def init_extensions(app):
    pass


def init_blueprints(app):
    from myapp.views import main as main_bp

    app.register_blueprint(main_bp)
