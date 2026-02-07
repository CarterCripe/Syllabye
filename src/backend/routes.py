import json

from flask import Blueprint, request, jsonify
from processor import SyllabusProcessor

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

@api.route('/syllabus', methods=['POST'])
def test_syllabus():
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


# Main Processing Route
@api.route('/process', methods=['POST'])
def process_syllabus():
    try:
        data = request.get_json()
        data = json.loads(data)
        processor = SyllabusProcessor(data)
        return data
    except ValueError as e:
        print(e)
        return 'error in the call'

# Question Answering Route
@api.route('/process', methods=['POST'])
def advanced_question():
    try:
        data = request.get_json()
        return data
    except ValueError as e:
        print(e)
        return 'error in the call'

