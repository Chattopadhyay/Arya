
# Arya – My AI Teaching Assistant

import streamlit as st
from datetime import datetime
import openai
from streamlit_option_menu import option_menu
import random

# Page Configuration
st.set_page_config(page_title='Arya – My AI Teaching Assistant', page_icon='🤖', layout='centered')

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
st.markdown('<div class="main-header">Arya – My AI Teaching Assistant</div>', unsafe_allow_html=True)
st.markdown('AI and ML, your way — faster, sharper, and brilliantly personal.')

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
        st.image('https://github.com/Chattopadhyay/Arya/raw/main/IMG_7891.JPEG', use_container_width=True)
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

# Quiz Generator Module
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
                if q and 'Answer:' in q:
                    question, answer = q.split('Answer:')
                    st.markdown(f'**Q{idx+1}:** {question.strip()}')
                    options = ['Option A', 'Option B', 'Option C', 'Option D']
                    selected_option = st.radio(f'Select your answer for Q{idx+1}:', options, key=f'ans_{idx}')

                    if st.button(f'Submit Answer for Q{idx+1}', key=f'submit_{idx}'):
                        if selected_option.strip() in answer.strip():
                            st.success('✅ Correct Answer!')
                            score += 1
                        else:
                            st.error(f'❌ Incorrect Answer. The correct answer is {answer.strip()}')

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
            prompt=f'Provide a detailed summary of the module: {selected_module} along with its industry applications and examples.',
            max_tokens=500
        )
        st.info(response.choices[0].text)
