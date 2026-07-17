# AI/ai_engine.py

from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv
import os
import time

from AI.prompts import MASTER_PROMPT
# Import local_ai_consultant for hybrid offline architecture
from AI.local_ai_consultant import local_ai_consultant

# -------------------------------------------------
# LOAD API KEY
# -------------------------------------------------
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# -------------------------------------------------
# CREATE GEMINI CLIENT
# -------------------------------------------------
try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    print(f"\n[!] Failed to initialize Gemini Client: {e}")
    client = None

# -------------------------------------------------
# GENERATE AI RESPONSE (WITH COMPREHENSIVE FALLBACK)
# -------------------------------------------------
def generate_ai_response(
    information,
    energy,
    faults,
    sustainability,
    recommendation,
    retries=2,
    delay=2
):
    """
    Generates content using the default Gemini 2.5 Flash endpoint using reports
    passed from the multi-agent system.
    """
    
    if not client:
        print("\n[!] Gemini Client missing. Forcing Offline Engine.")
        return local_ai_consultant(information, energy, faults, sustainability, recommendation)
    
    # Construct the structural report prompt from the multi-agent outputs
    analysis_report = f"""
ENERGY ANALYSIS REPORT
-------------------------------------------------
Electricity Bill:
{information}

-------------------------------------------------
ENERGY ANALYSIS:
{energy}

-------------------------------------------------
FAULT DETECTION:
{faults}

-------------------------------------------------
SUSTAINABILITY ANALYSIS:
{sustainability}

-------------------------------------------------
RECOMMENDATIONS:
{recommendation}

-------------------------------------------------
Please act as an AI Energy and Sustainability Consultant.
"""

    full_prompt = MASTER_PROMPT + analysis_report

    for attempt in range(retries):
        try:
            print(f"\n[~] Attempting to contact Gemini API (Attempt {attempt + 1})...")
            # Generate content using the new release endpoint mapping
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=full_prompt
            )
            
            if response.text and not response.text.startswith("Error"):
                print("[+] Gemini API Call Successful!")
                return response.text
                
        except APIError as e:
            print(f"\n[!] Gemini API Error Code {e.code}: {e.message}")
            if e.code == 429 and attempt < retries - 1:
                print(f"[~] Rate limit hit. Retrying in {delay * (attempt + 1)} seconds...")
                time.sleep(delay * (attempt + 1))
                continue
            
            print("[!] API limit reached. Triggering Offline Engine.")
            return local_ai_consultant(information, energy, faults, sustainability, recommendation)
            
        except Exception as e:
            print(f"\n[!] Unexpected Gemini Error: {str(e)}")
            print("[!] Triggering Offline Engine.")
            return local_ai_consultant(information, energy, faults, sustainability, recommendation)

    # Final Catch-all in case the logic exits loop conditions safely
    return local_ai_consultant(information, energy, faults, sustainability, recommendation)