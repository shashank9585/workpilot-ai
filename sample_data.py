"""
WorkPilot AI - Sample Data
Embedded sample datasets so users can instantly test the tool.
"""

# ============================================================
# SAMPLE 1: Financial Audit (Contract vs Invoice)
# ============================================================
SAMPLE_CONTRACT_TXT = """
SERVICE AGREEMENT
Client: Acme Corp
Vendor: DesignPro Studio
Date: January 15, 2026

SCOPE OF WORK & RATES:
1. Web Development - $50/hour
2. UI/UX Design - $75/hour  
3. SEO Optimization - $40/hour
4. Content Writing - $30/hour

PROJECTED HOURS (Q1 2026):
- Web Development: 40 hours
- UI/UX Design: 20 hours
- SEO Optimization: 15 hours
- Content Writing: 10 hours

PAYMENT TERMS: Net 30 days from invoice date.
"""

SAMPLE_INVOICE_TXT = """
INVOICE #2026-0042
From: DesignPro Studio
To: Acme Corp
Date: March 31, 2026

LINE ITEMS:
1. Web Development Services
   Rate: $65/hour
   Hours: 40
   Subtotal: $2,600

2. UI/UX Design Services
   Rate: $75/hour
   Hours: 20
   Subtotal: $1,500

3. SEO Optimization
   Rate: $45/hour
   Hours: 15
   Subtotal: $675

4. Content Writing
   Rate: $30/hour
   Hours: 10
   Subtotal: $300

TOTAL DUE: $5,075
Payment Terms: Net 30
"""

# ============================================================
# SAMPLE 2: SOW Generator (Messy Discovery Call Notes)
# ============================================================
SAMPLE_DISCOVERY_NOTES_TXT = """
Call with Sarah Chen - TechStart Inc
Date: July 15, 2026

Notes:
- They're a B2B SaaS startup, Series A, ~50 employees
- Need complete website redesign, current site is 5 years old
- Main goal: improve lead conversion (currently 1.2%, want 3%+)
- Key pages: Homepage, Pricing, Features, Blog, Contact, Demo booking
- Must integrate with HubSpot for lead capture
- Timeline: want it live by end of September (so ~10 weeks)
- Budget: mentioned $15k-$20k range, flexible for quality
- Design style: clean, modern, similar to Linear or Notion
- Need mobile-first approach, 60% of traffic is mobile
- Content: they'll provide copy, we do design + dev
- SEO basics included, no ongoing marketing
- Exclusions: no mobile app, no custom backend integrations beyond HubSpot
- Next steps: send proposal by Friday, schedule follow-up next Tuesday
- Decision maker: Sarah (CEO) + Mike (CTO)
"""

# ============================================================
# SAMPLE 3: Client Status Report (Rough Notes)
# ============================================================
SAMPLE_WEEKLY_NOTES_TXT = """
TechStart Project - Week 3 Update (for Sarah/Mike)

DONE:
- Homepage wireframes approved
- Color palette and typography finalized
- HubSpot integration tested successfully
- Blog template built

IN PROGRESS:
- Pricing page design (80% done)
- Mobile responsive testing
- Content migration from old site

BLOCKERS:
- Waiting on final product screenshots from their team (asked 3x)
- Need approval on homepage copy before we can finalize

NEXT WEEK:
- Finish pricing page
- Start features page
- Begin frontend development
- Demo booking page design

NOTE: They seemed happy with progress, just need to nudge them on the screenshots.
"""

# ============================================================
# SAMPLE 4: Meeting Breakdown (Transcript)
# ============================================================
SAMPLE_MEETING_NOTES_TXT = """
Sprint Planning Meeting - July 18, 2026
Attendees: You, Sarah Chen, Mike (CTO), Priya (Designer)

DISCUSSION:
- Reviewed last week's progress
- Sarah wants to launch blog by August 1st
- Mike raised concern about HubSpot form styling
- Priya showed new pricing page mockups, approved with minor tweaks
- Discussed SEO strategy for launch

DECISIONS MADE:
- Blog launch moved to August 5th (need more time for content)
- HubSpot forms will use custom CSS (Priya to handle)
- Going with Option B for pricing page layout

ACTION ITEMS:
- You: Finish pricing page frontend by Wednesday
- Priya: Update pricing page mockups by tomorrow EOD
- Sarah: Send final product screenshots by Tuesday
- Mike: Provide HubSpot API credentials by Monday
- You: Draft blog launch announcement email

FOLLOW UPS:
- Check in with Sarah on screenshot status Monday
- Confirm Mike has sent API creds

NEXT MEETING: Thursday July 24, 2026 at 2 PM IST
"""

# ============================================================
# HELPER: Create downloadable sample files
# ============================================================
def get_sample_file_content(sample_type):
    """Return the text content for a given sample type."""
    samples = {
        "contract": ("Sample_Contract.txt", SAMPLE_CONTRACT_TXT),
        "invoice": ("Sample_Invoice.txt", SAMPLE_INVOICE_TXT),
        "discovery": ("Sample_Discovery_Call_Notes.txt", SAMPLE_DISCOVERY_NOTES_TXT),
        "weekly": ("Sample_Weekly_Notes.txt", SAMPLE_WEEKLY_NOTES_TXT),
        "meeting": ("Sample_Meeting_Notes.txt", SAMPLE_MEETING_NOTES_TXT),
    }
    return samples.get(sample_type, ("", ""))