import json
from datetime import datetime, timezone
from pathlib import Path

from app.rag.loader import load_documents
from app.rag.chunker import chunk_text


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DOCUMENTS_DIR = BASE_DIR / "data" / "documents"
OUTPUT_DIR = BASE_DIR / "data" / "chunks"
OUTPUT_FILE = OUTPUT_DIR / "chunks.jsonl"


def generate_chunks(
    documents_dir: Path = DOCUMENTS_DIR,
    chunk_size: int = 500,
    overlap: int = 100,
):
    """
    Load documents, split them into chunks,
    attach metadata, and return the chunk records.
    """

    documents = load_documents(documents_dir)

    chunks = []

    updated_at = datetime.now(timezone.utc).isoformat()

    for document in documents:

        filename = document["filename"]

        document_id = Path(filename).stem

        title = document.get(
            "title",
            document_id.replace("_", " ").title(),
        )

        text = document["text"]

        document_chunks = chunk_text(
            text,
            chunk_size=chunk_size,
            overlap=overlap,
        )

        for index, chunk in enumerate(document_chunks):

            chunk_record = {
                "chunk_id": f"{document_id}_{index:03d}",
                "document_id": document_id,
                "title": title,
                "source_path": str(
                    documents_dir / filename
                ),
                "updated_at": updated_at,
                "chunk_index": index,
                "text": chunk,
            }

            chunks.append(chunk_record)

    return chunks


def save_chunks(
    chunks,
    output_file: Path = OUTPUT_FILE,
):
    """
    Save chunk records as JSONL.
    """

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as file:

        for chunk in chunks:
            file.write(
                json.dumps(
                    chunk,
                    ensure_ascii=False,
                )
                + "\n"
            )


def main():

    chunks = generate_chunks()

    save_chunks(chunks)

    print("=" * 60)
    print("CHUNK PIPELINE")
    print("=" * 60)

    print(f"Documents : {len(list(DOCUMENTS_DIR.iterdir()))}")
    print(f"Chunks    : {len(chunks)}")
    print(f"Output    : {OUTPUT_FILE}")


if __name__ == "__main__":
    main()