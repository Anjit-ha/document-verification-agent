import json

from agents.base_agent import BaseAgent


class ExtractorAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "prompts/extractor.txt"
        )

    def run(
        self,
        document,
        extraction_plan,
        refinement_instruction=""
    ):

        if isinstance(extraction_plan, dict):

            extraction_plan = json.dumps(
                extraction_plan,
                indent=4,
                ensure_ascii=False
            )

        prompt = f"""
DOCUMENT

{document}

==========================

EXTRACTION PLAN

{extraction_plan}

==========================

REFINEMENT

{refinement_instruction}

==========================

Follow the extraction plan.

Extract ALL information section by section.

If refinement instructions are provided,
ONLY re-extract the requested sections.

Return ONLY valid JSON.
"""

        return self.ask(prompt)