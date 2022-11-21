from flask import Flask

from backend.extensioons import db
from backend.routes.auth import auth_bp
from backend.routes.error import error_bp
from backend.routes.health import health_bp
from backend.routes.users import users_bp


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://sergio:my-password@localhost:5432/backenddb"

    db.app = app
    db.init_app(app)
    db.create_all()

    app.register_blueprint(health_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(error_bp)
    app.register_blueprint(auth_bp)
    return app
