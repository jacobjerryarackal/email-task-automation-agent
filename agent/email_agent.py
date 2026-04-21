import google.generativeai as genai
import os
from dotenv import load_dotenv
from agent.prompt import PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-pro")


def process_email(email_text):
    full_prompt = PROMPT + "\n\nEmail:\n" + email_text

    response = model.generate_content(full_prompt)

    return response.text