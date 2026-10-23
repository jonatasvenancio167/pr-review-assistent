import re
from dataclasses import dataclass

@dataclass(frozen=True)
class HunkHeader:
    old_start: int
    old_count: int
    new_start: int
    new_count: int

class CodeAnalysisService:
    def parse_hunk_header(self, line: str) -> HunkHeader:
        pattern = (
            r"^@@ -(?P<old_start>\d+)(?:,(?P<old_count>\d+))?"
            r" \+(?P<new_start>\d+)(?:,(?P<new_count>\d+))? @@"
        )

        match = re.match(pattern, line)

        if match is None:
            raise ValueError("Cabeçalho de alterações inválido.")

        return HunkHeader(
            old_start=int(match.group("old_start")),
            old_count=int(match.group("old_start") or "1"),
            new_start=int(match.group("new_start")),
            new_count=int(match.group("new_count") or "1")
        )