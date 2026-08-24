import pytest

from app.db.repository import DocumentRepository
from app.db.database import get_connection


@pytest.fixture
def repo():
    conn = get_connection()
    conn.execute("DELETE FROM documents")
    conn.commit()
    conn.close()

    return DocumentRepository()