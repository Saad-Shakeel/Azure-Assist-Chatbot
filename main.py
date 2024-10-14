import streamlit as st
import time
import google.generativeai as genai
import button
# Configure Gemini API
Gemeni_API = "AIzaSyB8GRg8nG7RaAYPddEJ0PuY-jVoysueJT4"
genai.configure(api_key=Gemeni_API)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Function to start a new chat session
def start_new_chat():
    return model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Role: Microsoft Azure Specialist\nGuidelines:\nAzure-Only Focus: Provide clear, detailed answers exclusively related to Microsoft Azure-its services, tools, features, and best practices. Avoid discussing other cloud platforms or unrelated technologies.\nLink to Azure Documentation: Whenever possible, include relevant Microsoft Azure documentation links for further reference.\nRedirect Off-Topic Inquiries: If the inquiry isn't about Azure, respond with: \"Thank you for your question! It appears that this topic isn't related to Azure. To get the help you need, I suggest contacting [relevant department/resource]. If you need any assistance with Azure, feel free to ask!",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Understood! I'm ready to assist you with your Microsoft Azure queries. \n\nI will provide:\n\n* **Azure-Specific Answers:** My responses will be exclusively focused on Microsoft Azure services, tools, features, and best practices. \n* **Detailed Explanations:**  I will provide comprehensive and informative answers.\n* **Azure Documentation Links:**  Where appropriate, I will include links to relevant Microsoft Azure documentation for your reference. \n* **Redirection for Off-Topic Inquiries:**  If your question is not related to Azure, I will politely redirect you to the appropriate resource.\n\nLet's get started!  What Azure questions can I help you with today? \n",
                ],
            },
        ]
    )

# Initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = start_new_chat()

# Set page configuration
st.set_page_config(
    page_title="Azure Assist",  
    page_icon="logo.png",  
    layout="wide",
    initial_sidebar_state="expanded"
)

# Streamlit app title and caption
st.title("Azure Assist 🌐")
st.subheader("Welcome to AzureBot! 🚀 How can I assist you in mastering Microsoft Azure today?")
st.caption("Developed by Saad Shakeel")
button.Button()
# "Start New Chat" button
if st.button("Start New Chat"):
    st.session_state.messages = []  # Clear chat history
    st.session_state.chat_session = start_new_chat()  # Start a new chat session
    st.rerun()  # Refresh the app to reflect the changes

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Tell me your Azure needs, and I'll provide the answers! 📘"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from the AI model
    chat_session = st.session_state.chat_session
    response = chat_session.send_message(prompt)

    def response_generator():
        content = response.text.split()  # Split the response into words
        generated_response = ""  # Initialize an empty string to build the response
        for word in content:
            generated_response += word + " "  # Add each word to the response
            yield generated_response.strip()  # Yield the current full sentence so far
            time.sleep(0.05)  # Adjust the speed of word generation here

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response_placeholder = st.empty()  # Create an empty placeholder to update text
        final_response = ""  # Initialize an empty string for the final response
        for sentence in response_generator():
            final_response = sentence  # Update the final response
            response_placeholder.markdown(final_response)

    # Pause briefly to ensure content is displayed correctly
    time.sleep(0.1)

    # Update the placeholder with the final response
    response_placeholder.markdown(final_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    st.rerun()
