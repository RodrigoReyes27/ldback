from flask import Flask
from flask_cors import CORS

cors = CORS()

def create_app() -> Flask:
    app = Flask(__name__)
    cors.init_app(app)
    from .user import user_blueprint
    
    app.register_blueprint(user_blueprint, url_prefix="/user")
    from .document import document_blueprint
    app.register_blueprint(document_blueprint, url_prefix="/document")

    return app
