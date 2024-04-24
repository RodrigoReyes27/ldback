from flask import jsonify, request
from firebase_admin import firestore, auth

from . import user_blueprint
from infrastructure.firebase import FIREBASE_CONFIG


@user_blueprint.route("/load_profile", methods=["GET"])
def load_profile_handle():
    try:
        token = request.headers.get("Authorization")
        token = token.replace("Bearer ", "")
    except KeyError:
        return jsonify(msg="Token must be set"), 4000
    
    try:
        decoded_token = auth.verify_id_token(token, check_revoked=True)

        firestore_client = firestore.client()
        users_ref = firestore_client.collection("Users")
        user_info = users_ref.document(decoded_token["uid"]).get().to_dict()
        
        return {
            "token": token,
            "email": decoded_token["email"],
            "uid": decoded_token["uid"],
            "name": user_info["name"],
            "lastname": user_info["lastname"],
            "rootDirectoryId":  user_info["root_directory_id"],
        }
    except ValueError:
        return jsonify(msg="Invalid Token"), 401
    except auth.RevokedIdTokenError:
        return jsonify(msg="Token has been revoked"), 401
    except auth.CertificateFetchError:
        return jsonify(msg="An error occurred while decoding token"), 401
    except auth.UserDisabledError:
        return jsonify(msg="User disabled"), 401
    except auth.ExpiredIdTokenError:
        return jsonify(msg="Token has expired"), 403
    except auth.InvalidIdTokenError:
        return jsonify(msg="Invalid Token"), 401
    