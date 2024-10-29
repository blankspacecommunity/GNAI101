# Import the 'os' module for interacting with the operating system
import os

# Attempt to import the 'google.generativeai' library
# This library allows us to interact with Google's generative AI models
try:
    import google.generativeai as genai
except ImportError:
    # If the library isn't installed, use 'pip' to install it, then try to import it again
    os.system('pip install google-generativeai')
    import google.generativeai as genai

# Activity 0: Creating a simple Command-Line Interface (CLI) chatbot using the Gemini model
# CLI refers to interacting with the program inside the terminal

# Configure the generative AI library with your personal API key
# This key allows access to Google's generative AI services. Replace 'YOUR_API_KEY' with your actual API key.
genai.configure(api_key='YOUR_API_KEY')

# Choose the generative model you want to use from Google's options
# Here, we use the 'gemini-1.5-flash' model, which is a fast and conversational AI model
model = genai.GenerativeModel('models/gemini-1.5-flash')

# Start a new chat session using the model
# The session allows us to keep track of the conversation flow
chat = model.start_chat()

# Set up an interactive loop where the user can type questions and get answers
while True:
    # Prompt the user for input
    user_input = input('You: ')
    
    # If the user types 'exit', break the loop to end the chat
    if user_input.lower() == 'exit':
        break
    
    # Send the user's message to the chat model and get a response
    response = chat.send_message(user_input)
    
    # Print the model's response
    print('Gemini:', response.text)
