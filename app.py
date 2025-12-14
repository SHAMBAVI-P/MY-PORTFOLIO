import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Monika P | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Aggressive CSS to Remove ALL White Space
st.markdown("""
    <style>
        header[data-testid="stHeader"] { display: none; }
        footer { display: none; }
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            margin: 0 !important;
        }
        iframe { display: block; border: none; }
    </style>
""", unsafe_allow_html=True)

# 3. Helper Function: Convert File to Base64
def get_file_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 4. Main Logic
html_file_path = "index.html"
image_file_path = "profile.jpg"
resume_file_path = "resume.pdf"  # Make sure your file is named exactly this

if not os.path.exists(html_file_path):
    st.error(f"Error: 'index.html' not found.")
else:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Inject Image (if exists)
    if os.path.exists(image_file_path):
        img_b64 = get_file_as_base64(image_file_path)
        html_content = html_content.replace(
            'src="profile.jpg"', 
            f'src="data:image/jpeg;base64,{img_b64}"'
        )
    
    # Inject Resume PDF (if exists)
    # ... (Keep your imports and file logic the same) ...

   # ... (rest of your code remains the same)

    # Inject Resume PDF
    if os.path.exists(resume_file_path):
        resume_b64 = get_file_as_base64(resume_file_path)
        html_content = html_content.replace(
            'href="resume.pdf"',
            f'href="data:application/pdf;base64,{resume_b64}"'
        )

    # FIX: 
    # 1. Height=950: Fits Laptop & Mobile Desktop Mode perfectly (Removes black space).
    # 2. Scrolling=True: Allows standard Mobile users to scroll down to see the rest.
    components.html(html_content, height=950, scrolling=True)