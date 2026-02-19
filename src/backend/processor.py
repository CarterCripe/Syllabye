from datetime import date
import json
import os
from agents.agent import Agent
from pathlib import Path
from dotenv import load_dotenv
from debug_config import is_debug
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
        self.prompt_dir = BASE_DIR / 'agents' / 'agent_prompts'
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

    # def get_course_name(self):
    #     #     get course name
    #     return "Underwater Basket Weaving"
    #
    # def get_course_id(self):
    #     #     get course id
    #     return "528491"
    #
    # def get_course_dates(self):
    #     #     get course id
    #     return "{'start_date': '2026-01-05', 'end_date': '2026-03-30'}"
    # def get_course_instructor(self):
    #     #     get course id
    #     return "Gandalf the Grey"

    def set_base_info(self):
        key = os.getenv("ANTHROPIC_API_KEY")
        if not key:
            if is_debug():
                print("CRITICAL ERROR: ANTHROPIC_API_KEY is not set in the environment! Retrying load...")
            start_path = Path(__file__).resolve().parent
            for path in [start_path] + list(start_path.parents):
                env_file = path / '.env'
                if env_file.exists():
                    load_dotenv(env_file)
                    key = os.getenv("ANTHROPIC_API_KEY")
                    if not key:
                        if is_debug():
                            print("CRITICAL ERROR: ANTHROPIC_API_KEY is not set in the environment! Retry Failed")
                    else:
                        print("RELOAD SUCCESSFUL: Proceeding...")
        try:
            agent: Agent = Agent.get_agent('claude', "getBaseInfo:latest", True, str(self.prompt_dir))
            raw_base_info = agent.invoke(str(self.data))
            if is_debug():
                print(f"DEBUGGING: raw_base_info: {raw_base_info}")
            items = raw_base_info.split(',')
            self.course_name = items[0]
            self.course_id = items[1]
            self.instructor = items[2]
            self.course_dates = items[3]

        except Exception as e:
            if is_debug():
                print(f"Error during base information retrieval: {e}")
            self.status = 'error'
            return None
        return None

    def get_processing_date(self):
        #     get today's date
        now = date.today()
        formatted_date = now.strftime("%Y/%m/%d")
        return str(formatted_date)

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
            if is_debug():
                print(f"Error in initialization: {e}")
            return {'status': 'error'}
        json_syllabus["status"] = 'valid'
        if is_debug():
            print(json.dumps(json_syllabus, indent=4))
        return json_syllabus

if __name__ == '__main__':
    os.environ['DEBUG_FLAG'] = str('True')
    test_string = {
        'text': 'When Mr Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday with a party of special magnificence, there was much talk and excitement in Hobbiton.'
    }
    softengr2 = 'testing/test_syllabi/softengr2.txt'
    networks = 'testing/test_syllabi/networks.txt'
    with open(softengr2, 'r') as f:
        test_syllabus = f.read()
    process = SyllabusProcessor(test_syllabus)
    process.initialize_syllabus()