"""
WorkPilot AI - Action Engine
Handles all user-facing actions: Gmail automation, CSV export, Markdown formatting.
"""

import urllib.parse
import pandas as pd
import io
from datetime import datetime

# ============================================================
# GMAIL AUTOMATION HACK
# ============================================================
def generate_gmail_url(to_email="", subject="", body=""):
    """
    Generate a Gmail compose URL with pre-filled fields.
    User clicks button -> Gmail opens with everything ready.
    """
    base_url = "https://mail.google.com/mail/"
    params = {
        "view": "cm",
        "fs": "1",
        "to": to_email,
        "su": subject,
        "body": body
    }
    query_string = urllib.parse.urlencode(params)
    return f"{base_url}?{query_string}"

# ============================================================
# CSV EXPORT
# ============================================================
def generate_audit_csv(discrepancies, total_overcharge):
    """Generate a downloadable CSV audit report."""
    if not discrepancies:
        return None, None
    
    df = pd.DataFrame(discrepancies)
    # Add summary row
    summary_row = pd.DataFrame([{
        "item": "TOTAL OVERCHARGE",
        "overcharge": total_overcharge
    }])
    df = pd.concat([df, summary_row], ignore_index=True)
    
    csv_data = df.to_csv(index=False).encode("utf-8")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"WorkPilot_Audit_Report_{timestamp}.csv"
    
    return csv_data, filename

def generate_meeting_csv(action_items, meeting_title):
    """Generate a downloadable CSV of meeting action items."""
    if not action_items:
        return None, None
    
    df = pd.DataFrame(action_items)
    csv_data = df.to_csv(index=False).encode("utf-8")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = "".join(c for c in meeting_title if c.isalnum() or c in " -_")[:30]
    filename = f"WorkPilot_Meeting_{safe_title}_{timestamp}.csv"
    
    return csv_data, filename

# ============================================================
# MARKDOWN FORMATTERS
# ============================================================
def format_sow_markdown(sow_data):
    """Format SOW data into professional Markdown."""
    md = f"# {sow_data.get('project_title', 'Project Proposal')}\n\n"
    md += f"**Client:** {sow_data.get('client_name', 'TBD')}\n"
    md += f"**Date:** {datetime.now().strftime('%B %d, %Y')}\n\n"
    
    md += "## 📋 Project Overview\n"
    md += f"{sow_data.get('project_goal', '')}\n\n"
    
    md += "## 🎯 Deliverables\n"
    for item in sow_data.get("deliverables", []):
        md += f"- {item}\n"
    md += "\n"
    
    md += "## 📅 Timeline\n"
    md += f"{sow_data.get('timeline', 'TBD')}\n\n"
    
    md += "## 💰 Estimated Budget\n"
    md += f"{sow_data.get('estimated_budget', 'TBD')}\n\n"
    
    md += "## ✅ Key Requirements\n"
    for item in sow_data.get("key_requirements", []):
        md += f"- {item}\n"
    md += "\n"
    
    md += "## ❌ Exclusions\n"
    for item in sow_data.get("exclusions", []):
        md += f"- {item}\n"
    md += "\n"
    
    md += "## 🚀 Next Steps\n"
    for item in sow_data.get("next_steps", []):
        md += f"- {item}\n"
    
    return md

def format_report_markdown(report_data):
    """Format client status report into email-ready Markdown."""
    md = f"{report_data.get('greeting', 'Hi there,')}\n\n"
    
    wins = report_data.get("wins_section", [])
    if wins:
        md += "## ✅ Wins This Week\n"
        for item in wins:
            md += f"- {item}\n"
        md += "\n"
    
    in_progress = report_data.get("in_progress_section", [])
    if in_progress:
        md += "## 🔄 Currently In Progress\n"
        for item in in_progress:
            md += f"- {item}\n"
        md += "\n"
    
    blockers = report_data.get("blockers_section", [])
    if blockers:
        md += "## ⚠️ Blockers / Needs Attention\n"
        for item in blockers:
            md += f"- {item}\n"
        md += "\n"
    
    next_week = report_data.get("next_week_section", [])
    if next_week:
        md += "## 📅 Plans for Next Week\n"
        for item in next_week:
            md += f"- {item}\n"
        md += "\n"
    
    md += f"{report_data.get('closing', 'Best regards')}\n"
    return md

def format_meeting_markdown(meeting_data):
    """Format meeting breakdown into actionable Markdown."""
    md = f"# 📝 {meeting_data.get('meeting_title', 'Meeting Notes')}\n\n"
    md += f"**Date:** {meeting_data.get('meeting_date', 'TBD')}\n"
    
    attendees = meeting_data.get("attendees", [])
    if attendees:
        md += f"**Attendees:** {', '.join(attendees)}\n\n"
    
    decisions = meeting_data.get("key_decisions", [])
    if decisions:
        md += "## 🎯 Key Decisions Made\n"
        for item in decisions:
            md += f"- {item}\n"
        md += "\n"
    
    action_items = meeting_data.get("action_items", [])
    if action_items:
        md += "## ✅ Action Items (Today's Tasks)\n"
        for item in action_items:
            priority_emoji = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(item.get("priority", "Medium"), "🟡")
            md += f"- {priority_emoji} **{item.get('task', '')}**\n"
            md += f"  - Owner: {item.get('owner', 'TBD')} | Deadline: {item.get('deadline', 'TBD')}\n"
        md += "\n"
    
    follow_ups = meeting_data.get("follow_ups", [])
    if follow_ups:
        md += "## 📌 Follow-Ups\n"
        for item in follow_ups:
            md += f"- {item}\n"
        md += "\n"
    
    next_meeting = meeting_data.get("next_meeting")
    if next_meeting:
        md += f"## 📅 Next Meeting: {next_meeting}\n"
    
    return md