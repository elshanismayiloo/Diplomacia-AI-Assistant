from openai import OpenAI

from backend.config import (
    OPENAI_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)

client = OpenAI(api_key=OPENAI_API_KEY)


def ask_ai(system_prompt: str, context: str, question: str) -> str:
    """
    Sends a question to the OpenAI model.
    """

    response = client.responses.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        max_output_tokens=MAX_TOKENS,
        input=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": f"""
Knowledge Context

{context}

----------------------------

User Question

{question}
""",
            },
        ],
    )

    return response.output_text.strip()
