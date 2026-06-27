from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

embedding_model = SentenceTransformer(MODEL_NAME)


def embed(text: str):
    """
    Returns embedding vector for a text.
    """
    return embedding_model.encode(
        text,
        convert_to_numpy=True
    ).tolist()
