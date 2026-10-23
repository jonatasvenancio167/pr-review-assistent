from pydantic import BaseModel, Field, field_validator

class ReviewRequest(BaseModel):
    diff: str = Field(
        min_length=1,
        description="Diff Git contendo as alterações que serão analisadas.",
    )

    @field_validator("diff")
    @classmethod
    def validate_diff(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("O diff não pode estar vazio.")

        return value