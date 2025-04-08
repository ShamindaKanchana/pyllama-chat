# ollama_connector.py
import requests
from utils.config import OLLAMA_API_URL, DEFAULT_MODEL

def get_ollama_response(prompt: str) -> str:
    response = requests.post(
        OLLAMA_API_URL,
        json={
            "model": DEFAULT_MODEL,
            "prompt": prompt,
            "stream": False  # ← Disable streaming
        }
    )
    return response.json().get("response", "Error: No response")