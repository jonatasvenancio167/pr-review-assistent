import re
from dataclasses import dataclass

from app.domain.entities.changed_line import ChangedLine
from app.domain.enum.change_type import ChangeType

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
            old_count=int(match.group("old_count") or "1"),
            new_start=int(match.group("new_start")),
            new_count=int(match.group("new_count") or "1")
        )

    def analyze(self, diff: str) -> list[ChangedLine]:
        if not diff.strip():
            raise ValueError('O diff não pode estar vazio.')

        lines = diff.splitlines()

        header = self.parse_hunk_header(lines[0])

        old_line = header.old_start
        new_line = header.new_start

        changes: list[ChangedLine] = []

        for line in lines[1:]:
            if line == r"\ No newline at end of file":
                continue

            if line.startswith("@@"):
                raise ValueError(
                    "Esta versão aceita apenas um bloco de alterações."
                )

            if not line:
                raise ValueError(
                    "Uma linha do bloco deve começar com espaço, + ou -."
                )

            prefix = line[0]
            content = line[1:]

            if prefix == " ":
                old_line += 1
                new_line += 1

            elif prefix == '-':
                changes.append(
                    ChangedLine(
                        content=content,
                        change_type=ChangeType.removed,
                        old_line_number=old_line,
                        new_line_number=None,
                    )
                )
                old_line += 1

            elif prefix == '+':
                changes.append(
                    ChangedLine(
                        content=content,
                        change_type=ChangeType.added,
                        old_line_number=None,
                        new_line_number=new_line,
                    )
                )

                new_line += 1

            else:
                raise ValueError(
                    f"Prefixo de linha inválido: {prefix!r}"
                )

        if (
            old_line - header.old_start != header.old_count
            or new_line - header.new_start != header.new_count
        ):
            raise ValueError(
                "A quantidade de linhas não corresponde ao cabeçalho."
            )

        return changes
