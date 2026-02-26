from debug_config import is_debug
from flask import Blueprint, request, jsonify
from processor import SyllabusProcessor

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

def register_routes(app):
    app.register_blueprint(api)


# Main Processing Route
@api.route('/process', methods=['POST'])
def process_syllabus():
    try:
        data = request.get_json()

        # Validates if requested field has correct text, if not return error
        if not data or 'text' not in data:
            return jsonify({
                'status': 'error',
                'message': 'No text provided'
            }), 400
        
        # This pulls just the text string from the data gathered
        raw_text = data['text']
        processor = SyllabusProcessor(raw_text)

        # Checks if text is empty or None
        if not processor.is_real_syllabus():
            return jsonify({'status': 'invalid'}), 400
        
        # Runs the LLM processing and assembles JSON response
        processed_syllabus = processor.initialize_syllabus()
        if is_debug():
            print(f"Successfully processed syllabus for: {processed_syllabus.get('course_name', 'unknown')}")
        # jsonify() wraps the python dict in a HTTP response with Content-Type: so frontend can parse it
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
        return 'You will have a detailed response to your question here...'
    except ValueError as e:
        if is_debug():
            print(e)
        return jsonify({'status': 'error'}), 500