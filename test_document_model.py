from app.db.models import Document


document = Document(
    document_id="DOC001",
    title="Python Basics",
    content="Python is a programming language.",
    source_path="docs/python.txt",
    updated_at="2026-08-20T10:00:00"
)

print(document)
print(document.model_dump())