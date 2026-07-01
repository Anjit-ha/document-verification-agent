from dataclasses import dataclass
from typing import List

from models.claim import Claim


@dataclass
class VerificationReport:
    overall_status: str
    summary: str
    claims: List[Claim]