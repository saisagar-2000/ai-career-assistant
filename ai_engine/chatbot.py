import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_chat_response(message):

    prompt = f"""
    You are a helpful career assistant for software engineers.

    Answer the following question clearly and concisely.

    Question:
    {message}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    return response.choices[0].message.content