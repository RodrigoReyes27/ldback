from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from .user import user_blueprint
    from .documentos import documentos_blueprint

    app.register_blueprint(user_blueprint, url_prefix="/user")
    
    app.register_blueprint(documentos_blueprint, url_prefix="/documentos")

    return app
