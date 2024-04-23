from flask import jsonify
from firebase_admin import firestore
from infrastructure.firebase.persistence.repos.document_repo import FirebaseDocumentRepo
from infrastructure.firebase.persistence.firebase_file_storage import FirebaseFileStorage
from . import document_blueprint

@document_blueprint.route("/delete_document/<id>", methods=["GET"])
def delete_document_handle(id):

    repo = FirebaseDocumentRepo()
    storage = FirebaseFileStorage()

    # Se consigue la respuesta
    try:
        repo.delete(str(id))
        document = repo.get(str(id))

        storage.delete(document.id_raw_doc)

        return jsonify({"msg": "El documento ${id} fue borrado."}), 200
    except:
        return jsonify({"error": "Document not found"}), 400
        



     



