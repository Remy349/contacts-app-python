from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()

login_manager.login_view = "auth.signin"
login_manager.login_message = ""

def create_app(config_class=Config):
    app = Flask(__name__)

    if config_class.SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        config_class.SQLALCHEMY_DATABASE_URI = config_class.SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1
        )

    if not config_class.SQLALCHEMY_DATABASE_URI:
        raise RuntimeError("DATABASE_URI is not set!")
    else:
        print("DATABASE_URI is ok!!!")

    app.config.from_object(config_class)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    from flaskr.main import bp as main_bp
    app.register_blueprint(main_bp)

    from flaskr.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    from flaskr.contact import bp as contact_bp
    app.register_blueprint(contact_bp, url_prefix="/contact")

    from flaskr.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app


from flaskr import models
