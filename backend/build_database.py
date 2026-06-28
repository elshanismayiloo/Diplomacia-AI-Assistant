from pathlib import Path

from backend.chunker import chunk_markdown
from backend.embeddings import embed
from backend.vector_store import collection

print("STEP 1")
KNOWLEDGE_BASE = Path("knowledge_base")


def build_database():
    print("STEP 2")
    """
    Reads all Markdown files, splits them into chunks,
    creates embeddings and stores them in ChromaDB.
    """

    # Delete previous collection contents
    try:
        existing = collection.get()

        if existing["ids"]:
            collection.delete(
                ids=existing["ids"]
            )

    except Exception:
        pass

    # Read every markdown file
    for file in KNOWLEDGE_BASE.rglob("*.md"):
        print("STEP 3")

        text = file.read_text(
            encoding="utf-8"
        )
        print("file")

        chunks = chunk_markdown(text)

        for index, chunk in enumerate(chunks):

            collection.add(
                ids=[
                    f"{file.as_posix()}::{index}"
                ],
                documents=[
                    chunk
                ],
                embeddings=[
                    embed(chunk)
                ],
                metadatas=[
                    {
                        "file": file.as_posix(),
                        "chunk": index
                    }
                ]
            )

    print("Knowledge Base indexed successfully.")


if __name__ == "__main__":
    build_database()
