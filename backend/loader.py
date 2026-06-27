from pathlib import Path


KNOWLEDGE_BASE_DIR = Path("knowledge_base")


def load_knowledge_base() -> str:
    """
    Reads every Markdown file inside the knowledge_base directory
    and returns a single text corpus.
    """

    documents = []

    for file in sorted(KNOWLEDGE_BASE_DIR.rglob("*.md")):
        try:
            content = file.read_text(encoding="utf-8")

            documents.append(
                f"""
==============================
FILE: {file.relative_to(KNOWLEDGE_BASE_DIR)}
==============================

{content}
"""
            )

        except Exception as e:
            print(f"Cannot read {file}: {e}")

    return "\n".join(documents)
