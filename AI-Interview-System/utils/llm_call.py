import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
import json

import json

def parse_json_response(response):
    try:
        # Remove exact triple backtick code fences if present
        if response.startswith("```json"):
            response = response[len("```json"):]

        if response.endswith("```"):
            response = response[:-3]

        # Also strip whitespace from ends
        response = response.strip()

        return json.loads(response)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        print("LLM response parsing failed. Raw response was:")
        print(response)
        return None


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not set in environment variables")

genai.configure(api_key=GOOGLE_API_KEY)

def get_response_from_llm(prompt: str) -> str:
    """
    Call Gemini 2.0 Flash model and get response.

    Args:
        prompt (str): The prompt string.

    Returns:
        str: Response text from Gemini.
    """
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini API: {e}"
