
# AryaGPT - AI Teaching Assistant (OpenAI 1.14.3 Compatible Version)

import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu
from openai import OpenAI

client = OpenAI()

st.set_page_config(page_title='AryaGPT - AI Teaching Assistant', layout='wide')

st.markdown("""
    <style>
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
        }
        @keyframes gradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">AryaGPT - AI Teaching Assistant</div>', unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title='Navigation',
        options=['Welcome Page', 'Module-Based Learning'],
        icons=['house', 'layers'],
        menu_icon='cast',
        default_index=0
    )

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.sidebar.markdown(f'*Current Time:* {current_time()}')

if selected == 'Welcome Page':
    st.image('https://github.com/Chattopadhyay/Arya/raw/main/IMG_7632.JPEG')
    st.success("Welcome to AryaGPT, your AI Teaching Assistant.")

elif selected == 'Module-Based Learning':
    st.header('Module-Based Learning')
    modules = ['Foundations of AI & ML', 'Supervised Learning', 'Unsupervised Learning', 'Neural Networks & Deep Learning']
    selected_module = st.selectbox('Select a Module:', modules)
    if st.button('Explore Module'):
        try:
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "system", "content": "You are an AI tutor providing deep dives into learning modules."},
                    {"role": "user", "content": f"Provide a detailed summary of the module: {selected_module}."}
                ],
                temperature=0.7
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"OpenAI API Error: {e}")
