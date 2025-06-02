import streamlit as st
from langchain_helper import load_faiss_vectorstore, get_answer_from_query

st.title("🩺 GenAI-Powered Patient Query Assistant")

vectorstore = load_faiss_vectorstore("faiss_index")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask your insurance question:")

if query:
    answer = get_answer_from_query(vectorstore, query)
    st.session_state.chat_history.append((query, answer))

if st.session_state.chat_history:
    for q, a in st.session_state.chat_history:
        st.markdown(f"**You:** {q}")
        st.markdown(f"**Assistant:** {a}")
