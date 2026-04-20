import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

 
st.set_page_config(page_title="Mood AI Chatbot", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f172a;
        color: white;
    }
    .title {
        text-align:center;
        font-size:40px;
        font-weight:bold;
        color:#38bdf8;
        margin-bottom:20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🤖 Mood Based AI Chatbot</div>', unsafe_allow_html=True)

 
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    max_new_tokens=100,
    temperature=0.9,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

# ---------------- MOOD SELECT ----------------
mood = st.selectbox(
    "Choose Chat Mood:",
    ["Funny 😄", "Sad 😢", "Angry 😡"]
)

# ---------------- SYSTEM PROMPT ----------------
if mood == "Funny 😄":
    system_prompt = "You are a funny assistant. Reply with humor and jokes."
elif mood == "Sad 😢":
    system_prompt = "You are a sad emotional assistant. Reply in a soft, emotional, sad tone."
elif mood == "Angry 😡":
    system_prompt = "You are an angry assistant. Reply in an aggressive, frustrated tone."

# ---------------- SESSION STATE ----------------
if "message" not in st.session_state or st.session_state.get("last_mood") != mood:
    st.session_state.message = [
        SystemMessage(content=system_prompt)
    ]
    st.session_state.last_mood = mood

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.message:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# ---------------- INPUT ----------------
prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.message.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.message)

        st.markdown(response.content)

    st.session_state.message.append(AIMessage(content=response.content))