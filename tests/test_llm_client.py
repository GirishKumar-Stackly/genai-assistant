import pytest
from unittest.mock import MagicMock, patch

from app.core.llm_client import LLMClient, LLMError


def test_llm_generate_success():
    client = LLMClient()

    mock_response = MagicMock()
    mock_response.ok = True
    mock_response.json.return_value = {
        "choices": [
            {
                "message": {
                    "content": "Generative AI creates new content."
                }
            }
        ]
    }

    with patch(
        "app.core.llm_client.requests.post",
        return_value=mock_response,
    ) as mock_post:

        result = client.generate(
            "Explain Generative AI."
        )

    assert result.text == "Generative AI creates new content."
    assert result.model == client.model_name
    assert result.latency_ms >= 0

    mock_post.assert_called_once()


def test_llm_generate_empty_response():
    client = LLMClient()

    mock_response = MagicMock()
    mock_response.ok = True
    mock_response.json.return_value = {
        "choices": [
            {
                "message": {
                    "content": ""
                }
            }
        ]
    }

    with patch(
        "app.core.llm_client.requests.post",
        return_value=mock_response,
    ):

        with pytest.raises(
            LLMError,
            match="empty response",
        ):
            client.generate(
                "Explain Generative AI."
            )


def test_llm_generate_unexpected_error():
    client = LLMClient()

    with patch(
        "app.core.llm_client.requests.post",
        side_effect=RuntimeError(
            "Something went wrong"
        ),
    ):

        with pytest.raises(
            LLMError,
            match="Unexpected LLM error",
        ):
            client.generate(
                "Explain Generative AI."
            )