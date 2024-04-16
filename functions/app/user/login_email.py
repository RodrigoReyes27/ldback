from flask import jsonify, request
import requests
import json

from . import user_blueprint
from .. import FIREBASE_CONFIG


@user_blueprint.route("/login_email", methods=["POST"])
def login_email_handle():
    try:
        data = request.get_json()
    except :
        return jsonify(msg=f"Email and Password must be set"), 400

    email: str
    password: str
    try:
        email = data["email"]
        password = data["password"]
    except KeyError:
        return jsonify(msg=f"Email and Password must be set"), 400
    

    payload = {
        "email": email, 
        "password": password
    }
    auth_response = requests.post(f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_CONFIG['apiKey']}", data=payload)

    if not auth_response.status_code == 200:
        return jsonify(msg=f"Incorrect Email or Password"), 401

    auth_token = json.loads(auth_response.content)["idToken"]
    return jsonify(msg=auth_token)
