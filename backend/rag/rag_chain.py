from backend.llm.groq_client import llm
from backend.rag.retriever import get_retriever


def ask_question(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Use ONLY the following documentation.

Documentation:
{context}

Question:
{question}

Answer clearly.
"""

    response = llm.invoke(prompt)

    return response.content