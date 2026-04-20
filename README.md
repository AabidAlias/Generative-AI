# 🤖 Generative AI Projects Collection

A beginner-friendly collection of **Generative AI mini-projects** built using **Python, LangChain, Mistral AI, Hugging Face, and Streamlit**.

This repository contains multiple AI-powered applications for learning, experimenting, and building real-world AI tools.

---

# 📁 Project Folder Structure

```bash
GENERATIVE AI/
│── .venv/
│── chatmodel/
│   ├── chat.py
│   └── huggingface.py
│
│── extractmodel/
│   ├── genextract.py
│   └── genextractwithUI.py
│
│── static/
│── templates/
│   └── index.html
│
│── .env
│── .gitignore
│── app.py
│── main.py
│── pyproject.toml
│── README.md
│── requirements.txt
│── uv.lock


🚀 Projects Included
1️⃣ AI Email Writer

Generate professional emails using Mistral AI.

Example Uses:
Leave application
Job request mail
College formal mail

Run:

python chatmodel/chat.py
2️⃣ Mood Based AI Chatbot

A Streamlit chatbot where responses change based on selected mood.

Available Moods:
😄 Funny
😢 Sad
😡 Angry
Features:
Real-time AI responses
Chat memory
Mood switching
Beautiful UI

Run:

streamlit run chatmodel/huggingface.py
3️⃣ Information Extractor (CLI)

Paste any paragraph and extract structured information.

Extracts:
Title / Name
Type
Genre
Language
Country
Keywords
Summary
Extra facts

Run:

python extractmodel/genextract.py
4️⃣ Information Extractor (Web UI)

Modern Streamlit version of the extractor.

Features:
Paste paragraph
Click Extract
Smart formatted output
Dark UI

Run:

streamlit run extractmodel/genextractwithUI.py
🛠️ Tech Stack
Python
LangChain
Mistral AI
Hugging Face
Streamlit
dotenv
⚙️ Installation Guide
1️⃣ Clone Repository
git clone https://github.com/yourusername/generative-ai-projects.git
cd generative-ai-projects
2️⃣ Create Virtual Environment
python -m venv .venv
Activate Environment
Windows
.venv\Scripts\activate
Mac/Linux
source .venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt