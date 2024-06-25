import streamlit as st
import openai
import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set your OpenAI API key here
openai_api_key = os.getenv('OPENAI_API_KEY')

# Validate the API key
if not openai_api_key:
    st.error("OpenAI API key not found. Please set it in the .env file.")
    st.stop()

openai.api_key = openai_api_key

st.set_page_config(page_title="MusicBot", page_icon=":musical_note:", layout="wide")

st.sidebar.title("MusicBot Options")
st.sidebar.write("Customize your experience")

if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

st.title("MusicBot")
st.write("Welcome to MusicBot! Ask me anything about music, and I'll do my best to provide helpful information.")

# Display conversation history
st.write("## Conversation History")
for chat in st.session_state.conversation_history:
    if chat["role"] == "user":
        st.write(f"**You:** {chat['content']}")
    else:
        st.write(f"**MusicBot:** {chat['content']}")

def get_bot_response(user_input):
    st.session_state.conversation_history.append({"role": "user", "content": user_input})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=st.session_state.conversation_history
        )
        bot_message = response['choices'][0]['message']['content'].strip()
        st.session_state.conversation_history.append({"role": "assistant", "content": bot_message})
        return bot_message
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, I couldn't process your request."

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        bot_response = get_bot_response(user_input)
        st.write(f"**You:** {user_input}")
        st.write(f"**MusicBot:** {bot_response}")
        st.experimental_rerun()

if st.button("Clear Conversation"):
    st.session_state.conversation_history = []
    st.experimental_rerun()

# Advanced options
st.sidebar.write("## Advanced Options")
with st.sidebar.expander("Prompt Patterns"):
    if st.checkbox("Use Persona-based responses"):
        st.write("Persona-based responses enabled.")
        # Implement persona-based response customization
    if st.checkbox("Enable Chain of Thought"):
        st.write("Chain of Thought enabled.")
        # Implement chain of thought customization

# Music Recommendations
st.sidebar.write("## Music Recommendations")
if st.sidebar.button("Get Song Recommendation"):
    recommendation = get_bot_response("Can you recommend a song?")
    st.sidebar.write(recommendation)

if st.sidebar.button("Get Artist Recommendation"):
    recommendation = get_bot_response("Can you recommend an artist?")
    st.sidebar.write(recommendation)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
