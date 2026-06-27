from pathlib import Path

from backend.chat import ask_ai
from backend.loader import load_knowledge_base


SYSTEM_PROMPT = Path(
    "prompts/system_prompt.md"
).read_text(encoding="utf-8")

CONTEXT = load_knowledge_base()

QUESTION = "Bilim Adamı nedir?"

print(
    ask_ai(
        SYSTEM_PROMPT,
        CONTEXT,
        QUESTION,
    )
)
