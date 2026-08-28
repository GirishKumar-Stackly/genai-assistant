from pathlib import Path

from app.rag.chunk_pipeline import generate_chunks


DOCUMENTS_DIR = Path("data/documents")


def test_chunks_are_generated():
    chunks = generate_chunks(
        DOCUMENTS_DIR,
        chunk_size=500,
        overlap=100,
    )

    assert len(chunks) > 0


def test_no_empty_chunks():
    chunks = generate_chunks(
        DOCUMENTS_DIR,
        chunk_size=500,
        overlap=100,
    )

    for chunk in chunks:
        assert chunk["text"].strip() != ""


def test_required_metadata_exists():
    chunks = generate_chunks(
        DOCUMENTS_DIR,
        chunk_size=500,
        overlap=100,
    )

    required_fields = {
        "chunk_id",
        "document_id",
        "title",
        "source_path",
        "updated_at",
        "chunk_index",
        "text",
    }

    for chunk in chunks:
        assert required_fields.issubset(chunk.keys())


def test_source_documents_exist():
    chunks = generate_chunks(
        DOCUMENTS_DIR,
        chunk_size=500,
        overlap=100,
    )

    for chunk in chunks:
        source_path = Path(chunk["source_path"])

        assert source_path.exists()


def test_chunk_size_is_respected():
    chunks = generate_chunks(
        DOCUMENTS_DIR,
        chunk_size=500,
        overlap=100,
    )

    for chunk in chunks:
        assert len(chunk["text"]) <= 500


def test_chunk_indexes_are_sequential():
    chunks = generate_chunks(
        DOCUMENTS_DIR,
        chunk_size=500,
        overlap=100,
    )

    documents = {}

    for chunk in chunks:
        document_id = chunk["document_id"]

        documents.setdefault(
            document_id,
            [],
        ).append(chunk["chunk_index"])

    for indexes in documents.values():
        assert indexes == list(
            range(len(indexes))
        )