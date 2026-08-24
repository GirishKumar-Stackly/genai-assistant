from fastapi import APIRouter, HTTPException

from app.db.models import Document
from app.db.repository import DocumentRepository
from app.services.document_service import DocumentService
from app.core.llm_client import LLMClient, LLMError


router = APIRouter(prefix="/documents", tags=["Documents"])


repository = DocumentRepository()
llm_client = LLMClient()

service = DocumentService(
    repository,
    llm_client
)


@router.post("/")
def create_document(document: Document):
    service.create_document(document)

    return {
        "message": "Document created successfully",
        "document_id": document.document_id,
    }


@router.get("/{document_id}")
def get_document(document_id: str):
    document = service.get_document(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return document


@router.get("/")
def get_all_documents():
    return service.get_all_documents()


@router.delete("/{document_id}")
def delete_document(document_id: str):
    document = service.get_document(document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    service.delete_document(document_id)

    return {
        "message": "Document deleted successfully",
        "document_id": document_id,
    }


@router.post("/{document_id}/summary")
def summarize_document(document_id: str):

    try:
        result = service.summarize_document(document_id)

        return {
            "document_id": document_id,
            "summary": result.text,
            "model": result.model,
            "latency_ms": result.latency_ms,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        )

    except LLMError as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc),
        )