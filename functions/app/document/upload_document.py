import os
import uuid
from io import BytesIO

from domain.document import Document
from flask import jsonify, request
from infrastructure.firebase.persistence import (FileMimeType,
                                                 FirebaseFileStorage)
from infrastructure.firebase.persistence.repos.document_repo import \
    FirebaseDocumentRepo
from werkzeug.utils import secure_filename

from . import document_blueprint


def allowed_file(filename):
    allowed_extensions = {".pdf", ".doc", ".docx", ".ppt", ".pptx"}
    # Revisa que haya un punto en el archivo y tambien que sea un archivo permitido
    return (
        "." in filename and os.path.splitext(
            filename)[1].lower() in allowed_extensions
    )


@document_blueprint.route("/upload_document", methods=["POST"])
def upload_document_handle():
    file = request.files["file"]
    user_id = request.form["userId"]
    if file.filename == "":
        return jsonify(msg="No selected file"), 400

    # Se saca el nombre del archivo
    filename = secure_filename(file.filename)

    if not allowed_file(filename):
        return jsonify(msg="Archivo no permitido"), 400

    # Se saca la parte final

    type_file = os.path.splitext(filename)[1].lower()

    payload = BytesIO()
    file.save(payload)
    # Aqui esta la magia
    storage = FirebaseFileStorage.create_from_firebase_config("documents")

    if type_file == ".pdf":
        mimetype = FileMimeType.PDF
    elif type_file == ".doc":
        mimetype = FileMimeType.DOC
    elif type_file == ".docx":
        mimetype = FileMimeType.DOCX
    elif type_file == ".ppt":
        mimetype = FileMimeType.PPT
    elif type_file == ".pptx":
        mimetype = FileMimeType.PPTX

    # Se agrega el archivo
    url = storage.add(payload, mimetype)

    # Se crea el UUID
    new_uuid = uuid.uuid4()

    document = Document(
        id=str(new_uuid),
        ownerId=user_id,
        idRawDoc=url,
        name=filename,
        extension=type_file,
        parsedLLMInput="",
        usersWithAccess=[],
        biblioGraphicInfo=None,
        summary=None,
        keyConcepts=[],
        relationships=[],
    )
    
    repo = FirebaseDocumentRepo()

    repo.add(document)

    return jsonify(
        {"message": "File uploaded successfully", "userId": user_id, "url": url}
    )
