from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap()

# Initializing application
def create_app():
    
    # Creating the app configurations
    app.config.from_object(Config)

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import mose as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    # from .request import configure_request
    # configure_request(app)

    return app