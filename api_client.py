"""
WorkPilot AI - API Client
Configured for xAI Grok API (Fast, reliable, allows cloud hosting).
"""

import requests
import json
import re

# ⚠️ PASTE YOUR GROK API KEY INSIDE THE QUOTES BELOW
   GROK_API_KEY = "YOUR_API_KEY_HERE"  

# xAI Grok API Endpoint
API_URL = "https://api.x.ai/v1/chat/completions"

def call_ai(system_prompt: str, user_prompt: str, require_json: bool = False) -> dict:
    """
    Calls the xAI Grok API.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    if require_json:
        messages[0]["content"] += "\n\nCRITICAL: You MUST output STRICT, VALID JSON ONLY. Do not include markdown formatting (like ```json), conversational text, or explanations."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROK_API_KEY}"
    }
    
    payload = {
        "model": "grok-beta",  # You can also use "grok-2-latest"
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": 2000
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=45)
        
        if response.status_code == 401:
            return {"error": "🔑 Invalid Grok API key. Please check the key you pasted."}
        elif response.status_code == 429:
            return {"error": "⏳ Rate limit reached. Please wait a moment and try again."}
        elif response.status_code != 200:
            return {"error": f"⚠️ API Error: {response.status_code} - {response.text}"}
        
        data = response.json()
        response_text = data["choices"][0]["message"]["content"]
        
        if require_json:
            # Clean up any markdown formatting the AI might accidentally add
            response_text = response_text.strip()
            response_text = re.sub(r'^```(?:json)?\s*', '', response_text, flags=re.MULTILINE)
            response_text = re.sub(r'\s*```$', '', response_text, flags=re.MULTILINE)
            response_text = response_text.strip()
            
            try:
                return json.loads(response_text)
            except json.JSONDecodeError:
                return {"error": f"🧠 AI failed to output valid JSON. Raw output snippet: {response_text[:150]}..."}
        
        return {"response": response_text}
        
    except requests.exceptions.Timeout:
        return {"error": "⏱️ Request timed out. Please try again."}
    except requests.exceptions.RequestException as e:
        return {"error": f"🌐 Network error: {str(e)}"}