from flask import Flask

from os import getenv
from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app
from flask_cors import CORS


load_dotenv()


cors = CORS()


def create_app() -> Flask:
    app = Flask(__name__)
    cors.init_app(app)
    from .user import user_blueprint
    from .documentos import documentos_blueprint

    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(documentos_blueprint, url_prefix="/documentos")

    from .document import document_blueprint

    app.register_blueprint(document_blueprint, url_prefix="/document")

    return app
