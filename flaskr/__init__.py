from flask import Flask
from config import Config
from flask_login import LoginManager

login_manager = LoginManager()

login_manager.login_view = "auth.signin"
login_manager.login_message = "Please sign in to access the principal page!"

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    login_manager.init_app(app)

    from flaskr.main import bp as main_bp
    app.register_blueprint(main_bp)

    from flaskr.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
