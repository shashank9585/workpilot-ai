"""
WorkPilot AI - API Client
Handles communication with apifreellm.com, including rate limit handling.
"""

import requests
import json
import re

# ⚠️ CRITICAL: Remove this hardcoded key and use st.secrets["API_KEY"] before public deployment!
API_KEY = "apf_qwy2n598j33z8p14ri8omuph" 
API_URL = "https://apifreellm.com/api/v1/chat"

def call_ai(system_prompt: str, user_prompt: str, require_json: bool = False) -> dict:
    """
    Calls the apifreellm API. 
    Combines system and user prompts into a single message string as required by the API.
    """
    # Combine prompts
    full_message = f"{system_prompt}\n\nUSER INPUT:\n{user_prompt}"
    
    if require_json:
        full_message += "\n\nCRITICAL INSTRUCTION: You MUST output STRICT, VALID JSON ONLY. Do not include any markdown formatting (like ```json), conversational text, or explanations."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "message": full_message
    }

    try:
        # Timeout set to 60s to account for free tier processing delays
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        
        # Handle Rate Limit (1 request per 20 seconds)
        if response.status_code == 429:
            return {"error": "⏳ Rate limit reached. The free API allows 1 request every 20 seconds. Please wait a moment and try again."}
        elif response.status_code == 401:
            return {"error": "🔑 Invalid API key. Please check your configuration."}
        elif response.status_code != 200:
            return {"error": f"⚠️ API Error: {response.status_code} - {response.text}"}
        
        data = response.json()
        
        if data.get("success"):
            response_text = data.get("response", "")
            
            # If we require JSON, clean it and parse it
            if require_json:
                # Remove markdown code blocks if the AI adds them anyway
                response_text = re.sub(r'^```(?:json)?\s*', '', response_text, flags=re.MULTILINE)
                response_text = re.sub(r'\s*```$', '', response_text, flags=re.MULTILINE)
                response_text = response_text.strip()
                
                try:
                    return json.loads(response_text)
                except json.JSONDecodeError:
                    return {"error": "🧠 AI failed to output valid JSON. The free model might have struggled. Please try again."}
            
            return {"response": response_text}
        else:
            return {"error": "API request failed. Please try again."}
            
    except requests.exceptions.Timeout:
        return {"error": "⏱️ Request timed out. The free tier may be experiencing high traffic. Please try again in 30 seconds."}
    except requests.exceptions.RequestException as e:
        return {"error": f"🌐 Network error: {str(e)}"}