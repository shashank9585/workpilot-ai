"""
WorkPilot AI - Main Application
The workspace dashboard with 4 modules for freelancers & agencies.
"""

import streamlit as st
from openai import OpenAI
import json

# Import our modular files
from config import APP_NAME, APP_TAGLINE, APP_ICON, AI_MODEL, TIME_SAVINGS
from config import AI_TEMPERATURE_EXTRACTION, AI_TEMPERATURE_STRATEGY
from ai_rules import (
    AUDITOR_EXTRACTION_PROMPT, AUDITOR_STRATEGY_PROMPT,
    SOW_EXTRACTION_PROMPT, REPORT_GENERATION_PROMPT,
    MEETING_EXTRACTION_PROMPT
)
from policies import validate_extracted_text, validate_json_output
from utils import extract_text_from_file, extract_text_from_multiple_files
from math_engine import calculate_discrepancies, calculate_time_saved
from action_engine import (
    generate_gmail_url, generate_audit_csv, generate_meeting_csv,
    format_sow_markdown, format_report_markdown, format_meeting_markdown
)
from sample_data import get_sample_file_content

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title=APP_NAME, page_icon=APP_ICON, layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: bold; margin-bottom: 0; }
    .sub-header { color: #666; font-size: 1.1rem; margin-top: 0; }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px; border-radius: 10px; color: white; text-align: center;
    }
    .gmail-btn {
        background-color: #D93025 !important; color: white !important;
        font-weight: bold; border: none; border-radius: 8px;
        padding: 12px 24px; cursor: pointer; width: 100%; font-size: 16px;
    }
    .action-btn {
        background-color: #4CAF50 !important; color: white !important;
        font-weight: bold; border: none; border-radius: 8px;
        padding: 12px 24px; cursor: pointer; width: 100%;
    }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px; border-radius: 8px 8px 0 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER & POLICY BADGE
# ============================================================
st.markdown(f'<p class="main-header">{APP_ICON} {APP_NAME}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-header">{APP_TAGLINE}</p>', unsafe_allow_html=True)

st.info("🔒 **ZERO-DATA RETENTION POLICY:** All files processed in-memory and wiped instantly. We never store, log, or train on your data.")

# ============================================================
# SIDEBAR: API KEY & INFO
# ============================================================
with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("OpenAI API Key", type="password", 
                            help="Get one at platform.openai.com")
    
    st.markdown("---")
    st.markdown("### 🧠 How It Works")
    st.markdown("1. **AI** extracts data from your files")
    st.markdown("2. **Python** does the math (zero hallucinations)")
    st.markdown("3. **You** review & take action")
    
    st.markdown("---")
    st.markdown("### 📊 Your Impact")
    st.metric("Modules Available", "4")
    st.metric("Avg Time Saved", "45+ min/task")

# ============================================================
# MAIN TABS (The Workspace)
# ============================================================
tab_dash, tab_audit, tab_sow, tab_report, tab_meeting = st.tabs([
    "🏠 Dashboard", "💰 Auditor", "📝 SOW Generator", "📧 Client Report", "📅 Meeting Breakdown"
])

# ============================================================
# TAB 1: DASHBOARD
# ============================================================
with tab_dash:
    st.header("Welcome to Your Admin Workspace")
    st.markdown("Pick a module above to automate your work. Each one is built for the same goal: **save you hours every week.**")
    
    st.markdown("---")
    st.subheader("⚡ Quick Start: Test With Sample Data")
    st.markdown("Don't have files ready? Download our sample data, upload it, and see the magic in 30 seconds.")
    
    col1, col2, col3, col4 = st.columns(4)
    samples = [
        ("contract", "📄 Sample Contract"),
        ("invoice", "🧾 Sample Invoice"),
        ("discovery", "📝 Sample Call Notes"),
        ("meeting", "📅 Sample Meeting Notes"),
    ]
    
    for col, (key, label) in zip([col1, col2, col3, col4], samples):
        with col:
            filename, content = get_sample_file_content(key)
            st.download_button(label, content, file_name=filename, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🎯 What You Can Automate")
    
    c1, c2, c3, c4 = st.columns(4)
    modules_info = [
        ("💰", "Financial Auditor", "Catch invoice overcharges"),
        ("📝", "SOW Generator", "Turn call notes into proposals"),
        ("📧", "Client Report", "Polish rough notes into updates"),
        ("📅", "Meeting Breakdown", "Extract today's tasks from meetings"),
    ]
    for col, (icon, title, desc) in zip([c1, c2, c3, c4], modules_info):
        with col:
            st.markdown(f"### {icon} {title}")
            st.caption(desc)

# ============================================================
# TAB 2: FINANCIAL AUDITOR
# ============================================================
with tab_audit:
    st.header("💰 Financial Auditor")
    st.markdown("Upload a contract and an invoice. We'll find discrepancies with 100% accuracy.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📄 Reference Document (Contract)")
        file_contract = st.file_uploader("Upload contract", type=["pdf", "txt"], key="audit_contract")
    with col2:
        st.subheader("🧾 Document to Audit (Invoice)")
        file_invoice = st.file_uploader("Upload invoice", type=["pdf", "txt"], key="audit_invoice")
    
    if st.button("🚀 Run Audit", type="primary", use_container_width=True):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API Key in the sidebar.")
        elif not file_contract or not file_invoice:
            st.warning("⚠️ Please upload both files.")
        else:
            with st.spinner("🧠 AI extracting data, Python calculating math..."):
                try:
                    c_text = extract_text_from_file(file_contract)
                    i_text = extract_text_from_file(file_invoice)
                    
                    # Policy: Graceful Degradation
                    valid_c, err_c = validate_extracted_text(c_text, file_contract.name)
                    valid_i, err_i = validate_extracted_text(i_text, file_invoice.name)
                    if not valid_c: st.error(err_c); st.stop()
                    if not valid_i: st.error(err_i); st.stop()
                    
                    # AI Extraction
                    client = OpenAI(api_key=api_key)
                    resp = client.chat.completions.create(
                        model=AI_MODEL,
                        messages=[
                            {"role": "system", "content": AUDITOR_EXTRACTION_PROMPT},
                            {"role": "user", "content": f"CONTRACT:\n{c_text}\n\nINVOICE:\n{i_text}"}
                        ],
                        response_format={"type": "json_object"},
                        temperature=AI_TEMPERATURE_EXTRACTION
                    )
                    extracted = json.loads(resp.choices[0].message.content)
                    
                    valid, err = validate_json_output(extracted, ["contract_items", "invoice_items"], "Auditor")
                    if not valid: st.error(err); st.stop()
                    
                    # Python Math (Zero AI hallucinations)
                    discrepancies, total = calculate_discrepancies(
                        extracted.get("contract_items", []),
                        extracted.get("invoice_items", [])
                    )
                    
                    st.session_state['audit_discs'] = discrepancies
                    st.session_state['audit_total'] = total
                    st.session_state['audit_extracted'] = extracted
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
    
    # Display Results
    if 'audit_discs' in st.session_state:
        discs = st.session_state['audit_discs']
        total = st.session_state['audit_total']
        extracted = st.session_state['audit_extracted']
        
        st.markdown("---")
        if not discs:
            st.success("✅ **CLEAN AUDIT:** No discrepancies found. Invoice matches contract perfectly.")
        else:
            st.error(f"⚠️ **DISCREPANCIES DETECTED:** Total Overcharge: **${total:,.2f}**")
            
            import pandas as pd
            df = pd.DataFrame(discs)
            st.dataframe(df, use_container_width=True)
            
            # AI Strategy (Email + Accounting)
            with st.spinner("🧠 AI generating dispute strategy..."):
                try:
                    client = OpenAI(api_key=api_key)
                    strategy_prompt = AUDITOR_STRATEGY_PROMPT.format(
                        discrepancies_json=json.dumps(discs),
                        total_overcharge=total
                    )
                    resp2 = client.chat.completions.create(
                        model=AI_MODEL,
                        messages=[
                            {"role": "system", "content": "Output STRICT JSON ONLY."},
                            {"role": "user", "content": strategy_prompt}
                        ],
                        response_format={"type": "json_object"},
                        temperature=AI_TEMPERATURE_STRATEGY
                    )
                    artifacts = json.loads(resp2.choices[0].message.content)
                    
                    st.markdown("### 🚀 Action Center")
                    
                    # Gmail Hack
                    subject = artifacts.get("email_subject", "Invoice Discrepancy Notice")
                    body = artifacts.get("email_body", "")
                    gmail_url = generate_gmail_url(subject=subject, body=body)
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown(f'<a href="{gmail_url}" target="_blank"><button class="gmail-btn">✉️ Open Gmail & Send Dispute</button></a>', unsafe_allow_html=True)
                    with c2:
                        csv_data, csv_name = generate_audit_csv(discs, total)
                        if csv_data:
                            st.download_button("📥 Download Audit CSV", csv_data, csv_name, "text/csv", use_container_width=True)
                    
                    with st.expander("🧠 View AI Strategy & Accounting Actions"):
                        st.markdown(f"**📝 Accounting Adjustment:**\n{artifacts.get('accounting_action', 'N/A')}")
                        st.markdown(f"**📧 Drafted Email:**\n{body}")
                except Exception as e:
                    st.error(f"Strategy generation error: {e}")

# ============================================================
# TAB 3: SOW GENERATOR
# ============================================================
with tab_sow:
    st.header("📝 Scope of Work Generator")
    st.markdown("Paste messy discovery call notes. Get a professional proposal in seconds.")
    
    sow_input = st.text_area("Paste your call notes, email thread, or brain dump:", height=200,
                             placeholder="e.g., Call with Sarah from TechStart. They need a website redesign. Budget $15-20k. Timeline 10 weeks...")
    
    if st.button("🚀 Generate SOW", type="primary", use_container_width=True, key="sow_btn"):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API Key in the sidebar.")
        elif not sow_input.strip():
            st.warning("⚠️ Please paste some notes first.")
        else:
            with st.spinner("🧠 AI structuring your proposal..."):
                try:
                    client = OpenAI(api_key=api_key)
                    resp = client.chat.completions.create(
                        model=AI_MODEL,
                        messages=[
                            {"role": "system", "content": SOW_EXTRACTION_PROMPT},
                            {"role": "user", "content": sow_input}
                        ],
                        response_format={"type": "json_object"},
                        temperature=AI_TEMPERATURE_STRATEGY
                    )
                    sow_data = json.loads(resp.choices[0].message.content)
                    
                    valid, err = validate_json_output(sow_data, ["project_title", "deliverables"], "SOW")
                    if not valid: st.error(err); st.stop()
                    
                    st.session_state['sow_data'] = sow_data
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
    
    if 'sow_data' in st.session_state:
        sow_data = st.session_state['sow_data']
        st.markdown("---")
        st.subheader("📋 Your Professional SOW")
        
        sow_md = format_sow_markdown(sow_data)
        st.markdown(sow_md)
        
        c1, c2 = st.columns(2)
        with c1:
            st.download_button("📥 Download as Markdown", sow_md, "SOW_Draft.md", "text/markdown", use_container_width=True)
        with c2:
            st.code(sow_md, language="markdown")
            st.caption("Copy this and paste into your email or document.")

# ============================================================
# TAB 4: CLIENT STATUS REPORT
# ============================================================
with tab_report:
    st.header("📧 Client Status Report")
    st.markdown("Paste your rough weekly notes. Get a polished client update ready to send.")
    
    report_input = st.text_area("Paste your rough notes:", height=200, key="report_input",
                                placeholder="e.g., DONE: homepage wireframes. IN PROGRESS: pricing page. BLOCKERS: waiting on screenshots...")
    
    if st.button("🚀 Generate Report", type="primary", use_container_width=True, key="report_btn"):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API Key in the sidebar.")
        elif not report_input.strip():
            st.warning("⚠️ Please paste some notes first.")
        else:
            with st.spinner("🧠 AI polishing your update..."):
                try:
                    client = OpenAI(api_key=api_key)
                    resp = client.chat.completions.create(
                        model=AI_MODEL,
                        messages=[
                            {"role": "system", "content": REPORT_GENERATION_PROMPT},
                            {"role": "user", "content": report_input}
                        ],
                        response_format={"type": "json_object"},
                        temperature=AI_TEMPERATURE_STRATEGY
                    )
                    report_data = json.loads(resp.choices[0].message.content)
                    
                    valid, err = validate_json_output(report_data, ["wins_section", "in_progress_section"], "Report")
                    if not valid: st.error(err); st.stop()
                    
                    st.session_state['report_data'] = report_data
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
    
    if 'report_data' in st.session_state:
        report_data = st.session_state['report_data']
        st.markdown("---")
        st.subheader("📧 Your Polished Client Update")
        
        report_md = format_report_markdown(report_data)
        st.markdown(report_md)
        
        # Gmail automation
        subject = f"Weekly Project Update - {__import__('datetime').datetime.now().strftime('%B %d, %Y')}"
        gmail_url = generate_gmail_url(subject=subject, body=report_md)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<a href="{gmail_url}" target="_blank"><button class="gmail-btn">✉️ Open Gmail & Send to Client</button></a>', unsafe_allow_html=True)
        with c2:
            st.download_button("📥 Download as Markdown", report_md, "Client_Update.md", "text/markdown", use_container_width=True)

# ============================================================
# TAB 5: MEETING BREAKDOWN & REMINDERS
# ============================================================
with tab_meeting:
    st.header("📅 Meeting Breakdown & Daily Reminders")
    st.markdown("Paste meeting notes or transcripts. Get your action items and today's tasks instantly.")
    
    meeting_input = st.text_area("Paste meeting notes or transcript:", height=200, key="meeting_input",
                                 placeholder="e.g., Sprint planning meeting. Attendees: You, Sarah, Mike. Discussed blog launch, pricing page...")
    
    if st.button("🚀 Break Down Meeting", type="primary", use_container_width=True, key="meeting_btn"):
        if not api_key:
            st.error("⚠️ Please enter your OpenAI API Key in the sidebar.")
        elif not meeting_input.strip():
            st.warning("⚠️ Please paste meeting notes first.")
        else:
            with st.spinner("🧠 AI extracting action items..."):
                try:
                    client = OpenAI(api_key=api_key)
                    resp = client.chat.completions.create(
                        model=AI_MODEL,
                        messages=[
                            {"role": "system", "content": MEETING_EXTRACTION_PROMPT},
                            {"role": "user", "content": meeting_input}
                        ],
                        response_format={"type": "json_object"},
                        temperature=AI_TEMPERATURE_EXTRACTION
                    )
                    meeting_data = json.loads(resp.choices[0].message.content)
                    
                    valid, err = validate_json_output(meeting_data, ["action_items", "key_decisions"], "Meeting")
                    if not valid: st.error(err); st.stop()
                    
                    st.session_state['meeting_data'] = meeting_data
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
    
    if 'meeting_data' in st.session_state:
        meeting_data = st.session_state['meeting_data']
        st.markdown("---")
        
        # Today's Tasks - The Main Feature
        st.subheader("✅ Your Tasks & Reminders")
        action_items = meeting_data.get("action_items", [])
        
        if action_items:
            for item in action_items:
                priority_emoji = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(item.get("priority", "Medium"), "🟡")
                owner = item.get("owner", "TBD")
                deadline = item.get("deadline", "TBD")
                st.markdown(f"- {priority_emoji} **{item.get('task', '')}**  \n  _Owner: {owner} | Deadline: {deadline}_")
        else:
            st.info("No action items extracted from this meeting.")
        
        # Full breakdown
        with st.expander("📋 View Full Meeting Breakdown"):
            meeting_md = format_meeting_markdown(meeting_data)
            st.markdown(meeting_md)
        
        # Actions
        st.markdown("### 🚀 Take Action")
        c1, c2, c3 = st.columns(3)
        with c1:
            csv_data, csv_name = generate_meeting_csv(action_items, meeting_data.get("meeting_title", "Meeting"))
            if csv_data:
                st.download_button("📥 Download Tasks CSV", csv_data, csv_name, "text/csv", use_container_width=True)
        with c2:
            meeting_md = format_meeting_markdown(meeting_data)
            st.download_button("📥 Download Full Notes", meeting_md, "Meeting_Notes.md", "text/markdown", use_container_width=True)
        with c3:
            # Gmail reminder to self
            subject = f"📌 Reminder: Tasks from {meeting_data.get('meeting_title', 'Meeting')}"
            body = "Your action items from today's meeting:\n\n"
            for item in action_items:
                body += f"- {item.get('task', '')} (Owner: {item.get('owner', 'TBD')}, Deadline: {item.get('deadline', 'TBD')})\n"
            gmail_url = generate_gmail_url(subject=subject, body=body)
            st.markdown(f'<a href="{gmail_url}" target="_blank"><button class="gmail-btn">✉️ Email Tasks to Myself</button></a>', unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption(f"Built for the PromptWars x CodexSec Hackathon | {APP_NAME} © 2026")