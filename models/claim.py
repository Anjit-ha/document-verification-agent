from dataclasses import dataclass


@dataclass
class Claim:
    field: str
    value: str
    evidence: str = ""
    verified: bool = False
    confidence: float = 0.0
    reason: str = ""