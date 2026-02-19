"""
Generic LLM Agent module supporting multiple providers (Anthropic Claude, Google Gemini).

Usage:
    agent = Agent.get_agent("claude", "my_prompt:1", prompt_dir="prompts")
    response = agent.invoke("What is the capital of France?")
"""

import os
from abc import ABCMeta, abstractmethod
from pathlib import Path
from dotenv import load_dotenv
try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # Fallback for older Python versions

# Optional imports for different providers
try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    Anthropic = None
    ANTHROPIC_AVAILABLE = False

try:
    import google.genai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    genai = None
    GEMINI_AVAILABLE = False


class Agent(metaclass=ABCMeta):
    """Base class for all LLM agents."""

    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    @abstractmethod
    def invoke(self, user_prompt: str) -> str:
        """
        Send a prompt to the LLM and return the response.

        Args:
            user_prompt: The user's input prompt

        Returns:
            The LLM's response text
        """
        pass

    @property
    @abstractmethod
    def model(self) -> str:
        """Return the model name."""
        pass

    @staticmethod
    def _load_system_prompt(prompt_ref: str, prompt_dir_path: Path) -> str:
        """
        Load a system prompt from a TOML file.

        Args:
            prompt_ref: Reference in format "name:version" (e.g., "assistant:1" or "assistant:latest")
            prompt_dir_path: Path to directory containing prompt TOML files

        Returns:
            The prompt string for the specified version
        """
        if not prompt_dir_path.is_dir():
            raise NotADirectoryError(f"Prompt directory not found: {prompt_dir_path}")

        fname, vers = prompt_ref.split(":")
        with open(str(prompt_dir_path / f"{fname}.toml"), 'rb') as file:
            toml_content = tomllib.load(file)

        if vers == "latest":
            versions = [key for key in toml_content.keys() if key.startswith('v')]
            version = max(versions, key=lambda v: int(v[1:]))
        else:
            version = f"v{vers}"

        return toml_content[version]

    @classmethod
    def get_agent(
            cls,
            agent_type: str,
            prompt: str,
            load_from_file: bool = True,
            prompt_dir: str = "prompts"
    ) -> "Agent":
        """
        Factory method to create an agent of the specified type.

        Args:
            agent_type: Type of agent ("claude" or "gemini")
            prompt: Either a prompt reference ("name:version") if load_from_file=True,
                   or the actual prompt string if load_from_file=False
            load_from_file: Whether to load prompt from TOML file
            prompt_dir: Directory containing prompt TOML files

        Returns:
            An Agent instance of the specified type
        """
        base_dir = Path(__file__).resolve().parent
        load_dotenv(base_dir / ".env")
        if load_from_file:
            system_prompt = cls._load_system_prompt(prompt, Path(prompt_dir))
        else:
            system_prompt = prompt

        if agent_type == "claude":
            return ClaudeAgent(
                system_prompt=system_prompt,
                api_key=os.getenv("ANTHROPIC_API_KEY"),
                model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-5-20250929")
            )
        elif agent_type == "gemini":
            return GeminiAgent(
                system_prompt=system_prompt,
                api_key=os.getenv("GEMINI_API_KEY"),
                model=os.getenv("GEMINI_MODEL", "gemini-3-flash-preview")
            )
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")


class ClaudeAgent(Agent):
    """Anthropic Claude LLM agent."""

    def __init__(self, system_prompt: str, api_key: str, model: str):
        super().__init__(system_prompt)
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("anthropic package is required for Claude support")
        self.client = Anthropic(api_key=api_key)
        self._model = model

    def invoke(self, user_prompt: str) -> str:
        response = self.client.messages.create(
            model=self._model,
            max_tokens=4096,
            temperature=0,
            system=self.system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        if response.content and len(response.content) > 0:
            return response.content[0].text
        return ""

    @property
    def model(self) -> str:
        return self._model


class GeminiAgent(Agent):
    """Google Gemini LLM agent (using Google AI SDK with API key)."""

    def __init__(self, system_prompt: str, api_key: str, model: str):
        super().__init__(system_prompt)
        if not GEMINI_AVAILABLE:
            raise ImportError("google-generativeai package is required for Gemini support")

        genai.configure(api_key=api_key)
        self.client = genai.GenerativeModel(
            model_name=model,
            system_instruction=system_prompt
        )
        self._model = model

    def invoke(self, user_prompt: str) -> str:
        response = self.client.generate_content(
            user_prompt,
            generation_config={
                "temperature": 0.3,
                "max_output_tokens": 4096,
            }
        )
        return response.text

    @property
    def model(self) -> str:
        return self._model


if __name__ == "__main__":
    # Example usage
    import dotenv
    dotenv.load_dotenv()

    # Option 1: Load prompt from file
    # agent = Agent.get_agent("claude", "assistant:latest", prompt_dir="prompts")

    gemini_test_prompt = "You are a poem writer that writes poems in the style of George RR Martin"

    claude_test_prompt = "You are a poem writer that writes poems in the style of JRR Tolkien"

    claude_agent = Agent.get_agent(
        "claude",
        claude_test_prompt,
        load_from_file=False
    )
    gemini_agent = Agent.get_agent(
        "gemini",
        gemini_test_prompt,
        load_from_file=False
    )

    response_claude = claude_agent.invoke("Write a poem about how claude is the best llm")
    responses_gemini = gemini_agent.invoke("Write a poem about how gemini is the best llm")
    print(f"Claude Poem: {response_claude}\n\nGemini Poem: {responses_gemini}")