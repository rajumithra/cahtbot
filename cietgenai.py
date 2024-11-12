import streamlit as st
import google.generativeai as genai

# Configure your API key for Gemini (replace with your actual key)
genai.configure(api_key="AIzaSyBT6cyhpiCVI6uxmHQiJ_EDN9_iCfblEr8")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to interact with Gemini
def chat_with_gemini(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit front-end code
st.title("Chalapthi AI Chatbot")
st.write("Welcome to the Chalapathi AI Chatbot! Type your message below:")

# Initialize session state to store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input box
user_input = st.text_input("You:", key="user_input")

# When user sends input, get response and update chat history
if st.button("Send"):
    if user_input:
        gemini_response = chat_with_gemini(user_input)
        
        # Store user input and bot response in chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Gemini", gemini_response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.write(f"**You:** {message}")
    else:
        st.write(f"**Gemini:** {message}")
