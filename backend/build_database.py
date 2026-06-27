from pathlib import Path

from backend.embeddings import embed
from backend.vector_store import collection

KNOWLEDGE_BASE = Path("knowledge_base")


def build_database():

    try:
        collection.delete(where={})
    except Exception:
        pass

    for file in KNOWLEDGE_BASE.rglob("*.md"):

        text = file.read_text(
            encoding="utf-8"
        )

        collection.add(
            ids=[
                str(file)
            ],
            documents=[
                text
            ],
            embeddings=[
                embed(text)
            ],
            metadatas=[
                {
                    "file": str(file)
                }
            ]
        )

    print("Knowledge Base indexed successfully.")


if __name__ == "__main__":
    build_database()
