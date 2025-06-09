import streamlit as st
from ingestion.pdf_loader import load_pdf
from embedding.embedder import embed_and_store
from retrieval.retriever import retrieve_answer

st.set_page_config (page_title="RAG Assistant: FAQ RH", layout="wide")
st.title("📄 HR AI Assistant")

uploaded_file = st.file_uploader ("📎 Upload HR pdf doc", type="pdf")

if uploaded_file:
    st.success("File Uploaded successfully!")
    st.warning("Processing file!")
    text_chuncks = load_pdf(uploaded_file)
    embed_and_store(text_chuncks)
    st.success("File processed (indexed) and stored successfully!")
    

question = st.text_input("❓ Ask a question about the HR document")

if question:
    with st.spinner("🔍 Searching for an answer..."):
        answer, sources = retrieve_answer(question)
        st.markdown(f"**Answer:** {answer}")
        st.markdown("**Sources:**")
        for source in sources:
            st.code(source)

