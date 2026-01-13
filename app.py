import streamlit as st
import ollama

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="🤖 AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# ---------- CUSTOM CSS ----------
st.markdown(
    """
    <style>
    body {
        background-color: #0f172a;
    }

    .main {
        background-color: #0f172a;
    }

    h1 {
        background: linear-gradient(90deg, #38bdf8, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        text-align: center;
    }

    .subtitle {
        text-align: center;
        color: #cbd5e1;
        margin-bottom: 30px;
        font-size: 16px;
    }

    .stChatMessage {
        background-color: #020617;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- HEADER ----------
st.markdown("<h1>🤖 ChatGPT AI Assistant</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Powered by Local LLM (Ollama • phi3:mini)</div>",
    unsafe_allow_html=True
)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("**Model:** phi3:mini")
    st.markdown("**Mode:** Local & Offline")
    st.markdown("---")
    st.markdown("👩‍💻 Built by You")
    st.markdown("🚀 LLM Project Demo")

# ---------- CHAT STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- DISPLAY CHAT ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- INPUT ----------
prompt = st.chat_input("Ask me anything... ✨")

if prompt:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.spinner("🤖 Thinking..."):
        response = ollama.chat(
            model="phi3:mini",
            messages=st.session_state.messages
        )
        ai_reply = response["message"]["content"]

    st.session_state.messages.append(
        {"role": "assistant", "content": ai_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
