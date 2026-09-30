from backend.llm.chains import optimize_code


class CodeOptimizer:

    @staticmethod
    def optimize(language: str, code: str):

        return optimize_code(
            language=language,
            code=code
        )