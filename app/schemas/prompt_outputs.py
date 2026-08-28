from enum import Enum

from pydantic import BaseModel, Field


class Category(str, Enum):
    TECHNOLOGY = "technology"
    SCIENCE = "science"
    BUSINESS = "business"
    OTHER = "other"


class SummaryOutput(BaseModel):
    summary: str = Field(..., min_length=1)


class ExtractionOutput(BaseModel):
    name: str | None = None
    company: str | None = None
    role: str | None = None
    location: str | None = None
    joining_date: str | None = None


class ClassificationOutput(BaseModel):
    category: Category
    reason: str = Field(..., min_length=1)