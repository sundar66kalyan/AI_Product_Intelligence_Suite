import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-exp")

client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt: str):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text

    except ClientError as e:
        return f"Gemini API Error: {e}"

    except Exception:
        return """
Executive Summary:
Gemini quota exceeded.

Strengths:
- Analysis unavailable

Weaknesses:
- Gemini quota exceeded

Opportunities:
- Retry later

Threats:
- API limit reached
"""