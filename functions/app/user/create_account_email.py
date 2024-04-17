from flask import jsonify, request
from firebase_admin import auth, firestore
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
        return jsonify(msg=f"Email, Password, Name and Lastname must be set"), 400

    email: str
    password: str
    name: str
    lastname: str
    try:
        email = data["email"]
        password = data["password"]
        name = data["name"]
        lastname = data["lastname"]
    except KeyError:
        return jsonify(msg=f"Email, Password, Name and Lastname must be set"), 400

    try:
        # Create user in Firebase Auth
        user_info: auth.UserRecord = auth.create_user(email=email, password=password)
        payload = {"email": email, "password": password, "returnSecureToken": True}
        auth_response = requests.post(
            f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_CONFIG['apiKey']}",
            data=payload,
        )
        
        if not auth_response.status_code == 200:
            return jsonify(msg=f"An error ocurred while creating the user."), 400
        
        auth_response = json.loads(auth_response.content)
        
        # Ref to Firestore
        firestore_client = firestore.client()
        users_ref = firestore_client.collection("Users")
        directory_ref = firestore_client.collection("Directory")
        
        # Find an available root directory id
        while True:
            root_directory_id = str(uuid.uuid4())
            if directory_ref.document(root_directory_id).get().to_dict() is None: break
        
        # Add user into Users collection
        users_ref.document(user_info.uid).set({
            "id": user_info.uid,
            "name": name,
            "lastname": lastname,
            "root_directory_id": root_directory_id
        })
        
        # Add new root directory for the user
        directory_ref.document(root_directory_id).set({
            "id": root_directory_id,
            "name": "Root Directory",
            "owner_id": auth_response["localId"]
        })

        auth_info = {
            "token": auth_response["idToken"],
            "email": email,
            "uid": auth_response["localId"],
            "name": name,
            "lastname": lastname,
            "root_directory_id": root_directory_id
        }
        return jsonify(auth_info)
    except ValueError:
        return jsonify(msg=f"Invalid Email or Password"), 400
    except FirebaseError:
        return jsonify(msg=f"An error ocurred while creating the user."), 400