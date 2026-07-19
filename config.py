"""
WorkPilot AI - Configuration Settings
Central place for all constants, API settings, and app metadata.
"""

# App Metadata
APP_NAME = "WorkPilot AI"
APP_TAGLINE = "Your Admin Co-Pilot for Freelancers & Agencies"
APP_ICON = "🚀"

# AI Model Settings
AI_MODEL = "gpt-4o-mini"  # Fast, cheap, reliable
AI_TEMPERATURE_EXTRACTION = 0.1  # Strict for data extraction
AI_TEMPERATURE_STRATEGY = 0.3    # Slightly creative for emails/reports

# Time Savings Metrics (for dashboard display)
TIME_SAVINGS = {
    "auditor": {"manual_min": 45, "ai_sec": 30},
    "sow": {"manual_min": 120, "ai_sec": 15},
    "report": {"manual_min": 30, "ai_sec": 10},
    "meeting": {"manual_min": 20, "ai_sec": 15},
}

# Edge Case Thresholds
MIN_TEXT_LENGTH = 50  # Characters - below this = likely scanned image
MAX_FILE_SIZE_MB = 10

# Supported File Types
SUPPORTED_FILE_TYPES = ["pdf", "txt"]