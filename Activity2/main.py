# Import the 'os' module for interacting with the operating system
import os

# Attempt to import the 'google.generativeai' library
# This library allows us to interact with Google's generative AI models
try:
    import google.generativeai as genai
    import streamlit as st
except ImportError:
    # If the library isn't installed, use 'pip' to install it, then try to import it again
    # What is pip? 
    # It's a package manager for Python that allows us to install external libraries

    # 'pip3 install google-generativeai' Try this command in your terminal to install the library

    os.system('pip3 install google-generativeai streamlit')
    import google.generativeai as genai

# Activity 2: Creating a simple web-based chatbot using the Gemini model and Streamlit

# What is Streamlit?
#   Streamlit is a Python library that allows you to create web applications with simple Python scripts.
#   It's easier to use than traditional web frameworks like Flask or Django.
#   Go here to explore more -> https://docs.streamlit.io/

# Configure the generative AI library with your personal API key
# Go Here -> https://aistudio.google.com/app/apikey and copy your API key

# This key allows access to Google's generative AI services. Replace 'YOUR_API_KEY' with your actual API key.
genai.configure(api_key="YOUR_API_KEY")

# Choose the generative model you want to use from Google's options
# Here, we use the 'gemini-1.5-flash' model, which is a fast and conversational AI model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Start a new chat session using the model
# The session allows us to keep track of the conversation flow
chat = model.start_chat()

# This line here sets a title for the website, Try changing the title and color ;)
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Gemini Pro Chatbot</h1>",
    unsafe_allow_html=True,
)

st.header("Hello Welcome What is question...?")
st.write("")

# This here is the input field where the user can type in their question.
prompt = st.text_input(
    "Enter your question please...", placeholder="Question", label_visibility="visible"
)

if st.button("[SUBMIT]", use_container_width=True):
    # Send the user's message to the chat model and get a response

    response = chat.send_message(prompt)
    st.write("")
    st.header("Response")
    st.write("")

    # What is markdown?
    # Markdown is a lightweight markup language with plain-text-formatting syntax.
    # Which Means -> bold, italic, lists, quotes, links, and images can be added to the text.
    # Eg -> **Bold Text**, *Italic Text*, [Link Text](https://www.google.com)
    # You can learn more about markdown here -> https://www.markdownguide.org/basic-syntax/

    # Finally we display the response from the model
    st.markdown(response.text)