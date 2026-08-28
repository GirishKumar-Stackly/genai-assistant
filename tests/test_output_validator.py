import pytest

from app.schemas.prompt_outputs import (
    SummaryOutput,
    ClassificationOutput,
)
from app.services.output_validator import (
    OutputValidationError,
    validate_output,
)


def test_valid_summary_output():
    response = """
    {
        "summary": "Python is a programming language."
    }
    """

    result = validate_output(
        response,
        SummaryOutput,
    )

    assert isinstance(result, SummaryOutput)
    assert result.summary == "Python is a programming language."


def test_invalid_json_output():
    response = """
    This is not valid JSON.
    """

    with pytest.raises(OutputValidationError, match="JSON_PARSE_FAILURE"):
        validate_output(
            response,
            SummaryOutput,
        )


def test_invalid_classification_output():
    response = """
    {
        "category": "finance",
        "reason": "This is a finance document."
    }
    """

    with pytest.raises(
        OutputValidationError,
        match="VALIDATION_FAILURE",
    ):
        validate_output(
            response,
            ClassificationOutput,
        )