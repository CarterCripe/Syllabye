from debug_config import is_debug
from flask import Blueprint, request, jsonify
from processor import SyllabusProcessor
from llm import LLM

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
        if not data or 'question' not in data:
            return jsonify({'status': 'error', 'message': 'No question provided'}), 400
        llm = LLM(data)
        return jsonify(llm.answer_tough_question())
    except Exception as e:
        if is_debug():
            print(f"Error processing tough question: {e}")
        return jsonify({'status': 'error'}), 500

# Search bar to get user's needs
@api.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        if not data or 'question' not in data or 'classes' not in data:
            return jsonify({'status': 'error', 'message': 'Missing question or classes'}), 400
        llm = LLM(data['question'])
        return jsonify(llm.get_search_info(data['classes']))
    except Exception as e:
        if is_debug():
            print(f"Error processing search: {e}")
        return jsonify({'status': 'error'}), 500