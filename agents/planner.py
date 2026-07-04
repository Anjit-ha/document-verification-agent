from agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "prompts/planner.txt"
        )

    def run(self, document):

        prompt = f"""
DOCUMENT

{document}

Generate an extraction plan.

Return JSON only.
"""

        return self.ask(prompt)