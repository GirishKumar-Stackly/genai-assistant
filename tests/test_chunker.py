from app.rag.chunker import chunk_text


def test_chunk_text_creates_chunks():
    text = "A" * 1000

    chunks = chunk_text(
        text,
        chunk_size=200,
        overlap=50,
    )

    assert len(chunks) > 1


def test_chunk_size_is_respected():
    text = "A" * 1000

    chunks = chunk_text(
        text,
        chunk_size=200,
        overlap=50,
    )

    assert all(len(chunk) <= 200 for chunk in chunks)


def test_overlap_is_present():
    text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 20

    chunks = chunk_text(
        text,
        chunk_size=100,
        overlap=20,
    )

    assert chunks[0][-20:] == chunks[1][:20]


def test_empty_text_returns_empty_list():
    result = chunk_text(
        "",
        chunk_size=200,
        overlap=50,
    )

    assert result == []


def test_invalid_chunk_size():
    try:
        chunk_text(
            "hello",
            chunk_size=0,
            overlap=0,
        )
    except ValueError:
        assert True
    else:
        assert False


def test_overlap_must_be_smaller_than_chunk_size():
    try:
        chunk_text(
            "hello",
            chunk_size=100,
            overlap=100,
        )
    except ValueError:
        assert True
    else:
        assert False