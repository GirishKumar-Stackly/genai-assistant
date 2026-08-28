import time
import requests

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

        self.base_url = "https://openrouter.ai/api/v1/chat/completions"

    def generate(self, prompt: str) -> LLMResponse:
        """
        Send a prompt to OpenRouter and return a structured response.
        """

        start_time = time.perf_counter()

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=payload,
                timeout=60,
            )

            if not response.ok:
                raise LLMError(
                    f"OpenRouter API failed: "
                    f"{response.status_code} - {response.text}"
    )

            data = response.json()

            text = data["choices"][0]["message"]["content"]

            if not text:
                raise LLMError("LLM returned an empty response.")

            end_time = time.perf_counter()

            latency_ms = (end_time - start_time) * 1000

            return LLMResponse(
                text=text,
                model=self.model_name,
                latency_ms=latency_ms,
            )

        except requests.RequestException as exc:
            raise LLMError(
                f"LLM API request failed: {exc}"
            ) from exc

        except (KeyError, IndexError, TypeError) as exc:
            raise LLMError(
                f"Invalid LLM response format: {exc}"
            ) from exc

        except LLMError:
            raise

        except Exception as exc:
            raise LLMError(
                f"Unexpected LLM error: {exc}"
            ) from exc