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
            from backend.chunker import chunk_markdown

...

chunks = chunk_markdown(text)

for i, chunk in enumerate(chunks):

    collection.add(

        ids=[
            f"{file}_{i}"
        ],

        documents=[
            chunk
        ],

        embeddings=[
            embed(chunk)
        ],

        metadatas=[
            {
                "file": str(file),
                "chunk": i
            }
        ]
    )
    )

    print("Knowledge Base indexed successfully.")


if __name__ == "__main__":
    build_database()
