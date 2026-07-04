import json
import os

from agents.planner import PlannerAgent
from agents.extractor import ExtractorAgent
from agents.evidence import EvidenceAgent
from agents.verifier import VerifierAgent
from agents.confidence import ConfidenceAgent
from agents.feedback import FeedbackAgent
from agents.judge import JudgeAgent

from utils.logger import logger


class AgentHarness:

    def __init__(
        self,
        max_iterations=3,
        confidence_threshold=0.90
    ):

        self.planner = PlannerAgent()
        self.extractor = ExtractorAgent()
        self.evidence = EvidenceAgent()
        self.verifier = VerifierAgent()
        self.confidence = ConfidenceAgent()
        self.feedback = FeedbackAgent()
        self.judge = JudgeAgent()

        self.max_iterations = max_iterations
        self.confidence_threshold = confidence_threshold

    def save_json(self, filename, data):

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

    def merge_claims(self, existing_claims, new_claims):

        merged = {}

        for claim in existing_claims:
            merged[claim["field"]] = claim

        for claim in new_claims:
            merged[claim["field"]] = claim

        return list(merged.values())

    def run(self, document):

        logger.info("=" * 60)
        logger.info("Starting Deep Extract Agent Harness")
        logger.info("=" * 60)

        revision_history = []

        verified_claims = []

        failed = []

        # --------------------------------------------------
        # STEP 1 : Planner
        # --------------------------------------------------

        logger.info("Generating extraction plan...")

        extraction_plan = self.planner.run(document)

        self.save_json(
            "plan.json",
            extraction_plan
        )

        # --------------------------------------------------
        # STEP 2 : Initial Extraction
        # --------------------------------------------------

        logger.info("Running initial extraction...")

        claims = self.extractor.run(
            document,
            extraction_plan
        )

        self.save_json(
            "iteration_1_claims.json",
            claims
        )

        # --------------------------------------------------
        # STEP 3 : Iterative Verification
        # --------------------------------------------------

        for iteration in range(self.max_iterations):

            logger.info(f"Iteration {iteration + 1}")

            # --------------------------------------------
            # Evidence
            # --------------------------------------------

            evidence = self.evidence.run(
                document,
                claims
            )

            self.save_json(
                f"iteration_{iteration+1}_evidence.json",
                evidence
            )

            # --------------------------------------------
            # Verification
            # --------------------------------------------

            verified = self.verifier.run(
                document,
                evidence
            )

            self.save_json(
                f"iteration_{iteration+1}_verified.json",
                verified
            )

            # --------------------------------------------
            # Confidence
            # --------------------------------------------

            confidence = self.confidence.run(
                verified
            )

            self.save_json(
                f"iteration_{iteration+1}_confidence.json",
                confidence
            )

            confidence_lookup = {

                item["field"]: item["confidence"]

                for item in confidence

            }

            for claim in verified:

                claim["confidence"] = confidence_lookup.get(
                    claim["field"],
                    0.0
                )

            # --------------------------------------------
            # Passed / Failed
            # --------------------------------------------

            passed = []

            failed = []

            for claim in verified:

                if (
                    claim.get("verified", False)
                    and
                    claim.get("confidence", 0.0)
                    >= self.confidence_threshold
                ):

                    passed.append(claim)

                else:

                    failed.append(claim)

            verified_claims = self.merge_claims(
                verified_claims,
                passed
            )

            revision_history.append(
                {
                    "iteration": iteration + 1,
                    "verified": len(passed),
                    "failed": len(failed),
                    "status": (
                        "SUCCESS"
                        if len(failed) == 0
                        else "REFINEMENT_REQUIRED"
                    )
                }
            )

            # --------------------------------------------
            # Stop if everything passed
            # --------------------------------------------

            if len(failed) == 0:

                logger.info("All claims verified successfully.")

                break

            # --------------------------------------------
            # Feedback
            # --------------------------------------------

            logger.info(
                f"{len(failed)} claims require refinement."
            )

            refinement = self.feedback.run(
                failed
            )

            self.save_json(
                f"iteration_{iteration+1}_feedback.json",
                refinement
            )

            # --------------------------------------------
            # Re-Extraction
            # --------------------------------------------

            claims = self.extractor.run(
                document,
                extraction_plan,
                refinement
            )

            self.save_json(
                f"iteration_{iteration+2}_claims.json",
                claims
            )

        # --------------------------------------------------
        # Final Merge
        # --------------------------------------------------

        final_claims = self.merge_claims(
            verified_claims,
            failed
        )

        # --------------------------------------------------
        # Judge
        # --------------------------------------------------

        report = self.judge.run(
            final_claims
        )

        report["claims"] = final_claims

        report["iterations"] = revision_history

        self.save_json(
            "report.json",
            report
        )

        logger.info("=" * 60)
        logger.info("Pipeline Completed Successfully")
        logger.info("=" * 60)

        return report