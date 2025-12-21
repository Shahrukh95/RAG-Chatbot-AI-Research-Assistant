import streamlit as st
from io import BytesIO
import requests

# BACKEND URL
BACKEND_URL = "http://localhost:8000"



# ---

# INTRO TAGS
st.title("RAG Chatbot")
st.text("Upload files and chat with all of them")
st.divider()


# FILE UPLOADER
uploaded_files = st.file_uploader(label="Upload a file", type=[],accept_multiple_files=True, help="Upload a PDF file, preferably research papers")

if uploaded_files:
    all_files = []
    for uploaded_file in uploaded_files:
        file_bytes = uploaded_file.getvalue() # GET THE FILE BYTES (to handle warning in requests library)
        all_files.append(
            ('files', (uploaded_file.name, BytesIO(file_bytes), uploaded_file.type))
        )


    
    # SEND ALL FILES TO THE BACKEND
    response = requests.post(url=BACKEND_URL + "/ingest", files=all_files)
    st.write(response.json())


# if uploaded_files:
#     for uploaded_file in uploaded_files:
#         file_name = uploaded_file.name
#         # file_type = uploaded_file.type

#         save_path = os.path.join(upload_folder, file_name)
        
#         with open(save_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())


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
