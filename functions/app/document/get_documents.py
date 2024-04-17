from flask import jsonify
from firebase_admin import firestore

from . import document_blueprint

@document_blueprint.route("/get_documents<id>", methods=["GET"])
def get_documents_handle(id):


