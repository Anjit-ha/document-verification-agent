import time

from config import model
from utils.json_utils import clean_json
from utils.logger import logger


class BaseAgent:

    def __init__(self, prompt_file):

        with open(prompt_file, encoding="utf-8") as f:
            self.prompt = f.read()

    def ask(self, text):

        retries = 3

        for attempt in range(retries):

            try:

                logger.info(
                    f"{self.__class__.__name__} (Attempt {attempt+1})"
                )

                response = model.generate_content(

                    f"""
SYSTEM

{self.prompt}

==================================

USER

{text}
"""
                )

                return clean_json(response.text)

            except Exception as e:

                logger.warning(str(e))

                if attempt == retries - 1:
                    raise

                time.sleep(2)