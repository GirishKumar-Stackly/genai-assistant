SUMMARY_PROMPT = """
Summarize the following document in a clear and concise way.

Document:

{document}
"""


EXTRACTION_PROMPT = """
Extract the following information from the document:

- name
- company
- role
- location
- joining_date

If a field is missing, return null.

Document:

{document}
"""


CLASSIFICATION_PROMPT = """
Classify the following document into exactly one category:

- technology
- science
- business
- other

Also provide a short reason.

Document:

{document}
"""