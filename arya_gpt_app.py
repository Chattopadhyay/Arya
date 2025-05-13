
# AryaGPT - AI Teaching Assistant

import streamlit as st
from datetime import datetime
import openai
from streamlit_option_menu import option_menu
import random

# Page Configuration
st.set_page_config(page_title='AryaGPT - Your AI Teaching Assistant', page_icon='🤖', layout='wide')

# Custom CSS for enhanced look and feel
st.markdown("""
    <style>
        body {
            background-color: #f8f9fc;
        }
        .main-header {
            background: linear-gradient(90deg, #4B6EAF, #6E87D6, #4B6EAF);
            background-size: 600% 600%;
            animation: gradientShift 10s ease infinite;
            color: white;
            padding: 30px;
            text-align: center;
            font-size: 28px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 2px 4px 10px rgba(0, 0, 0, 0.2);
        }
        @keyframes gradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        .subtitle {
            color: #DDE6F1;
            font-size: 18px;
            margin-top: -15px;
        }
        .feature-card {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(8px);
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 4px 6px 18px rgba(0, 0, 0, 0.15);
        }
        .sidebar .stButton button {
            background-color: #4B6EAF;
            color: white;
            border-radius: 5px;
        }
        .block-container {
            max-width: 1200px;
            margin: auto;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            font-size: 14px;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">AryaGPT - Your AI Teaching Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Empowering Classrooms with AI-Driven Learning</div>', unsafe_allow_html=True)

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

    # Feature Cards in Grid Layout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='feature-card'>
        <strong>Student Q&A:</strong> Get real-time answers to your questions.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='feature-card'>
        <strong>Lecture Assistance:</strong> Generate lecture notes and key takeaways instantly.
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class='feature-card'>
        <strong>Quiz Generator:</strong> Create quizzes for instant assessments.
        </div>
        """, unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    with col4:
        st.markdown("""
        <div class='feature-card'>
        <strong>Module-Based Learning:</strong> Dive deep into specific AI/ML topics.
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class='feature-card'>
        <strong>Code Generator:</strong> Generate Python code for AI/ML models.
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""<div class='footer'>
    Developed and Powered by AryaGPT | © 2025
    </div>""", unsafe_allow_html=True)
