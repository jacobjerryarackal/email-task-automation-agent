from google import genai
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Task(BaseModel):
    task: str
    priority: str
    deadline: str

class EmailDetails(BaseModel):
    tasks: list[Task]
    summary: str


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
        model="gemini-3-pro-preview",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": EmailDetails,
        },
    )

    return response.parsed