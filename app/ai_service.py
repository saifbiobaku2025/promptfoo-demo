from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def ask_support_bot(question: str) -> str:

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
You are a customer support assistant.

Question:
{question}
"""
    )

    return response.text