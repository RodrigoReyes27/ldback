from flask import Blueprint

document_blueprint = Blueprint("document_blueprint", __name__)

# prevent circular imports
from .upload_document import *
from .get_document import *
from .get_documents import *
from .delete_document import *
from .rename_document import *