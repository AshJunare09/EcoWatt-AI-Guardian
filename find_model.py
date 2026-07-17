import os
from dotenv import load_dotenv
from google import genai

# Load configuration
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("--- Fetching Available Google AI Models ---")
try:
    client = genai.Client(api_key=api_key)
    models = client.models.list()
    
    found_flash = False
    for model in models:
        # We only want to see the fast 'flash' models
        if "flash" in model.name.lower():
            print(f"✅ Active Flash Model Name: {model.name}")
            found_flash = True
            
    if not found_flash:
        print("⚠️ No 'flash' models found. Printing ALL available models instead:")
        for model in models:
            print(f"- {model.name}")
            
except Exception as e:
    print(f"[ERROR] Could not fetch models: {str(e)}")