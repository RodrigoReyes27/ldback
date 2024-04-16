import logging
import os
from io import BytesIO

from flask import jsonify, request

from . import document_blueprint
from infrastructure.firebase.persistence import FirebaseFileStorage, FileMimeType


@document_blueprint.route("/upload_document", methods=["POST"])
def upload_document_handle():
    file = request.files["file"]
    user_id = request.form["userId"]
    if file.filename == "":
        return jsonify(msg="No selected file")

    payload = BytesIO()
    file.save(payload)
    storage = FirebaseFileStorage.create_from_firebase_config("mis_docs")
    url = storage.add(payload, FileMimeType.PNG)

    return jsonify(
        {"message": "File uploaded successfully", "userId": user_id, "url": url}
    )
