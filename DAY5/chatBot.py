import ollama
import streamlit as st

st.title("Welcome to ChatBot App!!")
with st.sidebar:
    uploaded_file=st.file_uploader("upload a text file..")
    if uploaded_file:
        st.write("FIle uploaded successfully")
        context=uploaded_file.read().decode("utf-8")
        st.text(context)
    


# Store conversation history
if "msgs" not in st.session_state:
    st.session_state.msgs = []

# Display previous messages
for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
question = st.chat_input("You:")

if question:

    # Add user message
    st.session_state.msgs.append({
        "role": "user",
        "content": question
    })

    # Display user message
    with st.chat_message("user"):
        st.write(question)

    # Get AI response
    with st.spinner("Thinking..."):

        response = ollama.chat(
            model="llama3.2:3b",
            messages=st.session_state.msgs
        )

    # Get answer
    answer = response["message"]["content"]

    # Add assistant message
    st.session_state.msgs.append({
        "role": "assistant",
        "content": answer
    })

    # Display assistant message
    with st.chat_message("assistant"):
        st.write(answer)