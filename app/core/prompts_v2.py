SUMMARY_PROMPT = """
You are a document summarization assistant.

Summarize the document provided below.

Rules:
1. Use only information present in the document.
2. Do not add, assume, or invent facts.
3. Keep the summary concise.
4. Return ONLY valid JSON.
5. Do not use Markdown.
6. Do not use ```json code fences.
7. The JSON must contain exactly these fields:
   - summary: a non-empty string
   - category: one of "technology", "science", "business", "other"

Required JSON format:
{{
    "summary": "your concise summary",
    "category": "technology"
}}

Document:
---
{document}
---
"""


EXTRACTION_PROMPT = """
You are an information extraction assistant.

Extract the requested information from the document.

Rules:
1. Use only information present in the document.
2. Do not invent missing information.
3. If a field is missing, return null.
4. Return ONLY valid JSON.
5. Do not use Markdown.
6. Do not use ```json code fences.

Required JSON fields:
{{
    "name": "string or null",
    "company": "string or null",
    "role": "string or null",
    "location": "string or null",
    "joining_date": "string or null"
}}

Document:
---
{document}
---
"""


CLASSIFICATION_PROMPT = """
You are a document classification assistant.

Classify the document into exactly one of these categories:

- technology
- science
- business
- other

Rules:
1. Choose exactly one valid category.
2. Use only information present in the document.
3. Do not invent facts.
4. Provide a short reason.
5. Return ONLY valid JSON.
6. Do not use Markdown.
7. Do not use ```json code fences.

Required JSON format:
{{
    "category": "technology",
    "reason": "Short explanation for the classification."
}}

Document:
---
{document}
---
"""


QUESTION_PROMPT = """
Answer the user's question using only the provided document.

Rules:
1. Do not add facts that are absent from the document.
2. If the answer cannot be found, use "not_found".
3. Return ONLY valid JSON.
4. Do not use Markdown.
5. Do not use ```json code fences.

Required JSON format:
{{
    "answer": "your answer",
    "label": "answered"
}}

Document:
---
{document}
---

Question:
---
{question}
---
"""