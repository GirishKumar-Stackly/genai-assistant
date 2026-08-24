from datetime import datetime
from unittest.mock import MagicMock
from app.db.models import Document
from app.services.document_service import DocumentService


def create_document():
    return Document(
        document_id="DOC001",
        title="Python Basics",
        content="Python is a programming language.",
        source_path="docs/python.txt",
        updated_at=datetime(2026, 8, 20, 10, 0),
    )


def test_create_and_get_document(repo):
    service = DocumentService(repo)

    document = create_document()

    service.create_document(document)

    result = service.get_document("DOC001")

    assert result is not None
    assert result.document_id == "DOC001"
    assert result.title == "Python Basics"


def test_get_all_documents(repo):
    service = DocumentService(repo)

    document = create_document()

    service.create_document(document)

    documents = service.get_all_documents()

    assert len(documents) >= 1
    assert documents[0].document_id == "DOC001"


def test_delete_document(repo):
    service = DocumentService(repo)

    document = create_document()

    service.create_document(document)
    service.delete_document("DOC001")

    result = service.get_document("DOC001")

    assert result is None

def test_summarize_document(repo):
    llm_client = MagicMock()

    llm_client.generate.return_value = "Python is a programming language."

    service = DocumentService(repo, llm_client)

    document = create_document()
    service.create_document(document)

    result = service.summarize_document("DOC001")

    assert result == "Python is a programming language."

    llm_client.generate.assert_called_once()