
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
    try:
        st.image('https://github.com/Chattopadhyay/Arya/raw/main/IMG_7632.JPEG', use_container_width=True)
    except Exception as e:
        st.error("Image could not be loaded. Please check the path or internet connection.")

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
                prompt=f'Generate {int(num_questions)} multiple-choice quiz questions on the topic: {quiz_topic} with options (A, B, C, D) and the correct answer clearly marked.',
                max_tokens=1000
            )
            
            questions = response.choices[0].text.strip().split('\n')
            score = 0
            
            for idx, q in enumerate(questions):
                if q:
                    st.markdown(f'**Q{idx+1}:** {q}')
                    options = ['Option A', 'Option B', 'Option C', 'Option D']
                    answer = st.radio(f'Select your answer for Q{idx+1}:', options, key=f'ans_{idx}')
                    if st.button(f'Submit Answer for Q{idx+1}', key=f'submit_{idx}'):
                        if '✔' in q:
                            st.success('✅ Correct Answer!')
                            score += 1
                        else:
                            st.error('❌ Incorrect Answer.')
            
            st.markdown(f'### 🏆 Your Final Score: {score} / {num_questions}')

# Module-Based Learning
elif selected == 'Module-Based Learning':
    st.header('Module-Based Learning')
    modules = [
        'Foundations of AI & ML',
        'Supervised Learning',
        'Unsupervised Learning',
        'Neural Networks & Deep Learning',
        'Natural Language Processing',
        'Recommendation Systems',
        'Generative AI & Prompt Engineering',
        'Ethics, Bias, and Future of Work'
    ]
    selected_module = st.selectbox('Select a Module:', modules)
    if st.button('Explore Module'):
        st.success(f'Loading content for: {selected_module}')
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'Provide a detailed summary of the module: {selected_module} and its industry applications.',
            max_tokens=500
        )
        st.info(response.choices[0].text)
