from flask import jsonify
from firebase_admin import firestore

from . import document_blueprint

@document_blueprint.route("/get_documents/<id>", methods=["GET"])
def get_documents_handle(id):

    db = firestore.client()
    collection = db.collection("Documents")

    query = collection.where("ownerId", "==", str(id))
    results = query.stream()

    documents = [doc.to_dict() for doc in results]

    if documents:
        return jsonify(documents), 200
    else:
        return jsonify({"error": "Document not found"}), 400 



     



