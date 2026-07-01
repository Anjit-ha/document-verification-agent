import json

from agents.base_agent import BaseAgent


class JudgeAgent(BaseAgent):

    def __init__(self):

        super().__init__("prompts/judge.txt")

    def run(self, verified):

        return self.ask(

            json.dumps(

                verified,

                indent=2

            )

        )