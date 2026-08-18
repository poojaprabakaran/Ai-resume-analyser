# import libs
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

from pdf import extractpdf # takes the def func from the pdf.py file

# Configure the API key
KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=KEY)

# Call the model

model= genai.GenerativeModel('gemini-3.1-flash-lite')

# Create def function to analyse pdf an job description

def analyse_resume(pdf_doc, job_des):

    if pdf_doc is None:
        st.warning("Drop a file in PDF format")
        return

    pdf_text = extractpdf(pdf_doc)
    st.write("Extracted Successfully ✅")

    prompt = f"""
You are an ATS resume analysis assistant.

Compare the following resume with the job description.

RESUME:
{pdf_text}

JOB DESCRIPTION:
{job_des}

Provide the following results clearly:

1. ATS Score
Give an estimated ATS score out of 100 and explain it in bullet points.

2. Job Fit Analysis
Say whether the candidate is a good fit for the job and explain why in bullet points.

3. SWOT Analysis
Provide:
- Strengths
- Weaknesses
- Opportunities
- Threats

4. Selection Probability
Give an estimated probability of getting selected and explain the important factors affecting it.

Keep the response clear and well structured.
"""

    response = model.generate_content(prompt)

    return response.text