from backend.chat.prompt import SYSTEM_PROMPT
from backend.chat.memory import ChatMemory
from backend.llm.groq_client import llm


class ChatService:

    def __init__(self):
        self.memory = ChatMemory()

    def ask(self, language, code, question):

        self.memory.add_user(question)

        prompt = f"""
Programming Language:
{language}

Source Code:
{code}

User Question:
{question}
"""

        response = llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", prompt)
            ]
        )

        answer = response.content

        self.memory.add_ai(answer)

        return answer