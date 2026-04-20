import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

# ---------------- PAGE UI ----------------
st.set_page_config(
    page_title="Information Extractor",
    page_icon="✨",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #38bdf8;
    margin-bottom: 5px;
}
.sub-title {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}
.result-box {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">✨ Information Extractor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Paste any paragraph and extract smart structured information instantly</div>', unsafe_allow_html=True)

# ---------------- MODEL ----------------
model = ChatMistralAI(
    model="mistral-small-2603"
)

# ---------------- PROMPT ----------------
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an intelligent information extraction assistant.

Your task is to read the given paragraph and extract all useful information in a clean human-readable format.

Focus on identifying:

1. Title / Name
2. Type
3. Genre / Category
4. Release Year / Date
5. Language
6. Country / Origin
7. Director / Creator
8. Producer / Author / Owner
9. Main Cast / Important People
10. Characters and Roles
11. Story / Main Description
12. Key Themes / Messages
13. Famous Quotes / Dialogues
14. Important Keywords
15. Any Extra Useful Facts
16. Quick Summary

Rules:
- Extract only what is clearly mentioned.
- If missing, write "Not Mentioned".
- Keep output clean.
- Do not return JSON.
"""),

    ("human", "extract information from the following paragraph: {paragraph}")
])

# ---------------- INPUT ----------------
para = st.text_area(
    "📄 Enter Paragraph",
    placeholder="Paste your paragraph here...",
    height=250
)

col1, col2 = st.columns(2)

with col1:
    extract_btn = st.button("🚀 Extract", use_container_width=True)

with col2:
    clear_btn = st.button("🗑 Clear", use_container_width=True)

if clear_btn:
    st.rerun()

# ---------------- OUTPUT ----------------
if extract_btn:
    if para.strip():
        with st.spinner("Analyzing paragraph..."):
            final_prompt = prompt.invoke({"paragraph": para})
            response = model.invoke(final_prompt)

        st.success("Extraction Complete ✅")

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(response.content)
        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("Please enter a paragraph first.")