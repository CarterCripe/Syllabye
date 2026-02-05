from flask import Blueprint, request, jsonify
from processor import SyllabusProcessor

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

@api.route('/syllabus', methods=['POST'])
def handle_syllabus():
    try:
        data = request.get_json()
        processor = SyllabusProcessor(data)
    except ValueError as e:
        print(e)
        return 'error in the call'
    result = processor.test_process()
    print("Returning result?")
    return result

def register_routes(app):
    app.register_blueprint(api)