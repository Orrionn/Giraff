from flask import Flask
from app.routers import main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app

if __name__ == "__main__":
    create_app().run(debug=True)