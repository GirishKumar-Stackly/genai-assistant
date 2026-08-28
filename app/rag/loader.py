from pathlib import Path


SUPPORTED_EXTENSIONS = {".txt", ".md"}


def load_document(file_path: Path) -> str:
    """
    Load a single text or Markdown document.
    """

    if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {file_path.suffix}"
        )

    return file_path.read_text(
        encoding="utf-8"
    )


def load_documents(folder_path: Path) -> list[dict]:
    """
    Load all supported documents from a folder.
    """

    documents = []

    for file_path in sorted(folder_path.iterdir()):

        if not file_path.is_file():
            continue

        if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        text = load_document(file_path)
        text = clean_text(text)

        documents.append(
            {
                "source_path": str(file_path),
                "filename": file_path.name,
                "text": text,
            }
        )

    return documents

def clean_text(text: str) -> str:
    """
    Normalize whitespace while preserving meaningful Markdown headings.
    """

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)