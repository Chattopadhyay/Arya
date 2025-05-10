
# AryaGPT - AI Teaching Assistant

import streamlit as st
from datetime import datetime
import openai

# Page Configuration
st.set_page_config(page_title='AryaGPT - Your AI Teaching Assistant', page_icon='🤖', layout='centered')

# Title and Description
st.title('🌟 AryaGPT - Your AI Teaching Assistant 🌟')
st.markdown('Empowering your classroom with **AI-driven insights** and **automation**.')

# Sidebar for Navigation
st.sidebar.title('🚀 Navigation')
options = ['Welcome Page', 'Student Q&A', 'Lecture Assistance', 'Quiz Generator', 'Module-Based Learning']
choice = st.sidebar.radio('Choose Functionality:', options)

# Current Date and Time
def current_time():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

st.sidebar.markdown(f'*🕒 Current Time:* {current_time()}')

# OpenAI Key (To be replaced with environment variable in deployment)
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Welcome Page
if choice == 'Welcome Page':
    st.header('Welcome to AryaGPT - Your Personalized AI Teaching Assistant')
    st.markdown('''
    - 💡 **Student Q&A:** Get real-time answers to your questions.
    - 📚 **Lecture Assistance:** Generate lecture notes and key takeaways instantly.
    - 📝 **Quiz Generator:** Create quizzes for instant assessments.
    - 📌 **Module-Based Learning:** Dive deep into specific AI/ML topics.

    Select a functionality from the sidebar to get started!
    ''')

# Student Q&A Module
elif choice == 'Student Q&A':
    st.header('💡 Student Q&A')
    st.markdown('Ask me anything related to **AI, ML, or Course Topics**!')
    question = st.text_input('🔍 Enter your question:')
    if st.button('Get Answer 💬'):
        if question:
            st.success(f'Answering your question: "{question}"')
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=question,
                max_tokens=150
            )
            st.info(response.choices[0].text)

# Lecture Assistance Module
elif choice == 'Lecture Assistance':
    st.header('📚 Lecture Assistance')
    st.markdown('Generate lecture notes and key takeaways instantly.')
    topic = st.text_input('📌 Enter Lecture Topic:')
    if st.button('Generate Lecture Notes 📝'):
        if topic:
            st.success(f'Generating notes for: "{topic}"')
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'Generate lecture notes on the topic: {topic}',
                max_tokens=300
            )
            st.info(response.choices[0].text)

# Quiz Generator Module
elif choice == 'Quiz Generator':
    st.header('📝 Quiz Generator')
    st.markdown('Create quizzes with instant question generation.')
    quiz_topic = st.text_input('📌 Enter Topic for Quiz:')
    num_questions = st.number_input('🔢 Number of Questions:', min_value=1, max_value=20, step=1)
    if st.button('Generate Quiz 🎯'):
        if quiz_topic:
            st.success(f'Generating {num_questions} questions for: "{quiz_topic}"')
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f'Generate {int(num_questions)} quiz questions on the topic: {quiz_topic}',
                max_tokens=400
            )
            st.info(response.choices[0].text)

# Module-Based Learning
elif choice == 'Module-Based Learning':
    st.header('📌 Module-Based Learning')
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
    if st.button('Explore Module 🚀'):
        st.success(f'Loading content for: {selected_module}')
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'Provide a detailed summary of the module: {selected_module}',
            max_tokens=500
        )
        st.info(response.choices[0].text)

st.sidebar.info('💡 AryaGPT v0.3 - Now with Real-Time Responses | Powered by OpenAI')
