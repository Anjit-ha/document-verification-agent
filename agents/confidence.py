try:
    from rust_utils import jaccard_similarity
    RUST_ENABLED = True
except ImportError:
    RUST_ENABLED = False


class ConfidenceAgent:

    def run(self, verified):

        confidence = []

        for claim in verified:

            # If verification failed, confidence is zero
            if not claim.get("verified", False):

                score = 0.0

            elif RUST_ENABLED:

                similarity = jaccard_similarity(
                    str(claim.get("value", "")),
                    str(claim.get("evidence", ""))
                )

                if similarity >= 0.90:
                    score = 0.99
                elif similarity >= 0.75:
                    score = 0.90
                elif similarity >= 0.50:
                    score = 0.75
                else:
                    score = 0.50

            else:

                # Fallback when Rust isn't available
                score = 0.90 if claim.get("verified", False) else 0.0

            confidence.append(
                {
                    "field": claim["field"],
                    "confidence": round(score, 2)
                }
            )

        return confidence