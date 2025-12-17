import streamlit as st
import os
import numpy as np

CURRENT_PATH = os.getcwd()
UPLOADED_DIR = "uploads"

st.title("RAG Chatbot")
st.text("Upload files and chat with all of them")
st.divider()

upload_folder = os.path.join(CURRENT_PATH, UPLOADED_DIR)
os.makedirs(upload_folder, exist_ok=True)

uploaded_files = st.file_uploader(label="Upload a file", type=["pdf"],accept_multiple_files=True, help="Upload a PDF file, preferably research papers")


if uploaded_files:
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name
        # file_type = uploaded_file.type

        save_path = os.path.join(upload_folder, file_name)
        
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask a question about the research papers..."):
    with st.chat_message("user"):
        st.write(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.write(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
