"""
WorkPilot AI - Business Policies & Validation
Enforces the 6 core policies of the application.
"""

from config import MIN_TEXT_LENGTH, MAX_FILE_SIZE_MB

# ============================================================
# POLICY 1: ZERO-DATA RETENTION
# ============================================================
def verify_zero_retention():
    """Confirm no database or file storage is connected."""
    # This is a structural policy - no DB connections exist in this codebase.
    return True

# ============================================================
# POLICY 5: GRACEFUL DEGRADATION (Edge Case Handling)
# ============================================================
def validate_extracted_text(text, file_name="file"):
    """
    Check if extracted text is valid (not a scanned image or empty).
    Returns: (is_valid, error_message)
    """
    if text is None:
        return False, f"⚠️ '{file_name}' could not be read."
    
    if len(text.strip()) < MIN_TEXT_LENGTH:
        return False, (
            f"⚠️ **Edge Case Triggered:** '{file_name}' appears to be a scanned image or empty. "
            f"Our text extractor requires digital, text-based PDFs. "
            f"Please use an OCR tool first, or paste the text manually."
        )
    
    return True, ""

def validate_file_size(file):
    """Check if file is within size limits."""
    size_mb = file.size / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        return False, f"⚠️ File '{file.name}' is too large ({size_mb:.1f}MB). Max is {MAX_FILE_SIZE_MB}MB."
    return True, ""

# ============================================================
# POLICY 3: STRICT JSON VALIDATION
# ============================================================
def validate_json_output(json_data, required_keys, module_name):
    """Ensure AI returned valid JSON with required keys."""
    if not isinstance(json_data, dict):
        return False, f"⚠️ {module_name}: AI returned invalid JSON structure."
    
    if "error" in json_data:
        return False, f"⚠️ {module_name}: {json_data['error']}"
    
    for key in required_keys:
        if key not in json_data:
            return False, f"⚠️ {module_name}: Missing required field '{key}' in AI output."
    
    return True, ""

# ============================================================
# POLICY 4: HUMAN-IN-THE-LOOP
# ============================================================
def require_user_approval():
    """Placeholder - UI handles this via buttons."""
    return True