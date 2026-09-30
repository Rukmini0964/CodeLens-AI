from langchain_chroma import Chroma
from backend.rag.embeddings import embedding_model

DB_PATH = "vector_db"


def create_vector_store(documents):

    vectordb = Chroma.from_documents(
        documents=documents,
        embedding=embedding_model,
        persist_directory=DB_PATH
    )

    return vectordb


def load_vector_store():

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model
    )