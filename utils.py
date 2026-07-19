"""
WorkPilot AI - Utility Functions
Handles file reading, text extraction, and basic data operations.
"""

import pdfplumber
import io

def extract_text_from_file(file) -> str:
    """
    Extract text from PDF or TXT file.
    Returns clean text string.
    """
    if file is None:
        return ""
    
    try:
        if file.type == "application/pdf":
            with pdfplumber.open(file) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                return text
        else:
            # TXT or other text file
            return file.read().decode("utf-8")
    except Exception as e:
        return f"ERROR: Could not read file - {str(e)}"

def extract_text_from_multiple_files(files) -> str:
    """Extract and combine text from multiple files."""
    combined_text = ""
    for file in files:
        combined_text += f"\n\n--- FILE: {file.name} ---\n\n"
        combined_text += extract_text_from_file(file)
    return combined_text

def safe_json_parse(json_string):
    """Safely parse JSON string, return dict or None."""
    import json
    try:
        return json.loads(json_string)
    except:
        return None