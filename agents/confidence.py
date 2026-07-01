import json

from agents.base_agent import BaseAgent


class ConfidenceAgent(BaseAgent):

    def __init__(self):

        super().__init__("prompts/confidence.txt")

    def run(self, verified_claims):

        prompt = f"""
Verified Claims

{json.dumps(verified_claims, indent=2)}

For every verified claim assign

confidence

between

0.0

and

1.0

based on

• evidence quality

• verification quality

• ambiguity

Return ONLY JSON.

Example

[
    {{
        "field":"Invoice Number",
        "confidence":0.98
    }}
]
"""

        return self.ask(prompt)