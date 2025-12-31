import streamlit as st
import pandas as pd
from datetime import datetime, timezone
from io import StringIO

st.set_page_config(page_title="AI Ethics Checklist", page_icon="✅", layout="centered")

st.title("AI Ethics Checklist")
st.write("Welcome — this app is running correctly.")

# Optional context fields (helps organisations)
st.subheader("Context (optional)")
org_name = st.text_input("Organisation / Team name", placeholder="e.g., Academy Achievers")
project_name = st.text_input("Project / Use case", placeholder="e.g., AI mentoring assistant")
reviewer = st.text_input("Reviewer name", placeholder="e.g., Paulette Watson")

st.divider()

# Checklist items
st.subheader("Checklist")
items = [
    "Fairness & Bias",
    "Transparency & Explainability",
    "Privacy & Data Protection",
    "Accountability & Governance",
    "Safety & Robustness",
]

# Keep state across reruns
if "checks" not in st.session_state:
    st.session_state.checks = {item: False for item in items}

for item in items:
    st.session_state.checks[item] = st.checkbox(item, value=st.session_state.checks[item])

st.divider()

# Build results
checked = [k for k, v in st.session_state.checks.items() if v]
total = len(items)
done = len(checked)
percent = int((done / total) * 100) if total else 0

timestamp_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

st.subheader("Summary")
st.write(f"**Completed:** {done}/{total} (**{percent}%**)  ")
st.write(f"**Timestamp:** {timestamp_utc}")

if org_name:
    st.write(f"**Organisation / Team:** {org_name}")
if project_name:
    st.write(f"**Project / Use case:** {project_name}")
if reviewer:
    st.write(f"**Reviewer:** {reviewer}")

# Create a tidy table for export
df = pd.DataFrame(
    [{"Item": item, "Selected": "Yes" if st.session_state.checks[item] else "No"} for item in items]
)

st.dataframe(df, use_container_width=True, hide_index=True)

# Build downloadable content
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

txt_lines = [
    "AI Ethics Checklist — Summary Report",
    "-----------------------------------",
    f"Timestamp: {timestamp_utc}",
    f"Organisation/Team: {org_name or 'N/A'}",
    f"Project/Use case: {project_name or 'N/A'}",
    f"Reviewer: {reviewer or 'N/A'}",
    "",
    f"Completed: {done}/{total} ({percent}%)",
    "",
    "Checklist results:",
]
for item in items:
    status = "YES" if st.session_state.checks[item] else "NO"
    txt_lines.append(f"- {item}: {status}")

txt_lines += [
    "",
    "Data & privacy:",
    "This app does not store user responses by default. Selections remain in the current browser session only.",
    "",
    "Paulette Watson MBE, 2025 Confidential. Shared only for academic evaluation.",
]
txt_report = "\n".join(txt_lines)

st.subheader("Download")
st.download_button(
    label="Download CSV",
    data=csv_buffer.getvalue(),
    file_name="ai_ethics_checklist_results.csv",
    mime="text/csv",
)

st.download_button(
    label="Download TXT Summary",
    data=txt_report,
    file_name="ai_ethics_checklist_summary.txt",
    mime="text/plain",
)

st.divider()
st.caption("Paulette Watson MBE, 2025 Confidential. Shared only for academic evaluation.")
