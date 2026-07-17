# AI/json_parser.py

import json


# -------------------------------------------------
# CLEAN THE AI RESPONSE
# -------------------------------------------------

def clean_response(ai_response):

    # Remove markdown if present
    ai_response = ai_response.replace("```json", "")
    ai_response = ai_response.replace("```", "")

    # Remove leading and trailing spaces
    ai_response = ai_response.strip()

    return ai_response


# -------------------------------------------------
# PARSE JSON RESPONSE
# -------------------------------------------------

def parse_ai_response(ai_response):

    try:

        # Clean the response
        cleaned_response = clean_response(ai_response)

        # Convert JSON string into Python dictionary
        data = json.loads(cleaned_response)

        return data

    except json.JSONDecodeError as e:

        print("\nJSON Parsing Error:\n")
        print(e)

        return None

    except Exception as e:

        print("\nUnexpected Error:\n")
        print(e)

        return None