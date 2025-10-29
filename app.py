import streamlit as st
import requests

st.set_page_config(page_title="Customer Support AI Chatbot", layout="centered")
API_URL = "http://127.0.0.1:8000/chat"

st.title("💬 Customer Support AI Chatbot")

if "history" not in st.session_state:
    st.session_state["history"] = []

for chat in st.session_state["history"]:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

query = st.chat_input("Ask me anything about our products or support...")
if query:
    st.session_state["history"].append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            res = requests.post(API_URL, json={"question": query})
            answer = res.json().get("answer")
            st.markdown(answer)
    st.session_state["history"].append({"role": "assistant", "content": answer})
