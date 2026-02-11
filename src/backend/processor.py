import datetime
import json


class SyllabusProcessor:
    # init class
    def __init__(self, data):
        self.data = data
        pass

    # temporary function
    def test_process(self) -> str:
        if self.data is None:
            return "Data is None!!!"
        else:
            return self.data

    def get_course_name(self):
        #     get course name
        return "Underwater Basket Weaving"

    def get_course_id(self):
        #     get course id
        return "528491"

    def get_course_dates(self):
        #     get course id
        return "{'start_date': '2026-01-05', 'end_date': '2026-03-30'}"
    def get_course_instructor(self):
        #     get course id
        return "Gandalf the Grey"

    def get_processing_date(self):
        #     get course id
        return "2026-02-11"

    def generate_syllabus_sections(self):
        sections = {
            'late_policy': 'The late_policy is...',
            'prerequisites': 'The prerequisites are...',
            'course_info': 'The course_info is...',
            'materials': 'The materials are...',
            'course_content': 'The course_content is...',
            'grading_scale': 'The grading_scale is...',
            'grading_categories': 'The grading_categories are...',
            'assignments': 'The assignments are...',
            'lab_info': 'The lab_info is...',
            'exam_policy': 'The exam_policy is...',
            'support_info': 'The support_info is...',
            'accommodations': 'The accommodations are...',
            'academic_integrity': 'The academic_integrity policy is...',
            'ai_policy': 'The ai_policy is...',
            'wellness_resources': 'The wellness_resources are...',
            'student_rights': 'The student_rights are...',
        }
        return sections

    def initialize_syllabus(self):
        json_syllabus = {
            'course_id': self.get_course_id(),
            'course_name': self.get_course_name(),
            'course_dates': self.get_course_dates(),
            'instructor': self.get_course_instructor(),
            'processing_date': self.get_processing_date(),
            'raw_text': self.data,
            'sections': self.generate_syllabus_sections()
        }
        print(json.dumps(json_syllabus, indent=4))
        return self.test_process()


test_data = {
    'text': 'When Mr Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday with a party of special magnificence, there was much talk and excitement in Hobbiton.'
}
process = SyllabusProcessor(test_data)
process.initialize_syllabus()