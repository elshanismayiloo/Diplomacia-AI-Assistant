from pathlib import Path

from backend.vector_store import collection

KNOWLEDGE_BASE = Path("knowledge_base")


def build_database():

    collection.delete(where={})

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
            ]
        )

    print("Knowledge Base indexed successfully.")


if __name__ == "__main__":
    build_database()
