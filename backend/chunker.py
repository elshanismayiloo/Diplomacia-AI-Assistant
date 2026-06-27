from pathlib import Path


def chunk_markdown(text: str):

    chunks = []

    current = []

    for line in text.splitlines():

        if line.startswith("# ") and current:

            chunks.append(
                "\n".join(current)
            )

            current = []

        current.append(line)

    if current:

        chunks.append(
            "\n".join(current)
        )

    return chunks
