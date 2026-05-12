import ollama
from typing import Dict, List

class LLMRouter:
    def __init__(self, default_model="hermes3:8b"):
        self.models: Dict[str, str] = {
            "hermes3:8b": "general, reasoning",
            "dolphin-llama3:13b": "uncensored, coding, creative",
            "wizardlm-uncensored:13b": "deep reasoning, long-form",
            "manus-core": "uncensored, tool use, execution",
            "tars-core": "uncensored, logic, code, tactical"
        }
        self.priorities = {
            "code": ["tars-core", "dolphin-llama3:13b", "hermes3:8b"],
            "research": ["wizardlm-uncensored:13b", "tars-core"],
            "execute": ["manus-core", "hermes3:8b"],
            "general": ["tars-core", "hermes3:8b"]
        }
        self.default = default_model

    def route(self, query: str, task_type: str = "general") -> str:
        candidates = self.priorities.get(task_type, self.priorities["general"])
        available = self._available_models()
        for m in candidates:
            if m in available:
                return m
        return self.default

    def _available_models(self) -> List[str]:
        try:
            return [m['name'] for m in ollama.list().get("models", [])]
        except:
            return []
