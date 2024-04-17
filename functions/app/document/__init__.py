from flask import Blueprint

document_blueprint = Blueprint("document_blueprint", __name__)

# prevent circular imports
from .upload_document import *
from .get_document import *
