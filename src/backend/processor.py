import datetime
import json
from agents.agent import Agent
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class SyllabusProcessor:
    # init class
    def __init__(self, data):
        self.data = data
        self.status = 'valid'
        self.course_id = 'invalid'
        self.course_name = 'invalid'
        self.instructor = 'invalid'
        self.course_dates = 'invalid'
        self.prompt_dir = BASE_DIR / 'src' / 'backend' / 'agents' / 'agent_prompts'
        pass

    # temporary function
    def test_process(self) -> str:
        if self.data is None:
            return "Data is None!!!"
        else:
            return self.data

    def is_real_syllabus(self) -> bool:
        if self.data is None:
            return False
        else:
            return True

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
    def set_base_info(self):
        try:
            prompt_path = self.prompt_dir / 'getBaseInfo.toml'
            agent: Agent = Agent.get_agent('claude', "", True, str(prompt_path))
            raw_base_info = agent.invoke(self.data)
            print(f"DEBUGGING: raw_base_info: {raw_base_info}")
            items = raw_base_info.split(',')
            self.course_name = items[1]
            self.course_id = items[0]
            self.instructor = items[2]
            self.course_dates = items[3]

        except Exception as e:
            print(f"Error during base information retrieval: {e}")
            self.status = 'error'
            return None
        return None

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
        try:
            self.set_base_info()
            json_syllabus = {
                'status': self.status,
                'course_id': self.course_id,
                'course_name': self.course_name,
                'course_dates': self.course_dates,
                'instructor': self.instructor,
                'processing_date': self.get_processing_date(),
                'raw_text': self.data,
                'sections': self.generate_syllabus_sections()
            }
        except ValueError as e:
            print(f"Error in initialization: {e}")
            return {'status': 'error'}
        json_syllabus["status"] = 'valid'
        print(json.dumps(json_syllabus, indent=4))
        return json_syllabus


test_data = {
    'text': 'When Mr Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday with a party of special magnificence, there was much talk and excitement in Hobbiton.'
}
process = SyllabusProcessor(test_data)
process.initialize_syllabus()