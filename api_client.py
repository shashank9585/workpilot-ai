"""
WorkPilot AI - API Client
Now using AINative Studio API (Free, allows cloud hosting, OpenAI-compatible)
Get your free API key at: https://ainative.studio/free-llm-api
"""

import requests
import json
import re

# ⚠️ CRITICAL: Replace with your AINative Studio API Key
# Get it free at: https://ainative.studio/free-llm-api
API_KEY = "e2137fe5-d9f1-4b76-955f-624eab799673" 
API_URL = "https://api.ainative.studio/v1/chat/completions"

def call_ai(system_prompt: str, user_prompt: str, require_json: bool = False) -> dict:
    """
    Calls the AINative Studio Chat Completion API.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    if require_json:
        messages[0]["content"] += "\n\nCRITICAL: You MUST output STRICT, VALID JSON ONLY. No markdown, no explanations."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "model": "llama-3.3-70b",  # Free, fast, reliable model on AINative
        "messages": messages,
        "temperature": 0.1,
        "max_tokens": 2000
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 401:
            return {"error": "🔑 Invalid API key. Get a free key at https://ainative.studio/free-llm-api"}
        elif response.status_code == 429:
            return {"error": "⏳ Rate limit reached. Please wait a moment and try again."}
        elif response.status_code != 200:
            return {"error": f"⚠️ API Error: {response.status_code} - {response.text}"}
        
        data = response.json()
        response_text = data["choices"][0]["message"]["content"]
        
        if require_json:
            # Clean up any markdown formatting the AI might add
            response_text = response_text.strip()
            response_text = re.sub(r'^```(?:json)?\s*', '', response_text, flags=re.MULTILINE)
            response_text = re.sub(r'\s*```$', '', response_text, flags=re.MULTILINE)
            response_text = response_text.strip()
            
            try:
                return json.loads(response_text)
            except json.JSONDecodeError:
                return {"error": "🧠 AI failed to output valid JSON. Please try again."}
        
        return {"response": response_text}
        
    except requests.exceptions.Timeout:
        return {"error": "⏱️ Request timed out. Please try again."}
    except requests.exceptions.RequestException as e:
        return {"error": f"🌐 Network error: {str(e)}"}