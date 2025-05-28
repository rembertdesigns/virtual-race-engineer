import streamlit as st
from rag.qa_chain import run_query

st.set_page_config(page_title="Virtual Race Engineer", layout="centered")

st.title("🏎️ Virtual Race Engineer Assistant")
st.markdown("Ask anything about F1 races, strategies, or performance!")

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        response = run_query(query)
        st.success(response)
