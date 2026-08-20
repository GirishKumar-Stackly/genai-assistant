import os
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

if not LLM_API_KEY:
    raise ValueError("LLM_API_KEY is missing")

if not MODEL_NAME:
    raise ValueError("MODEL_NAME is missing")