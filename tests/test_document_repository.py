from datetime import datetime

from app.db.models import Document


def create_document():
    return Document(
        document_id="DOC001",
        title="Python Basics",
        content="Python is a programming language.",
        source_path="docs/python.txt",
        updated_at=datetime(2026, 8, 20, 10, 0),
    )


def test_save_and_get_document(repo):
    document = create_document()

    repo.save(document)

    result = repo.get("DOC001")

    assert result is not None
    assert result.document_id == "DOC001"
    assert result.title == "Python Basics"


def test_get_missing_document(repo):
    result = repo.get("DOES_NOT_EXIST")

    assert result is None


def test_get_all_documents(repo):
    document = create_document()

    repo.save(document)

    documents = repo.get_all()

    assert len(documents) >= 1
    assert documents[0].document_id == "DOC001"

def test_update_document(repo):
    document = create_document()

    repo.save(document)

    updated_document = Document(
        document_id="DOC001",
        title="Advanced Python",
        content="Python is a powerful programming language.",
        source_path="docs/python.txt",
        updated_at=datetime(2026, 8, 20, 11, 0),
    )

    repo.save(updated_document)

    result = repo.get("DOC001")

    assert result is not None
    assert result.title == "Advanced Python"
    assert result.content == "Python is a powerful programming language."

def test_delete_document(repo):
    document = create_document()

    repo.save(document)

    repo.delete("DOC001")

    result = repo.get("DOC001")

    assert result is None