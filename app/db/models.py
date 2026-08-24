from datetime import datetime

from pydantic import BaseModel, Field, field_validator


class Document(BaseModel):
    document_id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    source_path: str = Field(..., min_length=1)
    updated_at: datetime

    @field_validator("content")
    @classmethod
    def content_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("content cannot be empty")
        return value