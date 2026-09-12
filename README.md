# MonIA
MonAI — Une application de chat avec intelligence artificielle.
import streamlit as st

st.set_page_config(
    page_title="MonAI",
    page_icon="🤖"
)

st.title("🤖 MonAI")
st.caption("Ton assistant personnel avec mémoire 🧠")

# Mémoire de la conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mémoire personnelle
if "memory" not in st.session_state:
    st.session_state.memory = []

# Afficher la mémoire
if st.session_state.memory:
    with st.sidebar:
        st.subheader("🧠 Ma mémoire")
        for item in st.session_state.memory:
            st.write("• " + item)

# Afficher la conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Écris ton message...")

if prompt:

    # Message utilisateur
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Détection simple de quelques informations à mémoriser
    texte = prompt.lower()

    if "je m'appelle " in texte:
        nom = prompt.split("je m'appelle ", 1)[1]
        souvenir = "Son prénom est " + nom
        if souvenir not in st.session_state.memory:
            st.session_state.memory.append(souvenir)

    elif "mon prénom est " in texte:
        nom = prompt.split("mon prénom est ", 1)[1]
        souvenir = "Son prénom est " + nom
        if souvenir not in st.session_state.memory:
            st.session_state.memory.append(souvenir)

    elif "j'aime " in texte:
        souvenir = prompt
        if souvenir not in st.session_state.memory:
            st.session_state.memory.append(souvenir)

    # Réponse
    if "bonjour" in texte or "salut" in texte:
        response = "Bonjour 👋 ! Je suis MonAI. Je peux maintenant commencer à mémoriser certaines informations."

    elif "mémoire" in texte:
        if st.session_state.memory:
            response = "🧠 Voici ce que je me souviens :\n\n" + "\n".join(
                "- " + x for x in st.session_state.memory
            )
        else:
            response = "🧠 Ma mémoire est encore vide."

    else:
        response = "J'ai bien reçu ton message 🤖"

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)
