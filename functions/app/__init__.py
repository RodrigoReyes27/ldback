from flask import Flask

from os import getenv
from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app

load_dotenv()

FIREBASE_CREDENTIALS = credentials.Certificate("app/cert/frida-research-firebase-adminsdk-krmnc-3f0287837c.json")

FIREBASE_CONFIG = {
    "apiKey": getenv("API_KEY"),
    "authDomain": getenv("AUTH_DOMAIN"),
    "databaseURL": getenv("DATABASE_URL"),
    "projectId": getenv("PROJECT_ID"),
    "storageBucket": getenv("STORAGE_BUCKET"),
    "appId": getenv("APP_ID"),
}

FIREBASE_ADMIN = initialize_app(FIREBASE_CREDENTIALS, FIREBASE_CONFIG)

from flask_cors import CORS

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