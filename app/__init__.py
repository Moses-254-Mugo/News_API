from config import Config
from flask import Flask
from config import Config

# Initializing application
app = Flask(__name__, instance_relative_config= True)

# Setting up configuration
app.config.from_object(Config)
app.config.from_pyfile('config.py')

from app import views