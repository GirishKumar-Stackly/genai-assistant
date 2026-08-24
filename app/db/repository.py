import sqlite3
from app.db.models import Document
from app.db.database import get_connection


class DocumentRepository:

    def save(self, document: Document):
        conn = get_connection()

        conn.execute( 
            """
            INSERT OR REPLACE INTO documents
            (document_id, title, content, source_path, updated_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                document.document_id,
                document.title,
                document.content,
                document.source_path,
                document.updated_at,
            ),
        )

        conn.commit()
        conn.close()

    def get(self, document_id: str):
        conn = get_connection()

        row = conn.execute(
            """
            SELECT document_id, title, content, source_path, updated_at
            FROM documents
            WHERE document_id = ?
            """,
            (document_id,),
        ).fetchone()

        conn.close()

        if row is None:
            return None

        return Document(
            document_id=row[0],
            title=row[1],
            content=row[2],
            source_path=row[3],
            updated_at=row[4],
        )

    def get_all(self):
        conn = get_connection()

        rows = conn.execute(
            """
            SELECT document_id, title, content, source_path, updated_at
            FROM documents
            """
        ).fetchall()

        conn.close()

        return [
            Document(
                document_id=row[0],
                title=row[1],
                content=row[2],
                source_path=row[3],
                updated_at=row[4],
            )
            for row in rows
        ]
    
    def delete(self, document_id: str):
        conn = get_connection()

        conn.execute(
        """
        DELETE FROM documents
        WHERE document_id = ?
        """,
        (document_id,),
    )

        conn.commit()
        conn.close()
    