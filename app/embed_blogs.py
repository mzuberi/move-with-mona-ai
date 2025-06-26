import os
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load .env and OpenAI key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load blog content from markdown files
from pathlib import Path

# Dynamically get the full path to /content folder
current_dir = Path(__file__).resolve().parent
content_dir = current_dir / "content"

if not content_dir.exists():
    raise FileNotFoundError(f"Content directory not found: {content_dir}")

loader = DirectoryLoader(str(content_dir), glob="**/*.md")
documents = loader.load()
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Create embeddings and store in ChromaDB
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = Chroma.from_documents(docs, embedding, persist_directory="app/chroma_store")
vectorstore.persist()

print("✅ Mona's blog memory embedded and saved!")
