from agents.tars import tars_instance
from agents.manus import Manus

class NubiaOrchestrator:
    def __init__(self):
        self.tars = tars_instance
        self.manus = Manus()

    def handle(self, user_input: str) -> str:
        # Simple routing: if contains "code" or "write", use TARS; else Manus
        if any(word in user_input.lower() for word in ["code", "program", "script"]):
            agent = "tars"
            answer = self.tars.solve(user_input)
        else:
            agent = "manus"
            sid = self.manus.execute_async(user_input)
            answer = f"Task initiated. Session ID: {sid} (Manus will work on it in background)"
        return answer

nubia = NubiaOrchestrator()
