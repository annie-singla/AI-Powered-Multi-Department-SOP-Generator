# AI-Powered-Multi-Department-SOP-Generator
Streamlit app that extracts disaster-specific content from District Disaster Management Plans (DMPs) and generates detailed SOPs by department using Azure OpenAI GPT-3.5 Turbo. Supports PDF parsing via PyMuPDF, disaster-type filtering, and department-wise task generation for rapid disaster response planning.
Here’s a **professional README.md** for your AI-Powered Multi-Department SOP Generator repo:

---

# 🌐 AI-Powered Multi-Department SOP Generator from DMPs

Generate structured, department-wise **Standard Operating Procedures (SOPs)** from **District Disaster Management Plans (DMPs)** using Azure OpenAI GPT-3.5 Turbo.
This Streamlit-based tool enables quick extraction of disaster-specific policies and conversion into actionable tasks for multiple government departments.

---

## 🚀 Features

* **Multi-PDF Upload**: Supports bulk upload of District DMP PDFs.
* **Disaster-Specific Filtering**: Extracts only relevant sections for selected disaster types (e.g., Flood, Earthquake, Cyclone).
* **Department-Wise SOP Generation**: Creates detailed task lists for key agencies like Health, Police, NDRF, Fire, PWD, Transport, Revenue, and Municipal bodies.
* **Interactive UI**: Built with Streamlit for easy file upload, content review, and SOP download.
* **Fast PDF Parsing**: Uses PyMuPDF (`fitz`) for accurate and fast text extraction.
* **Powered by Azure OpenAI**: Leverages GPT-3.5 Turbo for semantic filtering and structured SOP creation.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Interactive web UI
* **PyMuPDF (fitz)** – PDF text extraction
* **Azure OpenAI GPT-3.5 Turbo** – Content filtering & SOP generation
* **Prompt Engineering** – Disaster-specific content extraction
* **File Handling** – Multi-file uploads & dynamic SOP downloads

---

## 📦 Installation

```
# Clone repository
git clone https://github.com/yourusername/dmp-sop-generator.git
cd dmp-sop-generator

# Install dependencies
pip install -r requirements.txt
```

---

## ⚙️ Configuration

1. Create an **Azure OpenAI resource** in your Azure portal.
2. Get your **API key**, **endpoint**, and **deployment name**.
3. Set them in your environment variables:

```
export AZURE_API_KEY="your_api_key"
export AZURE_ENDPOINT="your_endpoint_url"
export AZURE_DEPLOYMENT="gpt-35-turbo"
export AZURE_API_VERSION="2024-12-01-preview"
```

---

## ▶️ Usage

```
streamlit run app.py
```

1. Upload one or more **District DMP PDFs**.
2. Select the **disaster type** (Flood, Earthquake, Cyclone, etc.).
3. View **extracted disaster-specific content**.
4. Get **department-wise SOPs** instantly.
5. **Download** generated SOP as a `.txt` file.

---

## 📌 Example Output

**For Flood:**

```
### Department: Health
- Set up emergency medical camps in flood-affected areas.
- Ensure adequate stock of medicines and water purification tablets.
- Deploy mobile medical units in remote areas.

### Department: Police
- Maintain law and order in relief camps.
- Assist in evacuation and crowd control.
- Coordinate with NDRF for rescue operations.
```

---

## 📄 License

MIT License – feel free to use and adapt.

---
