import json
from agents.agent import Agent
from pathlib import Path
try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib
from debug_config import is_debug
BASE_DIR = Path(__file__).resolve().parent

class LLM:
    def __init__(self, question):
        self.data = question
        self.prompt_dir = BASE_DIR / 'agents' / 'agent_prompts'

    def answer_tough_question(self):
        prompt_name = 'toughQuestion:latest'
        model = 'gemini'
        try:
            if is_debug():
                print("DEBUGGING: (Tough Q) Awaiting LLM response...")
            agent: Agent = Agent.get_agent(model, prompt_name, True, str(self.prompt_dir))
            answer = agent.invoke(str(self.data))
            if is_debug():
                print(f"DEBUGGING: (Tough Q) raw_sections output: {answer}")
            cleaned = {
                'status': 'valid',
                'answer': answer
            }
            return cleaned

        except Exception as e:
            if is_debug():
                print(f"Error generating tough q answer: {e}")
            return {'status': 'error'}

    def get_search_info(self, classes):
        model = 'gemini'
        prompt = self.inject_classes(classes)
        try:
            if is_debug():
                print("DEBUGGING: (Search) Awaiting LLM response...")
            agent: Agent = Agent.get_agent(model, prompt, False)
            answer = agent.invoke(str(self.data))
            if is_debug():
                print(f"DEBUGGING: (Search) raw_sections output: {answer}")
            try:
                result = json.loads(answer)
                result["status"] = "valid"
            except json.JSONDecodeError:
                result = {"status": "invalid"}
            return result

        except Exception as e:
            if is_debug():
                print(f"Error generating search info: {e}")
            return {'status': 'error'}

    def inject_classes(self, classes):
        with open("./agents/agent_prompts/searchInfo.toml", 'rb') as file:
            toml_content = tomllib.load(file)
            versions = [key for key in toml_content.keys() if key.startswith('v')]
            version = max(versions, key=lambda v: int(v[1:]))
        prompt = toml_content[version].replace("{supported_classes}", classes)
        return prompt
