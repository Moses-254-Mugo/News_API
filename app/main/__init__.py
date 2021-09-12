# from . import views, errors
from flask import Blueprint
mose = Blueprint('mose', __name__)
from .views import *
from .errors import *


