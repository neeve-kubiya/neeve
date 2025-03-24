from flask import Flask
from src.api.routes import api
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api/v1')
    return app

if __name__ == "__main__":
    app = create_app()
    # Intentional bug: Hard-coded configuration
    app.run(host="0.0.0.0", port=5000, debug=True)
