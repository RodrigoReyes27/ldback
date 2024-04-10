from flask import Blueprint

user_blueprint = Blueprint("user_blueprint", __name__)

# prevent circular imports
from .create_account import *
