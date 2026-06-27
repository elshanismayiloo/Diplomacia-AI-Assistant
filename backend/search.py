from backend.embeddings import embed
from backend.vector_store import collection


def search_knowledge(
    query: str,
    limit: int = 5
) -> str:
    """
    Semantic search using ChromaDB.
    """

    results = collection.query(
        query_embeddings=[
            embed(query)
        ],
        n_results=limit
    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    return "\n\n".join(documents)
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
