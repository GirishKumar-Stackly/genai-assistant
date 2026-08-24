from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_document():
    response = client.post(
        "/documents/",
        json={
            "document_id": "API001",
            "title": "FastAPI Basics",
            "content": "FastAPI is a Python web framework.",
            "source_path": "docs/fastapi.txt",
            "updated_at": "2026-08-20T12:00:00",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Document created successfully"
    assert data["document_id"] == "API001"


def test_get_document():
    response = client.get("/documents/API001")

    assert response.status_code == 200

    data = response.json()

    assert data["document_id"] == "API001"
    assert data["title"] == "FastAPI Basics"


def test_get_missing_document():
    response = client.get("/documents/DOES_NOT_EXIST")

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Document not found"


def test_delete_document():
    response = client.delete("/documents/API001")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Document deleted successfully"
    assert data["document_id"] == "API001"


def test_get_deleted_document():
    response = client.get("/documents/API001")

    assert response.status_code == 404