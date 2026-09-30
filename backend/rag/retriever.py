from backend.rag.vector_store import load_vector_store


def get_retriever():

    db = load_vector_store()

    return db.as_retriever(
        search_kwargs={"k": 3}
    )