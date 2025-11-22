from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI

from src.config import VECTOR_STORE_DIR, EMBEDDING_MODEL, OPENAI_API_KEY, USE_OPENAI


def load_llm():
    if USE_OPENAI:
        return OpenAI(
            temperature=0.0, model="gpt-4o-mini", openai_api_key=OPENAI_API_KEY
        )
    else:
        raise NotImplementedError(
            "Only OpenAI LLM configured. Add local LLM if needed."
        )


def load_rag_chain():
    # Embeddings + vector store
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectordb = Chroma(
        persist_directory=str(VECTOR_STORE_DIR), embedding_function=embeddings
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    # Conversation memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # LLM
    llm = load_llm()

    # Use ConversationalRetrievalChain to include memory
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, memory=memory
    )
    return qa_chain
