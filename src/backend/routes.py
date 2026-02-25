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

        if not data or 'text' not in data:
            return jsonify({
                'status': 'error',
                'message': 'No text provided'
            }), 400
        
        # This pulls just the text string from the data gathered
        raw_text = data['text']
        processor = SyllabusProcessor(raw_text)

        if not processor.is_real_syllabus():
            return jsonify({'status': 'invalid'}), 400
        
        processed_syllabus = processor.initialize_syllabus()
        if is_debug():
            print(f"Successfully processed syllabus for: {processed_syllabus.get('course_name', 'unknown')}")
        return jsonify(processed_syllabus)
    except Exception as e:
        if is_debug():
            print(f"Error processing syllabus: {e}")
        return jsonify({
            'status': 'error', 
            'message': str(e)
            }), 500


# Question Answering Route
@api.route('/complex-question', methods=['POST'])
def advanced_question():
    try:
        data = request.get_json()
        return jsonify(data)
    except Exception as e:
        if is_debug():
            print(e)
        return jsonify({'status': 'error'}), 500