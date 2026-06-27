from pathlib import Path

KNOWLEDGE_BASE_DIR = Path("knowledge_base")


def search_knowledge(query: str, limit: int = 5) -> str:
    """
    Very simple keyword search.
    Returns the most relevant markdown documents.
    """

    query = query.lower()

    results = []

    for file in KNOWLEDGE_BASE_DIR.rglob("*.md"):

        text = file.read_text(
            encoding="utf-8"
        )

        score = text.lower().count(query)

        if score > 0:
            results.append(
                (
                    score,
                    file,
                    text
                )
            )

    results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    context = []

    for score, file, text in results[:limit]:

        context.append(
            f"""
======================
{file.name}
======================

{text}
"""
        )

    return "\n".join(context)
