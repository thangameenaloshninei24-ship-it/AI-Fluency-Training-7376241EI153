"""Shared configuration: chooses the LLM provider and holds the lab data."""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # reads the .env file in this folder

PROVIDER = os.getenv("PROVIDER", "ollama").strip().lower()

if PROVIDER == "ollama":                      # Option A: local model, no key
    BASE_URL = "http://localhost:11434/v1"
    API_KEY = "ollama"
    MODEL = os.getenv("MODEL", "qwen2.5:1.5b")

elif PROVIDER == "groq":                      # Option B: free cloud key
    BASE_URL = "https://api.groq.com/openai/v1"
    API_KEY = os.getenv("GROQ_API_KEY")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

elif PROVIDER == "huggingface":               # Option C: free cloud key
    BASE_URL = "https://router.huggingface.co/v1"
    API_KEY = os.getenv("HF_TOKEN")
    MODEL = os.getenv("MODEL", "openai/gpt-oss-20b")

else:
    raise SystemExit(
        f"Unknown PROVIDER '{PROVIDER}'. Use ollama, groq or huggingface."
    )

if not API_KEY:
    raise SystemExit(
        f"No API key found for PROVIDER={PROVIDER}. Check your .env file."
    )

client = OpenAI(base_url=BASE_URL, api_key=API_KEY)


# Currency values in Indian Rupees
# Example values for practicing tool calling
CURRENCY_RATES = {
    "USD": 88.0,
    "KWD": 287.0
}


QUESTIONS = [
    "Which currency gives more Indian Rupees? USD or KWD"
]


def banner(system_name):
    print(f"\n=== {system_name} | provider: {PROVIDER} | model: {MODEL} ===\n")