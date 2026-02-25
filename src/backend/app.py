import os

from flask import Flask
from routes import register_routes
from flask_cors import CORS
from dotenv import load_dotenv
from pathlib import Path
import argparse
from debug_config import is_debug

def load_env_from_root(start_path: Path):
    for path in [start_path] + list(start_path.parents):
        env_file = path / '.env'
        if env_file.exists():
            load_dotenv(env_file)
            return True
    return False

def parse_args():
    parser = argparse.ArgumentParser('Syllabye Backend')
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
    return parser.parse_args()

def create_app():
    app = Flask(__name__)

    # This is what should actually be here, but we need an offical ID that we get from having the extension on the Chrome Web Store
            # ALLOWED_ORIGIN = "chrome-extension://specific chrome extenion id here"
            # CORS(app, origins=ALLOWED_ORIGIN)
    CORS(app, origins="chrome-extension://*")
        
    app.config['DEBUG'] = True
    register_routes(app)
    return app

if __name__ == '__main__':
    if load_env_from_root(Path(__file__).resolve().parent):
        print("ENV: Loaded successfully")
        args = parse_args()
        os.environ['DEBUG_FLAG'] = str(args.debug)
        if is_debug():
            print("DEBUG MODE ENABLED")
        app = create_app()
        app.run(host='0.0.0.0', port=6767)
    else:
        print(f"ENV NOT FOUND: PROGRAM SHUTTING DOWN")