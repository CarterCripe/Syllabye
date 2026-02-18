from flask import Flask
from routes import register_routes
from flask_cors import CORS
from dotenv import load_dotenv
from pathlib import Path

def load_env_from_root(start_path: Path):
    for path in [start_path] + list(start_path.parents):
        env_file = path / '.env'
        if env_file.exists():
            load_dotenv(env_file)
            return True
    return False


def create_app():
    app = Flask(__name__)
    CORS(app, origins=['http://localhost:6766'])
    app.config['DEBUG'] = True
    register_routes(app)
    return app

if __name__ == '__main__':
    if load_env_from_root(Path(__file__).resolve().parent):
        print("ENV: Loaded successfully")
        app = create_app()
        app.run(host='0.0.0.0', port=6767)
    else:
        print(f"ENV NOT FOUND: PROGRAM SHUTTING DOWN")