# src/ui_streamlit.py
import streamlit as st
import requests

st.title("Past Questions RAG Bot")
q = st.text_input("Ask a question:")

if st.button("Ask"):
    if q.strip():
        resp = requests.post("http://127.0.0.1:8000/ask", json={"q": q})
        if resp.ok:
            st.write(resp.json()["answer"])
        else:
            st.error(f"Error: {resp.text}")
    else:
        st.warning("Please enter a question")
