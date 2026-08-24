from app.db.models import Document
from app.db.repository import DocumentRepository
from app.core.llm_client import LLMClient
from app.core.prompts import SUMMARY_PROMPT


class DocumentService:

    def __init__(
        self,
        repository: DocumentRepository,
        llm_client: LLMClient | None = None
    ):
        self.repository = repository
        self.llm_client = llm_client

    def create_document(self, document: Document):
        self.repository.save(document)

    def get_document(self, document_id: str):
        return self.repository.get(document_id)

    def get_all_documents(self):
        return self.repository.get_all()

    def delete_document(self, document_id: str):
        self.repository.delete(document_id)

    def summarize_document(self, document_id: str):

        if self.llm_client is None:
            raise RuntimeError("LLM client is not configured")

        document = self.repository.get(document_id)

        if document is None:
            raise ValueError("Document not found")

        prompt = SUMMARY_PROMPT.format(
            document=document.content
        )

        return self.llm_client.generate(prompt)