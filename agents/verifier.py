import json

from agents.base_agent import BaseAgent


class VerifierAgent(BaseAgent):

    def __init__(self):

        super().__init__("prompts/verifier.txt")

    def run(self, document, claims):

        return self.ask(

            f"""

DOCUMENT

{document}

CLAIMS

{json.dumps(claims,indent=2)}

"""

        )