from flask import jsonify, request

from . import user_blueprint


@user_blueprint.route("/delete_account", methods=["POST"])
def delete_account_handle():
    body = request.get_json()
    if not body:
        return jsonify(), 400
    if body["sure"] == "not_sure":
        return jsonify(), 400
    return jsonify(msg="Ok")
