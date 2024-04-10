from flask import jsonify, request

from . import user_blueprint


@user_blueprint.route("/create_account", methods=["POST"])
def create_account_handle():
    return jsonify(msg="Ok")
