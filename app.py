import streamlit as st

st.set_page_config(
    page_title="MonAI",
    page_icon="🤖"
)

st.title("🤖 MonAI")
st.caption("Ton assistant personnel")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Écris ton message...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    response = "Bonjour 👋 ! Je suis MonAI."

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)
