import json

from agents.base_agent import BaseAgent


class EvidenceAgent(BaseAgent):

    def __init__(self):

        super().__init__("prompts/evidence.txt")

    def run(self, document, claims):

        prompt = f"""
DOCUMENT

{document}

==========================

EXTRACTED CLAIMS

{json.dumps(claims, indent=2, ensure_ascii=False)}

==========================

Retrieve supporting evidence for every claim.

Return JSON only.
"""

        return self.ask(prompt)