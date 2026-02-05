from flask import Flask
from routes import register_routes
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:6766'])
    app.config['DEBUG'] = True
    register_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=6767)