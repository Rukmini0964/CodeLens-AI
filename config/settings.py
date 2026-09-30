import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the project root
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model Name
MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.1-8b-instant"
)

# Optional settings
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "8000"))

