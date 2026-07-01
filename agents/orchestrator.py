import json
import os

from agents.extractor import ExtractorAgent
from agents.evidence import EvidenceAgent
from agents.verifier import VerifierAgent
from agents.confidence import ConfidenceAgent
from agents.judge import JudgeAgent

from utils.logger import logger


class AgentHarness:

    def __init__(self):

        self.extractor = ExtractorAgent()
        self.evidence = EvidenceAgent()
        self.verifier = VerifierAgent()
        self.confidence = ConfidenceAgent()
        self.judge = JudgeAgent()

    def save_json(self, filename, data):
        """Save JSON output from each agent."""

        os.makedirs("output", exist_ok=True)

        with open(
            f"output/{filename}",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def run(self, document_text):
        print("Running NEW orchestrator...")

        logger.info("=" * 60)
        logger.info("Starting Agent Harness")
        logger.info("=" * 60)

        # --------------------------------------------------
        # Step 1 : Extract Claims
        # --------------------------------------------------

        logger.info("Running Extractor Agent...")

        claims = self.extractor.run(document_text)

        self.save_json("extracted_claims.json", claims)

        logger.info(f"Extracted {len(claims)} claims.")

        # --------------------------------------------------
        # Step 2 : Retrieve Evidence
        # --------------------------------------------------

        logger.info("Running Evidence Agent...")

        evidence = self.evidence.run(document_text, claims)

        self.save_json("evidence.json", evidence)

        logger.info("Evidence collected.")

        # --------------------------------------------------
        # Step 3 : Verify Claims
        # --------------------------------------------------

        logger.info("Running Verification Agent...")

        verified = self.verifier.run(document_text, evidence)

        self.save_json("verified_claims.json", verified)

        logger.info("Verification completed.")

        # --------------------------------------------------
        # Step 4 : Confidence Scoring
        # --------------------------------------------------

        logger.info("Running Confidence Agent...")

        confidence = self.confidence.run(verified)

        self.save_json("confidence_scores.json", confidence)

        logger.info("Confidence scores generated.")

        # --------------------------------------------------
        # Merge Confidence Scores
        # --------------------------------------------------

        confidence_lookup = {
            item["field"]: item["confidence"]
            for item in confidence
        }

        for claim in verified:

            claim["confidence"] = confidence_lookup.get(
                claim["field"],
                0.0
            )

        # --------------------------------------------------
        # Step 5 : Judge
        # --------------------------------------------------

        logger.info("Running Judge Agent...")

        report = self.judge.run(verified)

        report["claims"] = verified

        self.save_json("report.json", report)

        logger.info("Final report saved.")

        logger.info("Pipeline completed successfully.")

        return report