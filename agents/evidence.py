import json

from agents.base_agent import BaseAgent


class EvidenceAgent(BaseAgent):

    def __init__(self):

        super().__init__("prompts/evidence.txt")

    def run(self, document: str, claims: list):

        prompt = f"""
DOCUMENT

{document}

CLAIMS

{json.dumps(claims, indent=2)}

Task:

For every claim, find the exact supporting sentence or paragraph
from the document.

If no evidence exists, return an empty string.

Return ONLY valid JSON.

Example

[
  {{
      "field":"Invoice Number",
      "value":"INV001",
      "evidence":"Invoice Number : INV001"
  }}
]
"""

        return self.ask(prompt)