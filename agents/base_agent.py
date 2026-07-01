from config import model
from utils.json_utils import clean_json


class BaseAgent:

    def __init__(self, prompt_file):

        with open(prompt_file, "r", encoding="utf-8") as f:
            self.prompt = f.read()

    def ask(self, text):

        response = model.generate_content(
            f"""
{self.prompt}

{text}
"""
        )

        return clean_json(response.text)