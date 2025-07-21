from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.monitor import *
import os
db = SQLAlchemy()

def create_app():
    print_usages()
    app = Flask(__name__)
    db_path = os.path.join("/app", "requests.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"



    db.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
