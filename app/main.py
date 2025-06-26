import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI

# Load .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load the vectorstore from disk
embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = Chroma(persist_directory="app/chroma_store", embedding_function=embedding)

# Set up retrieval-based QA chain
retriever = vectorstore.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=openai_api_key
    ),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)


# Streamlit UI
st.set_page_config(page_title="Move With Mona AI", layout="centered")
st.title("Move With Mona AI ✧")
st.write("Welcome love — how are you feeling today?")

user_input = st.text_input("Type anything...")

if user_input:
    with st.spinner("Mona is searching her heart..."):
        result = qa_chain({"query": user_input})
        response = result["result"]
        st.success(response)

        # Optional: show where it came from
        with st.expander("✨ Source Memory"):
            for doc in result["source_documents"]:
                st.markdown(f"**From:** `{doc.metadata['source']}`")
                st.markdown(doc.page_content[:400] + "...")
