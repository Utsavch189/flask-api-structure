from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints for different API versions
    from .v1.routes import v1_bp

    app.register_blueprint(v1_bp, url_prefix='/api/v1')

    return app
