from pathlib import Path

from backend.chat import ask_ai


SYSTEM_PROMPT = Path(
    "prompts/system_prompt.md"
).read_text(encoding="utf-8")


CONTEXT = """
Bilim Adamı fabrikalarda elde edilen geliri artırır.

Vergi Uzmanı çalışırken ödenen vergiyi azaltır.

Akademik Kariyer beceri geliştirme süresini maksimum %30 azaltabilir.
"""


QUESTION = "Bilim Adamı nedir?"


print(
    ask_ai(
        SYSTEM_PROMPT,
        CONTEXT,
        QUESTION,
    )
)
