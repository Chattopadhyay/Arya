import streamlit as st
import openai
from datetime import datetime
from streamlit_option_menu import option_menu

# ✅ Easier: directly assign API key
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

st.set_page_config(page_title='AryaGPT', layout='wide')
st.markdown("<h1 style='text-align: center;'>AryaGPT - AI Teaching Assistant</h1>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu(
        menu_title='Navigation',
        options=['Welcome Page', 'Module-Based Learning'],
        icons=['house', 'book'],
        menu_icon='cast',
        default_index=0
    )

def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
st.sidebar.markdown(f'*Current Time:* {current_time()}')

if selected == 'Welcome Page':
    st.image('https://github.com/Chattopadhyay/Arya/raw/main/IMG_7632.JPEG', use_column_width=True)
    st.success("Welcome to AryaGPT – your AI-powered teaching companion.")

elif selected == 'Module-Based Learning':
    st.header('Module-Based Learning')
    modules = ['Foundations of AI & ML', 'Supervised Learning', 'Unsupervised Learning', 'Neural Networks']
    selected_module = st.selectbox('Select a Module:', modules)
    if st.button('Explore Module'):
        try:
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=f"Explain the module: {selected_module} with real-world examples.",
                max_tokens=500
            )
            st.write(response.choices[0].text.strip())
        except Exception as e:
            st.error(f"OpenAI error: {e}")