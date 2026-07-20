<div align="center">

# 🚀 WorkPilot AI

### The AI Operations Workspace for Freelancers & Agencies

**From Documents to Decisions. From Notes to Action.**

WorkPilot AI is a modular AI workspace that transforms contracts, invoices, meeting notes, emails, and project discussions into actionable business outputs.

<br>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)]()
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)]()
[![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()

<br>

### 🌐 Live Demo

**https://workpilot-ai-6dsby5ksu9fp6d4rj3m6wz.streamlit.app/**

> 🚀 **No setup required — Open the app, try the built-in sample datasets, and explore every workflow instantly.**

---

⭐ **If you like this project, consider giving it a Star on GitHub!**

</div>

---

# 📖 Overview

Freelancers and agency owners spend hours every week on repetitive administrative work.

Instead of delivering projects, they're reviewing invoices, writing proposals, preparing client updates, and organizing meeting notes.

Most AI assistants generate text.

**WorkPilot AI generates completed work.**

Instead of writing prompts, users simply choose a workflow, upload their files (or use built-in sample data), review the extracted information, and receive professional business outputs ready to download or send.

---

# ✨ Features

## 💰 Financial Auditor

Compare contracts against invoices and instantly detect billing discrepancies.

**Outputs**

- ✅ Invoice Audit Report
- ✅ Overcharge Detection
- ✅ CSV Export
- ✅ Gmail Dispute Draft

---

## 📝 Scope of Work Generator

Turn messy client discovery notes into professional proposals.

**Outputs**

- ✅ Scope of Work
- ✅ Proposal Draft
- ✅ Markdown Export
- ✅ Copy to Clipboard

---

## 📧 Client Reports

Transform rough weekly notes into polished client-ready updates.

**Outputs**

- ✅ Professional Email
- ✅ Weekly Report
- ✅ Wins & Risks Summary
- ✅ Next Steps

---

## 📅 Meeting Breakdown

Extract structured action items from meeting transcripts.

**Outputs**

- ✅ Tasks
- ✅ Owners
- ✅ Deadlines
- ✅ Meeting Summary

---

# ⚙️ How It Works

```text
               Upload Documents
        (PDF • TXT • Notes • CSV)
                     │
                     ▼
          Universal File Parser
                     │
                     ▼
      AI Extraction Engine (JSON)
                     │
                     ▼
     Python Validation & Processing
      • Calculations
      • Formatting
      • Validation
                     │
                     ▼
            Action Engine
   CSV • Markdown • Gmail • Reports
```

---

# 🧠 Engineering Philosophy

WorkPilot AI separates **AI Intelligence** from **Business Logic**.

Instead of letting AI perform calculations or make business decisions:

- 🤖 AI extracts structured information
- 🐍 Python validates every calculation
- 👤 Users approve every action
- 📄 Outputs are deterministic and structured

This significantly reduces hallucinations while producing predictable, business-ready results.

---

# 🔒 Privacy & Safety

WorkPilot AI is designed around privacy-first principles.

- ✅ Zero Data Retention
- ✅ Files processed entirely in memory
- ✅ No database
- ✅ No logging
- ✅ Human-in-the-loop approval
- ✅ Strict JSON validation
- ✅ AI never performs calculations
- ✅ AI never sends emails automatically
- ✅ Graceful handling of invalid files

---

# 📦 Sample Workspace

Don't have documents?

No problem.

WorkPilot AI includes downloadable sample datasets so anyone can test the complete experience within minutes.

Included samples:

### 💰 Financial

- Vendor Contract
- Vendor Invoice
- Expected Audit Result

### 📝 Projects

- Discovery Call Notes
- Website Proposal
- AI Project Notes

### 📧 Reports

- Weekly Progress Notes
- Client Status Updates

### 📅 Meetings

- Product Meeting
- Client Meeting
- Sales Discussion

---

# 📊 Why WorkPilot AI?

| Traditional AI Assistants | WorkPilot AI |
|----------------------------|--------------|
| Requires detailed prompts | Guided workflows |
| Returns paragraphs of text | Generates finished business outputs |
| AI performs calculations | Python validates calculations |
| Manual formatting required | Ready-to-use exports |
| Suggests actions | Produces actionable deliverables |
| General-purpose assistant | Purpose-built operations workspace |

---

# 🛠 Tech Stack

| Layer | Technology |
|---------|------------|
| Frontend | Streamlit |
| AI Engine | OpenAI GPT-4o |
| Backend | Python |
| PDF Processing | pdfplumber |
| Data Processing | Pandas |
| Export Formats | CSV, Markdown |
| Hosting | Streamlit Community Cloud |

---

# 📂 Project Structure

```text
workpilot-ai/

├── app.py
├── config.py
├── ai_rules.py
├── policies.py
├── utils.py
├── math_engine.py
├── action_engine.py
├── sample_data.py
├── assets/
└── requirements.txt
```

---

# 🚀 Quick Start

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/workpilot-ai.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

Open the local Streamlit URL in your browser and start with the built-in sample workspace.

---

# 🌐 Live Demo

No installation required.

**Try WorkPilot AI instantly:**

👉 https://workpilot-ai-6dsby5ksu9fp6d4rj3m6wz.streamlit.app/

Explore every workflow using the built-in sample datasets before uploading your own files.

---

# 📈 Impact

| Workflow | Manual Time | AI Time | Time Saved |
|-----------|------------:|---------:|-----------:|
| Financial Audit | 45 min | 30 sec | 44.5 min |
| Scope of Work | 2 hrs | 20 sec | ~2 hrs |
| Client Reports | 30 min | 15 sec | 29.5 min |
| Meeting Breakdown | 20 min | 15 sec | 19.75 min |

### ⚡ Estimated Weekly Time Saved

**15+ Hours**

---

# 🗺️ Roadmap

- Workflow Builder
- Google Drive Integration
- CRM Integrations
- Team Collaboration
- Custom Templates
- Analytics Dashboard
- Additional AI Workspaces

---

# 🤝 Contributing

Contributions, ideas, bug reports, and feature requests are welcome.

Feel free to fork the repository, open an issue, or submit a pull request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

<div align="center">

## 🚀 Try WorkPilot AI

### https://workpilot-ai-6dsby5ksu9fp6d4rj3m6wz.streamlit.app/

**Built for the PromptWars × CodexSec Hackathon**

If you found this project interesting or useful, consider giving it a ⭐ on GitHub.

Made with ❤️ using Python, Streamlit & OpenAI.

</div>
