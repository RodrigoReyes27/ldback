from flask import jsonify, request
from firebase_admin import auth
from firebase_admin.exceptions import FirebaseError
import requests
import json

from . import user_blueprint
from infrastructure.firebase import FIREBASE_CONFIG


@user_blueprint.route("/create_account_email", methods=["POST"])
def create_account_email_handle():
    try:
        data = request.get_json()
    except:
        return jsonify(msg=f"Email and Password must be set"), 400

    email: str
    password: str
    try:
        email = data["email"]
        password = data["password"]
    except KeyError:
        return jsonify(msg=f"Email and Password must be set"), 400

    try:
        auth.create_user(email=email, password=password)
        payload = {"email": email, "password": password}
        auth_response = requests.post(
            f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_CONFIG['apiKey']}",
            data=payload,
        )

        auth_token = json.loads(auth_response.content)["idToken"]
        return jsonify(msg=auth_token)
    except ValueError:
        return jsonify(msg=f"Invalid Email or Password"), 400
    except FirebaseError:
        return jsonify(msg=f"An error ocurred while creating the user."), 400
