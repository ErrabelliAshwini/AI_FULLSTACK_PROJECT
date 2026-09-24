import streamlit as st
import ollama

st.title("My AI ChatBot")
st.write("Welcome! Ask me anything.")

# Badges
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] "
    ":orange-badge[⚠️ Needs review] "
    ":gray-badge[Deprecated]"
)

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
question = st.chat_input("Type your message....")

if question:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # Get response from Ollama
    response = ollama.chat(
        model="llama3.2:3b",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)