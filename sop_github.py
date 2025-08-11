#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 14:54:31 2025

@author: carousell
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 21 17:41:13 2025

@author: carousell
"""

import streamlit as st
import fitz  # PyMuPDF
from openai import AzureOpenAI

# 🔐 Azure OpenAI credentials
AZURE_API_KEY = ""
AZURE_ENDPOINT = ""
AZURE_DEPLOYMENT = ""
AZURE_API_VERSION = ""

client = AzureOpenAI(
    api_version=AZURE_API_VERSION,
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY
)

st.set_page_config(page_title="🛡️ AI-Powered DMP SOP Generator", layout="wide")
st.title("🌐 AI-Powered Multi-Department SOP Generator from DMPs")
st.markdown("Upload District Disaster Management Plans (DMPs), select a disaster, and get structured SOPs by department.")

# Upload PDFs
uploaded_files = st.file_uploader("📄 Upload DMP PDFs", type=["pdf"], accept_multiple_files=True)

# Select disaster
disaster_type = st.selectbox(
    "🌪️ Select Disaster Type",
    ["Landslide", "Flood", "Earthquake", "Cyclone", "Heatwave", "Drought"]
)

# Extract text from PDF
def extract_text_from_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return " ".join([page.get_text() for page in doc])
    except Exception as e:
        return f"Error: {e}"

# Filter DMP content relevant to disaster
def filter_relevant_dmp(text, disaster):
    messages = [
        {"role": "system", "content": f"You are an expert in disaster policy. Extract only content relevant to {disaster} from this DMP."},
        {"role": "user", "content": text[:8000]}
    ]
    response = client.chat.completions.create(
        messages=messages,
        max_tokens=2048,
        temperature=0.4,
        top_p=1.0,
        model=AZURE_DEPLOYMENT
    )
    return response.choices[0].message.content.strip()

# Generate Multi-Department SOPs
def generate_multi_department_sop(text, disaster):
    departments = [
        "Health", "Police", "NDRF", "Fire & Emergency", "PWD",
        "Transport", "Revenue", "Municipal/ULBs"
    ]

    prompt = f"""
You are a disaster management expert. Based on the following content related to {disaster}, generate detailed SOPs organized by department.
Respond in the following format:

### Department: [Department Name]
- Task 1
- Task 2
...

Content:
{text}
    """

    messages = [
        {"role": "system", "content": f"Generate multi-department SOPs for a '{disaster}' disaster from the following DMP content."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        messages=messages,
        max_tokens=2048,
        temperature=0.5,
        top_p=1.0,
        model=AZURE_DEPLOYMENT
    )

    return response.choices[0].message.content.strip()

# Main logic
if uploaded_files:
    for file in uploaded_files:
        st.subheader(f"📘 {file.name}")
        with st.spinner("📤 Extracting content..."):
            text = extract_text_from_pdf(file)
            relevant = filter_relevant_dmp(text, disaster_type)

        st.success("✅ Relevant content extracted.")
        with st.expander("📄 View Disaster-Specific Content"):
            st.text_area("Extracted Content", relevant, height=300)

        with st.spinner("🧠 Generating SOPs by department..."):
            sop_output = generate_multi_department_sop(relevant, disaster_type)

        st.text_area("📜 Generated Multi-Department SOP", sop_output, height=400)
        base_filename = file.name.replace(".pdf", "").replace(" ", "_")
        st.download_button("⬇️ Download SOP", sop_output, file_name=f"SOP_{disaster_type}_{base_filename}.txt")
else:
    st.info("👆 Upload at least one DMP PDF to begin.")
