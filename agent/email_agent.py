from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def process_email(email_text):
    prompt = f"""
You are an AI assistant that processes emails.

Extract:
- Tasks
- Priority (High, Medium, Low)
- Deadlines
- Summary

Return JSON only.

Email:
{email_text}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",  # ✅ updated working model
        contents=prompt
    )

    return response.text