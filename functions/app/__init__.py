from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from .user import user_blueprint

    app.register_blueprint(user_blueprint, name_prefix="/user")

    return app
