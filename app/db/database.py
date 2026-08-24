import sqlite3


DATABASE_PATH = "documents.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)

def create_tables():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            document_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            source_path TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()