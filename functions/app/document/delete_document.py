from flask import jsonify
from firebase_admin import firestore
from infrastructure.firebase.persistence.repos.document_repo import FirebaseDocumentRepo
from infrastructure.firebase.persistence.firebase_file_storage import FirebaseFileStorage
from . import document_blueprint

from infrastructure.firebase import FIREBASE_CONFIG, FIREBASE_APP

@document_blueprint.route("/delete_document/<id>", methods=["GET"])
def delete_document_handle(id):

    repo = FirebaseDocumentRepo()
    storage = FirebaseFileStorage.create_from_firebase_config("documents")

    # Se consigue la respuesta
    try:
        document = repo.get(str(id))
        repo.delete(str(id))

        storage.delete(document.id_raw_doc)

        return jsonify({"msg": f"El documento {id} fue borrado."}), 200
    except Exception as e:
        return jsonify({"msg": f"Error deleting document {id}: {e}"}), 400
        
        



     



