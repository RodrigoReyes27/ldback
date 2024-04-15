from flask import Blueprint

documentos_blueprint = Blueprint("documentos_blueprint", __name__)

from .parse_pptx import *


# prevent circular imports

