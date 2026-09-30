from langchain_community.document_loaders import TextLoader

from backend.rag.splitter import split_documents
from backend.rag.vector_store import create_vector_store


def ingest(file_path):

    loader = TextLoader(file_path)

    documents = loader.load()

    chunks = split_documents(documents)

    create_vector_store(chunks)

    print("Documents added successfully.")