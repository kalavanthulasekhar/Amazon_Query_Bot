import streamlit as st
import os

api_key = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI


def load_data():
    with open("data/docs.txt", "r", encoding="utf-8") as f:
        return f.read()

context_data = load_data()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)


def ask_bot(query):
    prompt = f"""
You are a helpful and friendly chatbot 😊.

STRICT RULES:
- Answer ONLY from the context below
- If answer is not found, say: "Sorry, I don't have that information."

Context:
{context_data}

Question:
{query}

Answer:
"""
    response = llm.invoke(prompt)
    return response.content


st.title("🤖 Amazon Chatbot (RAG - Gemini)")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask your question:")

if user_input:
    answer = ask_bot(user_input)

    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", answer))

for role, msg in st.session_state.chat:
    st.write(f"**{role}:** {msg}")