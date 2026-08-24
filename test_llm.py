from app.core.llm_client import LLMClient


client = LLMClient()

result = client.generate(
    "Explain Generative AI in one simple sentence."
)

print("Response:",result.text)
print("Model:",result.model)
print("Latency:",result.latency_ms,"ms")