import json

from agents.base_agent import BaseAgent


class FeedbackAgent(BaseAgent):

    def __init__(self):

        super().__init__("prompts/feedback.txt")

    def run(self, failed_claims):

        return self.ask(

            json.dumps(

                failed_claims,

                indent=2

            )

        )