
# AryaGPT - AI Teaching Assistant

import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(page_title='AryaGPT - Your AI Teaching Assistant', page_icon='🤖', layout='centered')

# Title and Description
st.title('🌟 AryaGPT - Your AI Teaching Assistant 🌟')
st.markdown('Empowering your classroom with **AI-driven insights** and **automation**.')

# Sidebar for Navigation
st.sidebar.title('🚀 Navigation')
options = ['Student Q&A', 'Lecture Assistance', 'Quiz Generator', 'Module-Based Learning']
choice = st.sidebar.radio('Choose Functionality:', options)

# Current Date and Time
def current_time():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

st.sidebar.markdown(f'*🕒 Current Time:* {current_time()}')

# Student Q&A Module
if choice == 'Student Q&A':
    st.header('💡 Student Q&A')
    st.markdown('Ask me anything related to **AI, ML, or Course Topics**!')
    question = st.text_input('🔍 Enter your question:')
    if st.button('Get Answer 💬'):
        if question:
            st.success(f'Answering your question: "{question}"')
            st.info('AI Response will appear here.')

# Lecture Assistance Module
elif choice == 'Lecture Assistance':
    st.header('📚 Lecture Assistance')
    st.markdown('Generate lecture notes and key takeaways instantly.')
    topic = st.text_input('📌 Enter Lecture Topic:')
    if st.button('Generate Lecture Notes 📝'):
        if topic:
            st.success(f'Generating notes for: "{topic}"')
            st.info('Lecture notes will appear here.')

# Quiz Generator Module
elif choice == 'Quiz Generator':
    st.header('📝 Quiz Generator')
    st.markdown('Create quizzes with instant question generation.')
    quiz_topic = st.text_input('📌 Enter Topic for Quiz:')
    num_questions = st.number_input('🔢 Number of Questions:', min_value=1, max_value=20, step=1)
    if st.button('Generate Quiz 🎯'):
        if quiz_topic:
            st.success(f'Generating {num_questions} questions for: "{quiz_topic}"')
            st.info('Quiz questions will be listed here.')

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
        st.info(f'Module content for "{selected_module}" will appear here.')

st.sidebar.info('💡 AryaGPT v0.2 - Integrated Course Outline | Powered by OpenAI')
