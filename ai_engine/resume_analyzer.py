import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(text):

    prompt = f"""
    You are a career coach.

Analyze the following resume and respond in this format and limit to 300 words:

Strengths:
- bullet points

Weaknesses:
- bullet points

Missing Skills:
- bullet points

Suggestions:
- bullet points

    Resume:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content