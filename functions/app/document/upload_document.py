import os

from flask import jsonify, request

from . import document_blueprint

@document_blueprint.route("/upload_document", methods=["POST"])
def upload_document_handle():
    file = request.files["file"]
    user_id = request.form["userId"]

    if file.filename == "":
        return jsonify(msg="No selected file")

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, file.filename)
    file.save(file_path)
    
    return jsonify({'message': 'File uploaded successfully', 'userId': user_id})

