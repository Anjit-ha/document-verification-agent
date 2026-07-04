import json

from agents.base_agent import BaseAgent


class VerifierAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "prompts/verifier.txt"
        )

    def run(
        self,
        document,
        evidence
    ):

        if isinstance(evidence, list):

            evidence = json.dumps(
                evidence,
                indent=4,
                ensure_ascii=False
            )

        prompt = f"""

DOCUMENT

{document}

========================

EXTRACTED EVIDENCE

{evidence}

========================

Verify every extracted field.

For each field decide

1. verified

2. evidence

3. reason

Do NOT invent values.

Return JSON only.

"""

        return self.ask(prompt)