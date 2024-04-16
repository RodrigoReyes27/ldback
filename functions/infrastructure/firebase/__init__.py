from os import getenv

from firebase_admin import credentials, initialize_app

creds: dict
with open("./cert/frida-research-firebase-adminsdk-krmnc-3f0287837c.json", "r") as f:
    creds = json.loads(f.read())


FIREBASE_CREDENTIALS = credentials.Certificate(
    "./cert/frida-research-firebase-adminsdk-krmnc-3f0287837c.json"
)

FIREBASE_CONFIG = {
    "apiKey": getenv("API_KEY"),
    "authDomain": getenv("AUTH_DOMAIN"),
    "databaseURL": getenv("DATABASE_URL"),
    "projectId": getenv("PROJECT_ID"),
    "storageBucket": getenv("STORAGE_BUCKET"),
    "appId": getenv("APP_ID"),
}

FIREBASE_APP = initialize_app(FIREBASE_CREDENTIALS, FIREBASE_CONFIG)
