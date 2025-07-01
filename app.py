
import streamlit as st
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

st.set_page_config(page_title="LangChain RAG Assistant", layout="centered")
st.title("🤖 LangChain RAG Assistant")
st.write("Ask questions about your uploaded documentation!")

# Load documents
with st.spinner("Loading documents..."):
    loader = DirectoryLoader("langchain_docs", glob="*.md", loader_cls=TextLoader)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)

    # Embed and store
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    retriever = vectorstore.as_retriever()

    # Load lightweight QA model
    qa_pipeline = pipeline('text2text-generation', model='google/flan-t5-base', max_length=256)
    llm = HuggingFacePipeline(pipeline=qa_pipeline)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

# UI
query = st.text_input("Ask a question about the docs:")
if query:
    with st.spinner("Thinking..."):
        result = qa_chain({"query": query})
        st.markdown("### 💬 Answer:")
        st.write(result["result"])

        with st.expander("📄 Source Chunks"):
            for i, doc in enumerate(result["source_documents"]):
                st.markdown(f"**Chunk {i+1}**")
                st.code(doc.page_content[:500])
