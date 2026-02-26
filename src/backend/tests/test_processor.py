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

def test_processing_date_return_str():
    processor = SyllabusProcessor("some text")
    result = processor.get_processing_date()
    assert isinstance(result, str)  

def test_processing_date_match_today():
    processor = SyllabusProcessor("some text")
    result = processor.get_processing_date()
    today = date.today().strftime("%Y/%m/%d")
    assert result == today

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
