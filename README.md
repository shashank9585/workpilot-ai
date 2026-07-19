# 🚀 WorkPilot AI

**Your Admin Co-Pilot for Freelancers & Agencies**

WorkPilot AI is a modular workspace that automates the boring administrative tasks freelancers and agency owners face every week. Built with real engineering, strict policies, and actionable outputs.

## 🎯 The Problem
Freelancers waste 10+ hours every week on administrative busywork:
- Manually checking vendor invoices against contracts
- Writing proposals from messy call notes
- Polishing rough notes into professional client updates
- Extracting action items from meeting transcripts

## 💡 The Solution
WorkPilot AI provides 4 specialized modules in one workspace:

1. **💰 Financial Auditor** - Catches invoice overcharges with 100% accuracy
2. **📝 SOW Generator** - Turns messy notes into professional proposals
3. **📧 Client Report** - Polishes rough notes into client-ready updates
4. **📅 Meeting Breakdown** - Extracts today's tasks from meeting notes

## 🛡️ Core Policies (What Makes This Real)

1. **Zero-Data Retention** - All files processed in-memory, wiped instantly
2. **AI Extracts, Python Calculates** - AI is forbidden from doing math (prevents hallucinations)
3. **Strict JSON Schema** - No conversational filler during extraction
4. **Human-in-the-Loop** - User reviews & approves before any action
5. **Graceful Degradation** - Catches scanned images, empty files, bad formats
6. **Sample Data Fallback** - Instant testing with embedded sample files

## 🚀 How It's Different From ChatGPT

| ChatGPT | WorkPilot AI |
|---------|--------------|
| User writes complex prompts | Zero prompts - just upload/paste |
| AI does the math (hallucinates) | Python does the math (100% accurate) |
| Outputs messy text | Outputs structured tables + CSVs |
| Says "you should email..." | Opens Gmail with pre-filled email |
| One-time use | Used every Monday, Wednesday, Friday |

## 🛠️ Tech Stack

- **Frontend:** Streamlit (Python)
- **AI Engine:** OpenAI API (gpt-4o-mini with strict JSON mode)
- **PDF Parsing:** pdfplumber
- **Data Logic:** pandas
- **Hosting:** Streamlit Community Cloud

## 📦 File Structure
