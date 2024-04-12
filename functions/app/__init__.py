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

def create_app() -> Flask:
    app = Flask(__name__)

    from .user import user_blueprint

    app.register_blueprint(user_blueprint, url_prefix="/user")

    return app
