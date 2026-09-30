from backend.llm.chains import explain_code


class CodeExplainer:

    @staticmethod
    def explain(language: str, code: str):

        return explain_code(
            language=language,
            code=code
        )