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
        try:
            agent: Agent = Agent.get_agent('claude', "getSections:latest", True, str(self.prompt_dir))
            raw_sections = agent.invoke(str(self.data))
            if is_debug():
                print(f"DEBUGGING: raw_sections: {raw_sections}")
            cleaned = raw_sections.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
            return json.loads(cleaned)
        
        except Exception as e:
            if is_debug():
                print(f"Error generating sections: {e}")

        return {
            'late_policy': 'Not specified.',
            'prerequisites': 'Not specified.',
            'course_info': 'Not specified.',
            'materials': 'Not specified.',
            'course_content': 'Not specified.',
            'grading_scale': 'Not specified.',
            'grading_categories': 'Not specified.',
            'assignments': 'Not specified.',
            'lab_info': 'Not specified.',
            'exam_policy': 'Not specified.',
            'support_info': 'Not specified.',
            'accommodations': 'Not specified.',
            'academic_integrity': 'Not specified.',
            'ai_policy': 'Not specified.',
            'wellness_resources': 'Not specified.',
            'student_rights': 'Not specified.'
        }

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

    softengr2 = 'testing/test_syllabi/softengr2.txt'
    networks = 'testing/test_syllabi/networks.txt'
    with open(softengr2, 'r') as f:
        test_syllabus = f.read()
    process = SyllabusProcessor(test_syllabus)
    process.initialize_syllabus()