import sys
import os
# Allows the pytest to go back up the directory and find the .py backend files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from processor import SyllabusProcessor
from datetime import date

def test_is_real_syllabus_with():
    processor = SyllabusProcessor("This is a valid syllabus.")
    assert processor.is_real_syllabus() == True

def test_is_real_syllabus_without():
    processor = SyllabusProcessor(None)
    assert processor.is_real_syllabus() == False

def test_is_real_syllabus_with_empty_str():
    processor = SyllabusProcessor("")
    assert processor.is_real_syllabus() == True

def test_processing_date_return_str():
    processor = SyllabusProcessor("some text")
    result = processor.get_processing_date()
    assert isinstance(result, str)  

def test_processing_date_match_today():
    processor = SyllabusProcessor("some text")
    result = processor.get_processing_date()
    today = date.today().strftime("%Y/%m/%d")
    assert result == today

def test_processing_date_format():
    processor = SyllabusProcessor("some text")
    result = processor.get_processing_date()
    parts = result.split("/")
    assert len(parts) == 3
    assert len(parts[0]) == 4
    assert len(parts[1]) == 2
    assert len(parts[2]) == 2

def test_initialize_syllabus_returns_dict():
    processor = SyllabusProcessor("Sample syllabus text")
    processor.set_base_info = lambda: None
    processor.generate_syllabus_sections = lambda: {}
    result = processor.initialize_syllabus()
    assert isinstance(result, dict)

def test_initialize_syllabus_has_fields():
    processor = SyllabusProcessor("Sample syllabus text")
    processor.set_base_info = lambda: None
    processor.generate_syllabus_sections = lambda: {}
    result = processor.initialize_syllabus()
    assert 'status' in result
    assert 'raw_text' in result
    assert 'processing_date' in result

def test_initialize_syllabus_raw_text_matches_input():
    processor = SyllabusProcessor("Sample syllabus text")
    processor.set_base_info = lambda: None
    processor.generate_syllabus_sections = lambda: {}
    result = processor.initialize_syllabus()
    assert result['raw_text'] == "Sample syllabus text"

def test_initialize_syllabus_status_is_valid():
    processor = SyllabusProcessor("Sample syllabus text")
    processor.set_base_info = lambda: None
    processor.generate_syllabus_sections = lambda: {}
    assert processor.initialize_syllabus()['status'] == 'valid'

def test_initialize_syllabus_all_keys():
    processor = SyllabusProcessor("Sample syllabus text")
    processor.set_base_info = lambda: None
    processor.generate_syllabus_sections = lambda: {}
    result = processor.initialize_syllabus()
    for key in ['status', 'course_id', 'course_name', 'course_dates',
                'instructor', 'processing_date', 'raw_text', 'sections']:
        assert key in result

def test_generate_sections_all_keys():
    processor = SyllabusProcessor("some text")
    processor.prompt_dir = "nonexistent/path"
    result = processor.generate_syllabus_sections()
    for key in ['late_policy', 'prerequisites', 'course_info', 'materials',
                'course_content', 'grading_scale', 'grading_categories', 'assignments',
                'lab_info', 'exam_policy', 'support_info', 'accommodations',
                'academic_integrity', 'ai_policy', 'wellness_resources', 'student_rights']:
        assert key in result

def test_processor_default_course_id():
    assert SyllabusProcessor("some text").course_id == 'invalid'

def test_processor_default_course_name():
    assert SyllabusProcessor("some text").course_name == 'invalid'

def test_processor_default_instructor():
    assert SyllabusProcessor("some text").instructor == 'invalid'

def test_processor_default_course_dates():
    assert SyllabusProcessor("some text").course_dates == 'invalid'

def test_processor_default_status():
    assert SyllabusProcessor("some text").status == 'valid'

def test_processor_stores_input_data():
    assert SyllabusProcessor("my syllabus text").data == "my syllabus text"