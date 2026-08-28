import json

from pydantic import BaseModel, ValidationError


class OutputValidationError(Exception):
    """Raised when LLM output cannot be validated."""


def clean_json_response(response_text: str) -> str:
    text = response_text.strip()

    if text.startswith("```json"):
        text = text[7:]

    elif text.startswith("```"):
        text = text[3:]

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def validate_output(
    response_text: str,
    output_model: type[BaseModel],
) -> BaseModel:

    cleaned_text = clean_json_response(response_text)

    try:
        data = json.loads(cleaned_text)

    except json.JSONDecodeError as exc:
        raise OutputValidationError(
            f"JSON_PARSE_FAILURE: {exc}"
        ) from exc

    try:
        return output_model.model_validate(data)

    except ValidationError as exc:
        raise OutputValidationError(
            f"VALIDATION_FAILURE: {exc}"
        ) from exc