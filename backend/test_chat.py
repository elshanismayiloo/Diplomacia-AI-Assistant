from pathlib import Path

from backend.chat import ask_ai
from backend.search import search_knowledge


SYSTEM_PROMPT = Path(
    "prompts/system_prompt.md"
).read_text(
    encoding="utf-8"
)

QUESTION = input("Question: ")

CONTEXT = search_knowledge(
    QUESTION
)

print()

print(
    ask_ai(
        SYSTEM_PROMPT,
        CONTEXT,
        QUESTION
    )
)
