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

model= genai.GenerativeModel('gemini-3.6-flash')

# Create def function to analyse pdf an job description

def analyse_resume(pdf_doc, job_des):
    
    if pdf_doc is not None:
        pdf_text = extractpdf(pdf_doc)
        st.write('Extracted Successfully✅')
        
    else:
        st.warning('Drop file in pdf format')
        
    ats_score = model.generate_content(f'''Compare the resume {pdf_text} with job description {job_des} 
                                       and get ATS score. Generate results in bullet points''')
    
    good_fit = model.generate_content(f'''Compare the resume {pdf_text} with job description {job_des} 
                                      and say am i a good fit for this job or not. Generate results in bullet points''')
    
    swot_analysis = model.generate_content(f'''Compare the resume {pdf_text} with job description {job_des} 
                                          and provide SWOT analysis. Generate results in bullet points''')
 
    prob = model.generate_content(f'''Compare the resume {pdf_text} with job description {job_des} 
                                       and give the probability to get selected for the given job.''')
    
    return {st.write(ats_score.text), 
           st.write(good_fit.text), 
           st.write(swot_analysis.text), 
           st.write(prob.text)} 
