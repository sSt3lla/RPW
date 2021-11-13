from flask import Flask
from .config import Config

#Need to use default variable trick to save data
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #Register
    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app