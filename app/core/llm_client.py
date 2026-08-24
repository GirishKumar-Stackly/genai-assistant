import time

from google import genai
from google.genai import errors
from pydantic import BaseModel

from app.core.config import LLM_API_KEY, MODEL_NAME


class LLMError(Exception):
    """Raised when an LLM request fails."""


class LLMResponse(BaseModel):
    text: str
    model: str
    latency_ms: float


class LLMClient:

    def __init__(self):
        self.api_key = LLM_API_KEY
        self.model_name = MODEL_NAME

        self.client = genai.Client(
            api_key=self.api_key
        )

    def generate(self, prompt: str) -> LLMResponse:
        """
        Send a prompt to the LLM and return a structured response.
        """

        start_time = time.perf_counter()

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )

            if not response.text:
                raise LLMError("LLM returned an empty response.")

            end_time = time.perf_counter()

            latency_ms = (end_time - start_time) * 1000

            return LLMResponse(
                text=response.text,
                model=self.model_name,
                latency_ms=latency_ms
            )

        except errors.APIError as exc:
            raise LLMError(
                f"LLM API request failed: {exc}"
            ) from exc

        except LLMError:
            raise

        except Exception as exc:
            raise LLMError(
                f"Unexpected LLM error: {exc}"
            ) from exc