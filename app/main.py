from app.core.config import LLM_API_KEY, MODEL_NAME


def smoke_check():
    return {
        "status": "ok",
        "model": MODEL_NAME,
        "api_key_loaded": bool(LLM_API_KEY),
    }


if __name__ == "__main__":
    print(smoke_check())