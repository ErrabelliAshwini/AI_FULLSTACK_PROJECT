
import streamlit as st
import ollama

# Page title
st.title("🤖 Welcome to ChatBot App!!")
st.write("Ask me anything!")

# Rerun button
if st.button("🔄 Rerun"):
    st.rerun()

# Store conversation history
if "msgs" not in st.session_state:
    st.session_state.msgs = []

# Display previous messages
for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
question = st.chat_input("Type your question...")

if question:

    # Display user message
    with st.chat_message("user"):
        st.write(question)

    # Save user message
    st.session_state.msgs.append({
        "role": "user",
        "content": question
    })

    # Show loading message
    with st.spinner("Thinking..."):

        # Get response from Ollama
        response = ollama.chat(
            model="llama3.2:3b",
            messages=st.session_state.msgs
        )

        answer = response["message"]["content"]

    # Save AI response
    st.session_state.msgs.append({
        "role": "assistant",
        "content": answer
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.write(answer)
        
