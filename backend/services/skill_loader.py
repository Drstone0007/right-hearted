import importlib, os, json

SKILLS_DIR = os.path.join(os.path.dirname(__file__), '..', 'skills')
def load_installed_skills():
    path = os.path.join(SKILLS_DIR, 'installed.json')
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return []

def load_skill_module(name):
    skill_path = os.path.join(SKILLS_DIR, name)
    if not os.path.isdir(skill_path):
        return None
    sys.path.insert(0, skill_path)
    module = importlib.import_module('skill')
    sys.path.pop(0)
    return module

def get_skill_tools():
    from langchain.tools import Tool
    tools = []
    for name in load_installed_skills():
        module = load_skill_module(name)
        if module and hasattr(module, 'run'):
            manifest_path = os.path.join(SKILLS_DIR, name, 'manifest.json')
            with open(manifest_path) as f:
                manifest = json.load(f)
            tools.append(Tool(
                name=manifest.get('name', name),
                func=lambda **kwargs, m=module: m.run(**kwargs),  # simplified
                description=manifest.get('description', '')
            ))
    return tools
