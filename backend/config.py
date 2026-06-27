import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.5"
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0.2"
    )
)

MAX_TOKENS = int(
    os.getenv(
        "MAX_TOKENS",
        "1500"
    )
)
