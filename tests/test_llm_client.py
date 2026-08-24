import pytest
from unittest.mock import MagicMock

from app.core.llm_client import LLMClient, LLMError


def test_llm_generate_success():
    client = LLMClient()

    mock_response = MagicMock()
    mock_response.text = "Generative AI creates new content."

    client.client.models.generate_content = MagicMock(
        return_value=mock_response
    )

    result = client.generate(
        "Explain Generative AI."
    )

    assert result.text == "Generative AI creates new content."
    assert result.model == client.model_name
    assert result.latency_ms >= 0


def test_llm_generate_empty_response():
    client = LLMClient()

    mock_response = MagicMock()
    mock_response.text = ""

    client.client.models.generate_content = MagicMock(
        return_value=mock_response
    )

    with pytest.raises(LLMError, match="empty response"):
        client.generate(
            "Explain Generative AI."
        )


def test_llm_generate_unexpected_error():
    client = LLMClient()

    client.client.models.generate_content = MagicMock(
        side_effect=RuntimeError("Something went wrong")
    )

    with pytest.raises(LLMError, match="Unexpected LLM error"):
        client.generate(
            "Explain Generative AI."
        )