import streamlit as st
from analysis import analyse_resume

st.title('CV ANALYZER🎯')

st.header('''This page helps you to compare your resume with the given Job description ''')

st.sidebar.subheader('Drop your resume here📑')

pdf_doc = st.sidebar.file_uploader('Click here to browse', type=['pdf'])

st.sidebar.markdown('Designed by Pooja P')
st.sidebar.markdown("LinkedIn:'https://www.linkedin.com/in/poojaprabakaran/'")

job_des = st.text_area('Copy paste the job description here', max_chars=10000)

submit = st.button('Generate ATS score')

if submit:
    with st.spinner('Getting Results...'):
     analyse_resume(pdf_doc, job_des)