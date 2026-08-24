from app.core.llm_client import LLMClient
from app.core.prompts import SUMMARY_PROMPT


client = LLMClient()

document = """
Generative AI is a branch of artificial intelligence that can create
new content such as text, images, audio, video and code.
It uses machine learning models trained on large datasets.
"""

prompt = SUMMARY_PROMPT.format(
    document=document
)

result = client.generate(prompt)

print("Summary:")
print(result.text)

print("\nModel:", result.model)
print("Latency:", result.latency_ms, "ms")