# src/ingest.py
from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from src.config import DATA_DIR, EMBEDDING_MODEL, VECTOR_STORE_DIR
from src.utils import read_pdf_text


def load_documents_from_folder(folder: Path):
    docs = []
    for p in folder.glob("**/*.pdf"):
        text = read_pdf_text(p)
        if text.strip():
            docs.append(Document(page_content=text, metadata={"source": str(p)}))
    return docs


def build_vector_store():
    docs = []
    for sub in ["lecture_notes", "past_questions", "solutions"]:
        docs += load_documents_from_folder(DATA_DIR / sub)

    if not docs:
        print(
            "No PDFs found. Add files to data/lecture_notes, past_questions, or solutions"
        )
        return

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    # Build Chroma vector store
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding_function=embeddings,
        persist_directory=str(VECTOR_STORE_DIR),
    )
    vectordb.persist()
    print("Vector store created at:", VECTOR_STORE_DIR)


if __name__ == "__main__":
    build_vector_store()
