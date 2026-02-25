import json
from debug_config import is_debug
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
        if is_debug():
            print(e)
        return 'error in the call'
    result = processor.test_process()
    if is_debug():
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
        if not processor.is_real_syllabus():
            return {'course_id': 'invalid'}
        processed_syllabus = processor.initialize_syllabus()
        if is_debug():
            print(f"Returning processed syllabus with data: {json.dumps([processed_syllabus])}")
        return json.dumps(processed_syllabus)
    except ValueError as e:
        if is_debug():
            print(e)
        return {'status': 'error'}

# Question Answering Route
@api.route('/complex-question', methods=['POST'])
def advanced_question():
    try:
        data = request.get_json()
        return 'You will have a detailed response to your question here...'
    except ValueError as e:
        if is_debug():
            print(e)
        return 'error in the call'

