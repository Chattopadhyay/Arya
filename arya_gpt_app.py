
# AryaGPT - AI Teaching Assistant

import streamlit as st
from datetime import datetime
import openai
from streamlit_option_menu import option_menu
import random

# Page Configuration
st.set_page_config(page_title='AryaGPT - Your AI Teaching Assistant', page_icon='🤖', layout='centered')

# Custom CSS for enhanced look and feel
st.markdown("""
    <style>
        .main-header {
            background-color: #4B6EAF;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 26px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .feature-card {
            background-color: #F5F5F5;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        }
        .sidebar .stButton button {
            background-color: #4B6EAF;
            color: white;
            border-radius: 5px;
        }
        .block-container {
            max-width: 800px;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown('<div class="main-header">AryaGPT - Your AI Teaching Assistant</div>', unsafe_allow_html=True)
st.markdown('Empowering your classroom with AI-driven insights and automation.')

# Sidebar for Navigation
with st.sidebar:
    selected = option_menu(
        menu_title='Navigation',
        options=['Welcome Page', 'Student Q&A', 'Lecture Assistance', 'Quiz Generator', 'Module-Based Learning', 'Code Generator'],
        icons=['house', 'chat-left-dots', 'book', 'clipboard-data', 'layers'],
        menu_icon='cast',
        default_index=0
    )

# Current Date and Time
def current_time():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

st.sidebar.markdown(f'*Current Time:* {current_time()}')

# OpenAI Key (To be replaced with environment variable in deployment)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Welcome Page
if selected == 'Welcome Page':
    try:
        st.image('https://github.com/Chattopadhyay/Arya/raw/main/IMG_7632.JPEG', use_container_width=True)
    except Exception as e:
        st.error("Image could not be loaded. Please check the path or internet connection.")

    st.markdown("""
    <div class='feature-card'>
    <strong>Student Q&A:</strong> Get real-time answers to your questions.
    </div>
    <div class='feature-card'>
    <strong>Lecture Assistance:</strong> Generate lecture notes and key takeaways instantly.
    </div>
    <div class='feature-card'>
    <strong>Quiz Generator:</strong> Create quizzes for instant assessments.
    </div>
    <div class='feature-card'>
    <strong>Module-Based Learning:</strong> Dive deep into specific AI/ML topics.
    </div>
    <div class='feature-card'>
    <strong>Code Generator:</strong> Generate Python code for AI/ML models.
    </div>
    """, unsafe_allow_html=True)
