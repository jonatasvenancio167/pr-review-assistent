from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4

from app.domain.entities.review_finding import ReviewFinding

@dataclass
class CodeReview:
    summary: str
    findings: list[ReviewFinding] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        if not self.summary.strip():
            raise ValueError("O resumo do review não pode estar vazio.")

    @property
    def has_findings(self) -> bool:
        return bool(self.findings)

    @property
    def total_findings(self) -> int:
        return len(self.findings)
        