from pathlib import Path

from app.rag.loader import (
    load_document,
    load_documents,
    clean_text,
)


DOCUMENTS_DIR = Path("data/documents")


def test_load_documents():
    documents = load_documents(DOCUMENTS_DIR)

    assert len(documents) == 5


def test_supported_files_are_loaded():
    documents = load_documents(DOCUMENTS_DIR)

    filenames = {
        document["filename"]
        for document in documents
    }

    assert "python.md" in filenames
    assert "fastapi.md" in filenames
    assert "sql.md" in filenames


def test_clean_text_removes_empty_lines():
    text = """
    # Python


    Python is a programming language.


    ## Features
    """

    cleaned = clean_text(text)

    assert cleaned == (
        "# Python\n"
        "Python is a programming language.\n"
        "## Features"
    )


def test_clean_text_preserves_headings():
    text = """
    # Python

    ## Features

    Python has a simple syntax.
    """

    cleaned = clean_text(text)

    assert "# Python" in cleaned
    assert "## Features" in cleaned


def test_load_single_document():
    file_path = DOCUMENTS_DIR / "python.md"

    text = load_document(file_path)

    assert "# Python" in text
    assert "programming language" in text