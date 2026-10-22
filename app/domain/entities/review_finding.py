from dataclasses import dataclass, field

from app.domain.enum.severity import Severity

@dataclass
class ReviewFinding:
    file_path: str
    line_start: str
    line_end: str
    severity: Severity
    title: str
    explanation: str
    suggestion: str | None = None
    reference_ids: list[str] = field(default_factory=list)
