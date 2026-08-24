from fastapi import FastAPI

from app.api.documents import router as document_router


app = FastAPI(
    title="GenAI Assistant",
    description="Document management API",
    version="1.0.0",
)


app.include_router(document_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }