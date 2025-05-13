
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

# Student Q&A
elif selected == 'Student Q&A':
    st.header('Student Q&A')
    question = st.text_input('Enter your question:')
    if st.button('Get Answer'):
        if question:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=question,
                max_tokens=150
            )
            st.write(response.choices[0].text)

# Lecture Assistance
elif selected == 'Lecture Assistance':
    st.header('Lecture Assistance')
    topic = st.text_input('Enter the lecture topic:')
    if st.button('Generate Lecture Notes'):
        if topic:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'Generate detailed lecture notes on {topic}.',
                max_tokens=500
            )
            st.write(response.choices[0].text)

# Quiz Generator
elif selected == 'Quiz Generator':
    st.header('Interactive Quiz Generator')
    quiz_topic = st.text_input('Enter Topic for Quiz:')
    num_questions = st.number_input('Number of Questions:', min_value=1, max_value=10, step=1)
    if st.button('Generate Interactive Quiz'):
        if quiz_topic:
            st.success(f'Generating {num_questions} questions for: "{quiz_topic}"')
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'Generate {int(num_questions)} multiple-choice quiz questions on the topic: {quiz_topic} with options (A, B, C, D) and the correct answer clearly marked.',
                max_tokens=1000
            )
            st.write(response.choices[0].text)

# Module-Based Learning
elif selected == 'Module-Based Learning':
    st.header('Module-Based Learning')
    modules = ['Foundations of AI & ML', 'Supervised Learning', 'Unsupervised Learning', 'Neural Networks & Deep Learning']
    selected_module = st.selectbox('Select a Module:', modules)
    if st.button('Explore Module'):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'Provide a detailed summary of the module: {selected_module}.',
            max_tokens=500
        )
        st.write(response.choices[0].text)

# Code Generator
elif selected == 'Code Generator':
    st.header('Code Generator')
    model_name = st.text_input('Enter the model name (e.g., Linear Regression, Decision Tree):')
    if st.button('Generate Code'):
        if model_name:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'Generate Python code for {model_name}.',
                max_tokens=300
            )
            st.code(response.choices[0].text)
