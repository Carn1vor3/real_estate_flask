from flask import Flask
from config import Config
from .extensions import db
from .routes.listings import listings_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.register_blueprint(listings_bp)

    return app
