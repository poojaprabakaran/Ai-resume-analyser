# 🎯 AI-Powered ATS Resume Analyzer

An AI-powered **ATS Resume Analyzer** built using **Python, Streamlit, Google Gemini API, and PyPDF**. The application analyzes a candidate's resume against a given job description and uses Generative AI to provide an estimated ATS score, job-fit analysis, SWOT analysis, and selection probability.

## 📌 About the Project

The **ATS Resume Analyzer** helps job seekers understand how well their resume aligns with a specific job description.

Users can upload their resume in **PDF format** and paste a job description into the application. The resume text is extracted from the PDF and combined with the job description in a structured prompt. Google Gemini then analyzes the information and generates a detailed assessment.

The project demonstrates the use of **Generative AI, prompt engineering, PDF text extraction, and Streamlit** to build a practical AI-powered career assistance application.

## ✨ Features

* 📑 Upload resumes in PDF format
* 📄 Extract text from uploaded resumes
* 📝 Accept job descriptions as input
* 🤖 Use Google Gemini Generative AI for resume analysis
* 📊 Generate an estimated ATS score out of 100
* 🎯 Analyze candidate-job fit
* 💪 Provide SWOT analysis
* 📈 Estimate selection probability
* 💡 Explain factors affecting the candidate's chances
* 🎨 Simple and interactive Streamlit interface

## 🛠️ Technologies Used

* **Python** – Application development
* **Streamlit** – Interactive web application
* **Google Gemini API** – Generative AI-powered resume analysis
* **PyPDF** – Extracting text from PDF resumes
* **python-dotenv** – Environment variable management

## 📂 Project Structure

```text
ATS-Resume-Analyzer/
│
├── interface.py       # Streamlit user interface
├── analysis.py        # Resume analysis and Gemini API integration
├── pdf.py             # PDF text extraction
├── requirements.txt   # Project dependencies
├── .env               # API key configuration (not uploaded to GitHub)
├── .gitignore
└── README.md
```

## 🔄 How It Works

The application follows a simple workflow:

```text
User uploads Resume PDF
          ↓
     PDF text extraction
          ↓
User enters Job Description
          ↓
Resume + Job Description
          ↓
 Structured prompt sent to
    Google Gemini API
          ↓
    AI Resume Analysis
          ↓
 ┌─────────────────────────┐
 │ ATS Score               │
 │ Job Fit Analysis        │
 │ SWOT Analysis            │
 │ Selection Probability   │
 └─────────────────────────┘
```

## 🤖 Generative AI Implementation

The project uses **Google Gemini Generative AI** to compare the candidate's resume with the provided job description.

The extracted resume text and job description are dynamically inserted into a structured prompt. The prompt instructs Gemini to act as an **ATS resume analysis assistant** and generate multiple evaluation results.

The model is instructed to provide:

* **ATS Score** – An estimated score out of 100 with supporting reasons
* **Job Fit Analysis** – Evaluation of how well the candidate matches the position
* **SWOT Analysis** – Strengths, weaknesses, opportunities, and threats
* **Selection Probability** – An estimated probability of selection and the factors influencing it

This demonstrates the use of **prompt engineering and contextual Generative AI** to transform unstructured resume and job-description text into a structured career assessment.

## 📄 PDF Processing

The application uses **PyPDF** to extract text from uploaded resume documents.

The PDF extraction process reads each page and combines the extracted text into a single text string, which is then provided to the Gemini model for analysis.

```python
for page in pdf.pages:
    raw_text += page.extract_text()
```

This allows the application to work with resumes stored as PDF documents without requiring manual text copying from the resume.

## 💡 Analysis Output

After submitting the resume and job description, the application generates an AI-powered report containing:

### 📊 ATS Score

An estimated score out of 100 indicating how closely the resume aligns with the job description.

### 🎯 Job Fit Analysis

An assessment of whether the candidate's skills and experience are relevant to the role.

### 🔍 SWOT Analysis

The model identifies:

* **Strengths**
* **Weaknesses**
* **Opportunities**
* **Threats**

### 📈 Selection Probability

An estimated probability of selection along with the key factors that may influence the outcome.

## 🔐 API Configuration

The application uses a Google Gemini API key stored as an environment variable.

Create a `.env` file:

```text
GOOGLE_API_KEY=your_api_key_here
```

The API key is loaded using `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv("GOOGLE_API_KEY")
```

> **Important:** Never upload your `.env` file or API key to GitHub. Add `.env` to your `.gitignore` file.

## ▶️ Running the Project

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run interface.py
```

The application will open in your browser.

## 💡 Example Use Case

A candidate applying for a **Data Analyst** position can:

1. Upload their resume as a PDF.
2. Copy and paste the Data Analyst job description.
3. Click **Generate ATS Score**.
4. Receive an AI-generated analysis of their resume and its alignment with the job.

The results can help the candidate identify areas of their resume that may need improvement before applying.

## ⚠️ Disclaimer

The ATS score and selection probability generated by this application are **AI-generated estimates** and should not be considered an actual prediction of an employer's hiring decision.

Actual ATS systems and recruitment processes may use different criteria and algorithms.

## 🔮 Future Enhancements

* 📌 Extract and identify important keywords from job descriptions
* 🔎 Highlight missing skills and keywords in the resume
* 📊 Provide a detailed ATS score breakdown
* 📝 Generate resume improvement suggestions
* ✍️ Generate optimized resume bullet points
* 📄 Compare multiple versions of a resume
* 💬 Add conversational follow-up questions
* 🧠 Improve prompt structure and analysis consistency

## 👩‍💻 Author

**Pooja Prabakaran**

Built as a practical **Generative AI project** to explore the integration of Google's Gemini API, prompt engineering, PDF processing, and Streamlit for an AI-powered resume analysis application.

