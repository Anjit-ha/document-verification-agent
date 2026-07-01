from agents.base_agent import BaseAgent


class ExtractorAgent(BaseAgent):

    def __init__(self):

        super().__init__("prompts/extractor.txt")

    def run(self, document):

        return self.ask(document)