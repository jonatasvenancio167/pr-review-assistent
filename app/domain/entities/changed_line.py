from dataclasses import dataclass

from app.domain.enum.change_type import ChangeType

@dataclass(frozen=True)
class ChangedLine:
    content: str
    change_type: ChangeType
    old_line_number: int | None
    new_line_number: int | None