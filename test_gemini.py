import os
from dotenv import load_dotenv
from google import genai

# Load configuration
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print(f"--- API Key Diagnostic ---")
print(f"API Key Found in .env: {'YES' if api_key else 'NO'}")
if api_key:
    print(f"Key Starts With: {api_key[:5]}...")

print("\n--- Testing Connection to Gemini ---")
try:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Hello Gemini! Confirm if you can read this message clearly.",
    )
    print("[SUCCESS] Gemini responded successfully!")
    print(f"Response text: {response.text}")
except Exception as e:
    print("[ERROR] Connection to Gemini shattered!")
    print(f"Error Message: {str(e)}")