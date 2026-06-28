from pathlib import Path

from google.genai import types

from backend.config import (
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS
)

from backend.gemini_client import client
from backend.search import search_knowledge


SYSTEM_PROMPT = Path(
    "prompts/system_prompt.md"
).read_text(
    encoding="utf-8"
)


def ask(question: str):

    context = search_knowledge(question)

    prompt = f"""
Knowledge Corpus

{context}

------------------------

User Question

{question}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=TEMPERATURE,
            max_output_tokens=MAX_TOKENS
        ),
        contents=prompt
    )

    return response.text
