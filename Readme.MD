# MusicBot

MusicBot is a Streamlit application that allows users to interact with a chatbot about music-related topics. The chatbot leverages OpenAI's GPT-4 model to generate responses.

## Prerequisites

- Python 3.7+
- Streamlit
- OpenAI Python client library
- Python-dotenv

## Setup

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
pip install streamlit openai python-dotenv

4. Create a .env file in the root directory of your project and add your OpenAI API key:
Create a .env file in the root directory of your project and add your OpenAI API key:

## Running the Application

1. Run the Streamlit app:
streamlit run musicbot.py

2. Open your web browser and go to http://localhost:8501 to access the application.

## Features
Chat Interface: Users can interact with the MusicBot by typing questions related to music.
Conversation History: The conversation history is displayed in the main interface.
Clear Conversation: Users can clear the conversation history with a button click.
Advanced Options: Users can enable persona-based responses and chain of thought for more advanced interactions.
Music Recommendations: Users can get song and artist recommendations from the sidebar.

## File Descriptions
musicbot.py: The main Streamlit application file.
style.css: The CSS file for custom styling.
.env: Environment file containing the OpenAI API key (not included in the repository for security reasons).

## Custom Styling

The style.css file provides custom styling for the Streamlit components. The following styles are included:

body {
    font-family: Arial, sans-serif;
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}

.stTextInput>div>input {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
}

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Streamlit
OpenAI
dotenv