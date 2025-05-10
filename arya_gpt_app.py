
# AryaGPT - AI Teaching Assistant

import streamlit as st
from datetime import datetime
import openai
from streamlit_option_menu import option_menu
import random

# Page Configuration
st.set_page_config(page_title='AryaGPT - Your AI Teaching Assistant', page_icon='🤖', layout='centered')

# Title and Description
st.title('AryaGPT - Your AI Teaching Assistant')
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
    st.image('https://raw.githubusercontent.com/Chattopadhyay/Arya/main/IMG_7632.JPEG', use_container_width=True)
    st.header('Welcome to AryaGPT - Your Personalized AI Teaching Assistant')
    st.markdown("""
    - Student Q&A: Get real-time answers to your questions.
    - Lecture Assistance: Generate lecture notes and key takeaways instantly.
    - Quiz Generator: Create quizzes for instant assessments.
    - Module-Based Learning: Dive deep into specific AI/ML topics.
    - Code Generator: Generate Python code for AI/ML models.

    Select a functionality from the sidebar to get started!
    """)

# Student Q&A Module
elif selected == 'Student Q&A':
    st.header('Student Q&A')
    st.markdown('Ask me anything related to AI, ML, or Course Topics!')
    question = st.text_input('Enter your question:')
    if st.button('Get Answer'):
        if question:
            st.success(f'Answering your question: "{question}"')
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=question,
                max_tokens=150
            )
            st.info(response.choices[0].text)

# Lecture Assistance Module
elif selected == 'Lecture Assistance':
    st.header('Lecture Assistance')
    st.markdown('Generate lecture notes and key takeaways instantly.')
    topic = st.text_input('Enter Lecture Topic:')
    if st.button('Generate Lecture Notes'):
        if topic:
            st.success(f'Generating notes for: "{topic}"')
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'Generate lecture notes on the topic: {topic}',
                max_tokens=300
            )
            st.info(response.choices[0].text)

# Interactive Quiz Generator Module
elif selected == 'Quiz Generator':
    st.header('Interactive Quiz Generator')
    st.markdown('Create interactive quizzes and test your knowledge.')
    quiz_topic = st.text_input('Enter Topic for Quiz:')
    num_questions = st.number_input('Number of Questions:', min_value=1, max_value=10, step=1)
    if st.button('Generate Interactive Quiz'):
        if quiz_topic:
            st.success(f'Generating {num_questions} questions for: "{quiz_topic}"')
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'Generate {int(num_questions)} multiple-choice quiz questions on the topic: {quiz_topic} with the correct answer marked and a brief explanation for each.',
                max_tokens=1000
            )
            st.code(response.choices[0].text, language='python')

# Code Generator
elif selected == 'Code Generator':
    st.header('Code Generator')
    st.markdown('Generate ready-to-use Python code for any AI or ML algorithm.')
    algo_name = st.text_input('Enter the Algorithm Name:')
    if st.button('Generate Code'):
        if algo_name:
            st.success(f'Generating Python code for: "{algo_name}"')
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'Generate Python code for the machine learning algorithm: {algo_name} with proper comments and structured format.',
                max_tokens=400
            )
            st.code(response.choices[0].text, language='python')
