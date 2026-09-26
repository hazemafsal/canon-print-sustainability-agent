# AI Print Sustainability Agent

An AI-powered sustainability analysis platform designed to analyze print-related operational data, identify potential environmental and operational issues, determine root causes, and generate data-driven sustainability recommendations.

## 🚀 Project Overview

The **AI Print Sustainability Agent** combines data analysis, machine learning, Retrieval-Augmented Generation (RAG), and agentic AI workflows to support sustainability analysis in printing operations.

The system processes operational data and uses multiple AI agents to move from:

**Data → Problem Detection → Root Cause Analysis → Evidence Retrieval → Sustainability Recommendation → Final Report**

---

## 🎯 Business Problem

Printing operations can generate significant environmental impact through:

* Excessive paper consumption
* High energy usage
* Printing inefficiencies
* Waste generation
* Poor device utilization
* Unnecessary printing
* Inefficient operational processes

Traditional reporting systems can show metrics, but they may not explain:

> **Why is the problem happening, and what should be done about it?**

This project aims to provide an AI-assisted workflow that goes beyond simple dashboards by identifying possible causes and generating actionable recommendations.

---

## 🧠 Key Features

### 1. Data Analysis

The system analyzes operational and sustainability-related data to identify:

* Usage patterns
* Printing activity
* Resource consumption
* Waste indicators
* Operational anomalies
* Sustainability metrics

### 2. AI Root-Cause Analysis

The Root Cause Agent analyzes detected problems and identifies possible contributing factors.

Example:

```text
Problem:
High printing waste

↓
Analysis

Possible causes:
- High-volume printing
- Incorrect print settings
- Repeated print jobs
- Low device utilization
```

### 3. RAG-Based Knowledge Retrieval

The RAG component retrieves relevant information from a sustainability knowledge base.

The workflow can be represented as:

```text
User / Operational Data
        ↓
Problem Detection
        ↓
Root Cause Analysis
        ↓
Knowledge Retrieval
        ↓
Relevant Sustainability Evidence
        ↓
AI Recommendation
```

This allows the AI system to use project-specific knowledge instead of relying only on a general language model.

### 4. Sustainability Recommendations

The system generates recommendations based on the detected issue and retrieved knowledge.

Examples include:

* Reducing unnecessary print jobs
* Improving printer utilization
* Optimizing print settings
* Reducing paper waste
* Improving operational monitoring
* Encouraging digital alternatives

### 5. Agentic AI Workflow

The application is organized into multiple components/agents.

A typical workflow is:

```text
                    ┌──────────────────┐
                    │   User / Data    │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Problem Analysis │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Root Cause Agent │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │   RAG Retrieval  │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Recommendation   │
                    │      Agent       │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ Final AI Report  │
                    └──────────────────┘
```

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │     Streamlit UI    │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │    Workflow Graph   │
                    └──────────┬──────────┘
                               ↓
          ┌────────────────────┼────────────────────┐
          ↓                    ↓                    ↓
   ┌─────────────┐     ┌──────────────┐     ┌──────────────┐
   │ Data Agent  │     │ Root Cause   │     │ RAG Agent    │
   │             │     │ Agent        │     │              │
   └──────┬──────┘     └──────┬───────┘     └──────┬───────┘
          │                   │                    │
          └───────────────────┼────────────────────┘
                              ↓
                    ┌─────────────────────┐
                    │ Recommendation      │
                    │ / Decision Layer    │
                    └──────────┬──────────┘
                               ↓
                    ┌─────────────────────┐
                    │ Sustainability      │
                    │ Report              │
                    └─────────────────────┘
```

---

## 📚 RAG Pipeline

The Retrieval-Augmented Generation pipeline follows:

```text
Documents
    ↓
Document Processing
    ↓
Text Chunking
    ↓
Embeddings
    ↓
Vector Search
    ↓
Relevant Context
    ↓
LLM
    ↓
Grounded Response
```

The purpose of RAG is to provide the AI system with relevant sustainability information during analysis.

---

## 🔍 Root-Cause Analysis

The Root Cause Agent is responsible for moving beyond simply identifying an issue.

For example:

```text
Observed Issue
     ↓
Analyze operational indicators
     ↓
Identify contributing factors
     ↓
Retrieve supporting knowledge
     ↓
Generate possible root causes
     ↓
Recommend corrective actions
```

The output can include:

* Detected problem
* Possible root cause
* Supporting evidence
* Recommended action
* Expected sustainability impact

---

## 🌱 Sustainability Analysis

The platform can support analysis across areas such as:

| Area           | Example Analysis                          |
| -------------- | ----------------------------------------- |
| Paper          | Paper consumption and waste               |
| Energy         | Energy-intensive printing activity        |
| Devices        | Printer utilization                       |
| Waste          | Unnecessary or repeated print jobs        |
| Operations     | Printing process inefficiencies           |
| Digitalization | Opportunities to reduce physical printing |

---

## 🛠️ Technologies

### Programming

* Python

### AI / ML

* Machine Learning
* Large Language Models
* Agentic AI
* Retrieval-Augmented Generation (RAG)
* Embeddings

### Application

* Streamlit

### Data

* Pandas
* NumPy

### Workflow

* Agent-based workflow
* Workflow graph architecture

### Development

* Git
* GitHub

---

## 📁 Project Structure

```text
canon_print_sustainability_agent/
│
├── agents/
│   ├── root_cause_agent.py
│   └── ...
│
├── data/
│   └── ...
│
├── rag/
│   └── ...
│
├── services/
│   └── ...
│
├── utils/
│   └── ...
│
├── workflow/
│   ├── graph.py
│   └── ...
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/canon-print-sustainability-agent.git
```

Enter the project directory:

```bash
cd canon-print-sustainability-agent
```

Create a virtual environment:

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```powershell
streamlit run app.py
```

The application will open in your browser.

---

## 🔐 Environment Variables

If the application uses an external AI API, store API keys in environment variables rather than directly inside Python files.

Example:

```text
.env
```

Do not upload `.env` to GitHub.

The `.gitignore` file should contain:

```text
.env
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
```

---

## 🖥️ Screenshots

Add screenshots of the working application here.

Example:

```text
screenshots/
├── dashboard.png
├── root-cause-analysis.png
├── rag-results.png
└── sustainability-recommendations.png
```

Then add them to the README:

```markdown
![Dashboard](screenshots/dashboard.png)

![Root Cause Analysis](screenshots/root-cause-analysis.png)

![Sustainability Recommendations](screenshots/sustainability-recommendations.png)
```

---

## 📊 Example Workflow

A typical analysis can look like:

```text
Input Operational Data
          ↓
Data Quality / Validation
          ↓
Identify Sustainability Issue
          ↓
Root Cause Analysis
          ↓
Retrieve Relevant Knowledge
          ↓
Generate Recommendations
          ↓
Final Sustainability Insight
```

---

## 💡 Example Output

```text
Sustainability Issue:
Elevated printing waste detected.

Potential Root Cause:
High frequency of unnecessary print jobs and inefficient
printing practices.

Recommended Actions:
1. Encourage digital document workflows.
2. Enable default duplex printing.
3. Monitor repeated print jobs.
4. Track printer utilization.
5. Establish sustainability KPIs.

Expected Benefit:
Potential reduction in paper consumption and printing waste.
```

---

## 🎓 Skills Demonstrated

This project demonstrates practical experience with:

* Python
* Data Analysis
* Machine Learning
* Generative AI
* Agentic AI
* RAG
* LLM integration
* Workflow orchestration
* Sustainability analytics
* Streamlit
* Git/GitHub

---

## 🔮 Future Improvements

Potential future improvements include:

* Real-time printer telemetry
* Automated sustainability KPI monitoring
* Carbon-footprint estimation
* Advanced anomaly detection
* Time-series forecasting
* Automated sustainability reports
* Multi-agent collaboration
* Enterprise data connectors
* Cloud deployment
* Monitoring and observability
* Role-based user interfaces

---

## 👨‍💻 Author

**Hazem Ahammed**

AI / ML & Data Science

Interested in:

* Artificial Intelligence
* Data Science
* Agentic AI
* Business Intelligence
* Sustainability Analytics

---

## 📄 License

This project is intended for educational, portfolio, and research purposes.
