from app.core.config import LLM_API_KEY, MODEL_NAME


class LLMClient:

    def __init__(self):
        self.api_key = LLM_API_KEY
        self.model_name = MODEL_NAME

    def generate(self, prompt: str) -> str:
        """
        Send a prompt to the LLM and return the response.
        """
        raise NotImplementedError